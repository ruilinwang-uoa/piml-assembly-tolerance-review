# -*- coding: utf-8 -*-
"""B-3/B-4 修复：Crossref 元数据核验 + 定向补检 + 正式参考文献列表生成
输出: literature/references.md, literature/crossref-verified.json, literature/targeted-search.md
"""
import json, re, time
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parent
LIT = ROOT / "literature"
MAILTO = "survey@local.dev"
S = requests.Session()
S.headers["User-Agent"] = f"lit-review-tool/1.0 (mailto:{MAILTO})"

# ---------- 解析编码表 ----------
ct = (LIT/"coding-table.md").read_text(encoding="utf-8")
entries = []
for line in ct.splitlines():
    if line.startswith("| ") and not line.startswith("| 编号") and "---" not in line:
        c = [x.strip() for x in line.strip("|").split("|")]
        if len(c) >= 10 and re.fullmatch(r"[A-Z]\d{2}", c[0]):
            entries.append({"id":c[0],"title":c[1],"year":c[2],"venue":c[3],"doi":c[9]})
print("entries:", len(entries))

def cr_get_doi(doi):
    r = S.get(f"https://api.crossref.org/works/{doi}?mailto={MAILTO}", timeout=30)
    if r.status_code != 200: return None
    return r.json()["message"]

def fmt_ref(m):
    au = m.get("author", [])
    names = ", ".join(f"{a.get('family','')} {a.get('given','')[:1]}." for a in au[:8])
    if len(au) > 8: names += ", et al."
    title = (m.get("title") or [""])[0]
    cont = (m.get("container-title") or [""])[0]
    yr = ""
    for k in ("published-print","published-online","issued"):
        if m.get(k): yr = str(m[k]["date-parts"][0][0]); break
    vol = m.get("volume",""); iss = m.get("issue",""); pg = m.get("page","")
    vi = f"{vol}" + (f"({iss})" if iss else "") + (f": {pg}" if pg else "")
    doi = m.get("DOI","")
    parts = [x for x in [names, f"({yr})", title+".", cont, vi, f"https://doi.org/{doi}"] if x]
    return " ".join(parts)

results, fails = {}, []
for e in entries:
    doi = e["doi"]
    if not doi or doi == "—":
        fails.append((e["id"], "无 DOI", e["title"][:60])); continue
    try:
        m = cr_get_doi(doi)
        if m is None:
            fails.append((e["id"], f"HTTP 非200", doi)); continue
        # 标题一致性粗检
        cr_title = ((m.get("title") or [""])[0]).lower()
        my_title = e["title"].lower()[:40]
        match = my_title[:25] in cr_title or cr_title[:25] in my_title
        yr = ""
        for k in ("published-print","published-online","issued"):
            if m.get(k): yr = str(m[k]["date-parts"][0][0]); break
        results[e["id"]] = {"ref": fmt_ref(m), "title_match": match,
                            "cr_title": (m.get("title") or [""])[0], "my_title": e["title"],
                            # 2026-09-16 新增显式字段（Table 2 年份同步/被引源）
                            "cr_year": yr,
                            "cr_venue": (m.get("container-title") or [""])[0],
                            "cr_cites": m.get("is-referenced-by-count", 0)}
        if not match:
            fails.append((e["id"], "标题不一致(须人工核对)", f"编码: {e['title'][:45]} || CR: {cr_title[:60]}"))
    except Exception as ex:
        fails.append((e["id"], f"异常 {ex}", doi))
    time.sleep(0.12)

print(f"verified={len(results)} fails={len(fails)}")
(LIT/"crossref-verified.json").write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- 定向补检：Kopatsch + CGAN aircraft assembly gap ----------
targeted = []
for label, q in [
    ("Kopatsch PINN tolerance", "Kopatsch physics-informed tolerance"),
    ("Kopatsch tolerance analysis", "Kopatsch tolerance analysis neural network"),
    ("CGAN aircraft assembly gap", "conditional generative adversarial surrogate aircraft assembly gap"),
    ("CGAN assembly gap surrogate", "CGAN surrogate model assembly gap prediction aircraft"),
]:
    try:
        r = S.get("https://api.crossref.org/works", params={
            "query.bibliographic": q, "rows": 5, "mailto": MAILTO,
            "filter": "from-pub-date:2023-01-01"}, timeout=30)
        items = r.json()["message"]["items"]
        targeted.append(f"\n### {label} — `{q}`\n")
        for it in items:
            t = (it.get("title") or [""])[0]
            c = (it.get("container-title") or [""])[0]
            yr = (it.get("issued",{}).get("date-parts",[[None]])[0][0])
            targeted.append(f"- {yr} | {t} | {c} | https://doi.org/{it.get('DOI','')}")
    except Exception as ex:
        targeted.append(f"\n### {label} — FAIL {ex}")
    time.sleep(0.3)

(LIT/"targeted-search.md").write_text(
    "# 定向补检记录（Crossref bibliographic search，2026-09-14）\n" + "\n".join(targeted), encoding="utf-8")

# ---------- 生成 references.md ----------
from datetime import date
GEN_DATE = str(date.today())
lines = ["# 正式参考文献列表（Crossref 元数据核验版）\n",
 f"> 生成：{GEN_DATE}。元数据来源：Crossref API 逐 DOI 核验。",
 "> ✅=标题一致性机检通过；⚠️=标题不一致或无 DOI，须人工核对（见文末清单）。",
 "> 注意：维度编码（机制/场景/保真度）仍为摘要级，全文精读尚未逐条执行。\n"]
warn_ids = {f[0] for f in fails}
for e in entries:
    rid = e["id"]
    if rid in results:
        mark = "✅" if results[rid]["title_match"] else "⚠️"
        lines.append(f"- [{rid}] {mark} {results[rid]['ref']}")
    else:
        lines.append(f"- [{rid}] ⚠️ {e['title']} ({e['year']}). {e['venue']}.（Crossref 未解析，编码表元数据）")
lines.append("\n## 须人工核对清单\n")
for fid, reason, detail in fails:
    lines.append(f"- [{fid}] {reason}: {detail}")
(LIT/"references.md").write_text("\n".join(lines), encoding="utf-8")
print("references.md written;", len(entries), "entries;", len(fails), "to check")
for f in fails: print(" ", f[0], f[1], f[2][:80])
