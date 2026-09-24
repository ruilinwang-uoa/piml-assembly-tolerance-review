# -*- coding: utf-8 -*-
"""Phase 2.2 筛查导出：新池相对旧池的增量记录 → 分块筛查文件 + 纳入标准卡。

用途：第三轮全量重检（harvest_v2）后，对【新增 Tier A 全部 + Tier B 高相关】记录执行
标题/摘要级筛查（LLM 辅助初筛 + 人工裁决），判决写入 literature/screening/decisions.json，
由 apply_screening.py 合并入编码表。筛查若需设量上限：按 (relevance, citations) 降序截断，
并在 decisions.json 元数据中如实记录截断（截断只可发生于筛查层，抓取层永不截断）。
"""
import csv
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent
LIT = ROOT / "literature"
SCREEN = LIT / "screening"; SCREEN.mkdir(exist_ok=True)
CHUNK = 50
TIER_B_MIN_RELEVANCE = 5   # Tier B 增量进入筛查的相关性阈值（文档化，可调）
SCREENING_CAP = 1200       # 筛查层文档化上限（按 relevance×citations 降序）；None = 不设

CRITERIA = """# 筛查纳入标准（eligibility criteria，与稿件 §2.2 一致，逐字）

**纳入（include）** 要求同时满足：
1. 方法为 learning-based 或 physics-informed（含 loss-based / architecture-based / data-based / hybrid 任一物理融入机制）；
2. 应用对象为 tolerance analysis、assembly deviation/gap prediction、variation propagation、geometry assurance 之一，
   或其直接邻近（fixture layout、tolerance allocation、digital-twin geometry assurance）。

**排除（exclude）** 任一即排除：
1. 术语碰撞的域外工作（optical band gaps、seismic inversion、power systems、fluid/turbulence、biomedical 等）；
2. 无任何物理约束/物理融入机制的纯数据方法（此类若属容差/装配预测则归 M 组基线，标记 baseline 而非 include-physics）；
3. 与制造/装配/容差完全无关的一般 ML/PDE 方法工作。

**判决写法**：decisions.json 中每条 {doi_or_title_key: {"verdict": "include"|"exclude"|"baseline", "group": "G1..G8 或 null", "reason": "一句话"}}。
- include + group → 合并入编码表对应组；
- baseline → 记录但不入物理信息核心统计（M 组基线语义）；
- exclude → 仅留痕。
"""


def norm_key(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())[:80]


def rkey(r):
    return ("doi:" + (r.get("doi") or "").lower()) if r.get("doi") else ("t:" + norm_key(r.get("title")))


def main():
    old = list(csv.DictReader(open(LIT / "archive" / "pool-v1.csv", encoding="utf-8-sig")))
    new = list(csv.DictReader(open(LIT / "pool.csv", encoding="utf-8-sig")))
    old_keys = {rkey(r) for r in old}
    delta = [r for r in new if rkey(r) not in old_keys]
    gone = len(old_keys) - sum(1 for k in (rkey(r) for r in new) if k in old_keys)

    cand = [r for r in delta if r["tier"] == "A" or (r["tier"] == "B" and int(r["relevance"] or 0) >= TIER_B_MIN_RELEVANCE)]
    cand.sort(key=lambda r: (int(r["relevance"] or 0), int(r["citations"] or 0)), reverse=True)
    capped = False
    if SCREENING_CAP is not None and len(cand) > SCREENING_CAP:
        capped = True
        cand = cand[:SCREENING_CAP]

    meta = {
        "old_pool": len(old), "new_pool": len(new), "delta_total": len(delta),
        "delta_by_tier": {t: sum(1 for r in delta if r["tier"] == t) for t in "ABC"},
        "old_pool_records_missing_from_new": gone,
        "candidates": len(cand),
        "tier_b_min_relevance": TIER_B_MIN_RELEVANCE,
        "screening_cap": SCREENING_CAP, "capped": capped,
        "criteria": "Tier A delta: all; Tier B delta: relevance >= %d" % TIER_B_MIN_RELEVANCE,
    }
    print(json.dumps(meta, ensure_ascii=False, indent=1))

    (SCREEN / "CRITERIA.md").write_text(CRITERIA, encoding="utf-8")
    # 分块：每块 50 条，标题/年份/出处/DOI/被引/相关性/摘要
    for i in range(0, len(cand), CHUNK):
        part = cand[i:i + CHUNK]
        lines = [f"# 筛查分块 {i//CHUNK + 1}（记录 {i+1}–{i+len(part)} / 共 {len(cand)}）\n"]
        for j, r in enumerate(part, start=i + 1):
            lines.append(f"## {j}. {r['title']}\n")
            lines.append(f"- year: {r['year']} | venue: {r['venue']} | tier: {r['tier']} | relevance: {r['relevance']} | citations: {r['citations']}")
            lines.append(f"- doi: {r['doi'] or '—'} | key: `{rkey(r)}`")
            lines.append(f"- source: {r['query_id']}\n")
            lines.append(f"**Abstract**: {r['abstract'][:1200] or '(no abstract in metadata)'}\n")
        (SCREEN / f"chunk-{i//CHUNK + 1:03d}.md").write_text("\n".join(lines), encoding="utf-8")
    # decisions 模板 + 元数据
    template = {"_meta": meta, "decisions": {rkey(r): {"title": r["title"][:80], "verdict": "", "group": None, "reason": ""} for r in cand}}
    (SCREEN / "decisions.json").write_text(json.dumps(template, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"chunks written: {(len(cand)+CHUNK-1)//CHUNK}; decisions template: {len(cand)} candidates")


if __name__ == "__main__":
    main()
