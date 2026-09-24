# -*- coding: utf-8 -*-
"""修订版 docx 构建：submission/manuscript-numbered.md → submission/manuscript.docx
（R1 返修专用：编号与 References 已在 md 中定稿，本脚本只做渲染，不改内容。
原 build_submission.py 从旧 manuscript.md 重建编号，会覆盖修订稿，勿再直接运行。）
"""
import json, re, shutil
from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm

SUB = Path(r"D:\Data\kimi-work\PINN\papers\survey-paper-piml\submission")
MD = SUB / "manuscript-numbered.md"
OUT = SUB / "manuscript.docx"

md = MD.read_text(encoding="utf-8")

FIGCAPS = [
    "Fig. 1. Annual publication trend of the retrieved literature pool (46,114 records within the 2015–2026 protocol window, of 46,239 deduplicated records; sources: OpenAlex, Semantic Scholar, and Crossref; 2026 data through September). The 2015 bar is inflated by the capped Crossref supplementary harvest — a harvest-order artifact, not a publication-volume signal (see Section 2.1).",
    "Fig. 2. PRISMA-style flow of record identification, deduplication, tiered screening, and coding: 64,393 retrieved records; 46,239 after deduplication; three relevance tiers (A 154 / B 1,190 / C 44,895); 449 re-harvest delta candidates screened (35 included — 30 physics-informed and 5 data-driven — 414 excluded); coded corpus of 131 works in eight thematic groups (G1–G8).",
    "Fig. 3. Evolution timeline of the three method generations: classical model-based, data-driven, and physics-informed tolerance analysis.",
    "Fig. 4. The three-dimensional taxonomy: physical-integration mechanism × task type × data fidelity. Cell shading indicates indicative occupancy under abstract-level coding; sparse cells mark research whitespace rather than verified empty sets.",
    "Fig. 5. Landscape heatmap of the coded corpus (n = 131) by thematic group (G1–G8) and validation type; cell counts derive from the coding table under the conservative validation-coding rules of Section 2.3.",
    "Fig. 6. Reference architecture positioning the physics-informed tolerance module within the CPPS layering, with products/equipment/information/control integration points.",
    "Fig. 7. The drift evaluation protocol: five drift axes with graded shift levels, extrapolation error decay curves as the proposed reporting format (schematic illustration, not measured data), and the deployment dossier supplying measurable contracts to the self-adaptive system of Section 8.3.",
    "Fig. 8. Readiness ladder (R1–R5) for physics-informed tolerance models with evidence gates between rungs, and the position of the coded corpus: two-thirds of coded research works (67%) are simulation-validated (R1), no coded physics-informed work documents crossing the R2→R3 gate, and existing digital-twin systems at R4 run data-driven or classical cores.",
]

def add_runs(par, text):
    for tok in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", text):
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**"):
            par.add_run(tok[2:-2]).bold = True
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            par.add_run(tok[1:-1]).italic = True
        else:
            par.add_run(tok)

shutil.copy(OUT, SUB / "manuscript.bak-pre-r1.docx")

doc = Document()
st = doc.styles["Normal"]
st.font.name = "Times New Roman"
st.font.size = Pt(11)

lines = md.splitlines()
i = 0
n_tables = 0
while i < len(lines):
    s = lines[i].rstrip()
    if not s:
        i += 1
        continue
    if s.strip().startswith("|"):                      # markdown 表格块 → Word 表格
        block = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            block.append(lines[i].strip())
            i += 1
        rows = [[c.strip() for c in r.strip("|").split("|")] for r in block]
        rows = [r for r in rows if not all(set(c) <= set("-: ") for c in r)]
        tbl = doc.add_table(rows=0, cols=len(rows[0]))
        tbl.style = "Light Grid Accent 1"
        for ri, r in enumerate(rows):
            cells = tbl.add_row().cells
            for ci, v in enumerate(r):
                cells[ci].text = re.sub(r"\*\*", "", v)
                for par in cells[ci].paragraphs:
                    for run in par.runs:
                        run.font.size = Pt(8)
                        run.font.bold = (ri == 0)
        doc.add_paragraph()
        n_tables += 1
        continue
    if s.startswith("# "):
        doc.add_heading(s[2:].strip(), level=1)
    elif s.startswith("## "):
        doc.add_heading(s[3:].strip(), level=2)
    elif s.startswith("### "):
        doc.add_heading(s[4:].strip(), level=3)
    elif s.startswith("- "):                            # 无序列表
        p = doc.add_paragraph(style="List Bullet")
        add_runs(p, s[2:])
    elif re.match(r"^\d+\. ", s):                       # 编号列表（贡献/Highlights 等）
        p = doc.add_paragraph(style="List Number")
        add_runs(p, re.sub(r"^\d+\. ", "", s))
    elif re.match(r"^\[\d+\] ", s):                     # References 条目
        p = doc.add_paragraph(s)
        p.paragraph_format.space_after = Pt(4)
    else:
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Cm(0.75)
        add_runs(p, s)
    i += 1

doc.add_page_break()
doc.add_heading("Figure captions", level=1)
for cap in FIGCAPS:
    doc.add_paragraph(cap)

doc.save(OUT)
print(f"manuscript.docx 构建完成：内嵌表格 {n_tables} 个，图注 {len(FIGCAPS)} 条")

# ---------- 同步更新 citation-map.json ----------
mp = SUB / "citation-map.json"
if mp.exists():
    m = json.loads(mp.read_text(encoding="utf-8"))
    k2n = m.get("key2num", {})
    bump = {k: (v + 1 if v >= 38 else v) for k, v in k2n.items()}
    m2 = {"note": "R1 revision 2026-09-20: numbers >=38 shifted +1 after inserting Karniadakis et al. 2021 as [38]; [38] has no coding key (new external citation).",
          "key2num": bump, "added_in_r1": {"[38]": "Karniadakis G., et al. (2021) Physics-informed machine learning. Nature Reviews Physics 3:422-440"}}
    shutil.copy(mp, SUB / "citation-map.bak-pre-r1.json")
    mp.write_text(json.dumps(m2, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"citation-map.json 已更新（{len(bump)} 键，>=38 全部 +1）")
