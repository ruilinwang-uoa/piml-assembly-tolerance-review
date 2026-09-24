# -*- coding: utf-8 -*-
"""Phase 5a-1 无数字补丁：主张校准 + C05 改指 + 交叉引用修正 + 术语统一 + 前置件去脚手架。

范围：仅不依赖统计数字的修订（数字级联由 patch_numbers_v5.py 在语料冻结+stats-v4 后执行）。
依据：PRE_SUBMISSION_REVIEW_2026-09-16 CRITICAL #1/#3/#5 + MAJOR 若干（Agent 1/2/3/4 清单）。
镜像约定：manuscript.md 命中恰 1 次；sections/ 恰 1 个文件含同串（同步替换）。
"""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent
M = "manuscript.md"
SEC = [f"sections/{n}" for n in [
    "00-front-matter.md", "01-introduction.md", "02-review-methodology.md", "03-background.md",
    "04-data-driven.md", "05-piml-taxonomy.md", "06-applications.md", "07-comparative.md",
    "08-open-challenges.md", "09-practical-implications.md", "10-conclusion.md"]]

# (old, new) —— 正文补丁（manuscript + 镜像 section）
BODY = [
    # --- 前置件 ---
    ("# 前置件（Front Matter）", "# Front matter"),
    ("## Abstract（≤250 词）", "## Abstract"),
    ("（词数：约 245 ✅；首句直击现实制造难题 ✅；末句强调对生产系统决策的支持 ✅）\n", ""),
    ("force an unsatisfying choice", "force an unsatisfactory choice"),
    ("Following PRISMA guidelines, 1,779 deduplicated records from OpenAlex and Semantic Scholar (2015–2026) were screened into a coded corpus of 94 works.",
     "Following PRISMA principles, we screened 1,779 deduplicated records from OpenAlex and Semantic Scholar (2015–2026) into a coded corpus of 94 works."),
    ("and none yet deploys a physics-informed model as the online core of a production geometry-assurance system",
     "and no coded work yet deploys a physics-informed model as the online core of a production geometry-assurance system"),
    ("The findings indicate that the field's limiting factor has shifted from algorithms to validation evidence and integration infrastructure, and they provide",
     "The synthesis suggests that validation evidence and integration infrastructure, more than method novelty, now limit deployment readiness, and the findings provide"),
    ("## Highlights（3–5 条，每条 ≤85 字符）", "## Highlights"),
    ("1. First systems-level review of physics-informed ML for assembly tolerance analysis.（83 字符 ✅）",
     "1. A systems-level review of physics-informed ML for assembly tolerance analysis."),
    ("2. A 3D taxonomy: integration mechanism × task type × data fidelity.（66 字符 ✅）",
     "2. A 3D taxonomy: integration mechanism × task type × data fidelity."),
    ("3. 74% of 72 coded research works rely on simulation-only validation.（66 字符 ✅）",
     "3. 74% of 72 coded research works rely on simulation-only validation."),
    ("4. No physics-informed model yet runs a production geometry-assurance loop.（73 字符 ✅）",
     "4. No coded work yet deploys a PIML core in a production geometry loop."),
    ("5. Research agenda: robustness, multi-fidelity fusion, self-adaptive surrogates.（78 字符 ✅）",
     "5. Research agenda: robustness, multi-fidelity fusion, self-adaptive surrogates."),
    ("## Keywords（1–7 个，四分类）", "## Keywords"),
    ("## 作者贡献声明（CRediT 占位）", "## CRediT authorship contribution statement"),
    ("（**待按实际作者分工填写**）", " *[To be completed per actual author contributions before submission.]*"),
    ("## Declaration of competing interest（占位）", "## Declaration of competing interest"),
    ("（**待确认**）", ""),
    ("## Data availability（占位 — DOI 待挂）", "## Data availability"),
    ("（**待办：Zenodo 沉积需作者账号操作；投稿前将占位替换为 \"available at https://doi.org/10.5281/zenodo.XXXXXXX\"。仓库内容清单见 delivery/reproducibility/README.md**）",
     " *[DOI to be inserted upon Zenodo deposition before submission.]*"),
    # --- §1 ---
    ("physics-informed neural networks (PINNs) [C01], physics-informed graph learning [C05], and their multi-fidelity and transfer-learning extensions",
     "physics-informed neural networks (PINNs) [C01] and physics-informed graph learning [A02], together with their multi-fidelity and transfer-learning extensions"),
    ("(Section 7, Fig. 1)", "(Section 2.1, Fig. 1)"),
    ("Existing surveys leave this intersection uncharted.", "Among the surveys we identified, none consolidates this intersection."),
    ("(loss-based, architecture-based, data-based, hybrid)", "(loss embedding, architecture embedding, data embedding, hybrid)"),
    ("task type (forward prediction, inverse identification, surrogate modeling, uncertainty quantification)",
     "task type (forward prediction/surrogate modeling, inverse identification, uncertainty quantification, optimization and control)"),
    ("The remainder of this paper is organized", "The remainder of this review is organized"),
    # --- §3.1 ---
    ("while root-sum-square (RSS) and Monte Carlo simulation trade conservatism for realism by exploiting the statistical independence of deviation sources [T09]",
     "while root-sum-square (RSS) stacking exploits the statistical independence of deviation sources and a linearization of the dimensional chain to combine variances in closed form, and Monte Carlo simulation trades conservatism for realism by sampling correlated and nonlinear chains that RSS cannot represent [T09]"),
    ("has been embedded into Jacobian and torsor models [T04], variational and vector-loop models [T05], and combined with",
     "has been embedded into Jacobian and torsor models [T04] and variational and vector-loop models [T05], and combined with"),
    ("Convex-set formulations, notably polytope-based models", "Convex-set formulations, in particular polytope-based models"),
    ("Anomaly detection over Skin Model Shapes representations", "Anomaly detection on Skin Model Shapes representations"),
    # --- §4 ---
    ("Recognizing that point predictions are insufficient for tolerance decisions, a third route foregrounds uncertainty.",
     "Because point predictions are insufficient for tolerance decisions, a third route foregrounds uncertainty."),
    ("a framing that the PIML literature later absorbs and extends (§5.3)", "a framing that the PIML literature later absorbs and extends (§5.2)"),
    ("for composite parts assembly processes", "for composite-part assembly processes"),
    ("with respect to geometrical deviations", "with respect to geometric deviations"),
    ("None of the reviewed works demonstrates reliable extrapolation beyond the training envelope without corrective re-training.",
     "No coded abstract reports reliable extrapolation beyond the training envelope without corrective re-training."),
    # --- §5.1/§5.2 ---
    ("Automatic differentiation makes the physics term exact with respect to the network's continuous output, eliminating discretization error at the loss level and, crucially for tolerancing,",
     "Automatic differentiation makes the physics term exact with respect to the network's continuous output — no discretized derivative operator is required, though the residual is still evaluated at finitely many collocation points — and, crucially for tolerancing,"),
    ("replaces the coordinate-MLP with message-passing networks over meshes or graphs [C05], aligning",
     "replaces the coordinate-MLP with message-passing networks over meshes or graphs, as demonstrated for bolted-flange assembly deviation prediction [A02], aligning"),
    ("graph topologies mirroring assembly interfaces [C05, A02]", "graph topologies mirroring assembly interfaces [A02]"),
    ("or mechanistically structured features (e.g., deviation mechanisms coupled with machine learning for assembly quality prediction [A01])",
     "or data drawn from physics-structured manifolds (e.g., manifold-learning-augmented generation of assembly stress fields [A08])"),
    ("This is the lightest-weight mechanism", "This is the lightest mechanism"),
    # --- §5.3 ---
    ("has not yet been systematically studied in tolerance applications", "has, to our knowledge, not yet been systematically studied in tolerance applications"),
    ("These four techniques map directly onto the limitations of §4.5: transfer and online learning attack out-of-distribution fragility; loss and architecture embedding attack physical inconsistency; multi-fidelity operation attacks data scarcity.",
     "These four techniques map directly onto the limitations of §4.5: transfer and online learning attack out-of-distribution fragility and data scarcity by adapting trained models to new envelopes and streaming data, while physics-constrained Bayesian optimization and physics-guided reinforcement learning embed physical consistency directly into decision-making."),
    # --- §6 ---
    ("(hybrid × forward surrogate × simulation+measurement)", "(hybrid × forward surrogate × multi-fidelity)"),
    ("to perceive flatness out-of-tolerance conditions dynamically", "to detect out-of-tolerance flatness conditions dynamically"),
    ("exemplifying data embedding: the physics enters through mechanistically structured features rather than through loss terms",
     "exemplifying loss embedding: the physics enters through the deviation-propagation mechanism embedded in the learning objective rather than through the architecture"),
    ("demonstrating efficient evaluation within the CAT community", "demonstrating efficient evaluation for the CAT community"),
    ("predict assembly stress fields rapidly", "rapidly predict assembly stress fields"),
    ("This line is where PIML meets the systems-level integration criterion", "This line is where PIML meets the system-level integration criterion"),
    ("Notably, current implementations predominantly use *data-driven* models inside the twin",
     "Current twin implementations in the coded corpus predominantly use *data-driven* models"),
    ("where alignment quality plays the role of assembly geometric quality", "where alignment quality is the analogue of assembly geometric quality"),
    ("Assembly-deviation-induced sealing leakage in PEMFC stacks couples deviation mechanisms",
     "Analysis of assembly-deviation-induced sealing leakage in PEMFC stacks couples deviation mechanisms"),
    ("they provide transferrable evidence of PIML's viability", "they provide transferable evidence of PIML's viability"),
    ("These adjacent domains matter for this review for two reasons", "These adjacent domains matter to this review for two reasons"),
    # --- §7 ---
    ("graph message passing [A02, C05]", "graph message passing [A02]"),
    ("The corpus reveals a near-total absence of shared benchmarks.", "The corpus reveals an absence of shared benchmarks."),
    ("each study constructs its own simulation campaign or proprietary measurement set",
     "each coded study constructs its own simulation campaign or proprietary measurement set"),
    ("Reproducibility practices are correspondingly weak: code and data availability statements are the exception rather than the norm.",
     "Reproducibility practices are correspondingly weak: across the coded corpus, code and data availability is the exception rather than the norm."),
    ("ad-hoc efficiency ratios", "ad hoc efficiency ratios"),
    ("they appear as ad-hoc speedup ratios", "they appear as ad hoc speedup ratios"),
    ("which jointly position each method family on the axes (industrial maturity, data fidelity) that the corpus can actually support",
     "which position each method family by thematic group and validation type — the axes the corpus can actually support"),
    ("would assert a cross-study comparability", "would assert cross-study comparability"),
    # --- §8 ---
    ("current physics-informed predictors are **static artifacts** — trained once, deployed frozen, and silently degrading when the operating envelope drifts (§5.3, §7.4 shortfall 5)",
     "current physics-informed predictors are **static artifacts** — trained once and, if deployed, frozen — with silent degradation to be expected when the operating envelope drifts (§5.3, §7.4 shortfall 5)"),
    ("but no reviewed work has yet assembled them into a closed, self-governing loop", "but no coded work has yet assembled them into a closed, self-governing loop"),
    ("potentially organized as collaborating agents around the surrogate model itself", "potentially organized as coordinated agents around the surrogate model itself"),
    ("We flag this as the single most consequential direction for the field.", "We flag this as arguably the most consequential direction for the field."),
    ("raises requirements the literature has not yet engaged", "raises requirements that the coded literature has not yet engaged"),
    ("within the CPPS layering of physical, information, and control layers, with explicit products/equipment/information/control integration points (Fig. 6)",
     "within the four-layer CPPS stack of equipment, information, control, and application layers, with explicit integration points across products, equipment, information, and control (Fig. 6)"),
    ("that coordinating agents would require", "that coordinated agents would require"),
    # --- §9 ---
    ("no physics-informed model has yet operated as the online core of a production geometry-assurance system (§7.2)",
     "no coded work documents a physics-informed model operating as the online core of a production geometry-assurance system (§7.2)"),
    ("no physics-informed model has yet crossed the R2→R3 gate", "no coded physics-informed work documents crossing the R2→R3 gate"),
    ("but every deployment should know, and document, which rung it occupies",
     "but the deploying organization should know and document which rung each deployment occupies"),
    ("Tolerance analysis in most manufacturers already generates three data tiers",
     "In typical manufacturing organizations, tolerance analysis already generates three data tiers"),
    ("These monitors are implementable in weeks and directly mitigate the single largest deployment risk identified by this review.",
     "These monitors require no new modeling expertise to implement and directly mitigate what this review identifies as a central deployment risk."),
    ("The evidence (§5–§7) indicates physics-informed learning earns",
     "Our synthesis of the coded corpus (§5–§7) suggests that physics-informed learning earns"),
    # --- §10/Limitations ---
    ("Three limitations of this review should be noted.", "This review has three limitations."),
    ("from a promising literature into dependable manufacturing practice", "from a promising research field into dependable manufacturing practice"),
    # --- 全局连字符/风格 ---
    ("accurate-but-slow finite element campaigns", "accurate-but-slow finite-element campaigns"),
    ("implies a finite element simulation or a physical measurement campaign", "implies a finite-element simulation or a physical measurement campaign"),
    ("whether finite element solvers, surrogate models, or physics-informed networks", "whether finite-element solvers, surrogate models, or physics-informed networks"),
    ("or dimensional chain constraints", "or dimensional-chain constraints"),
]

# 封面信同步（仅 2 处无数字项）
COVER = [
    ("First systems-level review of physics-informed ML for assembly tolerance analysis.",
     "A systems-level review of physics-informed ML for assembly tolerance analysis."),
    ("no physics-informed model yet operates as the online core of a production geometry-assurance system",
     "no coded work yet documents a physics-informed model operating as the online core of a production geometry-assurance system"),
]

fails = []


def apply(rel, old, new, want):
    p = ROOT / rel
    t = p.read_text(encoding="utf-8")
    n = t.count(old)
    if n != want:
        fails.append(f"{rel}: 期望 {want}, 实得 {n} :: {old[:60]}")
        return False
    if new is not None and new != old:
        p.write_text(t.replace(old, new), encoding="utf-8")
    return True


def main():
    patched = 0
    for old, new in BODY:
        ok = apply(M, old, new, 1)
        # 镜像：恰好一个 section 文件应含同串（前置件补丁在 00；正文在对应节）
        hits = [s for s in SEC if (ROOT / s).read_text(encoding="utf-8").count(old) >= 1]
        if not ok:
            continue
        for s in hits:
            apply(s, old, new, 1)
        if len(hits) > 1:
            fails.append(f"镜像多命中（{len(hits)} 个 section）: {old[:60]}")
        patched += 1
    for old, new in COVER:
        if apply("delivery/cover-letter.md", old, new, 1):
            patched += 1
    print(f"patched: {patched}/{len(BODY) + len(COVER)}")
    if fails:
        print("FAILED:")
        for f in fails:
            print(" -", f)
        raise SystemExit(1)
    print("OK: 全部无数字主张补丁已应用（manuscript + sections 镜像 + cover letter）")


if __name__ == "__main__":
    main()
