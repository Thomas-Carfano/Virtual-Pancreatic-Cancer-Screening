# Known-Bad Claims Denylist

> A running list of factual claims we've already proven wrong in this project. **Before publishing any new content, check whether your claim contradicts any entry here.** If it does, use the corrected value (or cite the primary source instead).
>
> Maintained alongside `must_verify_claim_types.md` and `structure_manifest.csv`. Last updated 2026-05-22.

## How to use this file

1. When commissioning a new content-generation agent, pass this file as a "do-not-repeat" reference.
2. Before any external-facing publication, grep your draft for the **denylisted phrases** in column 1.
3. If a match appears, swap to the **correct value** in column 2.
4. Update the file whenever a new error is confirmed in audits.

## Denylist

### Drug clinical status

| Denylisted claim | Correct value | Primary source | Verified |
|---|---|---|---|
| MRTX1133 is in Phase 1/2 / showing ~30–40% response rate / ~70–80% disease control | NCT05737706 terminated before Phase 2; registry reason "formulation challenges"; secondary reporting cites variable/suboptimal PK. Remains preclinical proof-of-concept and best self-docking positive control. | ClinicalTrials.gov NCT05737706 + FierceBiotech 2025 | 2026-05-22 |
| Sotorasib FDA-approved for PDAC | FDA-approved for **KRAS G12C+ NSCLC (May 2021)** and **KRAS G12C+ CRC + panitumumab (Jan 2025)** only. PDAC use is off-label. | FDA Drugs labels | 2026-05-22 |
| Adagrasib FDA-approved (with PDAC implied) | FDA-approved for **KRAS G12C+ NSCLC (Dec 2022)** and **KRAS G12C+ CRC + cetuximab (Jun 2024)** only. PDAC use is off-label. | FDA Drugs labels | 2026-05-22 |
| Divarasib (GDC-6036) FDA-approved (Roche/Genentech 2024) | Investigational. Phase 3 head-to-head vs sotorasib/adagrasib ongoing. **Not FDA-approved.** | ClinicalTrials.gov + Genentech IR | 2026-05-22 |
| Zenocutuzumab "FDA approved Dec 2024 for NRG1+ tumors including PDAC" | Zenocutuzumab-zbco received FDA **accelerated** approval Dec 4 2024 for advanced/unresectable/metastatic **NRG1 fusion-positive NSCLC OR pancreatic adenocarcinoma after prior systemic therapy**. May 8 2026 added cholangiocarcinoma after prior systemic therapy. Use exact indication language, not "NRG1+ tumors including PDAC." | FDA approval pages Dec 2024 + May 2026 | 2026-05-22 |
| Pelareorep "Phase 3 cleared by FDA" / "62% ORR in PDAC" (no caveat) | FDA aligned on Phase 3 trial design 2025; trial launch H1 2026 — NOT yet enrolling. 62% ORR is from n=13 evaluable in GOBLET Cohort 1; later updates 69% ORR. Small n, wide CI. | Oncolytics Biotech IR 2025 + GOBLET ASCO 2025 | 2026-05-22 |
| Trastuzumab deruxtecan / T-DXd is "most clinically validated ADC across solid tumors including PDAC" | The tumor-agnostic FDA approval technically covers PDAC at HER2 IHC 3+ — but the **DESTINY-PanTumor02 PDAC cohort was closed for futility (0 ORR in first 15 of 25 patients)**. Practical PDAC efficacy is null. | ESMO 2023 + AstraZeneca update | 2026-05-22 |

### Lab attributions

| Denylisted claim | Correct value | Primary source | Verified |
|---|---|---|---|
| The Folding@home KRAS-VHL E3 ligase MD work was done by the Chodera lab at MSKCC | Done by **Xuhui Huang's lab at UW-Madison** (with HKUST collaborators). Primary paper: **Qiu et al. *JACS Au* 2024** (DOI 10.1021/jacsau.4c00503). Chodera lab is a separate F@h power-user, but did not author the KRAS-VHL paper. | F@h blog 2025-09-18 + Qiu et al. JACS Au 2024 | 2026-05-22 |
| PMV Pharmaceuticals (now Pfizer) / "Pfizer's 2023 acquisition of PMV consolidated the program" | **PMV Pharmaceuticals remains independent** (NASDAQ: PMVP). Pfizer never acquired PMV. | SEC filings + NASDAQ listing | 2026-05-22 |

### Platform / software compatibility

| Denylisted claim | Correct value | Primary source | Verified |
|---|---|---|---|
| OpenMM has Apple Metal backend | Upstream OpenMM platforms are CUDA, HIP, OpenCL, CPU, Reference. **No native Metal platform.** On Apple Silicon use the OpenCL platform, or the third-party `philipturner/openmm-metal` plugin (translates OpenCL kernels to Metal). | github.com/openmm/openmm docs + philipturner/openmm-metal | 2026-05-22 |
| OpenFE requires Rosetta 2 emulation on Apple Silicon | **OpenFE installs natively on osx-arm64.** macOS x86_64 is no longer supported. The real Apple-Silicon constraint is that OpenFE's GPU-accelerated FEP backend is CUDA-only — falls back to OpenMM CPU/OpenCL. | docs.openfree.energy/en/stable/installation.html | 2026-05-22 |
| `brew install miniforge` is the correct syntax | Miniforge is distributed as a Cask: **`brew install --cask miniforge`**. Conda-forge upstream recommends the PKG installer over Homebrew because Homebrew auto-updates can destroy environments. | github.com/conda-forge/miniforge | 2026-05-22 |
| fpocket is GPL-3 | fpocket is **MIT** (Discngine/fpocket master branch). An intermediate audit incorrectly flagged it as GPL-3 and a subsequent verification confirmed MIT. Any binary bundle should preserve the LICENSE file from the exact source/version used. | raw.githubusercontent.com/Discngine/fpocket/master/LICENSE | 2026-05-22 |

### Epidemiology

| Denylisted claim | Correct value | Primary source | Verified |
|---|---|---|---|
| US PDAC ~64,000 new cases / 4th leading cancer death | **~67,530 new cases / 3rd leading cancer death (ACS 2026)** — surpassed breast for #3 several years ago | ACS *Cancer Facts & Figures 2026* | 2026-05-22 |
| TP53 mutation rate in PDAC is 13–50% | **~65–75% (modern consensus; range 60–80%)** — the "13–50%" range conflated mutation rate with downstream survival numbers | Multiple TCGA-PAAD + cohort reviews | 2026-05-22 |
| Stromal volume of PDAC tumors is 50–80% | **80–90% canonical** | Standard PDAC histology reviews | 2026-05-22 |
| KRAS G12V in PDAC is ~29% | **~32.5%** (CCR 2025); literature range 30–36% | Modern cohort analyses | 2026-05-22 |
| R175H is ~10% of PDAC (the largest non-Y220C structural mutant) | **~3% PDAC overall; ~5–6% of TP53-mutant PDAC** — still the largest structural mutant in PDAC but ~2× overstated in some drafts | TCGA-PAAD + IARC TP53 database | 2026-05-22 |

### Cell line characteristics

| Denylisted claim | Correct value | Primary source | Verified |
|---|---|---|---|
| Hs 766T is a KRAS-WT line | **Hs 766T is KRAS Q61H homozygous** (Cellosaurus CVCL_0334). Historical literature has the WT call wrong; Cellosaurus explicitly flags this. **BxPC-3 is the only true KRAS-WT line** in the canonical PDAC panel. | Cellosaurus CVCL_0334 | 2026-05-22 |
| AsPC-1 has SMAD4 homozygous deletion | **AsPC-1 has SMAD4 R100T homozygous missense** — protein is expressed but inactivated. Different mechanism, different drug vulnerability profile than a deletion. | Cellosaurus + DepMap | 2026-05-22 |
| AsPC-1 has CDKN2A homozygous deletion | **AsPC-1 has CDKN2A frameshift** (no protein either way, but mechanistically distinct) | Cellosaurus | 2026-05-22 |
| Capan-1 has SMAD4 homozygous deletion | **Capan-1 has SMAD4 S343* stop-gain** | Cellosaurus | 2026-05-22 |

### Software versions / dataset sizes (volatile — re-verify before use)

| Denylisted claim | Correct value (as of mid-2026) | Primary source | Verified |
|---|---|---|---|
| AlphaFold3 weights released Feb 2025 | **Released November 2024** (non-commercial use only) | DeepMind release notes | 2026-05-22 |
| Enamine REAL ~70B compounds | **~94.5B as of April 2026** | Enamine product page | 2026-05-22 |
| ZINC22 ~55B 2D compounds | **~37.2B 2D / ~4.5B 3D** per Tingle & Irwin 2023 | Tingle *J Chem Inf Model* 2023 | 2026-05-22 |
| PDC (CPTAC) ~70 TB of holdings | **~29 TB managed; ~785 TB cumulative downloads** | ICF client story | 2026-05-22 |
| Docking@Home is an existing BOINC project | **Retired May 2014** — University of Delaware closed it for lack of resources. Cite only as a historical precedent. | UDel project news | 2026-05-22 |

### PDB IDs and structural biology

| Denylisted claim | Correct value | Primary source | Verified |
|---|---|---|---|
| PDB 7JWU = p53 Y220C structure | **PDB 7JWU = human ALDH1A1 + (R)-28 pyrazolopyrimidinone** (Hurley/Buchman 2020). For Y220C use 2VUK (PhiKan083), 5G4N/5G4O (fluorinated PhiKan083), 5O1C/H/I (MB-series), 9BR4 (rezatapopt). | RCSB | 2026-05-22 |
| PDB 7T47 = KRAS G12C + divarasib | **PDB 7T47 = KRAS G12D + MRTX1133 + GppCp** (active-state version of 7RPZ). For divarasib + G12C use **9PZY** or **9DMM**. | RCSB | 2026-05-22 |
| PDB 8A32 = rezatapopt + Y220C | **PDB 8A32 = Y220C + ligand KVA** (Joerger/SGC iodophenol-class stabilizer — same chemotype family as rezatapopt but not rezatapopt). The verified **rezatapopt + Y220C is PDB 9BR4**. PDB 9BR3 has a rezatapopt-series intermediate (PC-10709). | RCSB | 2026-05-22 |
| PDB 4LO8 = p53 G245S DBD | **PDB 4LO8 = Clostridium botulinum 14-subunit neurotoxin complex.** Not p53. | RCSB | 2026-05-22 |
| PDB 7XZS = MQ-DBD covalent | **PDB 7XZS = Ricin A chain bound to a pteridine.** Not p53. | RCSB | 2026-05-22 |
| PDB 7Z1V = brigimadlin + MDM2 | **PDB 7Z1V = PARP15 catalytic domain.** Not MDM2. | RCSB | 2026-05-22 |
| PDB 6FF9 = MQ-DBD covalent | **PDB 6FF9 = R280K p53 apo + Zn²⁺ only.** No drug bound. | RCSB | 2026-05-22 |
| PDB 8AZV = KRAS G12D apo | **PDB 8AZV = KRAS + BI-2865** (inhibitor complex). Not apo. | RCSB | 2026-05-22 |
| PDB 4DSO = KRAS G12D apo | **PDB 4DSO contains GSP (GTP-analog) + benzamidine + Mg²⁺.** Not apo. | RCSB | 2026-05-22 |
| 8DC4 = Aprea-licensed / Pfizer Y220C chemotype | **8DC4 = Y220C + carbazole KG3 from the Shokat lab (UCSF).** Not Aprea, not Pfizer. | RCSB | 2026-05-22 |
| NF1 arginine finger is R789 | **R1276 in NF1; R789 is the arginine finger of p120-GAP / RASA1.** | UniProt + GAP biochemistry literature | 2026-05-22 |
| KRAS is 189 residues | **KRAS has two isoforms: KRAS4A (189 aa) and KRAS4B (188 aa).** All clinical KRAS inhibitors target KRAS4B. Default to KRAS4B numbering unless explicitly noted. | UniProt P01116 | 2026-05-22 |

### Citation hygiene

| Denylisted claim | Correct value | Primary source | Verified |
|---|---|---|---|
| Collisson 2011 Cell | **Collisson *Nature Medicine* 2011** | nature.com/articles/nm.2344 | 2026-05-22 |
| Puleo 2018 has 4 PDAC subtypes | **5 subtypes** (Pure Classical, Immune Classical, Desmoplastic, Stroma-Activated, Pure Basal-like) | Gastroenterology 2018 | 2026-05-22 |
| Placek et al. *Nature Medicine* 2023 (EHR PDAC risk prediction) | **Placido et al.** (Davide Placido first author) | nature.com/articles/s41591-023-... | 2026-05-22 |
| F@h KRAS-VHL paper by Tu et al. JACS Au 2024 | **Qiu et al. JACS Au 2024** (Yunrui Qiu first author) | DOI 10.1021/jacsau.4c00503 | 2026-05-22 |
| Wassman 2013 Nat Comms describes Y220C cavity dynamics | **Wassman 2013 describes the L1/S3 transiently open pocket relevant across multiple p53 mutants** (especially R175H, validated by Cys124 mutagenesis abolishing PRIMA-1 activity) — NOT Y220C-specific. Y220C dynamics work is from subsequent Joerger/Fersht papers. | nature.com/articles/ncomms2361 | 2026-05-22 |
| LIT-PCBA is a reliable VS benchmark | **Severe data leakage per 2025 audit** (arXiv:2507.21404 — Huang/Knight/Naprienko, SieveStack). 2,491 inactives duplicated across splits; 323 ALDH1 active analog pairs; a trivial memorization-only baseline matches state-of-the-art deep models. Use only as historical secondary benchmark. | arxiv.org/abs/2507.21404 | 2026-05-22 |

### Math / units

| Denylisted claim | Correct value | Primary source | Verified |
|---|---|---|---|
| 10B compounds × 1 conformation × 5 sec/CPU ≈ 50B core-hours ≈ 5M CPU-years | **= 50B CPU-seconds ≈ 14M core-hours ≈ 1,600 core-years.** Earlier claim was off by ~3,500× due to unit error. | Back-of-envelope | 2026-05-22 |
