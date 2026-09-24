# -*- coding: utf-8 -*-
"""综述论文全套图表生成（Fig.1–Fig.8，英文标注，投稿口径）
数据来源：literature/pool.csv、coding-table.md（经 statslib 规则）、
literature/section6-stats-v4.json（存在时图 2/5/8 数字自动取自统计，评审修复 v4，2026-09-16）。
"""
import csv, json, re, sys
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
import statslib

STATS_P = ROOT / "literature/section6-stats-v4.json"
STATS = json.loads(STATS_P.read_text(encoding="utf-8")) if STATS_P.exists() else None

import matplotlib
matplotlib.use("Agg")
# Inline styling (replaces the retired daimon_runtime.setup_plot dependency, 2026-09-16)
matplotlib.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial", "Microsoft YaHei"],
    "axes.titlesize": 11, "axes.titleweight": "bold",
    "axes.labelsize": 10,
    "xtick.labelsize": 9, "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": False,
    "figure.dpi": 100, "savefig.dpi": 300,
})
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

FIG = ROOT / "figures"; FIG.mkdir(exist_ok=True)

# ---------- 数据（statslib 为唯一规则源） ----------
pool = list(csv.DictReader(open(ROOT/"literature/pool.csv", encoding="utf-8-sig")))
coded = statslib.parse_coding_table(ROOT/"literature/coding-table.md")
N_CODED = len(coded)
corpus_n = (STATS or {}).get("corpus", {}).get("total", N_CODED)

# ---------- Fig.1 年度趋势（协议窗口 2015–2026，窗口外记录不入图并在副题注明） ----------
W0, W1 = 2015, 2026
pool_w = [r for r in pool if r["year"] and str(r["year"]).isdigit() and W0 <= int(r["year"]) <= W1]
n_out = len(pool) - len(pool_w)
yr_all = [W0, W1]
years = list(range(W0, W1 + 1))
tA = [sum(1 for r in pool_w if r["tier"]=="A" and str(r["year"])==str(y)) for y in years]
tB = [sum(1 for r in pool_w if r["tier"]=="B" and str(r["year"])==str(y)) for y in years]
tC = [sum(1 for r in pool_w if r["tier"]=="C" and str(r["year"])==str(y)) for y in years]
fig, ax = plt.subplots(figsize=(9, 5.2))
ax.bar(years, tA, label="Core: PIML × tolerance/assembly", color="#c0392b")
ax.bar(years, tB, bottom=tA, label="Adjacent: PIML × manufacturing/structures", color="#e67e22")
ax.bar(years, tC, bottom=[a+b for a,b in zip(tA,tB)], label="Background: general PIML methods", color="#95a5a6")
for i,y in enumerate(years):
    ax.text(y, tA[i]+tB[i]+tC[i]+8, str(tA[i]+tB[i]+tC[i]), ha="center", fontsize=9)
# 2015 bar is inflated by the capped Crossref supplementary harvest (harvest-order artifact) — mark it
i15 = years.index(2015)
ax.annotate("harvest artifact:\ncapped Crossref queries\n(see Section 2.1)",
            xy=(2015, tA[i15]+tB[i15]+tC[i15]), xytext=(2016.4, tA[i15]+tB[i15]+tC[i15]-1200),
            fontsize=8.5, color="#7b241c", ha="left", va="top",
            arrowprops=dict(arrowstyle="->", color="#7b241c", lw=1.0))
ax.set_xlabel("Publication year"); ax.set_ylabel("Number of records")
ax.set_title(f"Publication trend of the retrieved literature pool\n(OpenAlex + Semantic Scholar + Crossref, deduplicated N={len(pool_w)} in the 2015–2026 search window; {yr_all[-1]} data through September)")
ax.legend(loc="upper right", fontsize=9); ax.set_xticks(years)
fig.savefig(FIG/"fig1-publication-trend.png", bbox_inches="tight"); plt.close(fig)
print("fig1 ok", sum(tA)+sum(tB)+sum(tC), "years", yr_all[0], yr_all[-1])

# ---------- Fig.2 PRISMA 流程（数字优先取 stats-v4 漏斗块；缺件回退实时计算） ----------
_hl = {}
_hlp = ROOT / "literature/harvest-v2-log.json"
if _hlp.exists():
    _hl = json.loads(_hlp.read_text(encoding="utf-8"))
fetched_n = (STATS or {}).get("funnel", {}).get("fetched_total") or _hl.get("dedup", {}).get("fetched_total") or "—"
pool_n = (STATS or {}).get("funnel", {}).get("pool_total") or len(pool)
tiers = (STATS or {}).get("funnel", {}).get("tiers") or dict(Counter(r["tier"] for r in pool))
tier_txt = f"A {tiers.get('A','—')} / B {tiers.get('B','—')} / C {tiers.get('C','—')}" if isinstance(tiers, dict) else str(tiers)
scr_n = (STATS or {}).get("funnel", {}).get("screening_candidates")
scr_txt = f"delta candidates {scr_n}" if scr_n else "round-1/2 screening + delta"
fig, ax = plt.subplots(figsize=(7.5, 8.5)); ax.axis("off")
boxes = [
 ("Identification", f"Records retrieved (n = {fetched_n})\nOpenAlex: Q1–Q7 uncapped (verbatim)\nSemantic Scholar: 3 complementary queries\n+ citation snowballing + Crossref: Q8–Q14\nTime window: 2015–2026"),
 ("Deduplication", f"After deduplication (n = {pool_n})\nDOI-first, normalized-title fallback"),
 ("Screening", "Three-relevance-tier auto-assignment +\nabstract-level screening\n(tiers: " + tier_txt + ";\n" + scr_txt + ")"),
 ("Coded corpus", f"Coded works (n = {corpus_n})\n8 thematic groups (G1–G8)\n(Table 2: representative works)"),
]
y = 0.93
for title, body in boxes:
    ax.add_patch(mpatches.FancyBboxPatch((0.08, y-0.165), 0.6, 0.185, boxstyle="round,pad=0.012",
                 fc="#f4f6f7", ec="#2c3e50", lw=1.4, transform=ax.transAxes))
    ax.text(0.38, y-0.022, title, ha="center", fontsize=12, fontweight="bold", transform=ax.transAxes)
    ax.text(0.38, y-0.052, body, ha="center", va="top", fontsize=9.5, transform=ax.transAxes)
    if y < 0.9:
        ax.annotate("", xy=(0.38, y+0.022), xytext=(0.38, y+0.066),
                    xycoords="axes fraction", arrowprops=dict(arrowstyle="-|>", lw=1.6, color="#2c3e50"))
    y -= 0.24
# 排除支流（右置，避让主链）
ax.add_patch(mpatches.FancyBboxPatch((0.72, 0.46), 0.27, 0.13, boxstyle="round,pad=0.01",
             fc="#fdf2e9", ec="#e67e22", lw=1.2, transform=ax.transAxes))
ax.text(0.855, 0.525, "Excluded at screening:\n449 delta candidates;\n35 included (30 physics-\ninformed + 5 data-driven),\n414 excluded (term collisions,\nprocess-only physics, ...)",
        ha="center", fontsize=8.5, transform=ax.transAxes)
ax.annotate("", xy=(0.72, 0.525), xytext=(0.68, 0.525), xycoords="axes fraction",
            arrowprops=dict(arrowstyle="-|>", lw=1.4, color="#e67e22"))
ax.set_title("PRISMA-style literature identification and screening flow", fontsize=13)
fig.savefig(FIG/"fig2-prisma-flow.png", bbox_inches="tight"); plt.close(fig)
print("fig2 ok")

# ---------- Fig.3 演进时间线 ----------
fig, ax = plt.subplots(figsize=(11, 5.6))
lanes = [("Classical tolerancing\n& variation models", "#95a5a6", [
    (2015,"Skin Model Shapes\npotentials [T01]"), (2016,"Jacobian–torsor +\nmfg. signature [T04]"),
    (2018,"Form errors + local\ndeformation [T03]"), (2024,"Non-Gaussian SMS\nassembly accuracy [T13]")]),
 ("Data-driven\nlearning", "#e67e22", [
    (2018,"NN geometric\nprediction [M10]"), (2020,"NN-GP composite\nassembly [M02]"),
    (2023,"DeviationGAN\n[M01]"), (2025,"FDQN tolerance\nclosed-loop [M09]")]),
 ("Physics-informed\nML", "#c0392b", [
    (2019,"PINN framework\n[C01]"), (2021,"Operator learning\nFNO/DeepONet [E13, E14]"),
    (2024,"SmartFixture\nphysics-guided RL [A05]"), (2026,"PIGL flange assembly\ndeviation [A02]")])]
for li,(name,color,events) in enumerate(lanes):
    yc = 2-li
    ax.axhline(yc, color=color, lw=3, alpha=0.35, zorder=1)
    ax.text(2014.4, yc, name, ha="right", va="center", fontsize=11, fontweight="bold", color=color)
    for ei,(yr, lbl) in enumerate(events):
        ax.scatter(yr, yc, s=90, color=color, zorder=3)
        off = 0.32 if ei % 2 == 0 else 0.62   # 交错高度防重叠
        ax.annotate(lbl, (yr, yc), xytext=(yr, yc+off), ha="center", fontsize=8,
                    arrowprops=dict(arrowstyle="-", lw=0.8, color=color, alpha=0.6))
ax.set_xlim(2014, 2027); ax.set_ylim(-0.6, 3.4); ax.set_yticks([])
ax.set_xlabel("Year"); ax.set_title("Three generations of methods for tolerance analysis and assembly deviation prediction (2015–2026)")
fig.savefig(FIG/"fig3-evolution-timeline.png", bbox_inches="tight"); plt.close(fig)
print("fig3 ok")

# ---------- Fig.4 三维分类法 ----------
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
mech = ["Loss\nembedding","Architecture\nembedding","Data\nembedding","Hybrid"]
task = ["Forward\nsurrogate","Inverse\nidentification","Uncertainty\nquantification","Optimization\n& control"]
fid  = ["Single-\nfidelity","Multi-\nfidelity","Online /\ncontinual"]
dense = {(0,0,0): "dense"}
cmap = {"dense":"#c0392d", "populated":"#e67e22", "sparse":"#f8f9f9"}
populated = {(0,0,0),(0,0,1),(1,0,0),(2,0,0),(3,0,0),(0,3,0),(1,1,0),(0,2,0),(3,0,1),(1,0,1),(0,0,2),(2,3,1)}
sparse_examples = {(1,1,1),(3,3,2),(1,2,1)}
for i in range(4):
    for j in range(4):
        for k in range(3):
            cell = (i,j,k)
            if cell == (0,0,0): c,s,alpha = cmap["dense"], 900, 0.9
            elif cell in populated: c,s,alpha = cmap["populated"], 500, 0.8
            elif cell in sparse_examples: c,s,alpha = "#2980b9", 500, 0.85
            else: c,s,alpha = cmap["sparse"], 320, 0.25
            ax.scatter(i, j, k, s=s, c=c, alpha=alpha, edgecolors="#2c3e50", linewidths=0.8, depthshade=False)
ax.text(0, 0, 0.42, "Loss×Fwd×Single\n(corpus core)", ha="center", fontsize=8, color="#c0392d")
ax.text(3, 3, 2.5, "Hybrid×Control×Online\n(open position)", ha="center", fontsize=8, color="#2980b9")
ax.set_xticks(range(4)); ax.set_xticklabels(mech, fontsize=8)
ax.set_yticks(range(4)); ax.set_yticklabels(task, fontsize=8)
ax.set_zticks(range(3)); ax.set_zticklabels(fid, fontsize=8)
ax.set_xlabel("Physical-integration mechanism", fontsize=10, labelpad=12)
ax.set_ylabel("Task type", fontsize=10, labelpad=12)
ax.set_zlabel("Data fidelity", fontsize=10, labelpad=8)
ax.set_title("Three-dimensional taxonomy of PIML for tolerance analysis", fontsize=12, pad=18)
handles = [plt.Line2D([],[],marker='o',ls='',color="#c0392d",label="Dense (corpus core)",markersize=10),
           plt.Line2D([],[],marker='o',ls='',color="#e67e22",label="Populated",markersize=10),
           plt.Line2D([],[],marker='o',ls='',color="#2980b9",label="Sparse (research opportunity)",markersize=10),
           plt.Line2D([],[],marker='o',ls='',color="#f8f9f9",markeredgecolor="#2c3e50",label="Empty",markersize=10)]
ax.legend(handles=handles, loc="upper left", fontsize=8.5)
fig.savefig(FIG/"fig4-taxonomy-3d.png", bbox_inches="tight"); plt.close(fig)
print("fig4 ok")

# ---------- Fig.5 版图热力图（组别 × 验证类型，statslib 规则） ----------
grp_names = {"A":"G1 PIML×assembly core","D":"G2 Digital twin","M":"G3 Data-driven",
             "T":"G4 Classical tolerancing","O":"G5 Tolerance allocation","E":"G6 PIML enabling",
             "C":"G7 Methods & reviews","K":"G8 Knowledge repr."}
order_g = ["A","D","M","T","O","E","C","K"]
order_v = [v for v in statslib.VAL_ORDER]  # Sim-only / Multi-fid / Meas-incl / Meas+Sim / N/A
M = np.zeros((len(order_g), len(order_v)), dtype=int)
for r in coded:
    vt = statslib.val_type(r) if statslib.entry_class(r) == "research" else "N/A"
    M[order_g.index(r["prefix"]), order_v.index(vt)] += 1
fig, ax = plt.subplots(figsize=(8.5, 5.5))
im = ax.imshow(M, cmap="OrRd", aspect="auto")
ax.set_xticks(range(len(order_v))); ax.set_xticklabels(order_v, fontsize=9, rotation=12)
ax.set_yticks(range(len(order_g))); ax.set_yticklabels([grp_names[g] for g in order_g], fontsize=9.5)
for i in range(len(order_g)):
    for j in range(len(order_v)):
        ax.text(j, i, M[i,j], ha="center", va="center",
                color="white" if M[i,j] > M.max()*0.55 else "#2c3e50", fontsize=11, fontweight="bold")
ax.set_title(f"Coded corpus landscape: thematic group × validation type (n = {corpus_n})\nSimulation-only validation dominates across all groups")
fig.colorbar(im, ax=ax, label="Number of coded works", shrink=0.85)
fig.savefig(FIG/"fig5-landscape-heatmap.png", bbox_inches="tight"); plt.close(fig)
print("fig5 ok\n", M)

# ---------- Fig.6 系统架构（CPPS 分层中的 PIML 容差模块） ----------
fig, ax = plt.subplots(figsize=(10.5, 7.5)); ax.axis("off"); ax.set_xlim(0,10); ax.set_ylim(0,10)
def box(x,y,w,h,label,fc,fs=9.5,ec="#2c3e50",bold=False):
    ax.add_patch(mpatches.FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.06",fc=fc,ec=ec,lw=1.4))
    ax.text(x+w/2,y+h/2,label,ha="center",va="center",fontsize=fs,
            fontweight="bold" if bold else "normal")
# 层
layers = [(0.3,7.6,9.4,1.9,"#eaf2f8","APPLICATION & DECISION LAYER"),
          (0.3,5.1,9.4,1.9,"#fef5e7","CONTROL & MONITORING LAYER"),
          (0.3,2.6,9.4,1.9,"#e8f8f5","INFORMATION / CYBER LAYER"),
          (0.3,0.3,9.4,1.7,"#f4f6f7","PHYSICAL / EQUIPMENT LAYER")]
for x,y,w,h,fc,name in layers:
    ax.add_patch(mpatches.FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.04",fc=fc,ec="#7f8c8d",lw=1.0,alpha=0.55))
    ax.text(x+0.15,y+h-0.28,name,fontsize=9,fontweight="bold",color="#5d6d7e")
# 应用层
box(0.7,7.85,2.7,1.15,"Tolerance evaluation\nrequests & risk reports","#aed6f1")
box(3.8,7.85,2.7,1.15,"Tolerance allocation &\nfixture/sequence decisions","#aed6f1")
box(6.9,7.85,2.7,1.15,"Quality audits &\ntraceability (MES/QMS)","#aed6f1")
# 控制层
box(0.7,5.22,4.1,1.35,"PIML TOLERANCE MODULE\nPrediction (forward/inverse) +\nshift monitors (MMD, UQ, gradient sign)","#f5b7b1",fs=9,bold=True)
box(5.2,5.22,4.4,1.35,"Deployment discipline:\nadvisory → closed-loop promotion;\ntripwire → human review","#fad7a0",fs=9)
# 信息层
box(0.7,2.72,2.8,1.35,"Skin Model Shapes &\ndeviation representations","#a9dfbf")
box(3.8,2.72,2.8,1.35,"Multi-fidelity data pyramid\n(analytical / FE / measurement)","#a9dfbf")
box(6.9,2.72,2.7,1.35,"Digital twin state &\nmodel registry","#a9dfbf")
# 物理层
box(0.7,0.42,4.1,1.0,"Assembly line: parts, fixtures,\njoining & clamping equipment","#d5dbdb")
box(5.2,0.42,4.4,1.0,"Measurement: CMM, laser scanning,\nin-situ sensors","#d5dbdb")
# 箭头
def arr(x1,y1,x2,y2,c="#2c3e50",style="-|>"):
    ax.annotate("",xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle=style,lw=1.7,color=c))
arr(2.75,2.05,2.75,2.67); arr(5.2,2.05,5.2,2.67)                    # 物理→信息
arr(2.1,4.12,2.1,5.17); arr(5.2,4.12,4.0,5.17)                      # 信息→控制
arr(7.4,4.12,7.4,5.17,"#7f8c8d","<|-|>")                            # twin 双向
arr(2.7,6.62,2.05,7.8); arr(3.9,6.62,5.1,7.8)                       # 控制→应用
arr(8.25,5.17,8.25,2.05,"#c0392b")                                  # 下行控制
ax.text(8.45,3.55,"control commands",fontsize=8,color="#c0392b",rotation=90)
ax.text(0.5,9.62,"Fig. 6  Reference architecture: the PIML tolerance module within CPPS layering\n(products / equipment / information / control integration points shown)",
        fontsize=11,fontweight="bold")
fig.savefig(FIG/"fig6-system-architecture.png", bbox_inches="tight"); plt.close(fig)
print("fig6 ok")

# ---------- Fig.7 漂移评估协议框架（概念框架图，衰减曲线为示意性格式） ----------
fig = plt.figure(figsize=(13.5, 6.8))
gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.15, 1.0], wspace=0.28,
                      left=0.045, right=0.985, top=0.86, bottom=0.10)
C_RED, C_ORG, C_BLU, C_GRN, C_PUR = "#c0392b", "#e67e22", "#2980b9", "#27ae60", "#8e44ad"

# Panel A: 五条漂移轴
axA = fig.add_subplot(gs[0]); axA.axis("off")
axA.set_title("A. Five drift axes (graded shift)", fontsize=11, fontweight="bold", loc="left")
axes_info = [("Material change", C_RED), ("Process-window change", C_ORG),
             ("Product-configuration change", C_BLU), ("Deviation correlation structure", C_GRN),
             ("Measurement-chain change", C_PUR)]
for i, (name, c) in enumerate(axes_info):
    y = 0.86 - i * 0.17
    axA.text(0.0, y + 0.035, name, fontsize=9.5, fontweight="bold", color=c, va="bottom")
    axA.add_patch(mpatches.FancyBboxPatch((0.0, y - 0.045), 0.30, 0.045,
                  boxstyle="round,pad=0.004", fc="#d5f5e3", ec=C_GRN, lw=0.8))
    axA.text(0.15, y - 0.022, "validated", fontsize=7.5, ha="center", va="center", color="#1e8449")
    for j, (x0, s) in enumerate(zip([0.30, 0.42, 0.54, 0.66], [0.25, 0.45, 0.65, 0.9])):
        axA.add_patch(mpatches.Rectangle((x0, y - 0.045), 0.115, 0.045, fc=c, ec="white", lw=0.6, alpha=s))
        axA.text(x0 + 0.057, y - 0.022, f"L{j+1}", fontsize=7, ha="center", va="center",
                 color="white" if s > 0.5 else "black")
    axA.annotate("", xy=(0.80, y - 0.022), xytext=(0.775, y - 0.022),
                 arrowprops=dict(arrowstyle="-|>", color=c, lw=1.6))
    axA.text(0.82, y - 0.022, "shift", fontsize=7.5, va="center", color=c)
axA.text(0.0, 0.02, "Envelope edge = boundary of validated training envelope;\nL1–L4 = prescribed graded shift levels per axis.",
         fontsize=8, color="#555555", va="bottom")
axA.set_xlim(0, 1); axA.set_ylim(0, 1)

# Panel B: 外推误差衰减曲线（示意图）
axB = fig.add_subplot(gs[1])
axB.set_title("B. Extrapolation error decay curves\n(reporting format, schematic)",
              fontsize=11, fontweight="bold", loc="left")
x = np.linspace(0, 4, 200)
curves = [("Correlation (most dangerous)", C_GRN, 1.3), ("Material", C_RED, 2.2),
          ("Process window", C_ORG, 2.8), ("Configuration", C_BLU, 3.3),
          ("Measurement chain", C_PUR, 3.8)]
for name, c, cross in curves:
    axB.plot(x, 1.0 + (x / cross) ** 1.2, color=c, lw=2, label=name)
    axB.plot([cross], [2.0], "o", color=c, ms=6, zorder=5)
axB.axvline(0, color="#1e8449", lw=1.4, ls="-")
axB.axhline(2.0, color="#7b241c", lw=1.4, ls="--")
axB.text(0.08, 2.1, "max admissible error growth (retraining threshold)\n● = threshold crossing per axis",
         fontsize=8, ha="left", va="bottom", color="#7b241c")
axB.axvspan(-0.9, 0, color="#d5f5e3", alpha=0.6)
axB.text(-0.45, 1.55, "validated\nenvelope", fontsize=8, ha="center", va="center", color="#1e8449")
axB.set_xlim(-0.9, 4.15); axB.set_ylim(0.9, 5.2)
axB.set_xticks([0, 1, 2, 3, 4]); axB.set_xticklabels(["edge", "L1", "L2", "L3", "L4"], fontsize=8.5)
axB.set_xlabel("Shift magnitude (graded levels per axis)", fontsize=9)
axB.set_ylabel("Prediction error (normalized)", fontsize=9)
axB.tick_params(labelsize=8.5)
axB.legend(fontsize=7.5, loc="upper left", framealpha=0.9)

# Panel C: 部署档案 → §8.3 规格层契约
axC = fig.add_subplot(gs[2]); axC.axis("off")
axC.set_title("C. Measurable contracts for the\nself-adaptive system (§8.3)",
              fontsize=11, fontweight="bold", loc="left")
axC.add_patch(mpatches.FancyBboxPatch((0.06, 0.80), 0.88, 0.14, boxstyle="round,pad=0.01",
              fc="#fdebd0", ec=C_ORG, lw=1.4))
axC.text(0.5, 0.87, "Deployment dossier\ndecay curves on all 5 axes + explicit retraining thresholds",
         fontsize=9, ha="center", va="center", fontweight="bold", color="#7e5109")
contracts = [("Detection signals", "drift monitoring agent", C_BLU),
             ("Acquisition targets", "physics-driven sampling agent", C_GRN),
             ("Regression thresholds", "post-update validation agent", C_PUR),
             ("Redeployment gates", "orchestration agent", C_RED)]
for i, (k, v, c) in enumerate(contracts):
    y = 0.62 - i * 0.155
    axC.annotate("", xy=(0.5, y + 0.062), xytext=(0.5, y + 0.095),
                 arrowprops=dict(arrowstyle="-|>", color="#777777", lw=1.1))
    axC.add_patch(mpatches.FancyBboxPatch((0.06, y - 0.055), 0.88, 0.115, boxstyle="round,pad=0.01",
                  fc="white", ec=c, lw=1.3))
    axC.text(0.5, y + 0.022, k, fontsize=9.5, ha="center", fontweight="bold", color=c)
    axC.text(0.5, y - 0.025, "→ " + v, fontsize=8.5, ha="center", color="#444444")
axC.text(0.5, -0.035, "Measurable contracts turn the multi-agent architecture\nfrom an organizational metaphor into an engineering specification.",
         fontsize=8, ha="center", color="#555555", style="italic")
axC.set_xlim(0, 1); axC.set_ylim(-0.08, 1)

fig.suptitle("Fig. 7  The drift evaluation protocol: five drift axes, decay-curve reporting, and the specification layer for self-adaptive surrogate systems.",
             fontsize=11.5, y=0.965)
fig.savefig(FIG/"fig7-drift-protocol.png", bbox_inches="tight"); plt.close(fig)
print("fig7 ok")

# ---------- Fig.8 就绪度阶梯（概念框架图；语料定位为真实统计口径） ----------
fig, ax = plt.subplots(figsize=(13.5, 6.9)); ax.axis("off")
levels = [
    ("R1", "Simulation-\nvalidated",
     "verification vs. simulation\nground truth; consistency\nchecks reported", "#7f8c8d"),
    ("R2", "Measurement-\nvalidated",
     "physical measurements in\ntraining/validation; decay\ncurves established on hardware", "#2980b9"),
    ("R3", "Advisory\ndeployment",
     "decision support with\nconsistency indicators;\ntripwires armed; logging on", "#27ae60"),
    ("R4", "Supervised\nclosed loop",
     "in control loop; bounded\nout-of-envelope growth;\nregression gates on updates", "#e67e22"),
    ("R5", "Autonomous self-\nadaptive operation",
     "self-adaptive architecture live;\nmeasurable contracts govern\nthe full lifecycle", "#c0392b"),
]
# Fig.8 语料定位带统计（stats-v4 优先；回退为图内既有口径）
_sim = (STATS or {}).get('sim_strict', {})
_mea = (STATS or {}).get('meas', {})
_r1_pct = (f"{round(_sim['pct'])}%" if _sim.get('pct') is not None else '74%')
_r2_pct = (f"{round(_mea['pct'])}%" if _mea.get('pct') is not None else '26%')
W, H, X0, Y0 = 2.35, 0.95, 0.4, 1.15
BW = W - 0.18
for i, (rk, name, ev, c) in enumerate(levels):
    x, y = X0 + i * W, Y0 + i * H
    ax.add_patch(mpatches.FancyBboxPatch((x, y), BW, 1.78, boxstyle="round,pad=0.02",
                 fc=c, ec="none", alpha=0.92))
    ax.text(x + BW / 2, y + 1.45, f"{rk}  {name}", fontsize=10.5, fontweight="bold",
            ha="center", va="center", color="white")
    ax.text(x + BW / 2, y + 0.58, ev, fontsize=7.6, ha="center", va="center", color="white")
    if i < 4:
        gx = x + W - 0.09
        ax.annotate("", xy=(gx + 0.16, y + H + 0.98), xytext=(gx - 0.16, y + 1.30),
                    arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.4))
base = 0.55
ax.plot([X0 - 0.1, X0 + 5 * W - 0.3], [base, base], color="#888888", lw=1)
tier1 = [
    (X0 + 0.5 * W - 0.09, f"{_r1_pct} of coded research works\n(simulation-only) sit at R1", "#7f8c8d"),
    (X0 + 2.0 * W - 0.09, "▲ physics-informed frontier:\nno model past the R2→R3 gate", "#c0392b"),
]
tier2 = [
    (X0 + 1.5 * W - 0.09, f"{_r2_pct} measurement-inclusive:\npartial R2 evidence", "#2980b9"),
    (X0 + 3.5 * W - 0.09, "◆ twins [D01, D03] operate at R4 —\nbut with data-driven/classical cores", "#e67e22"),
]
for xm, txt, c in tier1:
    ax.plot([xm, xm], [base, base + 0.12], color=c, lw=1.2)
    ax.text(xm, base - 0.08, txt, fontsize=7.8, ha="center", va="top", color=c)
for xm, txt, c in tier2:
    ax.plot([xm, xm], [base, base + 0.12], color=c, lw=1.2, ls="--")
    ax.text(xm, base - 0.62, txt, fontsize=7.8, ha="center", va="top", color=c)
ax.text(X0 - 0.1, Y0 + 4 * H + 2.3,
        "Fig. 8  Readiness ladder for physics-informed tolerance models (R1–R5):\nevidence gates (arrows) between rungs, and the position of the coded corpus.",
        fontsize=11, fontweight="bold", va="bottom")
ax.text(X0 - 0.1, Y0 + 4 * H + 1.95,
        "The appropriate terminal rung follows decision criticality; every deployment should document the rung it occupies.",
        fontsize=8.5, color="#555555", style="italic", va="bottom")
ax.set_xlim(0, X0 + 5 * W + 0.4); ax.set_ylim(-1.15, Y0 + 4 * H + 2.75)
fig.savefig(FIG/"fig8-readiness-ladder.png", bbox_inches="tight"); plt.close(fig)
print("fig8 ok")

print("\nALL FIGS DONE")
