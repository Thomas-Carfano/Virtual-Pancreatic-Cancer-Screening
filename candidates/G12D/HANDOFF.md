# KRAS G12D — repurposing candidate handoff

> **In one sentence:** of ~6,400 existing approved/clinical drugs, these are the ones a computer
> predicts might fit the most common pancreatic-cancer driver protein (KRAS G12D) — ranked **leads
> to test in a lab**, not proven drugs or medical advice.

**Target:** KRAS G12D switch-II pocket (PDB **7RPZ**, MRTX1133-binding site).
**Library:** Broad Drug Repurposing Hub, 6,389 approved/clinical drugs.
**Engine validation:** AutoDock Vina 1.2.5 — MRTX1133 self-redock **0.506 Å**; enrichment gate (40 known G12D actives vs 600 property-matched ChEMBL decoys) **ROC-AUC 0.690 / EF 1% 6.56×**. Modest discrimination — treat rankings as noisy, trust clusters not ranks.

## Why KRAS G12D matters

G12D is the **single most common KRAS mutation in pancreatic cancer (~40%)** and the dominant disease driver. Until MRTX1133 (Mirati), no noncovalent G12D inhibitors existed. A repurposed approved drug hitting this pocket would be enormously impactful (existing safety data, fast clinical path).

## Top 10 ranked candidates

| # | Drug | Score (kcal/mol) | Known target | Note |
|---|---|---|---|---|
| 1 | **tivantinib** | −12.05 | c-MET | MET drug, previously studied in PDAC |
| 2 | arcyriaflavin-a | −11.79 | CDK4/5, CK1 | (also high on PARP1 — generic shape-fitter) |
| 3 | nemiralisib | −11.70 | PI3Kδ | (PARP1 overlap) |
| 4 | GDC-0834 | −11.64 | BTK | |
| 5 | sanguinarium-chloride | −11.57 | natural alkaloid | published anti-cancer activity |
| 6 | **LY2801653 (merestinib)** | −11.54 | MET / TAM kinases | **2nd MET inhibitor in top 6** |
| 7 | TC-F-2 | −11.49 | tool compound | |
| 8 | SAM-315 | −11.45 | kinase tool | |
| 9 | BMS-566419 | −11.30 | IKKβ | |
| 10 | exo-IWR-1 | −11.28 | Tankyrase / Wnt | cancer-pathway |

## The most interesting signal: G12D-selective hits (NOT in PARP1 top-200)

**The MET-inhibitor cluster** — four MET drugs at the top of an unbiased screen is a real chemotype pattern. The MET ATP-pocket shares geometry with KRAS switch-II.
- `tivantinib` (#1), `LY2801653 / merestinib` (#2 selective), `PHA-665752`, `SU11274`.

**Other PDAC-coherent leads:**
- **BMS-833923** (Hedgehog/Smoothened) — Hedgehog is a known PDAC pathway; this exact drug has had PDAC clinical trials.
- **atovaquone** — antimalarial with published anti-cancer activity via OXPHOS inhibition.
- **avapritinib** (KIT/PDGFRα), **LDN-212854 / LDN193189** (BMP-signaling).

Full list: `top25_selective.csv`.

## Suggested first wet-lab assay

1. **In-cell killing in KRAS G12D PDAC lines:** **AsPC-1**, **SU.86.86**, **Hs 766T** (all G12D+). 72-h CellTiter-Glo viability, dose–response 10 nM – 10 μM.
2. **Selectivity control:** **BxPC-3** (KRAS-wild-type PDAC) — drug should kill G12D+ lines preferentially.
3. **Mechanism readout:** **pERK / pAKT immunoblot** at 1–2 h post-treatment. If the drug genuinely engages KRAS, MAPK signaling should drop.
4. **If selective killing observed:** escalate to direct binding (SPR / ITC vs purified KRAS-G12D-GDP) and competition with MRTX1133.

Rough CRO cost (Reaction Biology / Crown / Eurofins): ~$1.5–3k per compound, turnaround 4–6 weeks.

## Honest caveats

- Gate AUC 0.690 = **meaningful signal, noisy rank**. The MET cluster is plausible, but could be a generic kinase-ATP chemotype effect — wet lab is the arbiter.
- Vina is an approximation (±3 kcal/mol). Individual hits are hypotheses.
- Vina doesn't model induced fit; some hits may require a different KRAS conformation.

## Files

- `top50.csv` — full top-50 ranked
- `top25_selective.csv` — G12D-selective leads (NOT also high on PARP1)
- Receptor + box: `pancscan/tier1/receptor.pdbqt`, `pancscan/tier1/dock_config.json`
- Full screen results: `pancscan/libraries/repurposing_hub/screen_KRAS_G12D/results.csv`
