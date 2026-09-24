# -*- coding: utf-8 -*-
"""E13（FNO，arXiv 无 Crossref 记录）被引数补采：OpenAlex 按 title 检索 cited_by_count，
回填 coding-table.md 的 被引 列（当前为 —）。幂等；仅在配额可用时运行。"""
import re
import sys
from pathlib import Path

import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent
TITLE = "Fourier Neural Operator for Parametric Partial Differential Equations"

r = requests.get("https://api.openalex.org/works",
                 params={"search": TITLE, "per_page": 5, "mailto": "survey@local.dev"}, timeout=30)
r.raise_for_status()
cites = None
for w in r.json().get("results", []):
    if TITLE[:30].lower() in (w.get("display_name") or "").lower():
        cites = w.get("cited_by_count", 0)
        print(f"matched: {w.get('display_name')[:60]} -> {cites}")
        break
if cites is None:
    print("no match; leaving 被引 as-is")
    raise SystemExit(0)

ct_p = ROOT / "literature/coding-table.md"
ct = ct_p.read_text(encoding="utf-8")
pat = re.compile(r"(\| E13 \| Fourier Neural Operator for Parametric Partial Differential Equations \| 2021 \| ICLR \(arXiv:2010\.08895\) \| )([^|]+)( \|)")
m = pat.search(ct)
if not m:
    print("E13 row not matched — check manually")
    raise SystemExit(1)
if m.group(2).strip() not in ("—", ""):
    print(f"already set: {m.group(2).strip()}")
    raise SystemExit(0)
ct = pat.sub(lambda mm: mm.group(1) + f" {cites} " + mm.group(3), ct, count=1)
ct_p.write_text(ct, encoding="utf-8")
print(f"E13 被引: — -> {cites}")

g = ROOT / "scripts/build_coding_table.py"
s = g.read_text(encoding="utf-8")
s2 = s.replace('"2021","ICLR (arXiv:2010.08895)","—"', f'"2021","ICLR (arXiv:2010.08895)","{cites}"')
if s2 != s:
    g.write_text(s2, encoding="utf-8")
    print("generator FALLBACK synced")
