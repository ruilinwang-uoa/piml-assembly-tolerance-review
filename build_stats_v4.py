# -*- coding: utf-8 -*-
"""build_stats_v4 —— 语料冻结后的一次性统计重建（Phase 3，2026-09-16）。

替代 build_stats_v3.py（其计数为硬编码字面量，从未读取编码表；评审 CRITICAL #1/#6）。
规则全部来自 statslib.py（唯一权威）；本脚本只做汇总，不做任何规则决策。
输出：
  literature/section6-stats-v4.json   —— 机读（图件/表格/checker/正文补丁共用）
  literature/stats-v4-report.md       —— 人读 crib sheet（正文补丁字符串的唯一来源）

口径定义（与 statslib 一致）：
  research        = entry_class == "research"
  sim_strict      = 验证类型 == Sim.-only                     （严格纯仿真份额分子）
  sim_upper       = Sim.-only + Multi-fidelity (sim.-based)   （保守编码下的纯仿真上界分子）
  meas            = Meas.-incl. + Meas.+Sim.
  验证可分类基数 n_classifiable = research 中验证类型 != N/A
"""
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import statslib

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

ROOT = Path(__file__).resolve().parent
LIT = ROOT / "literature"


def pct(k, n):
    return round(100 * k / n, 1) if n else None


def ci_str(k, n):
    lo, hi = statslib.wilson(k, n)
    return f"95% CI {round(lo*100)}–{round(hi*100)}%" if n else "-"


def subgroup(recs, prefixes):
    sub = [r for r in recs if statslib.entry_class(r) == "research" and r["prefix"] in prefixes]
    vt = Counter(statslib.val_type(r) for r in sub)
    sim = vt.get("Sim.-only", 0)
    sim_ub = sim + vt.get("Multi-fidelity (sim.-based)", 0)
    meas = vt.get("Meas.-incl.", 0) + vt.get("Meas.+Sim.", 0)
    n_class = sum(v for k, v in vt.items() if k != "N/A")
    return {"n": len(sub), "n_classifiable": n_class,
            "sim_strict": sim, "sim_strict_pct": pct(sim, n_class),
            "sim_upper": sim_ub, "sim_upper_pct": pct(sim_ub, n_class),
            "meas": meas, "meas_pct": pct(meas, n_class),
            "ci_strict": ci_str(sim, n_class), "ci_upper": ci_str(sim_ub, n_class)}


def main():
    recs = statslib.parse_coding_table(LIT / "coding-table.md")
    research = [r for r in recs if statslib.entry_class(r) == "research"]
    nonres = [r for r in recs if statslib.entry_class(r) != "research"]
    vt = Counter(statslib.val_type(r) for r in research)
    n_class = sum(v for k, v in vt.items() if k != "N/A")
    sim = vt.get("Sim.-only", 0)
    sim_ub = sim + vt.get("Multi-fidelity (sim.-based)", 0)
    meas = vt.get("Meas.-incl.", 0) + vt.get("Meas.+Sim.", 0)

    # 年度趋势（研究类、验证可分类；sim_strict 口径）
    yearly = []
    for y in sorted({r["year"] for r in research if r["year"].isdigit()}):
        ry = [r for r in research if r["year"] == y and statslib.val_type(r) != "N/A"]
        if ry:
            yearly.append((int(y), sum(1 for r in ry if statslib.val_type(r) == "Sim.-only"), len(ry)))
    z, p = statslib.trend_test(yearly)

    piml_dt = subgroup(recs, ("A", "D"))
    ddriven = subgroup(recs, ("M",))
    classical = subgroup(recs, ("T", "O"))
    enabling = subgroup(recs, ("E",))

    # PRISMA 漏斗（来自 harvest 日志 + 新池 + 筛查元数据；缺件为 null 并如实标注）
    funnel = {"fetched_total": None, "pool_total": None, "tiers": None,
              "screening_candidates": None, "screening_capped": None, "corpus_total": len(recs)}
    hlog = LIT / "harvest-v2-log.json"
    if hlog.exists():
        hl = json.loads(hlog.read_text(encoding="utf-8"))
        funnel["fetched_total"] = hl.get("dedup", {}).get("fetched_total")
        funnel["pool_total"] = hl.get("dedup", {}).get("pool_total")
        funnel["tiers"] = hl.get("pool_summary", {}).get("tiers")
    dmeta = LIT / "screening" / "decisions.json"
    if dmeta.exists():
        dm = json.loads(dmeta.read_text(encoding="utf-8")).get("_meta", {})
        funnel["screening_candidates"] = dm.get("candidates")
        funnel["screening_capped"] = dm.get("capped")

    out = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "rules": "statslib.py v4 (see docstring); corpus frozen per PROJECT-STATE 2026-09-16",
        "corpus": {"total": len(recs), "groups": dict(sorted(Counter(r["group"] for r in recs).items()))},
        "research": {"n": len(research), "non_research": len(nonres),
                     "n_classifiable": n_class,
                     "val_counts": {k: vt.get(k, 0) for k in statslib.VAL_ORDER}},
        "sim_strict": {"k": sim, "n": n_class, "pct": pct(sim, n_class), "ci": ci_str(sim, n_class)},
        "sim_upper": {"k": sim_ub, "n": n_class, "pct": pct(sim_ub, n_class), "ci": ci_str(sim_ub, n_class)},
        "meas": {"k": meas, "n": n_class, "pct": pct(meas, n_class), "ci": ci_str(meas, n_class)},
        "subgroups": {"piml_dt": piml_dt, "data_driven": ddriven, "classical": classical, "enabling": enabling},
        "trend": {"basis": "sim_strict share of classifiable research per year",
                   "yearly": [{"year": y, "sim": k, "n": n} for y, k, n in yearly],
                   "cochran_armitage_z": z, "p_value": p},
        "funnel": funnel,
    }
    (LIT / "section6-stats-v4.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---- 人读 crib sheet：正文补丁字符串的唯一来源 ----
    L = []
    L.append("# Stats v4 report（正文补丁 crib sheet）\n")
    L.append(f"生成：{out['generated']}；规则：statslib.py（entry_class/val_type 文档化规则）\n")
    L.append(f"- 编码语料总数: **{len(recs)}**（组分布: " + ", ".join(f"{g}={n}" for g, n in out['corpus']['groups'].items()) + "）")
    L.append(f"- 研究类 n=**{len(research)}**（非研究类 {len(nonres)}：C/K 组、综述、知识/无验证基础）")
    L.append(f"- 验证可分类 n=**{n_class}**；分布: " + ", ".join(f"{k}={vt.get(k,0)}" for k in statslib.VAL_ORDER if vt.get(k,0)))
    L.append(f"- **严格纯仿真份额: {sim}/{n_class} = {pct(sim,n_class)}% ({ci_str(sim,n_class)})**")
    L.append(f"- **纯仿真上界（含多保真仿真锚定）: {sim_ub}/{n_class} = {pct(sim_ub,n_class)}% ({ci_str(sim_ub,n_class)})**")
    L.append(f"- 含实测: {meas}/{n_class} = {pct(meas,n_class)}% ({ci_str(meas,n_class)})\n")
    L.append("## 子组（Wilson 95% CI）\n")
    for name, s in (("PIML/数字孪生 (G1+G2)", piml_dt), ("数据驱动 (G3)", ddriven),
                    ("传统容差 (G4+G5)", classical), ("PIML使能 (G6)", enabling)):
        L.append(f"- {name}: n={s['n']}（可分类 {s['n_classifiable']}）；严格纯仿真 {s['sim_strict']} "
                 f"({s['sim_strict_pct']}%, {s['ci_strict']})；上界 {s['sim_upper']} ({s['sim_upper_pct']}%, {s['ci_upper']})；含实测 {s['meas']}")
    L.append("\n## 年度趋势（严格纯仿真份额，Cochran–Armitage）\n")
    L.append("- " + "; ".join(f"{y}: {k}/{n}" for y, k, n in yearly))
    L.append(f"- z={z}, p={p}" + ("（p<0.05：随年份显著下降）" if p is not None and p < 0.05 else "（未达显著）") + "\n")
    L.append("## PRISMA 漏斗\n")
    L.append(f"- 抓取 {funnel['fetched_total']} → 去重池 {funnel['pool_total']}（分层 {funnel['tiers']}）"
             f" → 增量筛查候选 {funnel['screening_candidates']}（截断={funnel['screening_capped']}） → 编码语料 {len(recs)}")
    (LIT / "stats-v4-report.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    print("\n".join(L))
    print("\nsection6-stats-v4.json + stats-v4-report.md written")


if __name__ == "__main__":
    main()
