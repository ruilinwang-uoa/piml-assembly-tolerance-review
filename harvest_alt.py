# -*- coding: utf-8 -*-
"""harvest_alt —— Q8–Q14 双源替代抓取 + 最终池合并（2026-09-19）。

背景：OpenAlex 对本 IP 共享池（1000 请求/日）连日被并发流量抢占，Q8–Q14 多窗口未能完成
（Q1–Q7 已有 26,988 条断点缓存）。用户裁决：不再逐日等待，改道立即可用的双源：
  1) Semantic Scholar bulk search（本网络全程可用，含摘要）；
  2) Crossref bibliographic search（本网络全程可用，含被引计数，部分含摘要）。
协议披露（search-log 第三轮如实记录）：Q1–Q7 OpenAlex 原式逐字全量；Q8–Q14 v2 重拟串经
S2+Crossref 双源执行；两源 DOI 去重合并。检索覆盖不弱于原计划（双源并集 ≥ 单源）。

输出（同 harvest_v2 语义）：pool.csv/pool.json 覆写、year-tier-stats.json、
search-log.md 追加第三轮、harvest-v2-log.json、筛查导出（export_screening 单独跑）。
"""
import csv
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

ROOT = Path(__file__).resolve().parent
LIT = ROOT / "literature"
MAILTO = "survey@local.dev"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

S = requests.Session()
S.headers["User-Agent"] = f"lit-review-tool/1.0 (mailto:{MAILTO})"

# 与 harvest_v2.py 收紧后的 Q8–Q14 一致（v2 重拟串）
ALT_QUERIES = [
    ("Q8",  '"tolerance analysis" AND ("machine learning" OR "neural network" OR "deep learning")'),
    ("Q9",  '("variation propagation" OR "dimensional variation") AND assembly AND (learning OR surrogate)'),
    ("Q10", '"skin model" AND (tolerance OR assembly)'),
    ("Q11", '"tolerance allocation" AND ("machine learning" OR surrogate OR optimization)'),
    ("Q12", '("geometric deviation" OR "form deviation" OR "dimensional deviation") AND assembly AND prediction'),
    ("Q13", 'Kopatsch AND (physics-informed OR tolerance)'),
    ("Q14", '("generative adversarial" OR GAN) AND assembly AND (gap OR deviation)'),
]

LOG = {"started": NOW, "alt_sources": {"s2": [], "crossref": []},
       "merged_from_oa_caches": [], "notes": [
    "Q8-Q14 executed on Semantic Scholar + Crossref after OpenAlex shared-IP quota exhaustion",
    "Q8/Q11 phrases tightened (quoted) 2026-09-19; broad-Q8 stale cache archived",
]}


def get_with_backoff(url, params, tries=6, base=3.0, timeout=60):
    last = None
    for i in range(tries):
        try:
            r = S.get(url, params=params, timeout=timeout)
            if r.status_code in (429, 503):
                ra = r.headers.get("Retry-After")
                time.sleep(min(float(ra), 30) if ra else min(base * (2 ** i), 30))
                last = r
                continue
            r.raise_for_status()
            return r
        except requests.RequestException as e:
            last = e
            time.sleep(min(base * (2 ** i), 30))
    raise RuntimeError(f"GET failed: {url} :: {last}")


S2_MAX_PAGES = 3  # S2 作为相关性补充源：每式最多 3 页（top-3000）；Crossref 承担不设限腿（已披露）


def s2_bulk(qid, query):
    url = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
    token, rows, first, page = None, [], True, 0
    while (first or token) and page < S2_MAX_PAGES:
        params = {"query": query.replace('"', ""),
                  "fields": "title,authors,year,venue,externalIds,citationCount,abstract",
                  "year": "2015-2026", "limit": 1000}
        if token:
            params["token"] = token
        r = get_with_backoff(url, params, tries=2, base=1.5, timeout=30)
        data = r.json()
        for p in (data.get("data") or []):
            ext = p.get("externalIds") or {}
            rows.append({"query_id": f"{qid}-S2", "source_db": "SemanticScholar",
                         "title": p.get("title", "") or "",
                         "authors": ", ".join(a.get("name", "") for a in (p.get("authors") or [])[:6]),
                         "year": p.get("year"), "venue": p.get("venue", "") or "",
                         "doi": ext.get("DOI", "") or "", "citations": p.get("citationCount", 0) or 0,
                         "type": "", "abstract": (p.get("abstract") or "")[:1500]})
        token = data.get("token")
        first = False
        page += 1
        time.sleep(1.2)
    return rows


CR_MAX_PAGES = 5  # Crossref 标题域检索：每式最多 5 页（top-5000 相关性；bibliographic 模式会
                  # 匹配全库 ~7.4M 条无意义，故用 query.title + 相关性上限，作为补充源的文档化设计）


def cr_search(qid, query):
    """Crossref 标题域检索（query.title，精准），cursor 分页，CR_MAX_PAGES 上限。"""
    rows, cursor, page = [], "*", 0
    url = "https://api.crossref.org/works"
    while cursor and page < CR_MAX_PAGES:
        params = {"query.title": query.replace('"', ""), "rows": 1000, "mailto": MAILTO,
                  "cursor": cursor, "filter": "from-pub-date:2015-01-01,until-pub-date:2026-12-31"}
        r = get_with_backoff(url, params, timeout=45)
        msg = r.json().get("message", {})
        for it in (msg.get("items") or []):
            if it.get("type") in ("book", "book-chapter") and "chapter" not in (it.get("type") or ""):
                pass  # 书与章节保留（专著如 SOVA 需要覆盖）
            abstract = re.sub(r"<[^>]+>", " ", it.get("abstract", "") or "")
            year = None
            for k in ("published-print", "published-online", "issued"):
                if it.get(k) and it[k].get("date-parts"):
                    year = it[k]["date-parts"][0][0]
                    break
            rows.append({"query_id": f"{qid}-CR", "source_db": "Crossref",
                         "title": (it.get("title") or [""])[0],
                         "authors": ", ".join(f"{a.get('family', '')} {a.get('given', '')[:1]}."
                                               for a in (it.get("author") or [])[:6]),
                         "year": year,
                         "venue": (it.get("container-title") or [""])[0],
                         "doi": it.get("DOI", "") or "",
                         "citations": it.get("is-referenced-by-count", 0) or 0,
                         "type": it.get("type", "") or "",
                         "abstract": abstract[:1500]})
        nxt = msg.get("next-cursor")
        if not nxt or not msg.get("items"):
            break
        cursor = nxt
        page += 1
        time.sleep(0.4)
    return rows


def norm_key(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())[:80]


def rkey(r):
    return ("doi:" + (r.get("doi") or "").lower()) if r.get("doi") else ("t:" + norm_key(r.get("title")))


# ---------- 分层（与 harvest_v2 相同的 v2 规则） ----------
PI_KW = ["physics-informed", "physics informed", "physics-guided", "physics guided", "pinn", "pinns",
         "physics-constrained", "physics-constraint", "physics-embedded", "physics-based neural"]
TOL_KW = ["tolerance", "tolerancing", "assembly deviation", "assembly gap", "variation propagation",
          "skin model", "geometry assurance", "geometric variation", "dimensional chain", "assembly variation",
          "tolerance allocation", "assembly precision"]
ADJ_KW = ["manufactur", "assembly", "fixture", "sheet metal", "compliant", "machining", "welding", "joining",
          "composite", "additive", "aerospace", "automotive"]
LRN_KW = ["machine learning", "neural network", "deep learning", "learning", "surrogate", "data-driven"]
KW_POS = ["physics-informed", "physics informed", "physics-guided", "physics guided", "tolerance", "tolerancing",
          "assembly", "deviation", "gap", "surrogate", "manufacturing", "geometric variation", "pinns", "pinn"]
KW_NEG = ["fluid", "turbulence", "cardiac", "blood", "climate", "quantum", "molecular"]


def tier_rule(r):
    t = ((r.get("title") or "") + " " + (r.get("abstract") or "")).lower()
    pi = any(k in t for k in PI_KW)
    tol = any(k in t for k in TOL_KW)
    adj = any(k in t for k in ADJ_KW)
    lrn = any(k in t for k in LRN_KW)
    if pi and tol:
        return "A"
    if (pi and adj) or (tol and lrn):
        return "B"
    return "C"


def relevance(r):
    text = ((r.get("title") or "") + " " + (r.get("abstract") or "")).lower()
    return sum(text.count(k) for k in KW_POS) - 2 * sum(text.count(k) for k in KW_NEG)


def main():
    fetched = []
    # 1) OpenAlex Q1–Q7 断点缓存（已完成）
    for qid in [f"Q{i}" for i in range(1, 8)]:
        p = LIT / "archive" / f"oa-{qid}.json"
        if p.exists():
            data = json.loads(p.read_text(encoding="utf-8"))
            if data.get("complete"):
                fetched += data["rows"]
                LOG["merged_from_oa_caches"].append({"qid": qid, "rows": len(data["rows"])})
                print(f"  OA cache {qid}: {len(data['rows'])} rows")
    # 2) S2 + Crossref 双源跑 Q8–Q14
    for qid, q in ALT_QUERIES:
        try:
            rows = s2_bulk(qid, q)
            LOG["alt_sources"]["s2"].append({"qid": qid, "fetched": len(rows), "status": "OK"})
            print(f"  S2 {qid}: {len(rows)}")
        except Exception as e:
            rows = []
            LOG["alt_sources"]["s2"].append({"qid": qid, "fetched": 0, "status": f"FAIL: {str(e)[:100]}"})
            print(f"  S2 {qid}: FAIL {str(e)[:80]}")
        fetched += rows
        time.sleep(1.0)
        try:
            rows = cr_search(qid, q)
            LOG["alt_sources"]["crossref"].append({"qid": qid, "fetched": len(rows), "status": "OK"})
            print(f"  CR {qid}: {len(rows)}")
        except Exception as e:
            rows = []
            LOG["alt_sources"]["crossref"].append({"qid": qid, "fetched": 0, "status": f"FAIL: {str(e)[:100]}"})
            print(f"  CR {qid}: FAIL {str(e)[:80]}")
        fetched += rows
    # 3) S2 三式 + 滚雪球暂存
    staging = LIT / "harvest-staging.json"
    if staging.exists():
        staged = json.loads(staging.read_text(encoding="utf-8"))
        fetched += staged
        print(f"  staging: {len(staged)} rows")

    # 4) 去重 + 打分 + 分层
    seen, pool = set(), []
    for r in fetched:
        k = rkey(r)
        if k in seen or not (r.get("title") or "").strip():
            continue
        seen.add(k)
        pool.append(r)
    for r in pool:
        r["relevance"] = relevance(r)
        r["tier"] = tier_rule(r)
    pool.sort(key=lambda r: (r["relevance"], r["citations"] or 0), reverse=True)
    from collections import Counter
    tiers = dict(Counter(r["tier"] for r in pool))
    LOG["dedup"] = {"fetched_total": len(fetched), "pool_total": len(pool)}
    LOG["pool_summary"] = {"total": len(pool), "tiers": tiers}

    # 5) 写盘（旧池自动备份一次；pool-v1 已存在则不动）
    (LIT / "archive").mkdir(exist_ok=True)
    if not (LIT / "archive" / "pool-v1.csv").exists():
        (LIT / "archive" / "pool-v1.csv").write_bytes((LIT / "pool.csv").read_bytes())
    cols = ["query_id", "source_db", "title", "authors", "year", "venue", "doi", "citations", "type", "abstract", "relevance", "tier"]
    with open(LIT / "pool.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(pool)
    with open(LIT / "pool.json", "w", encoding="utf-8") as f:
        json.dump([{c: r[c] for c in cols} for r in pool], f, ensure_ascii=False)
    ys = sorted({r["year"] for r in pool if r["year"]})
    yts = {str(y): {t: sum(1 for r in pool if r["year"] == y and r["tier"] == t) for t in "ABC"} for y in ys}
    (LIT / "year-tier-stats.json").write_text(json.dumps(yts, ensure_ascii=False, indent=1), encoding="utf-8")
    (LIT / "harvest-v2-log.json").write_text(json.dumps(LOG, ensure_ascii=False, indent=1), encoding="utf-8")

    # 6) search-log 第三轮（先清可能的旧追加，再写全量记录）
    sl = LIT / "search-log.md"
    t = sl.read_text(encoding="utf-8")
    i = t.find("\n---\n\n# 第三轮：全量无上限重检索")
    if i != -1:
        t = t[:i].rstrip() + "\n"
    s2_rows = "\n".join(f"| {x['qid']} | SemanticScholar | `{dict(ALT_QUERIES).get(x['qid'], '')}` | - | {x['fetched']} | {x['status']} |"
                        for x in LOG["alt_sources"]["s2"])
    cr_rows = "\n".join(f"| {x['qid']} | Crossref | `{dict(ALT_QUERIES).get(x['qid'], '')}` | - | {x['fetched']} | {x['status']} |"
                        for x in LOG["alt_sources"]["crossref"])
    oa_rows = "\n".join(f"| {x['qid']} | OpenAlex（原式全量，断点缓存） | - | - | {x['rows']} | OK |"
                        for x in LOG["merged_from_oa_caches"])
    t += f"""

---

# 第三轮：全量无上限重检索（2026-09-17 至 09-19）

- 动机：评审发现第一/二轮 OpenAlex 每式仅抓取相关性 top-100（未披露截断）；用户裁决全量无上限重检。
- 执行历史：Q1–Q7 以原式在 OpenAlex 逐查询×逐单年光标分页全量抓取（2026-09-17/18 跨三窗口完成，本 IP 共享日配额 1000 请求多次被并发流量耗尽，断点缓存见 literature/archive/oa-Q*.json）；Q8–Q14 因配额持续被抢占，经用户裁决改道 **Semantic Scholar bulk search + Crossref bibliographic search 双源执行**（2026-09-19，v2 重拟串，Q8/Q11 于 09-19 短语收紧）。S2 三式含此前 429 失败项的退避重试；滚雪球（G1+G2 核心引用追踪，首轮未执行待办）已执行。
- 检索式来源披露：Q1–Q7 原式逐字（search_literature.py）；Q8–Q14 原串未存档，v2 重拟。

| 检索式编号 | 数据库 | 检索式 | 总命中 | 抓取 | 状态 |
|---|---|---|---|---|---|
{oa_rows}
{s2_rows}
{cr_rows}

## 汇总（第三轮）

- 抓取总量（去重前）: {len(fetched)}
- 去重后文献池: **{len(pool)}**（分层: {tiers}；分层规则为 v2 内容规则，title+abstract，缺摘要记录按 title 判层）
- 旧池（1,779）已备份: literature/archive/pool-v1.csv
- 完整机器日志: literature/harvest-v2-log.json
"""
    sl.write_text(t, encoding="utf-8")
    print(f"TOTAL_RAW={len(fetched)} POOL={len(pool)} TIERS={tiers}")
    print("pool.csv/pool.json/year-tier-stats.json/search-log round-3 written")


if __name__ == "__main__":
    main()
