# -*- coding: utf-8 -*-
"""build_table2_selection —— Table 2（精选对比矩阵）确定性再生成（Phase 4，2026-09-16）。

替代手维护的 literature/table1-selection.md（文件名/表号已过时、A09 缺失违反"G1–G2 全收"规则、
C01 因非数值被引被漏、标题截断、年份与 Crossref 不一致、验证类型映射缺陷——评审 MAJOR #12/#13）。
规则（文档化、确定性）：
  - G1–G2 全收（含 A07/D01/D02/A09 及筛查合并后的新增核心条目）；
  - G3–G8 按被引 top-k（配额沿用历史表实测值，运行时从旧表自校准读取）；
  - 被引源：编码表 OpenAlex 快照；非数值（如 C01"高被引"）→ crossref-verified.json cr_cites；
  - 标题/年份以 crossref-verified.json 为准（全称、去截断、年份同步），无记录时回退编码表；
  - 验证类型 = statslib.val_type（研究类映射；非研究类 → N/A）；
  - 输出英文分析列（方法/机制/保真度/验证），组别列新增；被引非数值记 "—"。
输出：literature/table2-selection.md（11 列）+ literature/table2-meta.json（行数等，供 checker）。
用法：python scripts/build_table2_selection.py [--dry-run]（dry-run 只报告缺失翻译/元数据，不写文件）
"""
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import statslib

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

ROOT = Path(__file__).resolve().parent
LIT = ROOT / "literature"
DRY = "--dry-run" in sys.argv

METHOD_EN = {
    "综述": "Review", "PINN": "PINN", "数字孪生": "Digital twin", "PIGL": "Physics-informed graph learning",
    "物理引导RL": "Physics-guided RL", "代理模型": "Surrogate model", "ML": "ML",
    "Skin Model Shapes": "Skin Model Shapes", "SMS": "Skin Model Shapes", "柔顺装配仿真": "Compliant-assembly simulation",
    "实测驱动": "Measurement-driven", "SOVA状态空间": "SOVA state-space", "优化": "Optimization",
    "算子学习": "Operator learning", "PIML+机理": "PIML + mechanism model", "物理约束BO": "Physics-constrained BO",
    "传统+ML混合": "Classical + ML hybrid", "物理信息DL": "Physics-informed DL", "流形学习+GAN": "Manifold learning + GAN",
    "混合建模": "Hybrid modeling", "物理代理": "Physics-based surrogate", "数字孪生+ML": "Digital twin + ML",
    "GAN": "GAN", "NN-GP": "NN-GP", "GP": "GP", "ML分类": "ML classification", "浅层学习": "Shallow learning",
    "贝叶斯": "Bayesian", "深度RL": "Deep RL", "NN": "NN", "降阶模型": "Reduced-order model",
    "多任务ML": "Multi-task ML", "CGAN代理": "CGAN surrogate", "SMS+FEA": "SMS + FEA",
    "Jacobian-Torsor": "Jacobian–Torsor", "Variational/Vector-loop": "Variational / vector-loop",
    "Jacobian+SMS": "Jacobian + SMS", "Polytope": "Polytope", "统计法": "Statistical method",
    "SMS+热": "SMS + thermal", "制造签名": "Manufacturing signature", "NSMS": "NSMS", "变动建模": "Variation modeling",
    "几何保证": "Geometry assurance", "系统思维": "Systems thinking", "本体": "Ontology",
    "系统级仿真": "System-level simulation", "夹具优化": "Fixture optimization", "影响系数法": "Influence-coefficient method",
    "FEA+实测": "FEA + measurement", "变动分析": "Variation analysis", "SMS生成": "SMS generation",
    "进化算法": "Evolutionary algorithm", "本体+优化": "Ontology + optimization", "采样优化": "Sampling optimization",
    "UQ+可靠性": "UQ + reliability", "成本建模": "Cost modeling", "变动管理": "Variation management",
    "FMECA": "FMECA", "误差优化": "Error optimization", "PINN+在线学习": "PINN + online learning",
    "PINN+迁移": "PINN + transfer", "PIML": "PIML", "PINN+UQ": "PINN + UQ", "物理信息BO": "Physics-informed BO",
    "工具": "Tool", "知识图谱": "Knowledge graph", "物理信息代理": "Physics-informed surrogate",
    "物理信息混合": "Physics-informed hybrid", "图学习代理": "Graph-learning surrogate",
    "学习代理": "Learning surrogate", "强化学习": "Reinforcement learning",
}
MECH_EN = {
    "—": "—", "损失嵌入": "Loss embedding", "无": "None (data-only)", "约束嵌入": "Constraint embedding",
    "数据嵌入": "Data embedding", "混合": "Hybrid", "无(纯数据)": "None (data-only)",
    "架构嵌入(算子)": "Architecture embedding (operator)", "损失嵌入(偏差机理)": "Loss embedding (deviation mechanism)",
    "混合(图+物理损失)": "Hybrid (graph + physics loss)", "架构嵌入(torsor)": "Architecture embedding (torsor)",
    "数据嵌入(物理流形)": "Data embedding (physical manifold)", "机理+数据": "Mechanism + data",
    "模型校准": "Model calibration", "输入不确定性建模": "Input-uncertainty modeling", "输入误差建模": "Input-error modeling",
    "不确定性建模": "Uncertainty modeling", "物理模型降阶": "Physics-based model reduction",
    "状态传播约束": "State-propagation constraint", "架构嵌入": "Architecture embedding", "加权损失": "Weighted loss",
    "损失嵌入(PDE残差)": "Loss embedding (PDE residual)", "损失嵌入(屈曲)": "Loss embedding (buckling)",
    "混合(图+约束)": "Hybrid (graph + constraint)",
}
FID_EN = {
    "仿真": "Simulation", "—": "—", "实测": "Measurement", "实测+仿真": "Measurement + simulation",
    "仿真+实测": "Simulation + measurement", "单保真": "Single-fidelity", "多保真(DT)": "Multi-fidelity (DT)",
    "实测+机理": "Measurement + mechanism", "FEA仿真": "FEA simulation", "多保真": "Multi-fidelity",
    "知识": "Knowledge", "知识+仿真": "Knowledge + simulation", "无数据": "Data-free",
    "在线数据": "Online data", "经验知识": "Empirical knowledge",
}
# 场景值级兜底（筛查并入条目的固定场景词表；优先用 SCEN_EN 逐条翻译）
SCEN_VALUE_EN = {
    "容差分析(筛查并入)": "Tolerance analysis (screening merge)",
    "容差分配": "Tolerance allocation",
    "装配偏差/变形预测(筛查并入)": "Assembly deviation/deformation prediction (screening merge)",
    "焊接变形预测(筛查并入)": "Welding distortion prediction (screening merge)",
    "夹具布局(筛查并入)": "Fixture layout (screening merge)",
    "几何质量预测(筛查并入)": "Geometric quality prediction (screening merge)",
    "制造几何相关(筛查并入)": "Manufacturing-geometry application (screening merge)",
}

# 逐条应用场景英文（按 ID；2026-09-16 依据编码表场景列翻译，dry-run 校验全覆盖）
SCEN_EN = {
    "A01": "Dynamic prediction of stringer-assembly deviations (aircraft)",
    "A02": "Assembly-deviation prediction in bolted flange connections",
    "A03": "Actuator placement in composite-structure assembly",
    "A04": "Variation propagation in large-scale assembly",
    "A05": "Fixture layout for thin-walled parts (assembly deformation)",
    "A06": "Active lens alignment (precision assembly)",
    "A07": "Multi-fidelity graph surrogate (scenario pending full-text check)",
    "A08": "Rapid assembly stress-field prediction",
    "A09": "Assembly deviation to sealing leakage (fuel cells)",
    "A10": "Direct tolerance-analysis application (CAT 2026)",
    "A11": "ERS point-layout planning in aircraft assembly",
    "C01": "General forward/inverse PDE solving",
    "C02": "PINN methods and trends (survey)",
    "C04": "PINN evolution (systematic review)",
    "C06": "PINNs for laminated composites",
    "C08": "Automated PINN tooling",
    "D01": "Large-diameter cabin-section docking assembly",
    "D02": "Assembly-precision inversion for industrial equipment",
    "D03": "Online geometry assurance in sheet-metal assembly",
    "D04": "Clamping-sequence optimization in sheet-metal assembly",
    "D05": "Welding-quality prediction in ship assembly",
    "E01": "Data-free surrogate for engineering optimization",
    "E04": "Contact-mechanics forward/inverse problems",
    "E05": "Complex beam systems (wing-adjacent)",
    "E06": "Domain-similarity transfer learning",
    "E08": "Robotic welding",
    "E09": "Uncertainty-weighted training",
    "E13": "Parametric PDE surrogate (tolerance transfer pending)",
    "E14": "Nonlinear operator learning for PDEs (tolerance transfer pending)",
    "K01": "Tolerancing-experience acquisition and reuse",
    "K02": "Curvilinear-fiber wing optimization",
    "M01": "End-to-end sheet-metal deviation prediction",
    "M02": "Composite-assembly deviation and residual stress",
    "M04": "Feed-forward dimensional-variation control of composite parts",
    "M05": "Anomaly detection on Skin Model Shapes",
    "M07": "Quality prediction in multistage manufacturing",
    "M08": "Part-quality estimation in multistage manufacturing",
    "M11": "Spot-weld sequencing under geometric deviations",
    "M13": "Real-time compliant-assembly variation simulation",
    "O01": "Tolerance allocation for complex assemblies",
    "O02": "Geometric tolerance determination in non-rigid assembly",
    "O07": "Tolerance management in composite-structure design",
    "O09": "Visual-quality–sustainability tolerance optimization",
    "O10": "Coaxiality in CNC turning",
    "T02": "Geometric-variation management (survey)",
    "T03": "Tolerance analysis with form errors and local deformation",
    "T04": "Rigid-part tolerance analysis (manufacturing signature)",
    "T05": "Rigid-part tolerance analysis",
    "T08": "General framework for assembly tolerance analysis",
    "T15": "Virtual geometry-assurance process",
    "T22": "Non-rigid assembly simulation (ANATOLEFLEX)",
    "T24": "Fixture layout in compliant sheet-metal assembly",
    "T32": "Variation propagation in multistage manufacturing (book)",
    "T33": "State-space modeling for sheet-metal dimensional control",
}


def historical_quotas():
    """从旧 table1-selection.md 实测各非核心组配额（保持历史选录函数不变）。"""
    old = LIT / "table1-selection.md"
    if not old.exists():
        return {"G3": 8, "G4": 10, "G5": 5, "G6": 7, "G7": 5, "G8": 2}
    import re
    counts = Counter()
    for ln in old.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*([A-Z])\d{2}\s*\|", ln)
        if m:
            counts[statslib.PREFIX2GROUP[m.group(1)]] += 1
    return {g: counts.get(g, 0) for g in ("G3", "G4", "G5", "G6", "G7", "G8")}


def main():
    recs = statslib.parse_coding_table(LIT / "coding-table.md")
    cv_path = LIT / "crossref-verified.json"
    cv = json.loads(cv_path.read_text(encoding="utf-8")) if cv_path.exists() else {}
    quotas = historical_quotas()

    def cites(r):
        if r["citations"] is not None:
            return r["citations"], "OA-snapshot"
        c = (cv.get(r["id"]) or {}).get("cr_cites")
        return (int(c), "Crossref") if c is not None else (-1, "—")

    selected = [r for r in recs if r["group"] in ("G1", "G2")]
    for g, k in quotas.items():
        pool = [r for r in recs if r["group"] == g]
        pool.sort(key=lambda r: (-cites(r)[0], r["id"]))
        selected += pool[:k]
    selected.sort(key=lambda r: r["id"])

    missing_scen = [r["id"] for r in selected if r["id"] not in SCEN_EN]
    missing_meta = [r["id"] for r in selected if r["id"] not in cv and r["doi"] not in ("", "—")]
    print(f"selection: {len(selected)} rows (G1–G2 full + quotas {quotas})")
    print(f"missing scenario EN: {missing_scen}")
    print(f"missing crossref meta: {missing_meta}")
    if DRY:
        return
    # 场景兜底：缺逐条翻译的用值级词表；仍缺则报错
    unresolved = [r["id"] for r in selected
                  if r["id"] not in SCEN_EN and r["scenario"] not in SCEN_VALUE_EN]
    assert not unresolved, f"SCEN 翻译缺 {unresolved}"
    missing_scen = [r["id"] for r in selected if r["id"] not in SCEN_EN and r["scenario"] in SCEN_VALUE_EN]

    hdr = ("| Ref | Work (title) | Year | Venue | Group | Method family | Physics integration | "
           "Application scenario | Fidelity | Validation | Citations |")
    lines = [
        "# Table 2 精选对比矩阵（§7.1 用，确定性生成）",
        "",
        f"> 生成：{date.today()}，scripts/build_table2_selection.py。规则：G1–G2 全收 + G3–G8 按被引 top-k（配额 {quotas}，自旧表校准）。",
        "> 标题/年份以 crossref-verified.json 为准；被引 = OpenAlex 快照（非数值以 Crossref 计数替代，标 — 为无记录）。",
        "> 验证类型 = statslib.val_type（摘要级保守编码，与 §2.3 声明一致）。",
        "",
        hdr,
        "| " + " | ".join(["---"] * 11) + " |",
    ]
    for r in selected:
        meta = cv.get(r["id"]) or {}
        title = meta.get("cr_title") or r["title"]
        year = meta.get("cr_year") or r["year"]
        cval, _ = cites(r)
        cval = str(cval) if cval >= 0 else "—"
        vt = statslib.val_type(r) if statslib.entry_class(r) == "research" else "N/A"
        lines.append(" | ".join([
            f"| {r['id']}", title.replace("|", "/"), str(year), (meta.get("cr_venue") or r["venue"]).replace("|", "/"),
            r["group"], METHOD_EN.get(r["method"], r["method"]), MECH_EN.get(r["mechanism"], r["mechanism"]),
            SCEN_EN.get(r["id"]) or SCEN_VALUE_EN[r["scenario"]],
            FID_EN.get(r["fidelity"], r["fidelity"]), vt, f"{cval} |",
        ]))
    (LIT / "table2-selection.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (LIT / "table2-meta.json").write_text(json.dumps({
        "rows": len(selected), "quotas": quotas, "generated": str(date.today()),
        "g1g2_full": sum(1 for r in recs if r["group"] in ("G1", "G2")),
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"written: table2-selection.md ({len(selected)} rows) + table2-meta.json")


if __name__ == "__main__":
    main()
