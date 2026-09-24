# -*- coding: utf-8 -*-
"""statslib —— 语料统计规则的唯一权威实现（v4，2026-09-16）

被 build_stats_v4.py / build_figures.py / build_table2_selection.py / check_consistency.py 共用。
规则变更必须在本文件 docstring 中记录，并重跑 build_stats_v4.py（语料冻结后任何规则变更即重开统计阶段）。

分类规则（entry_class）——"研究类" vs "非研究类"：
  非研究类，若满足任一：
    R1. 前缀 C（G7 方法与综述背景）或 K（G8 知识表示）——方法学/综述/知识表示条目；
    R2. 方法类别（方法列）含 "综述" —— 即使落在 T 等应用组，综述条目不参与验证统计
        （修复：T19 旧口径中被计入 53 篇纯仿真）；
    R3. 保真度为 "—" 或 "知识" —— 无验证基础（综述/知识/工具条目）。
  其余为研究类（含多保真/多保真(DT)/在线数据条目——修复 v3 将 A07/D01/D02 误逐出研究集的映射缺陷）。

保真度→验证类型映射（val_type）——摘要级保守编码，逐条规则及理由：
  实测+机理 / 实测            → Meas.-incl.        （物理机理 + 实测数据）
  在线数据                    → Meas.-incl.        （在线采集 = 实测来源）
  仿真+实测                   → Meas.+Sim.         （两种证据并用）
  仿真 / FEA仿真              → Sim.-only          （纯仿真验证）
  无数据                      → Sim.-only          （数据无关代理，保守归入仿真类）
  单保真                      → Sim.-only          （单一保真度源；v3 期为 A09 的隐性规则，此处显式化）
  多保真 / 多保真(DT)         → Multi-fidelity (sim.-based)  （v4 新类：研究类、以仿真为锚的多源保真；
                                                                数字孪生 (DT) 条目的在线几何数据在摘要级
                                                                保守处理为仿真锚定，方向性偏差已在 §2.3 声明）
  知识 / 知识+仿真 / —        → N/A                （非研究类，不进入验证统计）
  OVERRIDES                   → 逐条人工覆盖表（当前为空；单保真规则已显式覆盖 A09 场景）。
"""
import re
from pathlib import Path

# ---------- 组元数据 ----------
GROUPS = {
    "G1": {"prefix": "A", "zh": "PIML × 装配/容差 核心", "en": "PIML × assembly/tolerance core"},
    "G2": {"prefix": "D", "zh": "数字孪生与在线几何保证", "en": "Digital twins & online geometry assurance"},
    "G3": {"prefix": "M", "zh": "数据驱动/ML 偏差预测", "en": "Data-driven ML deviation prediction"},
    "G4": {"prefix": "T", "zh": "传统容差分析与变动建模", "en": "Classical tolerance analysis & variation modeling"},
    "G5": {"prefix": "O", "zh": "容差分配与优化", "en": "Tolerance allocation & optimization"},
    "G6": {"prefix": "E", "zh": "PIML 使能技术", "en": "PIML enabling technologies"},
    "G7": {"prefix": "C", "zh": "方法与综述背景", "en": "Methods & review background"},
    "G8": {"prefix": "K", "zh": "知识表示 × 容差", "en": "Knowledge representation × tolerancing"},
}
PREFIX2GROUP = {v["prefix"]: k for k, v in GROUPS.items()}

# 验证类型显示顺序（图 5 / 表 2 / 统计报告一致使用）
VAL_ORDER = ["Sim.-only", "Multi-fidelity (sim.-based)", "Meas.-incl.", "Meas.+Sim.", "N/A"]

# 逐条人工覆盖表：{"A07": "Meas.+Sim.", ...} —— 变更须在文件头 docstring 记录理由
OVERRIDES = {}


def parse_coding_table(path):
    """解析 coding-table.md → list[dict]（命名字段；不信任列序，按表头名映射）。"""
    text = Path(path).read_text(encoding="utf-8")
    header_zh = ["编号", "文献", "年份", "出处", "被引", "方法", "机制", "场景", "保真度", "DOI"]
    rows = []
    for line in text.splitlines():
        if not (line.startswith("| ") and "---" not in line):
            continue
        cells = [x.strip() for x in line.strip("|").split("|")]
        if len(cells) < 10 or not re.fullmatch(r"[A-Z]\d{2}", cells[0]):
            continue
        rows.append(dict(zip(header_zh, cells[:10])))
    recs = []
    for r in rows:
        raw_cit = r["被引"]
        try:
            cit = int(raw_cit)
        except ValueError:
            cit = None  # "高被引" / "—" 等非数值
        recs.append({
            "id": r["编号"], "title": r["文献"], "year": r["年份"], "venue": r["出处"],
            "citations": cit, "citations_raw": raw_cit,
            "method": r["方法"], "mechanism": r["机制"], "scenario": r["场景"],
            "fidelity": r["保真度"], "doi": r["DOI"],
            "prefix": r["编号"][0], "group": PREFIX2GROUP[r["编号"][0]],
        })
    return recs


def entry_class(rec):
    """'research' | 'non-research'（规则见文件头 docstring R1–R3）。"""
    if rec["prefix"] in ("C", "K"):
        return "non-research"
    if "综述" in rec["method"]:
        return "non-research"
    if rec["fidelity"] in ("—", "知识"):
        return "non-research"
    return "research"


def val_type(rec):
    """保真度→验证类型（映射规则见文件头 docstring；OVERRIDES 优先）。"""
    if rec["id"] in OVERRIDES:
        return OVERRIDES[rec["id"]]
    f = rec["fidelity"]
    if "实测" in f and "仿真" in f:
        return "Meas.+Sim."
    if "实测" in f or "在线" in f:
        return "Meas.-incl."
    if f in ("仿真", "FEA仿真", "无数据", "单保真"):
        return "Sim.-only"
    if f in ("多保真", "多保真(DT)"):
        return "Multi-fidelity (sim.-based)"
    return "N/A"  # 知识 / 知识+仿真 / — 及未知值


def wilson(k, n, z=1.96):
    """Wilson 95% 置信区间（比例 k/n），返回 (lo, hi)；n==0 返回 (0.0, 0.0)。"""
    if n == 0:
        return 0.0, 0.0
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return (c - h) / d, (c + h) / d


def trend_test(yearly):
    """Cochran–Armitage 趣势检验（纯 Python，正态近似）。

    yearly: [(year, k_sim, n_total), ...] 按年升序、n_total>0。
    检验 H0: 各年 sim 比例无趋势 vs H1: 随年份线性变化（双侧）。
    返回 (stat_z, p_value)；样本过小（总 n<20 或年数<3）返回 (None, None)。
    """
    import math
    pts = [(y, k, n) for (y, k, n) in yearly if n > 0]
    if len(pts) < 3:
        return None, None
    scores = [y for (y, _, _) in pts]
    ks = [k for (_, k, _) in pts]
    ns = [n for (_, _, n) in pts]
    N = sum(ns); K = sum(ks)
    if N < 20 or K == 0 or K == N:
        return None, None
    ybar = sum(s * n for s, n in zip(scores, ns)) / N
    T = sum(k * (s - ybar) for k, s in zip(ks, scores))
    S2 = (K * (N - K) / (N - 1)) * sum(n * (s - ybar) ** 2 for s, n in zip(scores, ns))
    if S2 <= 0:
        return None, None
    z = T / (S2 ** 0.5)
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / (2 ** 0.5))))
    return round(z, 3), round(p, 4)


def validation_stats(recs):
    """研究类验证统计汇总（供 build_stats_v4 / 报告使用）。"""
    research = [r for r in recs if entry_class(r) == "research"]
    nonresearch = [r for r in recs if entry_class(r) != "research"]
    vt = {}
    for r in research:
        vt[val_type(r)] = vt.get(val_type(r), 0) + 1
    return {"research": research, "non_research": nonresearch, "val_counts": vt}


if __name__ == "__main__":
    # 冒烟自检：解析 + 打印映射表与统计口径，供人工签核
    root = Path(__file__).resolve().parent
    recs = parse_coding_table(root / "literature" / "coding-table.md")
    print(f"parsed {len(recs)} coding-table rows")
    from collections import Counter
    print("groups:", dict(sorted(Counter(r['group'] for r in recs).items())))
    stats = validation_stats(recs)
    print(f"research n={len(stats['research'])}  non-research n={len(stats['non_research'])}")
    print("validation-type counts (research):", {k: stats['val_counts'].get(k, 0) for k in VAL_ORDER})
    for r in sorted(stats["research"], key=lambda x: x["id"]):
        print(f"  {r['id']}: fidelity={r['fidelity']!r:14} -> {val_type(r)}")
