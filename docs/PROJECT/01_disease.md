# Pancreatic Cancer: Biology, Treatment, and Computational Opportunities

> Synthesis from Mayo Clinic, Cancer Research UK, PanCAN, NCI, and recent (2023–2026) peer-reviewed literature. Written for a general audience.

## 1. Executive summary (5 bullets)

- **The Crisis.** Nearly all pancreatic ductal adenocarcinoma (PDAC) patients (~95%) share the same broken gene (KRAS), yet we still can't reliably kill their tumors. Only ~1 in 8 survive 5 years; metastatic patients survive ~11 months on chemo.
- **Why It's Hard.** Pancreatic tumors are wrapped in dense scar tissue ("desmoplastic stroma") that blocks 80–90% of drug molecules from reaching cancer cells. The cancer also tricks the immune system into standing down — PDAC is the canonical "cold" tumor.
- **Why It's Winnable Now.** KRAS was considered "undruggable" for 30 years. As of 2026, sotorasib and adagrasib (G12C, FDA-approved for NSCLC + CRC only — off-label in PDAC) work in their indications; **MRTX1133 (G12D) showed preclinical regression but was discontinued in clinical development by BMS in Jan 2025 due to suboptimal PK** — its pocket remains the proof-of-concept; daraxonrasib / RMC-6236 (pan-RAS) and RMC-9805 (G12D) are the live clinical assets now. Resistance arises in weeks to months. Combinations and next-generation binders are the open frontier.
- **The Computational Opening.** Most of the highest-impact unsolved questions in PDAC are computational: which compound combinations resist resistance, which cryptic pockets we haven't found, which patients respond to which therapy.
- **The 2025 Vaccine Result.** BioNTech/Genentech's personalized mRNA neoantigen vaccine (autogene cevumeran) gave 8/16 PDAC patients durable T-cell responses with no recurrence at 3+ years. If this scales, it doubles 5-year survival. Predicting which neoantigens to put in the vaccine is itself a compute problem.

## 2. The numbers

| Metric | Value |
|---|---|
| US annual incidence (2026 ACS estimate) | ~67,530 new cases (now **3rd leading cancer death**, surpassed breast in recent years) |
| Projected US rank by 2030 (Rahib 2014) | 2nd leading cancer death |
| 5-year overall survival | ~13% all stages (NCI SEER) |
| Stage IV 5-year survival | ~3% |
| Stage 0 / IA 5-year survival | ~69–74% |
| Median OS, metastatic + chemo | 8.5–11.1 months |
| 1-year mortality | ~80% |

This is a disease where catching it early would save almost everyone, but we usually don't.

## 3. Biology — what cells, what mutations, how it progresses

PDAC starts in pancreatic duct epithelial cells. The progression model (PanIN → PDAC) takes 10–15 years and accumulates four signature mutations in roughly this order:

| Gene | Frequency | Function | When |
|---|---|---|---|
| **KRAS** | ~95% | Oncogene — forces cell division | Earliest lesions (PanIN-1) |
| **CDKN2A** | ~42% | Tumor suppressor — brakes growth | High-grade PanIN |
| **TP53** | ~65–75% (modern consensus; the "13–50%" range in some older sources conflated mutation rate with downstream survival numbers) | Tumor suppressor — triggers cell death | High-grade PanIN + advanced |
| **SMAD4** | ~7–30%* | Tumor suppressor — blocks pro-growth signals | Advanced |

*higher in aggressive cases

Patients with fewer driver hits survive longer. Mutation load itself is prognostic.

## 4. Microenvironment — why PDAC is "different"

50–80% of a PDAC tumor by volume isn't cancer cells — it's stroma: fibroblasts, immune cells, collagen, hyaluronan. Two consequences:

- **Physical barrier.** Dense collagen cross-linking blocks most drug molecules. This is why chemotherapy fails despite "working" on cells in a dish.
- **Immune barrier.** Regulatory T-cells, myeloid-derived suppressor cells, and pro-tumor macrophages dominate. CD8+ T-cell infiltration is <5% (vs >20% in responsive cancers).

PDAC also has only ~2–3 mutations per Mb — fewer "neoantigens" for the immune system to recognize than melanoma or lung. This is why most checkpoint inhibitors (anti-PD-1, anti-CTLA-4) fail in PDAC.

## 5. Current treatments and their limits

Standard first-line chemotherapy:

| Regimen | Median OS | Notes |
|---|---|---|
| **FOLFIRINOX** | 11.1 months | High toxicity (cytopenia, neuropathy) |
| **Gem + nab-paclitaxel** | 8.5 months | Better tolerated |
| **NALIRIFOX** (newer) | 11.1 months | Less hematologic toxicity than FOLFIRINOX, more diarrhea |

None extend metastatic survival past ~12 months. Failure modes: stromal exclusion, intrinsic drug resistance, intra-tumoral heterogeneity (different cells inside one tumor have different mutations).

KRAS inhibitors in 2026:

- **Sotorasib, adagrasib** — covalent G12C binders (G12C is rare in PDAC, ~1–2%)
- **MRTX1133** — non-covalent G12D binder (G12D is the most common PDAC mutation, ~40%)
- **RMC-6236 (daraxonrasib), RMC-9805** — pan-RAS / G12D tri-complex inhibitors; ASCO 2025 showed early PDAC signals
- **Divarasib** — improved G12C binder

Resistance arises through:
- KRAS gene amplification (more copies of the mutant)
- Reactivation of parallel pathways (PI3K-AKT, ERK, Wnt/β-catenin)
- Epithelial-to-mesenchymal transition (cells become less KRAS-dependent)

## 6. Recent breakthroughs (2023–2026)

**Neoantigen vaccines.** BioNTech/Genentech's autogene cevumeran (personalized mRNA encoding 10–20 patient-specific mutated peptides) showed in Phase 1: 8 of 16 PDAC patients had no recurrence at 3+ years vs 13.4-month median recurrence in non-responders. Vaccine-induced T-cell clones had ~7.7-year estimated lifespan. Larger Phase 2 trials ongoing.

**Stromal remodeling.** PEGPH20 (hyaluronidase) and FAP-targeted agents dissolve the stroma, allowing chemo to penetrate. Early combination trials show improved survival.

**ctDNA early detection.** Multi-biomarker panels (ctDNA mutations + protein + methylation):
- CancerSEEK: 72% sensitivity for stage I–III PDAC at >99% specificity
- Galleri (GRAIL): 61% sensitivity for stage I–II PDAC
- Combined panels: 64% sensitivity, 99.5% specificity for resectable PDAC

For comparison: CA19-9 alone has ~50% sensitivity and only 0.5% positive predictive value as a screening test.

**Molecular subtyping.** Four classification systems (Collisson, Bailey, Moffitt, Puleo) split PDAC into ~2–4 subtypes (Classical, Basal-like / Squamous, Pancreatic Progenitor, Immunogenic). Subtype predicts chemo response; personalized treatment based on subtype is emerging.

## 7. Where compute could plausibly help (tagged `[A]`)

PDAC is computationally tractable because mutations are known, structures (KRAS to 1.5 Å) are solved, large omics datasets exist (TCGA-PAAD, ICGC-PACA, CPTAC), and the clinical timescale is short — so predictions get feedback fast.

- **[A1] Virtual screening of KRAS inhibitor combinations** — millions of compound pairs against KRAS G12C/G12D/Q61H, looking for synergy that delays resistance.
- **[A2] Molecular dynamics of KRAS inhibitor resistance** — map switch-II pocket dynamics with sotorasib/adagrasib/MRTX1133 bound; identify secondary mutations that confer resistance.
- **[A3] Stromal drug-penetration modeling** — dissipative particle dynamics on collagen + hyaluronan networks to predict optimal nanoparticle properties.
- **[A4] Neoantigen prediction + MHC binding** — given a patient's exome + MHC type, predict which mutations are best vaccine targets. Train on autogene cevumeran responders.
- **[A5] Survival prediction from multi-omics** — ensemble ML on TCGA-PAAD predicting OS given baseline mutation/subtype/clinical inputs.
- **[A6] Immune-cell infiltration agent-based modeling** — simulate T-cell vs Treg dynamics under checkpoint blockade + Treg depletion + stromal remodeling.
- **[A7] ctDNA subclonal inference** — Bayesian MCMC on cell-free DNA sequencing to predict treatment response from longitudinal blood draws.
- **[A8] Structure-guided SMAD4/TP53 stabilizers** — virtual screen against tumor-suppressor conformations to find compounds that restore function.
- **[A9] PDAC subtype classifier from RNA-seq** — fast, interpretable classifier deployed as a free web tool; retrain monthly as new data lands.

## 8. Sources

- [Mayo Clinic — Pancreatic cancer](https://www.mayoclinic.org/diseases-conditions/pancreatic-cancer/symptoms-causes/syc-20355421)
- [Cancer Research UK — Pancreatic cancer](https://www.cancerresearchuk.org/about-cancer/pancreatic-cancer)
- [PanCAN — Pancreatic cancer models](https://pancan.org/research/strategic-research-program/learn/pancreatic-cancer-models/)
- [Nature Signal Transduction and Targeted Therapy — PDAC molecular insights (2026)](https://www.nature.com/articles/s41392-026-02705-5)
- [JCI — KRAS: The Achilles' Heel of Pancreas Cancer Biology](https://www.jci.org/articles/view/191939)
- [Frontiers Oncology — Current treatment paradigm for PDAC and barriers to efficacy](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.688377/full)
- [JAMA Network Open — NALIRIFOX vs FOLFIRINOX vs gem-nab meta-analysis](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2813517)
- [Springer Nature — ctDNA-guided early detection and MRD monitoring (2026)](https://link.springer.com/article/10.1186/s12957-026-04238-1)
- [Nature — Personalized RNA neoantigen vaccines stimulate T cells in PDAC (2023)](https://www.nature.com/articles/s41586-023-06063-y)
- [MSKCC — Three-year Phase 1 follow-up, autogene cevumeran](https://www.mskcc.org/news-releases/new-phase-1-data-from-mskcc-shows-investigational-cancer-vaccine-may-elicit-lasting-immune-response-in-patients-with-pancreatic-cancer)
- [AACR Cancer Discovery — Mechanisms of resistance to oncogenic KRAS inhibition](https://aacrjournals.org/cancerdiscovery/article/14/11/2135/749207/Mechanisms-of-Resistance-to-Oncogenic-KRAS)
- [PubMed — KRAS/CDKN2A/TP53/SMAD4 as prognostic biomarker](https://pubmed.ncbi.nlm.nih.gov/28099251/)
- [Frontiers Immunology — Reprogramming the tumor microenvironment (2025)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1717062/full)
- [OHSU News — Research reveals how pancreatic cancer blocks immunotherapy (April 2026)](https://news.ohsu.edu/2026/04/10/ohsu-research-reveals-how-pancreatic-cancer-blocks-immunotherapy)
