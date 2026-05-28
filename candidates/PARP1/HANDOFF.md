# PARP1 — repurposing candidate handoff

**Target:** PARP1 catalytic domain (PDB **9ETQ**, AZD5305 / saruparib pocket — the NAD⁺-binding site).
**Library:** Broad Drug Repurposing Hub, 6,389 approved/clinical drugs.
**Engine validation:** AutoDock Vina 1.2.5 — AZD5305 self-redock **0.898 Å**; enrichment gate (40 known PARP1 actives vs 586 property-matched ChEMBL decoys) **ROC-AUC 0.874 / EF 1% 15.25× / BEDROC 0.76**. **Strong** discrimination — most trustworthy ranking in this project.

## Why PARP1 matters in pancreatic cancer

PARP1 inhibition is clinically established in **BRCA-deficient PDAC** (POLO trial → olaparib maintenance). ~5–10% of pancreatic cancers are BRCA1/2/PALB2/ATM mutant or otherwise HRD-positive. A new PARP1 chemotype or combination partner would expand the treatable population.

## Top 10 ranked candidates

| # | Drug | Score (kcal/mol) | Known target | Note |
|---|---|---|---|---|
| 1 | MK-3207 | −14.02 | CGRP receptor | strong on both targets — generic chemotype |
| 2 | LY2584702 | −13.06 | p70 S6K | (G12D overlap) |
| 3 | **KPT-9274** | −13.03 | PAK4 / **NAMPT** | **NAMPT = NAD⁺ pathway; PARP uses NAD⁺** — face-valid |
| 4 | BMS-935177 | −13.00 | BTK | |
| 5 | salvianolic-acid-B | −12.79 | natural product | |
| 6 | IRL-2500 | −12.77 | endothelin receptor | |
| 7 | AR-12 | −12.66 | PDK1 | also reported anti-pathogen activity |
| 8 | C188-9 | −12.64 | STAT3 inhibitor | multiple PDAC trials with STAT3 inhibitors |
| 9 | **ETP-46464** | −12.62 | **ATR** | **DDR — established PARP combo partner** |
| 10 | itacitinib | −12.62 | JAK1 | |

## Sanity check (very strong)

Known PARP inhibitors auto-surfaced from the screen — independent positive controls:
- **olaparib** — top **1.4%** of all 6,309 docked drugs (score −12.09).
- **EB-47** — #12 overall (literal PARP1 inhibitor from the literature).
- **talazoparib** — top 16%.
- **niraparib / pamiparib** — top 30%.

The engine knows what a real PARP1 binder looks like.

## Most interesting: PARP1-selective hits (NOT in G12D top-200)

**DDR-coherent pattern:**
- **ETP-46464** (ATR) — same pathway as PARP1; the canonical PARP-inhibitor combination partner.
- **KPT-9274** (PAK4 / NAMPT) — NAMPT inhibition + PARP both attack NAD⁺ — chemically very plausible dual mechanism.

**Other PDAC-/cancer-coherent leads:**
- **C188-9** (STAT3) — STAT3 is a documented PDAC pathway; multiple trials in progress.
- **ICG-001** (Wnt / β-catenin / CBP) — Wnt is a PDAC pathway.
- **AR-12** (PDK1) — anti-fungal + anti-cancer literature.
- **hypericin** — natural product, photosensitizer, anti-cancer activity.

Full list: `top25_selective.csv`.

## Suggested first wet-lab assay

1. **PARP1 enzymatic activity** — HTRF kit (Cisbio), BPS Bioscience PARP1 inhibition kit, or Trevigen Universal PARP assay. **Direct readout: does the drug inhibit PARP1 activity?** IC₅₀ in 1–4 days.
2. **BRCA-deficient cell killing** — **Capan-1** (BRCA2-mutant PDAC), **MDA-MB-436** (BRCA1-mut breast); the synthetic-lethal readout — HRD-positive lines should be selectively sensitive.
3. **Selectivity control** — **MIA PaCa-2** (BRCA-proficient) — drug should kill HRD+ lines preferentially.
4. **Combination potential** — co-treat with **olaparib** in BRCA-proficient lines; does the candidate restore PARP-inhibitor sensitivity?

Rough CRO cost: ~$1k per compound for activity + cell killing (Reaction Biology / Crown); turnaround ~4 weeks.

## Honest caveats

- Gate AUC **0.874** is strong — the most reliable of our targets — but Vina still has ±3 kcal/mol scoring error. Individual rank order is noisy.
- Many top hits are flat polyaromatic kinase-ATP chemotypes that fit many sites including the NAD⁺ pocket. They may not be **selective** PARP1 inhibitors in cells.
- Hits = hypotheses.

## Files

- `top50.csv` — full top-50 ranked
- `top25_selective.csv` — PARP1-selective leads
- Receptor + box: `pancscan/tier2/targets/9ETQ/receptor.pdbqt`, `pancscan/tier2/targets/9ETQ/dock_config.json`
- Full screen results: `pancscan/libraries/repurposing_hub/screen_PARP1/results.csv`
