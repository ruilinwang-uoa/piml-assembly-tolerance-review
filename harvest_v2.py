# -*- coding: utf-8 -*-
"""harvest_v2 —— 第三轮全量无上限重检索（2026-09-16，评审修复 Phase 2.1）

背景：第一/二轮 OpenAlex 检索每式仅抓取相关性 top-100（per_page=100 单页），评审判定为未披露的截断
（PRE_SUBMISSION_REVIEW_2026-09-16 CRITICAL #2）；用户裁决：全量无上限重检索。
本脚本：
  1) Q1–Q7 用原始检索式（search_literature.py 逐字恢复，窗宽 2019–2026）；
     Q8–Q14 原始串不可恢复（round-2 未留脚本），按 search-log.md 主题重新拟定并披露（v2 重拟）；
  2) OpenAlex 逐查询×逐单年 光标分页全量抓取（per_page=200，单年命中必 <10k，绕开 cursor 上限）；
  3) Semantic Scholar S2-Q1/S2-Q2 重试（指数退避；首轮曾 429 失败未重试）+ S2-Q6 复跑；
  4) 滚雪球（首轮日志中未执行的待办）：G1+G2 核心 16 篇的 S2 引用/被引追踪（SB-fwd/SB-bwd）；
  5) 去重（DOI 优先→规范化标题，规则与首轮一致）+ 相关性粗打分（规则与首轮一致）；
  6) 分层：原 tier 规则脚本已佚，本文件实现 v2 规则并用旧池 (A245/B306/C1228) 校准对照，全部写入日志披露；
  7) 输出：pool.csv/pool.json 覆写（旧池备份至 literature/archive/pool-v1.csv）、
     harvest-v2-log.json、year-tier-stats.json 刷新、search-log.md 追加第三轮。
"""
import csv, json, re, shutil, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

ROOT = Path(__file__).resolve().parent
LIT = ROOT / "literature"
ARCH = LIT / "archive"; ARCH.mkdir(exist_ok=True)
SCREEN = LIT / "screening"; SCREEN.mkdir(exist_ok=True)

MAILTO = "survey@local.dev"
UA = {"User-Agent": f"piml-tolerance-survey-harvest/2.0 (mailto:{MAILTO})"}
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

# ---------- 检索式 ----------
# Q1–Q7：原始串（scripts/search_literature.py 逐字）；Q8–Q14：v2 重拟（原串不可恢复，主题源自 search-log.md round-2）
QUERIES_V2 = [
    ("Q1",  '"physics-informed" AND (tolerance OR tolerancing)', 2019, 2026, "verbatim"),
    ("Q2",  '"physics-informed" AND ("assembly deviation" OR "assembly gap" OR "gap prediction")', 2019, 2026, "verbatim"),
    ("Q3",  '"physics-informed neural network" AND (manufacturing OR assembly)', 2019, 2026, "verbatim"),
    ("Q4",  '"physics-guided" AND (tolerance OR assembly OR manufacturing)', 2019, 2026, "verbatim"),
    ("Q5",  '"physics-informed" AND surrogate AND (manufacturing OR assembly)', 2019, 2026, "verbatim"),
    ("Q6",  '"physics-informed graph learning"', 2019, 2026, "verbatim"),
    ("Q7",  '"physics-informed" AND ("digital twin") AND (manufacturing OR assembly)', 2019, 2026, "verbatim"),
    ("Q8",  '"tolerance analysis" AND ("machine learning" OR "neural network" OR "deep learning")', 2015, 2026, "v2-respecified-tightened"),
    ("Q9",  '("variation propagation" OR "dimensional variation") AND assembly AND (learning OR surrogate)', 2015, 2026, "v2-respecified"),
    ("Q10", '"skin model" AND (tolerance OR assembly)', 2015, 2026, "v2-respecified"),
    ("Q11", '"tolerance allocation" AND ("machine learning" OR surrogate OR optimization)', 2015, 2026, "v2-respecified-tightened"),
    ("Q12", '("geometric deviation" OR "form deviation" OR "dimensional deviation") AND assembly AND prediction', 2015, 2026, "v2-respecified"),
    ("Q13", 'Kopatsch AND (physics-informed OR tolerance)', 2015, 2026, "v2-respecified"),
    ("Q14", '("generative adversarial" OR GAN) AND assembly AND (gap OR deviation)', 2015, 2026, "v2-respecified"),
]
S2_QUERIES = [  # 首轮 S2-Q1/S2-Q2 曾 429 失败未重试；本轮带退避重试
    ("S2-Q1", 'physics-informed AND (tolerance OR tolerancing)'),
    ("S2-Q2", 'physics-informed AND (assembly deviation OR assembly gap OR gap prediction)'),
    ("S2-Q6", 'physics-informed graph learning'),
]
FIELDS = "id,doi,title,display_name,publication_year,authorships,primary_location,cited_by_count,type,abstract_inverted_index"

# 滚雪球种子：G1+G2 全部（运行时从 coding-table.md 读取 DOI，prefix A/D）
def load_snowball_seeds():
    seeds = {}
    for line in (LIT / "coding-table.md").read_text(encoding="utf-8").splitlines():
        if not (line.startswith("| ") and "---" not in line):
            continue
        c = [x.strip() for x in line.strip("|").split("|")]
        if len(c) >= 10 and re.fullmatch(r"[AD]\d{2}", c[0]) and c[9].startswith("10."):
            seeds[c[0]] = c[9]
    return seeds


SNOWBALL_SEEDS = load_snowball_seeds()

LOG = {"started": NOW, "openalex": [], "s2": [], "snowball": [], "dedup": {}, "tier": {}, "notes": [
    "Q1-Q7 verbatim from search_literature.py; Q8-Q14 re-specified in v2 (original strings not archived)",
    "per-query x per-single-year cursor pagination, per_page=200, no fetch caps",
    "2026-09-19: Q8/Q11 phrases tightened (quoted) after first-day volume revealed unquoted 'tolerance "
    "analysis/allocation' matched drug-tolerance noise (Q8-2015 alone >14k hits); stale broad-Q8 cache archived",
]}

session = requests.Session()
session.headers.update(UA)


class BanError(RuntimeError):
    """OpenAlex 长时封锁（Retry-After > 300s）——立即中止，交由断点续传。"""


def http_get(url, params, tries=8, base_sleep=2.0):
    """带退避的 GET（429/5xx 重试；遵守 Retry-After；长时封锁抛 BanError 立即中止）。"""
    last = None
    for i in range(tries):
        try:
            r = session.get(url, params=params, timeout=60)
            if r.status_code == 429:
                try:
                    ra_s = float(r.headers.get("Retry-After", "60"))
                except ValueError:
                    ra_s = 60.0
                if ra_s > 300:
                    raise BanError(f"OpenAlex quota exhausted (Retry-After={ra_s:.0f}s)")
                time.sleep(min(ra_s + 2, 130.0))
                last = r
                continue
            if r.status_code >= 500:
                time.sleep(min(base_sleep * (2 ** i), 60.0))
                last = r
                continue
            r.raise_for_status()
            return r
        except BanError:
            raise
        except requests.RequestException as e:
            last = e
            time.sleep(min(base_sleep * (2 ** i), 60.0))
    raise RuntimeError(f"GET failed after {tries} tries: {url} :: {last}")


def deinvert(idx):
    if not idx:
        return ""
    pos = {}
    for w, ps in idx.items():
        for p in ps:
            pos[p] = w
    return " ".join(pos[i] for i in sorted(pos))


def rec_from_openalex(w, qid):
    authors = ", ".join(a["author"]["display_name"] for a in w.get("authorships", [])[:6])
    src = ((w.get("primary_location") or {}).get("source") or {})
    return {
        "query_id": qid, "source_db": "OpenAlex",
        "title": w.get("display_name", "") or "",
        "authors": authors,
        "year": w.get("publication_year"),
        "venue": src.get("display_name", "") or "",
        "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
        "citations": w.get("cited_by_count", 0) or 0,
        "type": w.get("type", "") or "",
        "abstract": deinvert(w.get("abstract_inverted_index"))[:1500],
    }


def openalex_year_full(qid, query, year):
    """单查询×单年，光标分页全量抓取。"""
    rows, cursor, pages = [], "*", 0
    while cursor:
        params = {
            "search": query,
            "filter": f"from_publication_date:{year}-01-01,to_publication_date:{year}-12-31",
            "per_page": 200, "select": FIELDS, "cursor": cursor, "mailto": MAILTO,
        }
        r = http_get("https://api.openalex.org/works", params)
        data = r.json()
        rows += [rec_from_openalex(w, qid) for w in data.get("results", [])]
        cursor = data.get("meta", {}).get("next_cursor")
        pages += 1
        time.sleep(0.6)  # 礼貌速率（该 IP 曾因高频被 429，2026-09-16 教训）
    return rows, pages


def run_openalex():
    """逐查询抓取；断点缓存粒度到年（archive/oa-Q#.json）。
    未完成缓存按年续抓：已完成年份直接沿用，仅抓缺失年份。长时封锁立即中止返回 incomplete。"""
    total, incomplete = [], False
    for qid, q, y0, y1, provenance in QUERIES_V2:
        cache = LIT / "archive" / f"oa-{qid}.json"
        qrows, qdetail, q_failed = [], [], False
        if cache.exists():
            data = json.loads(cache.read_text(encoding="utf-8"))
            if data.get("complete"):
                total += data["rows"]
                LOG["openalex"].append({**data["log"], "resumed_from_cache": True})
                print(f"  {qid}: resumed from cache ({len(data['rows'])} rows)", flush=True)
                continue
            if data.get("rows"):
                # 年级续抓：沿用已完成年份，仅补缺失
                qrows = data["rows"]
                qdetail = data["log"]["years"]
                done_years = {d["year"] for d in qdetail if d.get("fetched", 0) > 0}
                print(f"  {qid}: year-level resume ({len(qrows)} rows cached, "
                      f"{len(done_years)} years done, fetching rest)", flush=True)
        try:
            for y in range(y0, y1 + 1):
                if any(d["year"] == y and d.get("fetched", 0) > 0 for d in qdetail):
                    continue  # 该年已有缓存
                try:
                    rows, pages = openalex_year_full(qid, q, y)
                except BanError:
                    raise
                except Exception as e:
                    qdetail.append({"year": y, "fetched": 0, "pages": 0, "status": f"FAIL: {str(e)[:120]}"})
                    print(f"  {qid}/{y}: FAIL {str(e)[:100]}", flush=True)
                    q_failed = True
                    continue
                qrows += rows
                qdetail.append({"year": y, "fetched": len(rows), "pages": pages})
                # 逐年断点（部分行 + 进度）
                cache.write_text(json.dumps({"complete": False, "rows": qrows, "log": {
                    "qid": qid, "query": q, "provenance": provenance,
                    "window": f"{y0}-01-01..{y1}-12-31", "fetched": len(qrows), "years": qdetail}},
                    ensure_ascii=False), encoding="utf-8")
                try:
                    rows, pages = openalex_year_full(qid, q, y)
                except BanError:
                    raise
                except Exception as e:
                    qdetail.append({"year": y, "fetched": 0, "pages": 0, "status": f"FAIL: {str(e)[:120]}"})
                    print(f"  {qid}/{y}: FAIL {str(e)[:100]}", flush=True)
                    q_failed = True
                    continue
                qrows += rows
                qdetail.append({"year": y, "fetched": len(rows), "pages": pages})
                # 逐年断点（部分行 + 进度）
                cache.write_text(json.dumps({"complete": False, "rows": qrows, "log": {
                    "qid": qid, "query": q, "provenance": provenance,
                    "window": f"{y0}-01-01..{y1}-12-31", "fetched": len(qrows), "years": qdetail}},
                    ensure_ascii=False), encoding="utf-8")
        except BanError as e:
            incomplete = True
            LOG["openalex_banned_midrun"] = str(e)
            print(f"  {qid}: BAN mid-run ({e}) — aborting openalex phase, progress cached", flush=True)
            break
        total += qrows
        qlog = {"qid": qid, "query": q, "provenance": provenance,
                "window": f"{y0}-01-01..{y1}-12-31", "fetched": len(qrows), "years": qdetail}
        cache.write_text(json.dumps({"complete": not q_failed, "rows": qrows, "log": qlog},
                                    ensure_ascii=False), encoding="utf-8")
        LOG["openalex"].append(qlog)
        print(f"  {qid}: fetched {len(qrows)} ({provenance}){' [partial]' if q_failed else ''}", flush=True)
    return total, incomplete


def s2_bulk(qid, query):
    """S2 bulk search，token 分页全量。"""
    url = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
    token, rows, first = None, [], True
    while first or token:
        params = {"query": query, "fields": "title,authors,year,venue,externalIds,citationCount,abstract",
                  "year": "2019-2026", "limit": 1000}
        if token:
            params["token"] = token
        r = http_get(url, params, tries=6, base_sleep=5.0)  # 429 退避由 http_get 处理
        data = r.json()
        for p in data.get("data", []):
            ext = p.get("externalIds") or {}
            rows.append({
                "query_id": qid, "source_db": "SemanticScholar",
                "title": p.get("title", "") or "", "authors": ", ".join(a.get("name", "") for a in (p.get("authors") or [])[:6]),
                "year": p.get("year"), "venue": p.get("venue", "") or "", "doi": ext.get("DOI", "") or "",
                "citations": p.get("citationCount", 0) or 0, "type": "",
                "abstract": (p.get("abstract") or "")[:1500],
            })
        token = data.get("token")
        first = False
        time.sleep(1.5)
    return rows


def run_s2():
    total = []
    for qid, q in S2_QUERIES:
        try:
            rows = s2_bulk(qid, q)
            LOG["s2"].append({"qid": qid, "query": q, "fetched": len(rows), "status": "OK"})
            print(f"  {qid}: fetched {len(rows)}")
        except Exception as e:
            LOG["s2"].append({"qid": qid, "query": q, "fetched": 0, "status": f"FAIL: {e}"})
            rows = []
            print(f"  {qid}: FAIL {e}")
        total += rows
    return total


def run_snowball():
    total = []
    fields = "title,year,venue,externalIds,citationCount,abstract"
    for seed_id, doi in SNOWBALL_SEEDS.items():
        pid = f"DOI:{doi}"
        for direction, endpoint in (("SB-fwd", "citations"), ("SB-bwd", "references")):
            try:
                offset, rows = 0, []
                while True:
                    url = f"https://api.semanticscholar.org/graph/v1/paper/{pid}/{endpoint}"
                    r = http_get(url, {"fields": fields, "limit": 1000, "offset": offset}, tries=6, base_sleep=5.0)
                    data = r.json()
                    items = [c.get("citingPaper") if direction == "SB-fwd" else c.get("citedPaper")
                             for c in (data.get("data") or [])]  # S2 对未收录论文返回 data:null
                    for p in items or []:
                        if not p:
                            continue
                        ext = p.get("externalIds") or {}
                        rows.append({
                            "query_id": f"{direction}:{seed_id}", "source_db": "SemanticScholar",
                            "title": p.get("title", "") or "", "authors": "",
                            "year": p.get("year"), "venue": p.get("venue", "") or "",
                            "doi": ext.get("DOI", "") or "", "citations": p.get("citationCount", 0) or 0,
                            "type": "", "abstract": (p.get("abstract") or "")[:800],
                        })
                    nxt = data.get("next")
                    if not nxt or len(data.get("data", [])) == 0:
                        break
                    offset = nxt
                    time.sleep(1.2)
                LOG["snowball"].append({"seed": seed_id, "direction": direction, "fetched": len(rows)})
                total += rows
                print(f"  {seed_id} {direction}: {len(rows)}")
            except Exception as e:
                LOG["snowball"].append({"seed": seed_id, "direction": direction, "fetched": 0, "status": f"FAIL: {e}"})
                print(f"  {seed_id} {direction}: FAIL {e}")
            time.sleep(1.0)
    return total


# ---------- 去重与相关性（与首轮规则一致） ----------
def norm_key(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())[:80]


def dedup(rows):
    seen, pool = set(), []
    for r in rows:
        key = ("doi:" + r["doi"].lower()) if r["doi"] else ("t:" + norm_key(r["title"]))
        if key in seen or not r["title"]:
            continue
        seen.add(key)
        pool.append(r)
    return pool


KW_POS = ["physics-informed", "physics informed", "physics-guided", "physics guided", "tolerance", "tolerancing",
          "assembly", "deviation", "gap", "surrogate", "manufacturing", "geometric variation", "pinns", "pinn"]
KW_NEG = ["fluid", "turbulence", "cardiac", "blood", "climate", "quantum", "molecular"]


def relevance(r):
    text = (r["title"] + " " + r["abstract"]).lower()
    return sum(text.count(k) for k in KW_POS) - 2 * sum(text.count(k) for k in KW_NEG)


# ---------- 分层（v2 规则；原脚本已佚，用旧池校准对照披露） ----------
PI_KW = ["physics-informed", "physics informed", "physics-guided", "physics guided", "pinn", "pinns",
         "physics-constrained", "physics-constraint", "physics-embedded", "physics-based neural"]
TOL_KW = ["tolerance", "tolerancing", "assembly deviation", "assembly gap", "variation propagation",
          "skin model", "geometry assurance", "geometric variation", "dimensional chain", "assembly variation",
          "tolerance allocation", "assembly precision"]
ADJ_KW = ["manufactur", "assembly", "fixture", "sheet metal", "compliant", "machining", "welding", "joining",
          "composite", "additive", "aerospace", "automotive"]
LRN_KW = ["machine learning", "neural network", "deep learning", "learning", "surrogate", "data-driven"]


def tier_rule(r):
    t = (r["title"] + " " + r["abstract"]).lower()
    pi = any(k in t for k in PI_KW)
    tol = any(k in t for k in TOL_KW)
    adj = any(k in t for k in ADJ_KW)
    lrn = any(k in t for k in LRN_KW)
    if pi and tol:
        return "A"
    if (pi and adj) or (tol and lrn):
        return "B"
    return "C"


def main():
    source = "all"
    if "--source" in sys.argv:
        source = sys.argv[sys.argv.index("--source") + 1]
    staging = LIT / "harvest-staging.json"
    print(f"=== harvest_v2: round-3 uncapped re-harvest (source={source}) ===")
    fetched = []
    oa_incomplete = False
    if source in ("all", "openalex"):
        # 预探测：短冷却（≤300s）睡满后无限重试（不计失败）；仅硬异常计失败（10 次）或
        # 长时封锁（>300s）才终止。任何"OpenAlex 未实际完成"的出口都必须 oa_incomplete=True。
        probe_ok = False
        hard_fails = 0
        probe_deadline = time.time() + 600  # 预探测自身上限 10 分钟
        while time.time() < probe_deadline and hard_fails < 10:
            try:
                probe = session.get("https://api.openalex.org/works",
                                    params={"search": "test", "per_page": 1, "mailto": MAILTO}, timeout=30)
                if probe.status_code == 200:
                    probe_ok = True
                    break
                ra = probe.headers.get("Retry-After", "60")
                try:
                    ra_s = float(ra)
                except ValueError:
                    ra_s = 60.0
                if ra_s > 300:
                    LOG["openalex_banned"] = {"retry_after_s": ra,
                                               "note": "IP throttle; rerun with --source all later"}
                    print(f"  OpenAlex banned (Retry-After={ra}s) — skipping openalex part", flush=True)
                    oa_incomplete = True
                    break
                print(f"  OpenAlex short cooldown ({ra_s:.0f}s), waiting...", flush=True)
                time.sleep(min(ra_s + 5, 130))
            except Exception as e:
                hard_fails += 1
                print(f"  OpenAlex probe hard fail ({hard_fails}/10): {e}", flush=True)
                time.sleep(10)
        if not probe_ok and not oa_incomplete:
            # 探测超时/反复硬失败：OpenAlex 未完成，绝不能落入最终写盘分支
            LOG["openalex_probe_timeout"] = True
            oa_incomplete = True
        if probe_ok:
            oa_rows, oa_inc = run_openalex()
            fetched += oa_rows
            oa_incomplete = oa_incomplete or oa_inc
        if oa_incomplete:
            # 配额耗尽/长时封锁/探测失败：保留断点缓存与 S2 暂存；不写 pool/search-log/year-tier
            (LIT / "harvest-v2-log.json").write_text(
                json.dumps(LOG, ensure_ascii=False, indent=1), encoding="utf-8")
            print("OpenAlex incomplete — progress cached in literature/archive/oa-Q*.json;"
                  " rerun with `--source all` when quota resets to resume", flush=True)
            raise SystemExit(2)
    if source in ("all", "s2"):
        fetched += run_s2()
        fetched += run_snowball()
        if source == "s2":
            staging.write_text(json.dumps(fetched, ensure_ascii=False), encoding="utf-8")
            print(f"staging saved: {len(fetched)} rows (S2+snowball); openalex part pending unban")
            return
    if staging.exists() and source == "all":
        staged = json.loads(staging.read_text(encoding="utf-8"))
        have = {("doi:" + r["doi"].lower()) if r["doi"] else ("t:" + norm_key(r["title"])) for r in fetched if r.get("title")}
        fetched += [r for r in staged
                    if ((("doi:" + r["doi"].lower()) if r["doi"] else ("t:" + norm_key(r["title"]))) not in have)]
        print(f"  merged staging: +{len(fetched)} cumulative rows")
    LOG["dedup"]["fetched_total"] = len(fetched)

    pool = dedup(fetched)
    LOG["dedup"]["pool_total"] = len(pool)

    for r in pool:
        r["relevance"] = relevance(r)
        r["tier"] = tier_rule(r)
    pool.sort(key=lambda r: (r["relevance"], r["citations"] or 0), reverse=True)

    # 分层校准：旧池（若有 tier 列）应用 v2 规则 vs 旧记录对照
    old_pool_path = LIT / "archive" / "pool-v1.csv"
    if not old_pool_path.exists():
        shutil.copy2(LIT / "pool.csv", old_pool_path)
        print(f"  backed up old pool -> {old_pool_path}")
    old = list(csv.DictReader(open(old_pool_path, encoding="utf-8-sig")))
    agree = sum(1 for r in old if tier_rule(r) == r.get("tier"))
    from collections import Counter
    old_v2 = Counter(tier_rule(r) for r in old)
    old_rec = Counter(r.get("tier") for r in old)
    LOG["tier"] = {
        "rule": "v2: A = physics-informed x tolerance/assembly-deviation; B = (PI x adjacent manufacturing) or (tolerance x learning, non-PI); C = rest",
        "calibration_on_pool_v1": {"records": len(old), "agreement": agree,
                                    "agreement_pct": round(100 * agree / max(len(old), 1), 1),
                                    "v2_rule_counts": dict(old_v2), "recorded_counts": dict(old_rec)},
    }
    print(f"  tier calibration vs pool-v1: {agree}/{len(old)} agree "
          f"(v2 {dict(old_v2)} vs recorded {dict(old_rec)})")

    cols = ["query_id", "source_db", "title", "authors", "year", "venue", "doi", "citations", "type", "abstract", "relevance", "tier"]
    with open(LIT / "pool.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader(); w.writerows(pool)
    with open(LIT / "pool.json", "w", encoding="utf-8") as f:
        json.dump([{c: r[c] for c in cols} for r in pool], f, ensure_ascii=False)

    ys = sorted({r["year"] for r in pool if r["year"]})
    yts = {str(y): {t: sum(1 for r in pool if r["year"] == y and r["tier"] == t) for t in "ABC"} for y in ys}
    (LIT / "year-tier-stats.json").write_text(json.dumps(yts, ensure_ascii=False, indent=1), encoding="utf-8")

    LOG["finished"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    LOG["pool_summary"] = {"total": len(pool), "tiers": dict(Counter(r["tier"] for r in pool)),
                            "years": f"{ys[0]}-{ys[-1]}" if ys else "-"}
    (LIT / "harvest-v2-log.json").write_text(json.dumps(LOG, ensure_ascii=False, indent=1), encoding="utf-8")

    # search-log.md 追加第三轮（保留历史，不改写）
    oa_rows = "\n".join(
        f"| {q['qid']} | OpenAlex | `{q['query']}` | -（全量） | {q['fetched']} | {q['provenance']} |"
        for q in LOG["openalex"])
    s2_rows = "\n".join(
        f"| {q['qid']} | SemanticScholar | `{q['query']}` | -（全量） | {q['fetched']} | {q['status']} |"
        for q in LOG["s2"])
    sb_rows = "\n".join(f"| {s['seed']} {s['direction']} | SemanticScholar | 引用追踪 | - | {s.get('fetched', 0)} | {s.get('status', 'OK')} |"
                        for s in LOG["snowball"])
    append_md = f"""

---

# 第三轮：全量无上限重检索（{NOW.split(' ')[0]}）

- 动机：评审发现第一/二轮 OpenAlex 每式仅抓取相关性 top-100（未披露截断）；用户裁决全量重检。
- 抓取方式：逐查询 × 逐单年光标分页（per_page=200），无抓取上限；S2 两式 429 失败项带指数退避重试；执行滚雪球（G1+G2 核心引用追踪，首轮未执行的待办）。
- Q8–Q14 检索式为 v2 重拟（原串未随 round-2 存档），主题与 round-2 一致；Q1–Q7 逐字沿用。

| 检索式编号 | 数据库 | 检索式 | 总命中 | 抓取 | 备注 |
|---|---|---|---|---|---|
{oa_rows}
{s2_rows}
{sb_rows}

## 汇总（第三轮）

- 抓取总量（去重前）: {len(fetched)}
- 去重后文献池: {len(pool)}（分层: {dict(Counter(r['tier'] for r in pool))}）
- 分层规则为 v2 重实现（原脚本佚）；对旧池 1,779 条的校准一致率 {round(100*agree/max(len(old),1),1)}%（v2 {dict(old_v2)} vs 旧记录 {dict(old_rec)}），详见 harvest-v2-log.json
- 旧池已备份: literature/archive/pool-v1.csv
"""
    with open(LIT / "search-log.md", "a", encoding="utf-8") as f:
        f.write(append_md)

    print(f"TOTAL_RAW={len(fetched)} POOL={len(pool)} TIERS={dict(Counter(r['tier'] for r in pool))}")


if __name__ == "__main__":
    main()
