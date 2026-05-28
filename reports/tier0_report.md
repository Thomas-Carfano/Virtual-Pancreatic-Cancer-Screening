# PancScan Tier 0 Smoke Test Report

- **Date:** 2026-05-26T15:26:39.882426
- **Target:** PDB 7RPZ (KRAS G12D + MRTX1133 + GDP + Mg²⁺)
- **Ligand code used:** 6IC

## Verdict

### ✅ PASS

## Acceptance criteria

| # | Criterion | Pass? |
|---|---|---|
| | ligand_code_6IC_present_in_pdb | ✅ |
| | GDP_cofactor_present | ✅ |
| | Mg_cofactor_present | ✅ |
| | rmsd_under_2_angstrom | ✅ |
| | top_score_under_minus_8 | ✅ |

## Key numbers

- Top-pose Vina score: **-14.66 kcal/mol**
- Top-pose RMSD vs crystal: **0.506 Å**

## HETATM components in PDB 7RPZ

| Component | Atom count |
|---|---|
| HOH | 275 |
| 6IC | 44 |
| GDP | 28 |
| MG | 1 |

## Docking box

- Center: (1.71, 4.93, -23.16)
- Size: (28.73, 26.68, 23.65) Å
- Native ligand atoms: 44

## All Vina poses

| Mode | Affinity (kcal/mol) | RMSD LB | RMSD UB |
|---|---|---|---|
| 1 | -14.66 | 0.00 | 0.00 |
| 2 | -9.01 | 2.74 | 4.46 |
| 3 | -8.77 | 1.72 | 2.93 |
| 4 | -8.29 | 3.60 | 9.70 |
| 5 | -8.23 | 4.04 | 9.26 |
| 6 | -8.20 | 4.01 | 9.21 |
| 7 | -8.20 | 4.36 | 7.84 |
| 8 | -8.07 | 4.41 | 11.28 |
| 9 | -7.92 | 5.93 | 11.46 |
| 10 | -7.87 | 3.09 | 9.63 |
| 11 | -7.87 | 4.61 | 8.01 |
| 12 | -7.86 | 5.09 | 8.22 |
| 13 | -7.83 | 4.61 | 8.29 |
| 14 | -7.80 | 4.41 | 7.24 |
| 15 | -7.73 | 5.81 | 12.24 |
| 16 | -7.66 | 4.63 | 7.94 |
| 17 | -7.49 | 5.50 | 11.89 |
| 18 | -7.40 | 5.22 | 11.75 |
| 19 | -7.39 | 5.43 | 9.77 |
| 20 | -7.38 | 5.39 | 11.18 |

## Environment

- python: 3.11.15
- vina: AutoDock Vina v1.2.5
- obabel: Open Babel 3.1.0 -- Nov 30 2023 -- 21:04:48
- rdkit: 2023.09.6
- Bio: 1.87
- numpy: 1.26.4
- spyrmsd: 0.9.0
- meeko_cli: found
