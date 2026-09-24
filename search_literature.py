# -*- coding: utf-8 -*-
"""综述论文系统性文献检索脚本（PRISMA 留痕）
数据库: OpenAlex (主) + Semantic Scholar bulk (辅)
输出: literature/pool.csv, literature/search-log.md, literature/pool.json
"""
import csv, json, time, sys, re
from pathlib import Path
from urllib.parse import quote

import requests

ROOT = Path(__file__).resolve().parent
LIT = ROOT / "literature"
LIT.mkdir(exist_ok=True)

QUERIES = [
    ("Q1", '"physics-informed" AND (tolerance OR tolerancing)'),
    ("Q2", '"physics-informed" AND ("assembly deviation" OR "assembly gap" OR "gap prediction")'),
    ("Q3", '"physics-informed neural network" AND (manufacturing OR assembly)'),
    ("Q4", '"physics-guided" AND (tolerance OR assembly OR manufacturing)'),
    ("Q5", '"physics-informed" AND surrogate AND (manufacturing OR assembly)'),
    ("Q6", '"physics-informed graph learning"'),
    ("Q7", '"physics-informed" AND ("digital twin") AND (manufacturing OR assembly)'),
]

FIELDS = "id,doi,title,display_name,publication_year,authorships,primary_location,cited_by_count,type,abstract_inverted_index"


def deinvert(idx):
    if not idx:
        return ""
    pos = {}
    for w, ps in idx.items():
        for p in ps:
            pos[p] = w
    return " ".join(pos[i] for i in sorted(pos))


def openalex_search(qid, query):
    url = ("https://api.openalex.org/works?search=" + quote(query) +
           "&filter=from_publication_date:2019-01-01,to_publication_date:2026-12-31"
           f"&per_page=100&select={FIELDS}&mailto=survey@local.dev")
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    data = r.json()
    out = []
    for w in data.get("results", []):
        authors = ", ".join(a["author"]["display_name"] for a in w.get("authorships", [])[:6])
        venue = ""
        loc = w.get("primary_location") or {}
        src = loc.get("source") or {}
        venue = src.get("display_name", "") or ""
        out.append({
            "query_id": qid, "source_db": "OpenAlex",
            "title": w.get("display_name", "") or "",
            "authors": authors,
            "year": w.get("publication_year"),
            "venue": venue,
            "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
            "citations": w.get("cited_by_count", 0),
            "type": w.get("type", ""),
            "abstract": deinvert(w.get("abstract_inverted_index"))[:1500],
        })
    return out, data.get("meta", {}).get("count", 0)


def s2_search(qid, query):
    url = ("https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=" + quote(query) +
           "&fields=title,authors,year,venue,externalIds,citationCount,abstract"
           "&year=2019-2026&limit=100")
    r = requests.get(url, timeout=60)
    if r.status_code == 429:
        time.sleep(5)
        r = requests.get(url, timeout=60)
    r.raise_for_status()
    out = []
    for p in r.json().get("data", []):
        ext = p.get("externalIds") or {}
        out.append({
            "query_id": qid, "source_db": "SemanticScholar",
            "title": p.get("title", "") or "",
            "authors": ", ".join(a.get("name", "") for a in (p.get("authors") or [])[:6]),
            "year": p.get("year"),
            "venue": p.get("venue", "") or "",
            "doi": ext.get("DOI", "") or "",
            "citations": p.get("citationCount", 0) or 0,
            "type": "",
            "abstract": (p.get("abstract") or "")[:1500],
        })
    return out, r.json().get("total", 0)


def norm_key(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())[:80]


def main():
    all_rows, log = [], []
    for qid, q in QUERIES:
        try:
            rows, total = openalex_search(qid, q)
            log.append(f"| {qid} | OpenAlex | `{q}` | {total} | {len(rows)} | OK |")
            all_rows += rows
        except Exception as e:
            log.append(f"| {qid} | OpenAlex | `{q}` | - | 0 | FAIL: {e} |")
        time.sleep(0.3)
    # S2 补充检索（仅核心 3 式，避免限流）
    for qid, q in [("Q1", QUERIES[0][1]), ("Q2", QUERIES[1][1]), ("Q6", QUERIES[5][1])]:
        try:
            rows, total = s2_search("S2-" + qid, q.replace('"', ""))
            log.append(f"| S2-{qid} | SemanticScholar | `{q}` | {total} | {len(rows)} | OK |")
            all_rows += rows
        except Exception as e:
            log.append(f"| S2-{qid} | SemanticScholar | `{q}` | - | 0 | FAIL: {e} |")
        time.sleep(2)

    # 去重：DOI 优先，其次规范化标题
    seen, pool = set(), []
    for r in all_rows:
        key = ("doi:" + r["doi"].lower()) if r["doi"] else ("t:" + norm_key(r["title"]))
        if key in seen or not r["title"]:
            continue
        seen.add(key)
        pool.append(r)

    # 相关性粗打分（标题+摘要关键词），仅用于排序，不作纳入决定
    kw_pos = ["physics-informed", "physics informed", "physics-guided", "physics guided",
              "tolerance", "tolerancing", "assembly", "deviation", "gap", "surrogate",
              "manufacturing", "geometric variation", "pinns", "pinn"]
    kw_neg = ["fluid", "turbulence", "cardiac", "blood", "climate", "quantum", "molecular"]
    for r in pool:
        text = (r["title"] + " " + r["abstract"]).lower()
        r["relevance"] = sum(text.count(k) for k in kw_pos) - 2 * sum(text.count(k) for k in kw_neg)
    pool.sort(key=lambda r: (r["relevance"], r["citations"] or 0), reverse=True)

    with open(LIT / "pool.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(pool[0].keys()))
        w.writeheader(); w.writerows(pool)
    with open(LIT / "pool.json", "w", encoding="utf-8") as f:
        json.dump(pool, f, ensure_ascii=False, indent=1)

    log_md = (
        "# 系统性文献检索日志（PRISMA 留痕）\n\n"
        f"- 检索日期: 2026-09-13\n- 时间窗: 2019-01-01 ~ 2026-12-31\n"
        "- 数据库: OpenAlex（主，works search，per_page=100）+ Semantic Scholar（辅，bulk search）\n\n"
        "| 检索式编号 | 数据库 | 检索式 | 总命中 | 抓取 | 状态 |\n|---|---|---|---|---|---|\n"
        + "\n".join(log) +
        f"\n\n## 汇总\n\n- 抓取总量（去重前）: {len(all_rows)}\n- 去重后文献池: {len(pool)}\n"
        "- 去重规则: DOI 优先，缺失时用规范化标题\n- 排序: 关键词相关性粗打分（仅排序用，不作纳入决定）\n"
        "\n## 下一步（PRISMA 筛选项）\n\n"
        "- [ ] 标题/摘要筛查：剔除明显越界（流体/医学/气候等）与无物理约束机制的论文\n"
        "- [ ] 全文评估：对高分文献执行纳入/排除标准\n"
        "- [ ] 追溯滚雪球：对核心文献做引用追踪（S2 citations API）\n"
    )
    (LIT / "search-log.md").write_text(log_md, encoding="utf-8")
    print(f"TOTAL_RAW={len(all_rows)} POOL={len(pool)}")
    for y in range(2019, 2027):
        n = sum(1 for r in pool if r["year"] == y)
        print(y, n)


if __name__ == "__main__":
    main()
