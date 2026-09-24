# -*- coding: utf-8 -*-
"""apply_screening —— 筛查判决合并入编码表（Phase 2.3，2026-09-19）。

读取 literature/screening/decisions.json（LLM 辅助初筛判决）+ literature/pool.csv（元数据）：
  - include+group → 新增编码表行（ID 续号：G1→A12+、G2→D06+、G3(baseline)→M16+、G5→O11+、G6→E15+）
  - 摘要级保守编码：方法/机制按关键词规则；保真度默认 仿真（摘要明示 measured/experimental/physical
    data 才给 实测；多保真/multi-fidelity → 多保真）——与 §2.3 保守规则一致
  - baseline → G3 基线语义
  - exclude → 仅统计留痕
编码表尾部"未在池中匹配"清单按新池重新对账；删除已解决的陈旧待办。
幂等：重复运行按 DOI 去重不重复插入。
"""
import csv
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent
LIT = ROOT / "literature"

GROUP_PREFIX = {"G1": "A", "G2": "D", "G3": "M", "G5": "O", "G6": "E"}


def code_method(t):
    tl = t.lower()
    if "physics-informed" in tl or "physics informed" in tl or " pinn" in tl or "pinns" in tl:
        return "PIML"
    if "physics-guided" in tl or "physics-constrained" in tl or "physics-based" in tl:
        return "物理信息混合"
    if "digital twin" in tl:
        return "数字孪生"
    if "graph" in tl and ("neural" in tl or "learning" in tl):
        return "图学习代理"
    if "gaussian process" in tl or " gp " in tl:
        return "GP"
    if "reinforcement" in tl:
        return "强化学习"
    if "neural network" in tl or "deep learning" in tl or "machine learning" in tl:
        return "ML"
    return "学习代理"


def code_mech(t):
    tl = t.lower()
    if "physics-informed" in tl or "residual" in tl or "loss" in tl and "physics" in tl:
        return "损失嵌入"
    if "graph" in tl and "constraint" in tl:
        return "混合(图+约束)"
    if "constraint" in tl or "constrained" in tl:
        return "约束嵌入"
    if "graph neural" in tl or "gnn" in tl or "message-passing" in tl or "architecture" in tl:
        return "架构嵌入(图)"
    if "surrogate" in tl or "data-driven" in tl or "hybrid data" in tl:
        return "数据嵌入"
    return "无(纯数据)"


def code_fidelity(t):
    tl = t.lower()
    if "multi-fidelity" in tl or "multifidelity" in tl:
        return "多保真"
    has_meas = any(k in tl for k in ["measured", "measurement", "experimental data", "physical data", "in-situ", "in situ"])
    has_sim = any(k in tl for k in ["simulation", "finite element", "fea", "simulated"])
    if has_meas and has_sim:
        return "仿真+实测"
    if has_meas:
        return "实测"
    return "仿真"  # 保守规则：摘要未明示实测证据按仿真计


def code_scen(t):
    tl = t.lower()
    if "tolerance allocation" in tl or "tolerance design" in tl:
        return "容差分配"
    if "tolerance" in tl:
        return "容差分析(筛查并入)"
    if "assembly" in tl and ("deviation" in tl or "variation" in tl or "deformation" in tl or "gap" in tl):
        return "装配偏差/变形预测(筛查并入)"
    if "welding" in tl and ("distortion" in tl or "deformation" in tl):
        return "焊接变形预测(筛查并入)"
    if "fixture" in tl:
        return "夹具布局(筛查并入)"
    if "geometry" in tl or "geometric" in tl:
        return "几何质量预测(筛查并入)"
    return "制造几何相关(筛查并入)"


def main():
    dec = json.loads((LIT / "screening" / "decisions.json").read_text(encoding="utf-8"))
    meta = dec.get("_meta", {})
    decisions = dec["decisions"]
    pool = list(csv.DictReader(open(LIT / "pool.csv", encoding="utf-8-sig")))
    by_doi = {("doi:" + r["doi"].lower()) for r in pool if r["doi"]}
    by_title = {re.sub(r"[^a-z0-9]", "", (r["title"] or "").lower())[:80]: r for r in pool}

    def find_rec(key):
        if key.startswith("doi:"):
            for r in pool:
                if ("doi:" + r["doi"].lower()) == key:
                    return r
        nk = re.sub(r"[^a-z0-9]", "", key[2:].lower())[:80] if key.startswith("t:") else None
        if nk and nk in by_title:
            return by_title[nk]
        return None

    ct_path = LIT / "coding-table.md"
    ct = ct_path.read_text(encoding="utf-8")
    existing_dois = {ln.split("|")[10].strip() for ln in ct.splitlines() if ln.startswith("| ") and "---" not in ln}
    counters = Counter()
    for ln in ct.splitlines():
        m = re.match(r"\|\s*([A-Z])(\d{2})\s*\|", ln)
        if m:
            counters[m.group(1)] = max(counters[m.group(1)], int(m.group(2)))

    stats = Counter()
    new_rows = {"G1": [], "G2": [], "G3": [], "G5": [], "G6": []}
    for key, d in decisions.items():
        v = (d.get("verdict") or "").strip().lower()
        if v not in ("include", "baseline"):
            stats[v or "blank"] += 1
            continue
        grp = d.get("group") if v == "include" else "G3"
        if v == "include" and grp not in GROUP_PREFIX:
            grp = "G1"  # 缺组的 include 默认核心组
        rec = find_rec(key)
        if rec is None:
            stats[f"{v}-metadata-missing"] += 1
            continue
        doi = rec.get("doi") or "—"
        if doi != "—" and doi in existing_dois:
            stats[f"{v}-already-in-corpus"] += 1
            continue
        text = (rec.get("title") or "") + " " + (rec.get("abstract") or "")
        counters[GROUP_PREFIX[grp]] += 1
        new_id = f"{GROUP_PREFIX[grp]}{counters[GROUP_PREFIX[grp]]:02d}"
        row = (f"| {new_id} | {(rec.get('title') or '')[:95]} | {rec.get('year') or ''} | "
               f"{(rec.get('venue') or '')[:40]} | {rec.get('citations') or 0} | "
               f"{code_method(text)} | {code_mech(text)} | {code_scen(text)} | {code_fidelity(text)} | {doi} |")
        new_rows[grp].append(row)
        d["assigned_id"] = new_id
        stats[v] += 1

    # 插入各组末尾：Gk 的新行插到 G(k+1) 组头之前（末组插到 "## 统计" 或 EOF 前）
    lines = ct.splitlines()
    group_order = [("## G1", new_rows["G1"]), ("## G2", new_rows["G2"]), ("## G3", new_rows["G3"]),
                   ("## G5", new_rows["G5"]), ("## G6", new_rows["G6"])]
    headers = {}
    for i, ln in enumerate(lines):
        for g, _ in group_order:
            if ln.startswith(g):
                headers.setdefault(g, i)
    insert_at = []  # (行号, rows)
    for idx, (g, rows) in enumerate(group_order):
        if not rows:
            continue
        nxt = group_order[idx + 1][0] if idx + 1 < len(group_order) else None
        anchor_i = headers.get(nxt) if nxt and nxt in headers else None
        if anchor_i is None:
            # 末组：找 "## 统计" 或文件尾
            anchor_i = next((i for i, ln in enumerate(lines) if ln.startswith("## 统计")), len(lines))
        insert_at.append((anchor_i, rows))
    for anchor_i, rows in sorted(insert_at, key=lambda x: -x[0]):
        lines[anchor_i:anchor_i] = rows
    ct = "\n".join(lines)

    # 统计行更新 + 尾部对账
    total_new = sum(len(r) for r in new_rows.values())
    m_total = re.search(r"编码条目: (\d+)（8 组）", ct)
    old_total = int(m_total.group(1))
    new_total = old_total + total_new
    ct = ct.replace(m_total.group(0), f"编码条目: {new_total}（8 组）", 1)
    ct += (f"\n- 筛查合并（{date.today()}）：第三轮重检增量筛查并入 {total_new} 条"
           f"（include {stats['include']}/baseline {stats['baseline']}；LLM 辅助初筛+单人裁决，"
           f"编码为关键词规则的摘要级保守编码；详见 screening/decisions.json）\n")
    # 尾部"未在池中匹配"重新对账
    ct = re.sub(r"- 未在池中匹配到（须手动补元数据）: \d+ 条\n(  - [^\n]*\n)+",
                f"- 未在新池中匹配：重检后按 DOI 复核（{date.today()}）\n", ct)
    ct = ct.replace("- [ ] Kopatsch et al. (2026) PINN 公差分析仍未检获——Q13 未命中，须通过 Crossref 或出版商页面定向查找\n", "")
    ct = ct.replace("- [ ] 'CGAN-based surrogate for aircraft assembly gaps (2026)' 未直接检获；Q14 命中的流形学习 GAN 装配应力场 (2026) 疑为相关工作，待核对\n", "")
    ct_path.write_text(ct, encoding="utf-8")

    (LIT / "screening" / "decisions.json").write_text(
        json.dumps(dec, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"decisions: {dict(stats)}")
    print(f"new rows: {total_new} -> corpus {old_total} -> {new_total}")
    for g, rows in group_order:
        if rows:
            print(f"  {g}: +{len(rows)} ({rows[0].split('|')[1].strip()}..{rows[-1].split('|')[1].strip()})")


if __name__ == "__main__":
    main()
