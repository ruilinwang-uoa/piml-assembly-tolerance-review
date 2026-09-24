# Reproducibility Package — Physics-Informed Machine Learning for Assembly Tolerance Analysis in Smart Manufacturing Systems: A Review

This repository contains the search records, screening materials, coded literature, analysis scripts, references, and figures used in the manuscript:

> **Physics-Informed Machine Learning for Assembly Tolerance Analysis in Smart Manufacturing Systems: A Review**

The repository provides the frozen evidence base used for the review and supports reproduction of the main quantitative analyses and figures.

## Repository structure

```text
.
├── README.md
├── search_literature.py
├── harvest_v2.py
├── harvest_alt.py
├── export_screening.py
├── apply_screening.py
├── build_coding_table.py
├── build_stats_v3.py
├── build_stats_v4.py
├── statslib.py
├── build_table2_selection.py
├── build_references.py
├── build_figures.py
├── check_consistency.py
├── fetch_e13_cites.py
├── build_docx_from_numbered.py
├── patch_claims_v5.py
├── patch_newwriting_v5.py
├── patch_numbers_v5.py
│
├── figures/
│   ├── fig1-publication-trend.png
│   ├── fig2-prisma-flow.png
│   ├── fig3-evolution-timeline.png
│   ├── fig4-taxonomy-3d.png
│   ├── fig5-landscape-heatmap.png
│   ├── fig6-system-architecture.png
│   ├── fig7-drift-protocol.png
│   └── fig8-readiness-ladder.png
│
└── literature/
    ├── pool.csv
    ├── pool.json
    ├── search-log.md
    ├── harvest-v2-log.json
    ├── year-tier-stats.json
    ├── coding-table.md
    ├── coding-candidates.json
    ├── section6-stats-v2.json
    ├── section6-stats-v3.json
    ├── section6-stats-v4.json
    ├── stats-v4-report.md
    ├── table1-selection.md
    ├── table2-selection.md
    ├── table2-meta.json
    ├── references.md
    ├── crossref-verified.json
    ├── literature-inventory.md
    ├── targeted-search.md
    └── screening/
        ├── CRITERIA.md
        ├── chunk-001.md ... chunk-009.md
        └── decisions.json
```

## Search and screening

The final deduplicated literature pool contains **46,239 records** collected from OpenAlex, Semantic Scholar, and Crossref. Search queries, retrieval logs, and related metadata are stored in the `literature/` directory.

Screening materials are stored in `literature/screening/`:

- `CRITERIA.md` — inclusion and exclusion criteria.
- `chunk-001.md` to `chunk-009.md` — screening batches.
- `decisions.json` — screening decisions and exclusion reasons.

The screening process used an LLM-assisted first pass followed by author adjudication.

## Coded corpus

The final coded corpus is stored in:

```text
literature/coding-table.md
```

It contains **131 works** organized into eight thematic groups covering physics-informed assembly/tolerance methods, digital twins and geometry assurance, data-driven deviation prediction, classical tolerance analysis, optimization, enabling technologies, methodological background, and knowledge representation.

## Statistical analysis

The main statistical analysis is implemented in:

```text
statslib.py
build_stats_v4.py
```

The corresponding outputs are:

```text
literature/section6-stats-v4.json
literature/stats-v4-report.md
```

To regenerate the main statistics:

```bash
python build_stats_v4.py
```

The representative comparison matrix used in the manuscript can be regenerated with:

```bash
python build_table2_selection.py
```

## References

Reference and bibliographic verification materials are stored in:

```text
literature/references.md
literature/crossref-verified.json
literature/targeted-search.md
literature/literature-inventory.md
```

Reference metadata can be refreshed with:

```bash
python build_references.py
```

Internet access is required for Crossref queries.

## Figures

The `figures/` directory contains the eight figures used in the manuscript. The scripted figure set can be regenerated with:

```bash
python build_figures.py
```

## Environment

The scripts were developed for **Python 3.10+**.

Install the main dependencies with:

```bash
python -m pip install requests numpy matplotlib
```

For the optional Word-generation utility:

```bash
python -m pip install python-docx
```

## Basic reproduction workflow

From the repository root:

```bash
python build_stats_v4.py
python build_table2_selection.py
python build_figures.py
```

The repository includes the frozen data and outputs used in the manuscript. Because external literature databases are continuously updated, a new live search may not return exactly the same records or metadata as the archived September 2026 snapshot.
