# -*- coding: utf-8 -*-
"""Phase 5b 新写作植入：SOVA 桥接（§3.1/§3.5）、算子学习（§5.1）、三个案例框（§6.1/§6.2/§6.3）、
Table 3 接口/时延规范（§8.4）。全部无数字依赖；引用键 T32/T33/E13/E14 已入 references.md。

依据：PRE_SUBMISSION_REVIEW_2026-09-16 MAJOR #15（SOVA/算子学习缺口）、Agent 6 建议分析 1/2
（案例框、DT/CPPS 规范表）。案例框仅基于编码条目的公开摘要与元数据（诚实边界已在文中声明）。
"""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent

# (section_file, 锚点, 插入文本[锚点后插入], 是否在锚点后插)
INSERTS = [
    # --- §3.1 SOVA 桥接段 ---
    ("sections/03-background.md",
     "and have been extended to include form defects and surface deformations in over-constrained assemblies [T07].",
     "\n\nA complementary systems-level line treats the assembly process itself as the propagation medium: stream-of-variation (SOVA) analysis models multistage manufacturing as a state-space system in which part deviations are the states, station-level fixture and machining errors are the inputs, and measurement observations close the loop [T32]. Rooted in state-space modeling of sheet-metal assembly for dimensional control [T33], this line accumulated the process-level error data, diagnosability analysis, and feedback-control connections that made variation propagation an explicitly *systems* discipline — the tradition within which digital-twin geometry assurance (§6.3) later re-emerged. Although SOVA's linear state-space core shares the linearization limits discussed below, its systems framing prefigures the equipment–product–control information flows that Section 8.4 places at the center of deployment."),
    # --- §3.5 传播算子枚举补 SOVA ---
    ("sections/03-background.md",
     "a *propagation operator* (algebraic, kinematic, or finite-element)",
     None),  # 用 REPLACE 处理
    # --- §5.1 算子学习（Two→Three developments）---
    ("sections/05-piml-taxonomy.md",
     "in which manufacturing deviations are natively expressed. Second, domain-specific reviews",
     None),  # 用 REPLACE 处理
    # --- §6.1 案例框 A01 ---
    ("sections/06-applications.md",
     "extending prediction from geometry to mechanics.",
     "\n\n**Case study (A01) — mechanism-integrated stringer-assembly prediction.** Xu et al. [A01] address flatness out-of-tolerance in aircraft stringer assembly, where multisource coupled deviations accumulate through the manipulator positioning–clamping–transplanting sequence. A screw-theory deviation-propagation model quantifies positioning errors, flexible clamping deformations, and inertial disturbances; the Lagrangian dynamic equation is then embedded into a spatiotemporal graph convolutional network, and the method is validated against measured assembly data — one of the few coded works combining a mechanistic propagation model, a learning architecture, and measurement evidence."),
    # --- §6.2 案例框 A05 ---
    ("sections/06-applications.md",
     "exemplified by buckling-surrogate-assisted intelligent optimization of curvilinear-fiber wings [K02].",
     "\n\n**Case study (A05) — physics-guided reinforcement learning for fixture layout.** SmartFixture [A05] trains a reinforcement-learning agent through direct interaction with FEA-based simulation to design fixture layouts for large-scale sheet parts. The framework targets the memorylessness and limited scalability of mathematical-optimization baselines: layout-design experience transfers across parts, and the agent scales to design spaces where fixed surrogate models struggle with representation capacity. Physics guidance enters through the FEA environment and the physical consistency of the learned policy rather than through a loss term — illustrating, in taxonomy terms, constraint embedding inside a decision loop (§5.3)."),
    # --- §6.3 案例框 D03（含案例框范围声明）---
    ("sections/06-applications.md",
     "and is arguably the highest-value open position in the landscape (Section 8).",
     "\n\n**Case study (D03) — online geometry assurance by twin calibration.** Sjöberg et al. [D03] close the loop for individualized sheet-metal assembly: a digital twin of the assembly cell is calibrated online with a Kalman filter, using the mismatch between simulated and realized assembly quality as the feedback signal, and a one-step look-ahead optimizer then sets control parameters for each individual product, trading predicted quality gain against uncertainty reduction. The twin's core is data-driven — physics enters through calibration rather than through the learning architecture — which is precisely why this work marks the R4 frontier of the readiness ladder (Section 9) while leaving the physics-informed online core open. *(Case boxes are compiled from the coded works' published abstracts and metadata; full-text quantitative details await the verification program described in Section 2.3.)*"),
    # --- §8.4 Table 3 ---
    ("sections/08-open-challenges.md",
     "The benchmark infrastructure of §8.5 should be designed to test models *in this architecture*, not in isolation.",
     "\n\nTable 3 makes these interface and latency requirements concrete by mapping each integration point of the reference architecture onto the data it must carry and the timing it must meet, together with the corpus works that already instantiate each element.\n\n**Table 3.** Interface and latency specification for integrating a physics-informed tolerance module into a CPPS digital twin (requirements synthesized from the coded digital-twin works; latency values indicate order-of-magnitude engineering budgets, not measured latencies).\n\n| Integration point | Direction | Payload and fidelity | Latency requirement | Corpus evidence |\n| --- | --- | --- | --- | --- |\n| Measurement ingest | Line → twin | Measured part/assembly geometry, point clouds; calibrated sensor models | Per measurement cycle (minutes) | [D01, D03] |\n| Twin synchronization | Ingest → twin state | Updated deviation state, fixture and process parameters | Per assembly cycle | [D01, D02] |\n| Surrogate inference | Twin → tolerance module | Deviation state and process parameters, fidelity-labeled | Seconds (within takt) | [A02, A08] |\n| Decision return | Tolerance module → control | Predicted quality, consistency indicators, recommended settings | Within station takt time | [D03, D05] |\n| MES/QMS logging | All → quality system | Predictions, outcomes, model version, envelope flags | Per event (audit trail) | [D01, D03] |"),
]

REPLACES = [
    # §3.5 传播算子枚举 + SOVA
    ("a *propagation operator* (algebraic, kinematic, or finite-element)",
     "a *propagation operator* (algebraic, kinematic, state-space, or finite-element)"),
    # §5.1 Two→Three developments + 算子学习句
    ("in which manufacturing deviations are natively expressed. Second, domain-specific reviews",
     "in which manufacturing deviations are natively expressed. Second, **operator learning** — Fourier neural operators [E13] and DeepONet [E14] — learns the solution operator of a parametric PDE family directly, amortizing the cost of repeated solves across design iterations and tolerance-allocation loops; mesh-free and graph-structured variants make these architectures natural candidates for learning the propagation operators of §3.5 at assembly scale. Third, domain-specific reviews"),
]

fails = []


def main():
    for sec, anchor, text in [(s, a, t) for (s, a, t) in INSERTS if t is not None]:
        for rel in (sec, "manuscript.md"):
            p = ROOT / rel
            t_ = p.read_text(encoding="utf-8")
            if t_.count(anchor) != 1:
                fails.append(f"{rel}: 锚点非唯一命中 :: {anchor[:60]}")
                continue
            if text.strip()[:60] in t_:
                print(f"  skip (already inserted): {rel} :: {anchor[:40]}")
                continue
            p.write_text(t_.replace(anchor, anchor + text), encoding="utf-8")
            print(f"  inserted into {rel} :: {anchor[:40]}...")
    for old, new in REPLACES:
        for rel in {s for (s, a, t) in INSERTS if a == old} | {"manuscript.md"}:
            p = ROOT / rel
            t_ = p.read_text(encoding="utf-8")
            n = t_.count(old)
            if n == 0 and new.split(". Second")[0][:40] in t_:
                print(f"  skip (already replaced): {rel}")
                continue
            if n != 1:
                fails.append(f"{rel}: 替换源非唯一命中（{n}） :: {old[:60]}")
                continue
            p.write_text(t_.replace(old, new), encoding="utf-8")
            print(f"  replaced in {rel} :: {old[:40]}...")
    if fails:
        print("FAILED:")
        for f in fails:
            print(" -", f)
        raise SystemExit(1)
    print("OK: 新写作植入完成（manuscript + sections 镜像）")


if __name__ == "__main__":
    main()
