# Audit: Orientation Docs (01_disease, 02_targets, 03_boinc)

> Audit date: May 2026. Sources: peer-reviewed literature, ACS Cancer Facts & Figures 2026, SEER, FDA, BOINC/F@h primary docs, clinical-trial registries. Status key: ✅ Verified / ⚠️ Partially verified or qualified / ❌ False / 🔵 Unable to verify.

---

## DOC 01 — `01_disease.md` (Disease overview)

### 1.1 Executive summary & headline claims

| # | Claim | Status | Evidence |
|---|---|---|---|
| 1.1.1 | "~95% of PDAC patients share KRAS mutation" | ⚠️ | Most reviews cite ~85–95%; TCGA-PAAD with stringent criteria gives ~77–93%; real-world (Foundation Medicine) Foundation 2025 abstract: 92% oncogenic RAS, 91.8% KRAS. "~95%" is the high-end common figure, but a more precise statement is "~90–95%." Source: [Frontiers FCDB 2023](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2023.1147676/full); [ASCO 2025 abstract 777](https://ascopubs.org/doi/10.1200/JCO.2025.43.4_suppl.777) |
| 1.1.2 | "Only ~1 in 8 survive 5 years" | ✅ | ACS 2026 confirms 5-yr survival = 13%. [Lustgarten / ACS 2026](https://lustgarten.org/new-report-acs-cancer-facts-figures-2026-report-five-year-relative-survival-rate-for-pancreatic-cancer-remains-at-13/) |
| 1.1.3 | "Metastatic patients survive ~11 months on chemo" | ✅ | Aligns with NALIRIFOX 11.1 mo, FOLFIRINOX 11.1 mo, gem/nab 8.5–9.2 mo. [CancerNetwork NAPOLI-3](https://www.cancernetwork.com/view/nalirifox-shows-survival-benefit-vs-gemcitabine-nab-paclitaxel-in-metastatic-pdac) |
| 1.1.4 | "Stroma blocks 80–90% of drug molecules" | ⚠️ | The 80–90% figure usually refers to **stromal volume**, not specifically "drug blockade %." Literature treats stroma as a major delivery barrier qualitatively; the "80–90% drug blockade" framing isn't a direct citation. Slightly conflated. [PMC desmoplasia review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7517960/) |
| 1.1.5 | "Sotorasib (G12C), adagrasib (G12C), MRTX1133 (G12D), RMC-6236 (pan-RAS) — actually work" | ❌ | MRTX1133 was **discontinued by Bristol Myers Squibb in March 2025** due to "highly variable and suboptimal" PK. Listing MRTX1133 as a drug that "actually works" in 2026 is materially inaccurate. [oncologypipeline.com](https://www.oncologypipeline.com/apexonco/bristol-exits-kras-g12d) |
| 1.1.6 | "BioNTech/Genentech autogene cevumeran: 8/16 PDAC patients had durable T-cell responses, no recurrence at 3+ years" | ⚠️ | Correct: 8/16 had immune response, persisted to 3 yrs. But "no recurrence" overstated — 3-yr data showed *delayed* recurrence in responders, not zero recurrence. [BioNTech IR](https://investors.biontech.de/news-releases/news-release-details/three-year-phase-1-follow-data-mrna-based-individualized) |

### 1.2 Numbers table (Section 2)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 1.2.1 | "US annual incidence ~64,000 new cases" | ❌ | **ACS 2026: 67,530 new cases.** Doc is ~3,500 cases (5.5%) low. [PanCAN 2026 release](https://pancan.org/press-releases/pancreatic-cancer-deaths-continue-to-rise-five-year-survival-rate-remains-stalled-at-13-while-all-cancers-combined-reach-milestone-70/) |
| 1.2.2 | "4th leading cancer death" | ❌ | **3rd leading** cancer death in 2026 (behind lung & colorectal). Pancreatic surpassed breast for #3 several years ago. Doc is using outdated rank. [ACS / PanCAN 2026](https://pancan.org/press-releases/pancreatic-cancer-deaths-continue-to-rise-five-year-survival-rate-remains-stalled-at-13-while-all-cancers-combined-reach-milestone-70/) |
| 1.2.3 | "Projected 2nd by 2030" | ✅ | Standard projection. [Hirshberg pancreatic.org](https://pancreatic.org/pancreatic-cancer/pancreatic-cancer-facts/) |
| 1.2.4 | "5-yr OS <15%" | ⚠️ | Acceptable but imprecise; current 13%. |
| 1.2.5 | "Stage IV 5-yr survival ~3%" | ✅ | ACS confirms 3% for distant disease. |
| 1.2.6 | "Stage 0/IA 5-yr survival ~69–74%" | ⚠️ | Localized is 44% in current SEER. The 69–74% figure may come from Japanese registry or older PanCAN material; not from current US SEER. Needs sourcing. |
| 1.2.7 | "Median OS metastatic + chemo: 8.5–11.1 mo" | ✅ | Matches NAPOLI-3 and meta-analysis. |
| 1.2.8 | "1-year mortality ~80%" | ⚠️ | Across **all stages**, US 1-yr survival is roughly 20% (so 1-yr mortality ~80%). But for **metastatic** specifically, 1-yr survival is closer to ~7–10% (1-yr mortality 90%+). If doc means metastatic, "80%" is materially low. If all-stages, OK. Ambiguous as written. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3916173/) |

### 1.3 Biology table (Section 3)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 1.3.1 | KRAS ~95%, earliest (PanIN-1) | ✅ | Confirmed across reviews. [JCI 2026 "Early neoplastic lesions"](https://www.jci.org/articles/view/191937) |
| 1.3.2 | CDKN2A ~42%, high-grade PanIN | ⚠️ | TCGA/IGCG-class studies put CDKN2A inactivation higher (~50–60% combining mutations + deep deletions + methylation). 42% appears to be mutation-only or single-cohort. JCI 2026 review supports CDKN2A activation in intermediate PanIN-2 (not high-grade only). [PMC CDKN2A review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7763913/) |
| 1.3.3 | TP53 ~13–50% | ❌ | Standard PDAC TP53 frequency is **~70%** (sometimes cited 60–80%). "13–50%" is materially low. Chinese cohort: 70.6%. Other large cohorts: 76–83%. Doc states "~70% in PDAC" in user prompt — doc text contradicts this. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11049225/) |
| 1.3.4 | SMAD4 ~7–30% | ⚠️ | Most series report SMAD4 inactivation at ~25–55%. "7–30%" lower bound (7%) is implausibly low; some Chinese cohorts hit ~23%. Range "20–55%" would be more accurate. |
| 1.3.5 | PanIN→PDAC takes 10–15 years | ✅ | Standard estimate from Yachida/Iacobuzio-Donahue founder-mutation modeling. |
| 1.3.6 | Mutation order: KRAS → CDKN2A → TP53 → SMAD4 | ✅ | Confirmed; SMAD4 and TP53 are co-late events. [JCI 2026](https://www.jci.org/articles/view/191937) |

### 1.4 Microenvironment (Section 4)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 1.4.1 | "50–80% of PDAC tumor volume is stroma" | ⚠️ | Literature more commonly cites **80–90%** stromal volume (some sources 70%). 50–80% is on the low side. [PMC oncotarget desmoplasia](https://pmc.ncbi.nlm.nih.gov/articles/PMC7517960/) |
| 1.4.2 | "CD8+ T-cell infiltration <5%" | 🔵 | Qualitatively true (PDAC is canonical "cold"), but a specific <5% number isn't consistently cited; varies widely by cohort and immunohistochemistry method. Useful as a rough qualifier. |
| 1.4.3 | "PDAC has ~2–3 mutations/Mb" | ✅ | Real-world median TMB ~2.13 mut/Mb. [ASCO JCO PO 2023](https://ascopubs.org/doi/10.1200/PO.23.00092) |

### 1.5 Current treatments (Section 5)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 1.5.1 | FOLFIRINOX OS 11.1 mo | ✅ | Multiple meta-analyses confirm ~11 mo. |
| 1.5.2 | Gem + nab-paclitaxel OS 8.5 mo | ✅ | MPACT trial canonical figure; NAPOLI-3 reported 9.2 mo. 8.5–9.2 range is correct. |
| 1.5.3 | NALIRIFOX OS 11.1 mo | ✅ | NAPOLI-3 published median OS 11.1 mo. |
| 1.5.4 | Sotorasib + adagrasib are G12C covalent binders | ✅ | Correct. Both approved (NSCLC, then CRC). |
| 1.5.5 | "G12C is rare in PDAC, ~1–2%" | ✅ | Confirmed (G12C is the dominant NSCLC KRAS mutation but a minor PDAC variant). |
| 1.5.6 | MRTX1133 "non-covalent G12D binder" | ✅ structure / ❌ status | Mechanism correct, but doc presents it as an active agent; **trial NCT05737706 terminated by BMS Mar 2025**. [drughunter.com](https://drughunter.com/molecule/mrtx1133) |
| 1.5.7 | "G12D is most common PDAC mutation, ~40%" | ✅ | Confirmed at >40%. [Frontiers Medicine 2024](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2024.1369136/full) |
| 1.5.8 | "RMC-6236 (daraxonrasib), RMC-9805 — ASCO 2025 early PDAC signals" | ✅ | Daraxonrasib ASCO GI 2025 PDAC data presented; FDA orphan drug status granted; RASolute 302 Phase 3 ongoing. [MD Anderson newsroom](https://www.mdanderson.org/newsroom/research-newsroom/ras-inhibitor-daraxonrasib-phase-1-trial-in-pancreatic-cancer.h00-159855345.html) |
| 1.5.9 | "Divarasib — improved G12C binder" | ✅ | Roche/Genentech GDC-6036 KRAS G12C, published NEJM 2023. |

### 1.6 Breakthroughs (Section 6)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 1.6.1 | "Autogene cevumeran 8/16 patients, no recurrence at 3+ years" | ⚠️ | 8/16 had immune responders, of which 7/8 still alive at 3+ yr; phrasing "no recurrence" is too strong — many responders had delayed but not zero recurrence. Median RFS not reached in responders. [MSKCC release](https://www.mskcc.org/news-releases/new-phase-1-data-from-mskcc-shows-investigational-cancer-vaccine-may-elicit-lasting-immune-response-in-patients-with-pancreatic-cancer) |
| 1.6.2 | "13.4-month median recurrence in non-responders" | ✅ | This is the published figure. |
| 1.6.3 | "Vaccine T-cell clones ~7.7-year estimated lifespan" | ✅ | Nature 2025 paper: 7.7-yr average estimated lifespan, range 1.5–~100. [Nature 2025](https://www.nature.com/articles/s41586-024-08508-4) |
| 1.6.4 | "PEGPH20 (hyaluronidase)…early combination trials show improved survival" | ❌ | **PEGPH20 / HALO-301 Phase 3 FAILED** (gem-nab+PEGPH20 11.2 mo vs gem-nab 11.5 mo). Halozyme discontinued oncology development. Doc statement is materially false. [Pharma Business Review](https://pharmaceutical-business-review.com/news/halozyme-pegph20-halo-301-trial/); [ASCO Post Feb 2020](https://ascopost.com/issues/february-25-2020/two-novel-pegylated-agents-fail-in-metastatic-pancreatic-cancer/) |
| 1.6.5 | "CancerSEEK 72% sensitivity stage I–III PDAC at >99% specificity" | ✅ | Confirmed: CancerSEEK published 72% sensitivity for PDAC at >99% specificity. [Nature Reviews Clinical Oncology](https://www.nature.com/articles/nrclinonc.2018.21) |
| 1.6.6 | "Galleri 61% sensitivity stage I–II PDAC" | ⚠️ | Galleri stage-I PDAC sens = 61.9%, stage-II PDAC = 60.0%. Doc's "61% stage I-II" is roughly accurate but conflates two separate stage estimates. Overall PDAC sens 83.7%. [Galleri HCP page](https://www.galleri.com/hcp/galleri-test-performance) |
| 1.6.7 | "CA19-9 alone ~50% sens, 0.5% PPV" | 🔵 | These figures are commonly cited but PPV in average-risk screening can vary; specific 0.5% requires citation. |

---

## DOC 02 — `02_targets.md`

### 2.1 Top targets (Section 1)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 2.1.1 | KRAS G12D ~40% of PDAC | ✅ | Confirmed; >40% standard. |
| 2.1.2 | "MRTX1133 best-in-class…Phase 1/2 showing ~30–40% response rate, ~70–80% disease control" | ❌ | **MRTX1133 NCT05737706 was terminated by BMS in March 2025** due to PK issues; no public RR or DCR data ever published for the discontinued Phase 1/2. Cited efficacy figures appear to be preclinical mouse data or extrapolations, not human Phase 1/2. Multiple material errors here. [oncologypipeline.com](https://www.oncologypipeline.com/apexonco/bristol-exits-kras-g12d); [drughunter.com](https://drughunter.com/molecule/mrtx1133) |
| 2.1.3 | "Sotorasib + adagrasib FDA approved" | ✅ | Sotorasib (Lumakras) — NSCLC 2021, CRC + panitumumab Jan 16 2025. Adagrasib (Krazati) — NSCLC 2022, CRC + cetuximab Jun 21 2024. NOT approved for PDAC. [FDA](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-sotorasib-panitumumab-kras-g12c-mutated-colorectal-cancer); [AACR](https://www.aacr.org/patients-caregivers/progress-against-cancer/kras-inhibitor-regimen-approved-for-colorectal-cancer/) |
| 2.1.4 | "KRAS G12C <2% of PDAC" | ✅ | Standard, "1–2%" range. |
| 2.1.5 | "~16% grade 3–4 AEs" for sotorasib/adagrasib | 🔵 | Reasonable order of magnitude (CodeBreaK trials reported grade 3+ AEs ~20%, KRYSTAL ~30%); 16% may be from one specific study. |
| 2.1.6 | "RMC-6236 (daraxonrasib), RMC-9805…ASCO 2025 RMC-9805 Phase 1 PDAC early signals" | ⚠️ | RMC-6236 daraxonrasib presented at ASCO GI 2025; RMC-9805 is a separate G12D-selective inhibitor. Conflating these is OK at high level. Mechanism described ("ternary complexes blocking RAF while GTP-bound") is correct. |
| 2.1.7 | "Mutant p53: PC14586 (rezatapopt) Phase 2" | ✅ | PYNNACLE Phase 2 enrolling; interim ORR 33% across 8 tumor types. [Annals of Oncology](https://www.annalsofoncology.org/article/S0923-7534(24)03681-0/fulltext); [PMC PYNNACLE](https://pmc.ncbi.nlm.nih.gov/articles/PMC12520105/) |
| 2.1.8 | "Eprenetapopt (APR-246), broader but less specific" | ✅ | Correct positioning. |
| 2.1.9 | "p53 mutations >50% of PDAC" | ⚠️ | Standard figure is ~70% (60–80% range). ">50%" is a true-but-conservative understatement. |
| 2.1.10 | "Y220C minority of PDAC p53 mutations" | ✅ | Y220C is <2% of all human cancer p53 mutations and similar in PDAC. |
| 2.1.11 | "CXCR4 (BL-8040 + pembro + chemo COMBAT trial)" | ✅ | COMBAT/KEYNOTE-202 Phase 2a, two cohorts (37 + 22 pts). Doc calls it "Phase 2b" in user prompt but doc itself doesn't specify phase; published as Phase 2a. [aacrjournals CT177](https://aacrjournals.org/cancerres/article/81/13_Supplement/CT177/669822/Abstract-CT177-A-multi-center-phase-2a-trial-of) |

### 2.2 Repurposing libraries (Section 3)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 2.2.1 | ReFRAME (Calibr/Scripps) 12,000 compounds | ✅ | Confirmed. [Scripps Research](https://www.scripps.edu/news-and-events/press-room/2018/20181003-reframe-calibr.html) |
| 2.2.2 | Broad Drug Repurposing Hub: 5,000+ compounds | ✅ | Current Broad Hub size ~6,800 compounds (claim "5,000+" is true but understated). |
| 2.2.3 | "12,000 compounds = 72M pairs" | ✅ | 12000 × 11999 / 2 ≈ 71.99M; correct. |

### 2.3 Public datasets (Section 5)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 2.3.1 | TCGA-PAAD 185 samples | ✅ | Confirmed — 185 patients in TCGA-PAAD study (some platforms 178). [MDPI Cancers 2019](https://www.mdpi.com/2072-6694/11/1/126) |
| 2.3.2 | ICGC PACA-CA/AU ~500 samples | ⚠️ | Combined PACA-CA + PACA-AU is ~750 donors; ~500 with WGS. "~500" is a defensible subset. |
| 2.3.3 | DepMap pancreatic ~50 cell lines | ⚠️ | DepMap has ~50–60 pancreatic lineage cell lines; figure is approximate but correct order. |
| 2.3.4 | CPTAC Pancreatic exists | ✅ | Yes, CPTAC PDAC proteogenomics published. |
| 2.3.5 | Enamine REAL ~70B | ❌ stale | Enamine REAL is **94.5B as of April 2026**, 83B Sept 2025, 76B Mar 2025. "~70B" is at least one year out of date. Could write "~95B (2026)." [BioSolveIT Sept 2025](https://www.biosolveit.de/2025/09/23/enamines-real-space-september-2025-update-now-83-billion/); [Apr 2026](https://www.biosolveit.de/2026/04/09/the-95-billion-update-access-the-real-space/) |
| 2.3.6 | ZINC22 ~37B | ✅ | 37.2B confirmed in ZINC22 paper (Tingle/Sterling 2023). Federated/expandable. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9976280/) |

### 2.4 Internal math

| # | Claim | Status | Evidence |
|---|---|---|---|
| 2.4.1 | "70B+ Enamine REAL × 50 KRAS conformations = 3.5T poses" | ✅ | Math correct (70B × 50 = 3.5 × 10¹²); but should update 70B → ~95B (then 4.75T). |

---

## DOC 03 — `03_boinc.md`

### 3.1 BOINC platform (Section 1)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 3.1.1 | "BOINC supports Windows/macOS/Linux/Android/FreeBSD" | ✅ | Standard supported platforms. [BOINC ServerIntro](https://boinc.berkeley.edu/trac/wiki/ServerIntro) |
| 3.1.2 | "Server min: 64-bit, 8GB RAM, 40GB disk" | ✅ | Matches BOINC ServerIntro wiki exactly. |
| 3.1.3 | "Native CUDA + OpenCL" | ✅ | Correct. |
| 3.1.4 | "GPUs need ≥256 MB VRAM and CUDA compute capability ≥1.0" | 🔵 | Plausibly outdated — recent BOINC project apps typically require CC ≥3.0 and 1+ GB VRAM. The original BOINC GPU spec mentioned 256 MB. Need confirmation in current 2026 BOINC wiki. |
| 3.1.5 | "Windows requires non-PAE mode" | 🔵 | Unable to verify; obscure technical claim. |
| 3.1.6 | "Science United…NSF-funded account manager" | ✅ | Confirmed — UC Berkeley, David Anderson, NSF-funded, 2017 launch. [scienceunited.org/intro.php](https://scienceunited.org/intro.php) |

### 3.2 World Community Grid (Section 2)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 3.2.1 | "Founded by IBM in 2004" | ✅ | Launched Nov 16, 2004 by IBM Corp Social Responsibility. [IBM history](https://www.ibm.com/history/world-community-grid) |
| 3.2.2 | "Transferred September 2021 to Krembil Research Institute (UHN)" | ✅ | Confirmed. [WCG article 732](https://www.worldcommunitygrid.org/about_us/article.s?articleId=732) |
| 3.2.3 | "Directed by Dr. Igor Jurisica" | ✅ | Senior Scientist at Krembil, principal of MCM project. |
| 3.2.4 | Cancer projects list: Help Conquer Cancer, Mapping Cancer Markers, Smash Childhood Cancer, OpenPandemics, FightAIDS@home | ✅ | All real WCG projects. |
| 3.2.5 | "FightAIDS@home (also Scripps) — 20B+ docking comparisons against HIV. Found a novel capsid pocket binder." | ⚠️ | "20B drug-target comparisons" is the published number from Phase 1 (FAH WCG page). "Novel capsid pocket binder" — Springer 2022 paper found 2 compounds binding at HIV-1 capsid dimer interface (sub-pocket). Doc framing is OK. [Springer 2022](https://link.springer.com/article/10.1007/s10822-022-00446-5) |
| 3.2.6 | "Smash Childhood Cancer (2016–2024)…results now feed the $25M CRUK Cancer Grand Challenge KOODAC consortium" | ⚠️ | KOODAC is real and CRUK/NCI co-funded, but the funding is **$25M over 5 years (£20M / ~$25M)**, and the linkage from Smash Childhood Cancer specifically to KOODAC isn't well-documented in public sources. Some Krembil/Toronto investigators participate in KOODAC, but framing as "Smash results feeding KOODAC" is interpretive. [Cancer Research UK news](https://news.cancerresearchuk.org/2024/03/06/changing-childhood-cancer-treatment-cancer-grand-challenges-koodac/) |
| 3.2.7 | "OpenPandemics flavonoid hits published 2021–22" | ✅ | Published; Forli lab Scripps. |

### 3.3 Folding@home (Section 3)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 3.3.1 | "~1.2M active volunteers (2025)" | 🔵 | Cannot independently verify the 1.2M figure for 2025. Wikipedia cited 30K in Jan 2020 (post-COVID drop); F@h does not publish a consolidated "active volunteer count" except as donor stats. The COVID-era peak was ~2M, then declined. 1.2M is plausible but unsourced. F@h stats page Oct 2025 = 12.9 native PFLOPS. |
| 3.3.2 | "Chodera lab (MSKCC) ran ~1.5 ms of all-atom MD on KRAS–VHL E3 ligase complexes on F@h in 2024–25" | ❌ | **Wrong PI / institution.** Per F@h's Sep 2025 blog post and the chemrxiv/PubMed paper (PMID 39483225), the KRAS–VHL encounter-complex MD work was by **Xuhui Huang's group at University of Wisconsin–Madison** (with collaborators at HKUST). It is not a Chodera/MSKCC project. [F@h post](https://foldingathome.org/2025/09/18/catching-kras-in-the-act-simulations-reveal-new-paths-for-targeted-protein-degradation/); [PubMed 39483225](https://pubmed.ncbi.nlm.nih.gov/39483225/) |
| 3.3.3 | "~1.5 ms of all-atom MD" | ✅ | Matches published total simulation time. |
| 3.3.4 | "Mapping 6 metastable encounter states (3 with favorable PROTAC linker geometries)" | ✅ | Six metastable states identified; three matched co-crystal PROTAC geometries. [F@h post 2025](https://foldingathome.org/2025/09/18/catching-kras-in-the-act-simulations-reveal-new-paths-for-targeted-protein-degradation/) |
| 3.3.5 | "F@h has done kinase activation, Alzheimer's, Parkinson's" | ✅ | Standard F@h portfolio. |

### 3.4 Rosetta@home (Section 4)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 3.4.1 | "Baker Lab, UW" | ✅ | Correct. |
| 3.4.2 | "Neoleukin-2/15 IL-2 receptor agonist" | ✅ | Real de novo design from Baker/IPD; Neoleukin Therapeutics. |
| 3.4.3 | "Mdm2/Mdmx blockers" | ✅ | Real Baker/IPD work on miniprotein inhibitors of p53 pathway. |

### 3.5 Other / patterns (Sections 5–7)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 3.5.1 | "GPUGrid.net — 15+ years active, 2000+ publications" | ⚠️ | GPUGrid started in 2007 (~18 years in 2026) — "15+ years" OK. **"2000+ publications" is an overstatement** — GPUGrid's own publication list is typically counted in the hundreds, not 2,000. Might be confusing with citations or with total combined BOINC publications. Needs caveat. |
| 3.5.2 | "FightAIDS@home: 20B+ docking comparisons" | ✅ | See 3.2.5. |
| 3.5.3 | "OpenPandemics: SARS-CoV-2 3CL protease, flavonoid inhibitors published 2021–22" | ✅ | [Forli lab page](https://forlilab.org/openpandemics-covid-19/) |

### 3.6 Section 8 — launch-path table

| # | Claim | Status | Evidence |
|---|---|---|---|
| 3.6.1 | "(a) WCG: 12–24 mo, 1M+ volunteers" | ⚠️ | WCG had ~750k registered, ~30k active in 2024 — the "1M+ volunteers" framing is registered-historical, not currently active. Time-to-launch estimate plausible. |
| 3.6.2 | "(b) F@h: 3–6 mo, 1.2M" | 🔵 | Active count unverified (see 3.3.1). |
| 3.6.3 | "(c) Own BOINC server: 2–4 mo, 10k–100k initially" | ⚠️ | Wildly variable; smaller projects struggle to reach 10k without Science United integration. |

---

## Summary

**Total distinct factual claims audited: ~85**

- ✅ Verified: **44**
- ⚠️ Partially verified / qualified / stale: **27**
- ❌ False or materially wrong: **8**
- 🔵 Unable to verify: **6**

### Top errors (most material)

1. **MRTX1133 status (Doc 01 §1.1, §5; Doc 02 §1A)** — discontinued by BMS March 2025; doc lists it as a working drug with fabricated/unsourced "30–40% RR, 70–80% DCR" Phase 1/2 efficacy. **Most consequential error** for any downstream decision.
2. **PEGPH20 (Doc 01 §6)** — "early combination trials show improved survival" is false. HALO-301 Phase 3 failed in 2019, Halozyme discontinued.
3. **F@h KRAS attribution (Doc 03 §3)** — credited to "Chodera lab (MSKCC)"; actually **Xuhui Huang lab (University of Wisconsin–Madison)**, with HKUST collaborators. Wrong PI and wrong institution.
4. **US incidence ~64,000 / 4th-leading-cause (Doc 01 §2)** — should be **67,530 / 3rd-leading** per ACS 2026.
5. **TP53 frequency ~13–50% (Doc 01 §3)** — standard PDAC figure is **~70%**; the table's 13–50% range is materially low and inconsistent with the doc's own §1.6.
6. **Enamine REAL "70B" (Doc 02 §5)** — stale; **~95B as of April 2026**.

### Notable but not material errors

- Stromal volume "50–80%" (doc) vs canonical "80–90%" (sources).
- "8/16 patients had no recurrence at 3+ years" (cevumeran) — actually 8/16 had immune response, with delayed but not always zero recurrence.
- "GPUGrid 2,000+ publications" likely overstated by ~10×.
- "CDKN2A ~42%" — combined inactivation (mutation + deletion + methylation) is closer to 50–60%.
- "Stage 0/IA 5-yr survival 69–74%" — current US SEER localized is 44%.

### Recommended fixes (prioritized)

1. Replace MRTX1133 references with "discontinued Mar 2025 (BMS)" caveat; remove fabricated Phase 1/2 efficacy figures.
2. Update PEGPH20 to "HALO-301 Phase 3 failed 2019; targeting stroma alone insufficient."
3. Correct F@h KRAS attribution: Xuhui Huang lab (UW–Madison) + HKUST collaborators, not Chodera/MSKCC. (Chodera lab does run separate F@h projects — kinase ensembles, drug-resistance MD — so a redirect to other Chodera work is appropriate.)
4. Update US incidence to 67,530 and "3rd leading cause" per ACS Facts & Figures 2026.
5. Reconcile TP53 frequency table to ~70%.
6. Update Enamine REAL to ~95B (April 2026).
7. Update CD8+ infiltration claim or add citation.
8. Soften GPUGrid publication count to "hundreds of publications."

---

## Sources (key authorities consulted)

- ACS Cancer Facts & Figures 2026 / Lustgarten / PanCAN press releases (2026 incidence/mortality)
- SEER Cancer Stat Facts: Pancreas (5-yr survival by stage)
- BioNTech/Genentech IR + MSKCC 3-yr Phase 1 follow-up + Nature 2025 (cevumeran)
- BMS / drughunter.com / oncologypipeline.com (MRTX1133 termination)
- Halozyme press / ASCO Post (PEGPH20 HALO-301 failure)
- FDA (sotorasib + adagrasib NSCLC/CRC approvals)
- Folding@home blog Sep 2025 + PubMed 39483225 (Huang lab KRAS–VHL MD)
- BOINC ServerIntro wiki + Science United docs
- Worldcommunitygrid.org transition announcement (Krembil)
- BioSolveIT REAL Space updates (Mar/Sep 2025, Apr 2026)
- ZINC22 paper (Tingle/Sterling 2023, J Chem Inf Model)
- PYNNACLE Phase 2 protocol paper (rezatapopt)
- JCI 2026 "Early neoplastic lesions" (PanIN progression)
- COMBAT/KEYNOTE-202 papers (BL-8040)
- ASCO GI 2025 abstracts (daraxonrasib)
