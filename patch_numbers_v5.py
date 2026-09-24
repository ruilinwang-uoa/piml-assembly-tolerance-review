# -*- coding: utf-8 -*-
"""Phase 5a-2 数字级联（2026-09-19）：语料冻结 131 条后的全量数字同步。

字符串唯一来源：literature/stats-v4-report.md（build_stats_v4.py 生成）。
关键数字：语料 131；研究类 112（可分类 111）；严格纯仿真 74/111=67%（CI 57–75）；
上界 77/111=69%；含实测 34/111=31%；池 46,239；抓取 64,393；分层 154/1190/44895；
筛查候选 449（35 并入）；Crossref 核验 121/131；Table 2 = 61 行；趋势 z=-0.17 p=0.87。
镜像：manuscript.md + sections/* + delivery 两文档。
"""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent

BODY = [
    # --- 前置件 ---
    ("we screened 1,779 deduplicated records from OpenAlex and Semantic Scholar (2015–2026) into a coded corpus of 94 works",
     "we screened 46,239 deduplicated records from OpenAlex, Semantic Scholar, and Crossref (2015–2026) into a coded corpus of 131 works"),
    ("74% of works are validated on simulation alone",
     "two-thirds of the coded research works (67%, 95% CI 57–75%) are validated on simulation alone"),
    ("3. 74% of 72 coded research works rely on simulation-only validation.",
     "3. 67% of 111 coded research works rely on simulation-only validation."),
    ("the deduplicated literature pool (1,779 records), the coding table (94 works)",
     "the deduplicated literature pool (46,239 records), the coding table (131 works)"),
    # --- §1 ---
    ("conducted following the PRISMA guidelines: fourteen query strings executed across OpenAlex and Semantic Scholar yielded 1,779 deduplicated records, from which tiered screening produced a coded corpus of 94 works organized into eight thematic groups (Section 7.1, Table 2)",
     "conducted following PRISMA principles: seventeen query executions across OpenAlex, Semantic Scholar, and Crossref — re-run without relevance caps and extended with citation snowballing — yielded 46,239 deduplicated records, from which tiered screening produced a coded corpus of 131 works organized into eight thematic groups (Section 7.1, Table 2)"),
    ("Publication volume at the intersection of PIML and manufacturing has grown from a handful of papers in 2019 to several hundred per year in 2025–2026 (Section 2.1, Fig. 1)",
     "Publication volume in PIML broadly has grown from a handful of papers in 2019 to several thousand per year by 2025–2026, while the physics-informed × tolerance/assembly intersection remains a small fraction of it — 154 core-tier records across the whole window (Section 2.1, Fig. 1)"),
    # --- §2.1 全段重写 ---
    ("The review was conducted following the PRISMA guidelines. OpenAlex served as the primary database and Semantic Scholar as a supplementary source. Fourteen query strings were constructed by crossing a physics-informed learning concept block (e.g., \"physics-informed\", \"physics-guided\", \"physics-informed neural network\", \"physics-informed graph learning\") with a tolerance-and-assembly concept block (e.g., tolerance, tolerancing, assembly deviation, assembly gap, variation propagation, skin model, tolerance allocation): seven primary queries (Q1–Q7, executed 2026-09-13, time window 2019–2026) and seven supplementary queries (Q8–Q14, with the window extended to 2015 to capture classical tolerancing and early data-driven work). Three complementary Semantic Scholar queries were attempted, of which one returned results and two were rate-limited; three additional works known to be relevant but not recovered by any query string were located through targeted follow-up searches on Crossref and arXiv. Records were deduplicated by DOI first and by normalized title otherwise, yielding a pool of 1,779 unique records whose annual distribution is shown in Fig. 1.",
     "The review was conducted following PRISMA reporting principles, and the protocol evolved across three rounds with all query logs preserved in the reproducibility package. Rounds 1–2 (2026-09-13) crossed a physics-informed learning concept block (e.g., \"physics-informed\", \"physics-guided\", \"physics-informed neural network\") with a tolerance-and-assembly concept block (e.g., tolerance, tolerancing, assembly deviation, assembly gap, variation propagation, skin model, tolerance allocation): seven primary queries (Q1–Q7, OpenAlex, 2019–2026 window) and seven supplementary queries (Q8–Q14, window extended to 2015), plus three Semantic Scholar queries and targeted Crossref/arXiv follow-ups. An internal audit found that these executions had harvested only the relevance-ranked top 100 records per query — an undisclosed cap — so a third round (2026-09-17 to 2026-09-19) re-executed the protocol without caps: Q1–Q7 verbatim on OpenAlex with full cursor pagination; Q8–Q14, whose original strings were not archived, re-specified and executed on Semantic Scholar and Crossref (title-field search); rate-limited Semantic Scholar queries retried with backoff; and forward and backward citation snowballing executed on the physics-informed assembly core. Records were deduplicated by DOI first and by normalized title otherwise, yielding a pool of 46,239 unique records within the 2015–2026 window whose annual distribution is shown in Fig. 1."),
    # --- §2.2 全段重写 ---
    ("Records were assigned to three relevance tiers by automated title-and-abstract keyword rules: Tier A (physics-informed methods × tolerance/assembly/deviation, 37 records), Tier B (physics-informed methods × adjacent manufacturing and structural domains, 305 records), and Tier C (general PIML methodology, 922 records). Tier A records underwent abstract-level full screening against explicit eligibility criteria: inclusion required a learning-based or physics-informed method applied to tolerance analysis, assembly deviation or gap prediction, variation propagation, or geometry assurance; exclusions removed term collisions outside manufacturing (e.g., optical band gaps, seismic inversion, power systems) and works lacking any physical-constraint mechanism. Classical tolerancing foundations and data-driven predecessors were coded from the supplementary queries and Tiers B–C to establish the review's baseline. Screening produced a coded corpus of 94 works organized into eight thematic groups (G1–G8; Section 7.1, Table 2). The identification, deduplication, and screening flow is summarized in Fig. 2.",
     "Records were assigned to three relevance tiers by automated title-and-abstract keyword rules: Tier A (physics-informed methods × tolerance/assembly/deviation, 154 records), Tier B (physics-informed methods in adjacent manufacturing and structural domains, or tolerance × learning without physics integration, 1,190 records), and Tier C (general PIML methodology and remaining records, 44,895 records). Tier A records and high-relevance Tier B records underwent abstract-level screening against explicit eligibility criteria: inclusion required a learning-based or physics-informed method applied to tolerance analysis, assembly deviation or gap prediction, variation propagation, or geometry assurance; exclusions removed term collisions outside manufacturing (e.g., optical band gaps, seismic inversion, power systems, immunological tolerance) and works lacking any physical-constraint mechanism. The re-harvest delta contributed 449 screening candidates, screened with LLM-assisted first passes under single-author adjudication — 35 inclusions (30 physics-informed works and 5 data-driven baselines) and 414 logged exclusions. Classical tolerancing foundations and data-driven predecessors were coded from the supplementary queries and Tiers B–C to establish the review's baseline. Screening produced a coded corpus of 131 works organized into eight thematic groups (G1–G8; Section 7.1, Table 2). The identification, deduplication, and screening flow is summarized in Fig. 2."),
    # --- §2.3 ---
    ("Bibliographic metadata of all 94 entries were verified against Crossref DOI records (91 verified; two arXiv preprints and one patent were cited from their original sources).",
     "Bibliographic metadata of all 131 entries were verified against Crossref DOI records (121 verified; seven arXiv preprints, one institutional-repository record, one patent, and one thesis were verified from their original sources)."),
    # --- §6.5 ---
    ("Three cross-cutting observations emerge from the 35 coded application works.",
     "Three cross-cutting observations emerge from the 44 coded application works (groups G1–G3)."),
    # --- §7.1 ---
    ("Table 2 positions 52 representative works",
     "Table 2 positions 61 representative works"),
    # --- §7.2 ---
    ("To quantify industrial maturity, we classified every coded research work (excluding reviews, pure method, and knowledge-representation entries, n=72) by validation type: measurement-inclusive (physical measurements used in training or validation) versus simulation-only. The result is stark: **53 of 72 research works (74%) are validated on simulation alone; only 19 (26%) involve physical measurements in any form.** The pattern holds within families: among physics-informed and digital-twin works (n=25 research entries), 18 (72%) are simulation-only; among data-driven deviation predictors (n=15), 10 (67%) are simulation-only.",
     "To quantify industrial maturity, we classified every coded research work by validation type — measurement-inclusive (physical measurements used in training or validation) versus simulation-only — excluding reviews, methodological background, knowledge-representation entries, and entries without a classifiable validation basis (n=111 classifiable of 112 research works). **74 of 111 research works (67%, 95% CI 57–75%) are validated on simulation alone; 34 (31%, 95% CI 23–40%) involve physical measurements in some form.** Because the conservative coding rule assigns simulation-only whenever an abstract is silent about measurements, the simulation-only share is an upper bound. Subgroup shares are statistically indistinguishable at this corpus size: physics-informed and digital-twin works (24 classifiable entries) are simulation-only at 54% (95% CI 35–72%), data-driven predictors (20) at 70% (95% CI 48–85%), classical tolerancing and allocation works (35) at 77% (95% CI 61–88%), and PIML enabling techniques (32) at 63% (95% CI 45–77%) — Wilson intervals overlap broadly — and a Cochran–Armitage trend test finds no significant change in the simulation-only share over publication years (z = −0.17, p = 0.87)."),
    # --- §7.4 ---
    ("1. **The validation gap.** 74% simulation-only validation (§7.2) means the field's central claim — physical consistency yields trustworthiness — is itself not yet validated under physical measurement conditions.",
     "1. **The validation gap.** Simulation-only validation in two-thirds of the corpus (§7.2) means the field's central claim — physical consistency yields trustworthiness — is validated under measurement conditions in only 31% of coded research works."),
    # --- §9 ---
    ("The validation gap is quantitative: 74% of research works in this field are validated on simulation alone",
     "The validation gap is quantitative: 67% of the coded research works (95% CI 57–75%) are validated on simulation alone"),
    ("74% of research works sit at R1, about a quarter present partial R2 evidence",
     "two-thirds of research works (67%) sit at R1, and under a third (31%) present partial R2 evidence"),
    # --- §10 + Limitations ---
    ("Through a systematic, PRISMA-guided survey of 1,779 deduplicated records distilled into a coded corpus of 94 works",
     "Through a systematic, PRISMA-guided survey of 46,239 deduplicated records distilled into a coded corpus of 131 works"),
    ("finding that 74% of research works are validated on simulation alone",
     "finding that two-thirds of research works (67%, 95% CI 57–75%) are validated on simulation alone"),
    ("This review has three limitations. First, the six-dimensional coding is abstract-level rather than full-text; where abstracts provided insufficient information, works were coded conservatively, so fine-grained mechanistic details of individual studies may be under-resolved. Second, literature retrieval interfaces evolve over time, and re-executing the protocol may return modestly different hit counts as new publications are indexed, although the tiering and screening rules are deterministic for a fixed pool. Third, the quantitative analyses are descriptive bibliometric statistics without inferential testing; shares such as the 74% simulation-only validation rate describe this corpus and should not be extrapolated to the field at large without further sampling.",
     "This review has three limitations. First, the coding is abstract-level rather than full-text: where abstracts provided insufficient information, works were coded conservatively, so fine-grained mechanistic details may be under-resolved and the simulation-only share is an upper bound. Second, the search protocol itself carries history: the first two rounds harvested only top-100 results per query (disclosed and remediated by the uncapped third round), the supplementary query strings were re-specified rather than recovered verbatim, the third-round delta screening used LLM-assisted first passes under single-author adjudication, and citation databases evolve so that re-execution may return different counts; all deviations are logged in the reproducibility package. Third, the quantitative analyses are descriptive bibliometric statistics with interval estimates but no inferential claims beyond a single trend test; shares such as the 67% simulation-only validation rate describe this corpus and should not be extrapolated to the field at large without further sampling."),
]

COVER = [
    ("we screened 1,779 deduplicated records (OpenAlex and Semantic Scholar, 2015–2026) into a coded corpus of 94 works",
     "we screened 46,239 deduplicated records (OpenAlex, Semantic Scholar, and Crossref, 2015–2026) into a coded corpus of 131 works"),
    ("74% of coded research works are validated on simulation alone",
     "two-thirds of coded research works (67%, 95% CI 57–75%) are validated on simulation alone"),
    ("3. 74% of 72 coded research works rely on simulation-only validation.",
     "3. 67% of 111 coded research works rely on simulation-only validation."),
]

fails = []


def apply(rel, old, new):
    p = ROOT / rel
    t = p.read_text(encoding="utf-8")
    n = t.count(old)
    if n != 1:
        fails.append(f"{rel}: hit={n} :: {old[:60]}")
        return False
    p.write_text(t.replace(old, new), encoding="utf-8")
    return True


def main():
    patched = 0
    for old, new in BODY:
        ok = apply("manuscript.md", old, new)
        if not ok:
            continue
        # 镜像：该串应恰好出现在一个 section 文件
        hits = [s.name for s in (ROOT / "sections").glob("*.md")
                if old in s.read_text(encoding="utf-8")]
        for name in hits:
            apply(f"sections/{name}", old, new)
        patched += 1
    for old, new in COVER:
        if apply("delivery/cover-letter.md", old, new):
            patched += 1
    print(f"patched: {patched}/{len(BODY) + len(COVER)}")
    if fails:
        print("FAILED:")
        for f in fails:
            print(" -", f)
        raise SystemExit(1)
    # 摘要词数复检
    md = (ROOT / "manuscript.md").read_text(encoding="utf-8")
    a = md[md.index("## Abstract"):md.index("## Highlights")].replace("## Abstract", "").strip()
    print(f"abstract word count: {len(a.split())} (limit 250) {'OK' if len(a.split()) <= 250 else 'OVER — needs trim'}")


if __name__ == "__main__":
    main()
