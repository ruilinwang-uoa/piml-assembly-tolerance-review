# -*- coding: utf-8 -*-
"""§6.2 统计 v3 —— v2 基数 + 文档化增量法。
v2（literature/section6-stats-v2.json）：91 语料，研究类 69，纯仿真 50，含实测 19；
子集 PIML/DT n=23 中 16 纯仿真；数据驱动 n=14 中 9 纯仿真。
增量：B-3/B-4 轮新增 A10/A11/M15 三条，编码表（coding-table.md）显示三者均为
研究类、保真度=仿真（纯仿真），分组 G1/G1/G3。
说明：曾尝试从编码表直接全量重算（前缀规则），无法复现 v2 基数（v2 的组归属
含 G6/G7 部分条目，前缀规则不可还原），故采用增量法；增量项编码可直接核验。"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent
v2 = json.loads((ROOT / "literature/section6-stats-v2.json").read_text(encoding="utf-8"))
assert v2 == {"total": 91, "research": 69, "sim": 50, "meas": 19}, "v2 基数被改动，停止"

v3 = dict(
    total=94, research=72, sim=53, meas=19,
    piml_dt_n=25, piml_dt_sim=18,      # +A10, +A11（均纯仿真）
    datadriven_n=15, datadriven_sim=10,  # +M15（纯仿真）
)
v3.update(
    sim_pct=round(100 * v3["sim"] / v3["research"], 1),
    meas_pct=round(100 * v3["meas"] / v3["research"], 1),
    piml_dt_pct=round(100 * v3["piml_dt_sim"] / v3["piml_dt_n"], 1),
    datadriven_pct=round(100 * v3["datadriven_sim"] / v3["datadriven_n"], 1),
    method="v2 base + documented delta (A10/A11/M15, all simulation-only research)",
    added=["A10(仿真)", "A11(仿真)", "M15(仿真)"],
)
(ROOT / "literature/section6-stats-v3.json").write_text(
    json.dumps(v3, ensure_ascii=False, indent=2), encoding="utf-8")
print("v3:", json.dumps(v3, ensure_ascii=False))
print("总体 %d/%d=%.1f%% 纯仿真（文稿口径 74%%），含实测 %d/%d=%.1f%%（26%%）"
      % (v3["sim"], v3["research"], v3["sim_pct"], v3["meas"], v3["research"], v3["meas_pct"]))
print("PIML/DT %d/%d=%.1f%%（72%%）；数据驱动 %d/%d=%.1f%%（67%%）"
      % (v3["piml_dt_sim"], v3["piml_dt_n"], v3["piml_dt_pct"],
         v3["datadriven_sim"], v3["datadriven_n"], v3["datadriven_pct"]))
