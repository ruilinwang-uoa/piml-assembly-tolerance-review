# -*- coding: utf-8 -*-
"""全文一致性体检（结构修订 v4 后）
A. 交叉引用：正文每个 §x.y / Section x.y 必须存在于标题集合
B. 图表配对：Fig.1–8、Table 1–2 均在正文被引用；FIGCAPS 与图文件齐全
C. 统计口径：74%/53/72/19/26%/72%/67%/1779/94/52 关键数字出现且一致
D. 引用键：正文键全集 ⊆ references.md 条目集
"""
import re, json, pathlib, sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parent
md = (ROOT / "manuscript.md").read_text(encoding="utf-8")
fails = []

# ---- A. 交叉引用 ----
heads = set()
for m in re.finditer(r"(?m)^(#{1,3}) (\d+(?:\.\d+)*)[\. ]", md):
    heads.add(m.group(2))
top = {h.split(".")[0] for h in heads}

refs = set()
for m in re.finditer(r"§(\d+(?:\.\d+)*)", md):
    refs.add(m.group(1))
for m in re.finditer(r"\bSections? (\d+(?:\.\d+)?)", md):
    refs.add(m.group(1))
# Sections 列表中的其余数字（"Sections 3, 4, 6" / "Sections 8 and 9" / "Sections 4–6"）
for m in re.finditer(r"\bSections ((?:\d+(?:\.\d+)?(?:\s*(?:,|–|and)\s*)?)+)", md):
    for n in re.findall(r"\d+(?:\.\d+)?", m.group(1)):
        refs.add(n)
bad = sorted(r for r in refs if r not in heads and r not in top)
print(f"A. 交叉引用 {len(refs)} 个唯一目标；无效目标: {bad or '无'}")
if bad: fails.append(("A", bad))

# ---- B. 图表配对 ----
for i in range(1, 9):
    n = len(re.findall(rf"Fig\. {i}\b", md))
    exists = bool(list(ROOT.glob(f"figures/fig{i}-*.png")))
    print(f"B. Fig.{i}: 正文引用 {n} 处；PNG 存在 {exists}")
    if n == 0 or not exists: fails.append(("B", f"Fig.{i}"))
for t in ["Table 1", "Table 2", "Table 3"]:
    n = len(re.findall(rf"\b{t}\b", md))
    print(f"B. {t}: 正文引用 {n} 处")
    if n == 0: fails.append(("B", t))
# Table 1 表格本体存在
assert "| Review | Focus |" in md, "Table 1 表格本体缺失"
# Table 2 行数与 table2-meta.json 一致（若存在）
t2m = ROOT / "literature/table2-meta.json"
if t2m.exists():
    import re as _re
    t2rows = 0
    for ln in (ROOT / "literature/table2-selection.md").read_text(encoding="utf-8").splitlines():
        if _re.match(r"\|\s*[A-Z]\d{2}\s*\|", ln):
            t2rows += 1
    t2expect = json.loads(t2m.read_text(encoding="utf-8"))["rows"]
    ok2 = t2rows == t2expect
    print(f"B. Table 2 行数 {t2rows} == meta {t2expect}: {'✅' if ok2 else '❌'}")
    if not ok2: fails.append(("B", "table2-rows"))
print("B. Table 1 表格本体 ✅；Table 2 为独立文件（table2-selection.md + table2.docx）")

# ---- C. 统计口径（stats-v4 存在时数据驱动；否则回退 v3 旧口径——过渡期预期红） ----
STATS4 = ROOT / "literature/section6-stats-v4.json"
if STATS4.exists():
    s4 = json.loads(STATS4.read_text(encoding="utf-8"))
    sim, meas = s4["sim_strict"], s4["meas"]
    corpus_total = s4["corpus"]["total"]
    pool_csv = ROOT / "literature/pool.csv"
    import csv as _csv
    pool_n = sum(1 for _ in _csv.DictReader(open(pool_csv, encoding="utf-8-sig")))
    checks = [
        (f"strict share {sim['k']}/{sim['n']}", f"{sim['k']} of {sim['n']}" in md or f"{sim['k']}/{sim['n']}" in md),
        (f"strict pct {round(sim['pct'])}%", f"{round(sim['pct'])}%" in md),
        (f"meas {meas['k']}/{meas['n']}", f"{meas['k']}" in md and f"{meas['n']}" in md),
        (f"pool {pool_n:,}", f"{pool_n:,}" in md),
        (f"corpus {corpus_total}", str(corpus_total) in md),
        ("table2 rows", str(json.loads(t2m.read_text(encoding='utf-8'))['rows']) in md if t2m.exists() else True),
    ]
    for name, ok in checks:
        print(f"C. {name}: {'✅' if ok else '❌'}")
        if not ok: fails.append(("C", name))
    stale_all = ["68 篇", "69 coded", "n=69", "50/69", "89 条", "89 works",
                 "94 works", "53 of 72", "18 (72%)", "10 (67%)", "52 representative",
                 "n = 91", "n=91", "2071", "74% of works"]
    for stale in stale_all:
        if stale in md:
            fails.append(("C-stale", stale)); print(f"C. 旧口径残留 ❌ {stale}")
    print("C. stats-v4 数据驱动校验 + 全量旧口径扫描完成")
else:
    stats = json.loads((ROOT / "literature/section6-stats-v3.json").read_text(encoding="utf-8"))
    checks = [
        ("74%", "74%" in md), ("53 of 72", "53 of 72" in md),
        ("18 (72%)", "18 (72%)" in md), ("10 (67%)", "10 (67%)" in md),
        ("1,779", "1,779" in md), ("94 works", "94 works" in md),
        ("52 representative", "52 representative" in md),
    ]
    cons = (stats["sim"] == 53 and stats["research"] == 72 and stats["total"] == 94)
    for name, ok in checks:
        print(f"C. {name}: {'✅' if ok else '❌'}")
        if not ok: fails.append(("C", name))
    print(f"C. section6-stats-v3.json 内部一致: {'✅' if cons else '❌'}（过渡期：stats-v4 未生成）")
    if not cons: fails.append(("C", "stats-json"))
    for stale in ["68 篇", "69 coded", "n=69", "50/69", "89 条", "89 works"]:
        if stale in md:
            fails.append(("C-stale", stale)); print(f"C. 旧口径残留 ❌ {stale}")
    print("C. 旧口径残留扫描完成")

# ---- D. 引用键 ----
keys = set()
for m in re.finditer(r"\[([A-Z]\d{2}(?:\s*,\s*[A-Z]\d{2})*)\]", md):
    keys.update(k.strip() for k in m.group(1).split(","))
refs = set()
for ln in (ROOT / "literature/references.md").read_text(encoding="utf-8").splitlines():
    if ln.startswith("## "): break
    m = re.match(r"- \[([A-Z]\d{2})\]", ln)
    if m: refs.add(m.group(1))
undef = sorted(keys - refs)
print(f"D. 正文引用键 {len(keys)} 个；references.md 未定义: {undef or '无'}")
if undef: fails.append(("D", undef))

# ---- E. 新节数字与 search-log 一致性抽查（2026-09-19 第三轮重检后口径） ----
meth = md.split("# 2. Review methodology")[1].split("# 3. Background")[0]
echk = [
    ("三轮协议披露", "PRISMA reporting principles" in meth and "Q1–Q7" in meth and "Q8–Q14" in meth),
    ("窗口 2019→2015", "2019–2026" in meth and "2015–2026" in meth),
    ("截断披露", "top 100" in meth and "without caps" in meth),
    ("池 46,239", "46,239" in meth),
    ("分层 154/1190/44895", "154 records" in meth and "1,190" in meth and "44,895" in meth),
    ("语料 131/8 组", "131 works" in meth and "eight thematic groups" in meth),
    ("121 核验", "121 verified" in meth),
    ("S2 重试声明", "rate-limited" in meth),
    ("LLM 辅助筛查披露", "LLM-assisted" in meth),
    ("筛查 449/35", "449" in meth and "35 inclusions" in meth),
]
for name, ok in echk:
    print(f"E. {name}: {'✅' if ok else '❌'}")
    if not ok: fails.append(("E", name))

print()
if fails:
    print("❌ 体检未通过:", fails); sys.exit(1)
print("✅ 全部通过")
