# Verification B — PDB Entries, Structural Biology, KRAS / MRTX1133

Scope: PDB entry claims (7RPZ, 6GJ7, 6OIM, 6UT0, 5G4N, 7JWU), KRAS mutation prevalence in PDAC, MRTX1133 specifics (preclinical, clinical status, combination biology), Y220C cryptic-pocket history, PMV Pharmaceuticals rezatapopt PYNNACLE trial, wwPDB validation reports, and CC0 licensing of PDB.

Verifier date: 2026-05-22.

---

### Claim 1: PDB 7RPZ is a "high-resolution KRAS G12D–MRTX1133 complex" that "captures KRAS G12D with MRTX1133"
**Source in reports:** Report 2, Executive Summary and Recommended Target sections; cited as `citeturn21view6`. Also referenced in Validation table (Layer 1 structural truth).
**Status:** Verified.
**Evidence:** RCSB entry https://www.rcsb.org/structure/7RPZ — title "KRAS G12D in complex with MRTX-1133." Protein is human KRAS (UniProt isoform 2B), 170-residue chain A, carrying the G12D mutation. Bound components:
- Ligand 6IC (MRTX-1133)
- GDP (guanosine-5'-diphosphate, the inactive nucleotide state)
- Mg2+ cofactor

Resolution 1.30 Å, X-ray diffraction, R-work 0.150 / R-free 0.171. Deposited 2021-08-05, released 2021-12-22.
**Notes:** "High-resolution" is fully justified (1.30 Å is sub-1.5 Å, very high resolution). The structure is GDP-bound (inactive state), which is the form MRTX1133 was designed to bind — consistent with the report's framing of "switch-II pocket of GDP-bound KRAS G12D." All elements of the claim hold.

---

### Claim 2: PDB 6GJ7 is a "KRAS G12D pocket structure" with "a distinct ligand class" from MRTX1133, suitable as orthogonal validation
**Source in reports:** Report 2, Recommended Target section ("6GJ7 demonstrates druggability of a KRAS G12D pocket with a distinct ligand class") and Validation table layer 1 ("at least one orthogonal KRAS G12D pocket structure such as 6GJ7"). Cited as `citeturn21view7`.
**Status:** Partially verified — protein identity is correct, but nucleotide state is GTP-mimetic (not GDP), and this materially affects whether it is a like-for-like orthogonal benchmark.
**Evidence:** RCSB entry https://www.rcsb.org/structure/6GJ7 — title "CRYSTAL STRUCTURE OF KRAS G12D (GPPCP) IN COMPLEX WITH 22." Protein is human KRAS bearing the G12D mutation. Bound components:
- GCP (phosphomethylphosphonic acid guanylate ester) — a non-hydrolyzable GTP analog (GMPPCP / GppCp), placing KRAS in the active GTP-like state
- F0B — small molecule labeled BI-2852, reported IC50 450–870 nM, binding a pocket between switch I and switch II
- Mg2+

Resolution 1.67 Å. The associated paper (Kessler et al., reporting BI-2852) describes the compound as binding both active and inactive KRAS at a switch I/II interface pocket — a chemotype and binding mode genuinely distinct from MRTX1133's switch-II pocket.
**Notes:** Important caveat for downstream validation use: 6GJ7 is GTP-mimetic (GppCp) whereas 7RPZ is GDP-bound. They are not in the same nucleotide state. The report's claim that 6GJ7 is a "distinct ligand class" is accurate (BI-2852 is a fragment-derived switch I/II pocket binder versus MRTX1133's switch-II pocket binder), and using it as an orthogonal benchmark guards against overfitting to the GDP state — but a reader must be aware the orthogonality also includes the nucleotide state, not just chemotype. The report does not explicitly call out this nucleotide-state difference; this should be noted in any benchmark protocol.

---

### Claim 3a: Sotorasib (AMG 510) binds KRAS G12C — verify via PDB 6OIM
**Source in reports:** Implied across both reports' discussion of KRAS-pathway druggability; AMG 510 is the canonical KRAS G12C clinical inhibitor.
**Status:** Verified.
**Evidence:** RCSB entry https://www.rcsb.org/structure/6OIM — title "Crystal Structure of human KRAS G12C covalently bound to AMG 510." Protein is human KRAS (G12C variant); ligand is AMG 510 (formula C30 H32 F2 N6 O3), labeled "bound form" indicating the covalent adduct. Resolution 1.65 Å. Released 2019-11-06. R-work 0.187 / R-free 0.220.
**Notes:** Entry summary reports "Mutation(s): 4" — this is standard for crystallographic KRAS constructs (the G12C disease mutation plus engineering mutations to enable crystallization, typically C51S/C80L/C118S or similar surface cysteine substitutions). G12C is among them. Original publication: Canon et al., Nature 2019, "The clinical KRAS(G12C) inhibitor AMG 510 drives anti-tumour immunity."

---

### Claim 3b: Adagrasib (MRTX849) binds KRAS G12C — verify via PDB 6UT0
**Source in reports:** Same as 3a — both reports treat MRTX849/adagrasib as background context for the KRAS G12C field that contrasts with MRTX1133's G12D-selective non-covalent mechanism.
**Status:** Verified.
**Evidence:** RCSB entry https://www.rcsb.org/structure/6UT0 — title "Identification of the Clinical Development Candidate MRTX849, a Covalent KRASG12C Inhibitor for the Treatment of Cancer." Protein is human KRAS G12C; ligand M1X is MRTX849 / adagrasib, described as "a potent, selective covalent inhibitor of KRAS G12C" forming a covalent bond to Cys12. Resolution 1.94 Å, R-free 0.212.
**Notes:** As with 6OIM, "Mutation(s): 4" indicates G12C plus engineering mutations to support expression/crystallization. Both 6OIM (sotorasib/AMG 510) and 6UT0 (adagrasib/MRTX849) accurately serve as canonical references for FDA-approved KRAS G12C covalent inhibitors. The contrast with MRTX1133 (non-covalent, G12D-selective) used in the reports is supportable.

---

### Claim 4: MRTX1133 is a non-covalent KRAS G12D binder; preclinical data show regression in KRAS G12D models including pancreatic
**Source in reports:** Report 2 Executive Summary, Recommended Target section ("MRTX1133 preclinical program established that potent, selective, non-covalent KRAS G12D inhibition is possible and showed marked tumor regression in multiple KRAS G12D models, including pancreatic models").
**Status:** Verified.
**Evidence:**
- Primary discovery paper: Wang et al., "Identification of MRTX1133, a Noncovalent, Potent, and Selective KRAS G12D Inhibitor," J Med Chem 2022 (https://pubs.acs.org/doi/10.1021/acs.jmedchem.1c01688). Reports MRTX1133 as the first non-covalent KRAS G12D-selective inhibitor; KD ~0.2 pM and IC50 < 2 nM against GDP-loaded KRAS G12D; ~700-fold selectivity over wild-type KRAS; evolved from the adagrasib scaffold with optimization for the D12 residue contact.
- Companion in vivo paper: Hallin et al., "Anti-tumor efficacy of a potent and selective non-covalent KRASG12D inhibitor," Nature Medicine 2022 (https://pubmed.ncbi.nlm.nih.gov/36216931/). Reports >1,000-fold cellular selectivity over KRAS WT lines and marked tumor regression (≥30%) in a subset of KRAS G12D CDX/PDX models — including 8 of 11 (73%) pancreatic ductal adenocarcinoma models.
**Notes:** The PDAC-specific tumor regression claim is documented in the Nature Medicine paper (8/11 PDAC models with ≥30% regression). Selectivity for KRAS G12D over wild-type and over other RAS isoforms is also documented in subsequent literature (e.g., bioRxiv preprint on H95 driving paralog selectivity for KRAS vs HRAS/NRAS).

---

### Claim 5: MRTX1133 clinical status — was it ever discontinued? Did Mirati/BMS replace it?
**Source in reports:** Reports do not explicitly state clinical status, but treat MRTX1133 as the validating preclinical exemplar. The user's separate question asks about discontinuation.
**Status:** Verified — MRTX1133 was discontinued in clinical development by Bristol Myers Squibb in 2025.
**Evidence:**
- BMS acquired Mirati Therapeutics in late 2023 for ~$4.8B (per Bristol Myers Squibb 2023 press release).
- ApexOnco / Oncology Pipeline reporting (https://www.oncologypipeline.com/apexonco/bristol-exits-kras-g12d) and FierceBiotech (https://www.fiercebiotech.com/biotech/bms-culls-2-clinical-programs-one-mirati-and-another-exscientia) reported that BMS terminated the MRTX1133 Phase 1/2 study after Phase 1 completion in January (2025). Reported reason: no safety concerns, but pharmacokinetics were "highly variable and suboptimal." Promised first-half 2024 data readout from Mirati never materialized.
- Drug Hunter molecule page (https://drughunter.com/molecule/mrtx1133) notes the difficult PK profile (PEG-piperidine, IV-only dosing required for the parent compound).
**Notes:** The preclinical biology claims in both reports remain accurate and useful — MRTX1133 remains the canonical proof-of-concept molecule for non-covalent KRAS G12D inhibition even though it is no longer in clinical development. Report 2's framing of MRTX1133 as a "validated binding concept" for a virtual-screening project is still defensible: the chemotype/pocket are validated even if the molecule itself was deprioritized for PK reasons. Several next-generation G12D programs (RMC-9805 from Revolution Medicines, ASP3082 from Astellas, HRS-4642 from Hengrui, INCB161734 from Incyte, etc.) are now in clinical development from other sponsors — replacement program(s) within BMS-Mirati's portfolio are less clearly documented. Worth flagging in the BOINC project framing that the original molecule is shelved, so the project should be positioned as discovering new chemotypes against a validated pocket, not as backing up a clinical program that no longer exists.

---

### Claim 6: MRTX1133 shows improved activity when co-targeting EGFR or PI3Kα
**Source in reports:** Report 2 ("the MRTX1133 literature shows bypass and feedback biology still matter, including improved activity from co-targeting EGFR or PI3Kα"); cited as `citeturn32view0`.
**Status:** Verified.
**Evidence:**
- Hallin et al., Nature Medicine 2022 (https://www.nature.com/articles/s41591-022-02008-6): "Pharmacological and CRISPR-based screens demonstrated that co-targeting KRASG12D with putative feedback or bypass pathways, including EGFR or PI3Kα, led to enhanced anti-tumor activity." Specific combinations tested in the paper include cetuximab (anti-EGFR mAb), afatinib (pan-ERBB), and BYL-719 / alpelisib (PI3Kα inhibitor).
- Subsequent literature (review in Clin Cancer Res 2024 — "A Small Molecule with Big Impact" https://aacrjournals.org/clincancerres/article/30/4/655/734212, and Journal of Gastrointestinal Oncology review by Haidar) corroborate the combination rationale: MRTX1133 inhibits ERRFI1 (a negative regulator of EGFR), causing feedback EGFR reactivation, so blocking EGFR rescues monotherapy resistance.
**Notes:** Citation is well supported. The combination data were reported alongside the primary in vivo paper; this is not later-stage clinical data but pharmacology / xenograft work.

---

### Claim 7: KRAS is mutated in 93% of PDAC tumors per the NCI TCGA pancreatic ductal adenocarcinoma study
**Source in reports:** Both reports. Report 1 Executive Summary: "KRAS alterations are present in roughly 93% of tumors in the NCI TCGA pancreatic ductal adenocarcinoma study" (`citeturn7search6` and `citeturn22search5`). Report 2 Executive Summary: "KRAS was mutated in 93% of tumors."
**Status:** Verified.
**Evidence:**
- NCI TCGA PDAC summary page (https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga/studied-cancers/pancreatic) states verbatim: "The gene KRAS, which encodes an important signaling protein involved in cell growth and cell death, was mutated in 93% of cancers in the study."
- Primary publication: Cancer Genome Atlas Research Network, "Integrated Genomic Characterization of Pancreatic Ductal Adenocarcinoma," Cancer Cell 2017 (https://www.cell.com/cancer-cell/fulltext/S1535-6108(17)30299-4) — 140/150 cases (93%) carried KRAS mutations, with G12D (n=62), G12V (n=41), G12R (n=28), and other codon 12/61 variants noted.
**Notes:** The 93% figure is specifically TCGA-PAAD cohort-derived (N=150). Larger and more recent cohorts (AACR Project GENIE, MSK-IMPACT, etc.) generally show KRAS mutation rates in PDAC of 85–95% depending on detection sensitivity and how borderline/IPMN cases are handled. The 93% statement is well-anchored to the TCGA source.

---

### Claim 8: KRAS G12D is the most common specific KRAS mutation in PDAC, present in ~35% of cases
**Source in reports:** Report 2 Executive Summary: "the NCI notes that KRAS G12D is the most common specific KRAS mutation in pancreatic cancer, present in about 35% of diagnosed cases" (`citeturn21view4`).
**Status:** Partially verified — the "most common" framing is correct; the 35% figure is at the low end of the published range. Most sources cite ~40%, and the user notes their internal `PROJECT/01_disease.md` and `PROJECT/15_targeted_therapy.md` cite ~40%.
**Evidence:**
- Hirshberg Foundation overview (https://pancreatic.org/an-overview-of-kras-and-its-importance-in-pancreatic-cancer/): "G12D (glycine replaced with aspartic acid) seen in ~40% of PDAC tumors."
- TCGA-PAAD cohort: G12D = 62/140 KRAS-mutant cases = ~44% of KRAS-mutant, ~41% of total cohort (62/150).
- Multi-cohort reviews report a range: MD Anderson cohort 39% of KRAS mutations; one cohort reported 45%; "highest prevalence" reported as 35% in another study. So the literature range is roughly 35–45%, with most sources clustering around 40%.
- CAP (College of American Pathologists) and npj Precision Oncology multi-cohort analyses consistently report ~40% as the central estimate.
**Notes:** The "most common specific KRAS mutation" half of the claim is unambiguously correct (G12D > G12V > G12R is the standard ordering in PDAC). The 35% figure is defensible as the low end of the range but is not the modal published value. The user's internal docs citing ~40% are better aligned with the consensus literature. Recommend updating PDAC-frequency citations to "~40% (range 35–45% across cohorts)" for accuracy. The NCI page itself does not give a specific percentage for G12D — it only gives the 93% overall KRAS rate — so the report's attribution to "the NCI notes…about 35%" is a slight overreach: the 35% number is from a specific cohort study, not from the NCI summary text I was able to find.

---

### Claim 9a: Boeckler 2008 PNAS established the Y220C pocket
**Source in reports:** This claim was in the user's verification task description, not in the source reports themselves (the source reports do not discuss Y220C/p53). Verifying independently as requested.
**Status:** Verified.
**Evidence:** Boeckler, Joerger, Frémont, Pesch, Lehmann, Fersht, "Targeted rescue of a destabilized mutant of p53 by an in silico screened drug," PNAS 2008, 105(30):10360–10365 (https://www.pnas.org/doi/10.1073/pnas.0805326105). The paper reports Y220C creates a destabilizing surface cavity (~4 kcal/mol), identifies the carbazole derivative PhiKan083 by in silico virtual screening, shows KD ~150 µM binding, and demonstrates raised melting temperature. Co-crystal structure of p53 Y220C–PhiKan083 was deposited as PDB 2VUK.
**Notes:** Fersht is senior author (last position). The discovery of the Y220C cavity and its druggability is correctly attributed to the Fersht lab. PhiKan083 (PDB 2VUK) is the canonical first-stabilizer entry.

---

### Claim 9b: Wassman 2013 Nature Communications identified a Y220C cryptic pocket
**Source in reports:** Verification task description only.
**Status:** Partially verified — the Wassman 2013 Nat Comms paper exists but it does NOT describe a Y220C-specific pocket; it describes a transiently open L1/S3 pocket relevant to multiple p53 mutants (including R175H), not Y220C specifically.
**Evidence:** Wassman et al., "Computational identification of a transiently open L1/S3 pocket for reactivation of mutant p53," Nature Communications 2013 (https://www.nature.com/articles/ncomms2361). The paper identifies a transiently open L1/S3 pocket between loop L1 and strand S3, validated by Cys124 mutagenesis abolishing PRIMA-1 activity against R175H mutant, and identifies stictic acid as a hit. The pocket is described as occurring "across several p53 variants," distinct from Y220C-specific pockets used in compounds like PhiKan083 / PK7088 / rezatapopt.
**Notes:** Important correction. Wassman 2013 is sometimes loosely cited as a "p53 cryptic pocket" paper, which is accurate, but it is NOT the Y220C-specific pocket paper. The Y220C pocket is the Boeckler 2008 / subsequent Joerger-Fersht papers. The Wassman paper actually argues for a pocket that works across multiple p53 mutants, which is conceptually different from the Y220C-mutation-induced surface crevice. If the verification target was to confirm "Wassman 2013 = Y220C cryptic pocket," that is a misattribution; if it was to confirm "Wassman 2013 = a p53 cryptic pocket paper," that is correct. The cleanest statement is: Boeckler 2008 = Y220C-specific cavity / PhiKan083; Wassman 2013 = transiently open L1/S3 pocket relevant to multiple mutants. The reports themselves do not make this claim, so this is informational rather than a correction to the reports.

---

### Claim 9c: PDB 5G4N is an early Fersht-lab Y220C fragment structure
**Source in reports:** Verification task description only.
**Status:** Partially verified — 5G4N is a Y220C structure from the Joerger/Fersht stream, but the bound ligand is a difluorinated PhiKan083 derivative, not a fragment per se.
**Evidence:** RCSB entry https://www.rcsb.org/structure/5G4N — title "Crystal structure of the p53 cancer mutant Y220C in complex with a difluorinated derivative of the small molecule stabilizer Phikan083." Deposition authors: Joerger, Bauer, Jones, Spencer. Ligand O83 = 1-[9-(2,2-difluoroethyl)-9H-carbazol-3-yl]-N-methylmethanamine. Resolution 1.35 Å.
**Notes:** This is a designed lead-optimization compound (fluorinated PhiKan083), not an early fragment. The 5G4O entry (trifluorinated PhiKan083 derivative) is paired with this one. Other early Fersht-lab Y220C fragments are documented elsewhere (e.g., 2J1X, 2VUK, 5ABA, 5AOK).

---

### Claim 9d: PDB 7JWU is a Y220C structure
**Source in reports:** Verification task description only.
**Status:** FALSE — 7JWU is NOT a p53 Y220C entry.
**Evidence:** RCSB entry https://www.rcsb.org/structure/7JWU — title "Crystal structure of human ALDH1A1 bound to compound (R)-28." Protein is human aldehyde dehydrogenase 1A1 (retinal dehydrogenase 1), bound to compound VMA (a pyrazolo[3,4-d]pyrimidinone), NAD cofactor, ytterbium, and chloride ions. Resolution 1.90 Å. Depositors: Hurley and Buchman, August 2020. This is an entirely different protein and ligand class.
**Notes:** If the intent was to cite a later/recent Y220C entry, the correct candidates are entries like 8A32 (JC769 iodophenol-based stabilizer), 5O1C/5O1H/5O1I (aminobenzothiazole MB-series), 5G4N/5G4O (fluorinated PhiKan083 derivatives), or rezatapopt/PC14586 co-crystals. 7JWU is unrelated. This is a clear PDB-ID confusion in whatever source originally cited 7JWU as Y220C. The source reports themselves do not cite 7JWU, so this is informational.

---

### Claim 10: PMV Pharmaceuticals' rezatapopt / PC14586 — Phase 2 PYNNACLE trial for Y220C
**Source in reports:** Verification task description only.
**Status:** Verified.
**Evidence:**
- PMV Pharmaceuticals investor relations site (https://ir.pmvpharma.com/news-releases/news-release-details/pmv-pharmaceuticals-announces-first-patient-dosed-global-tumor/): rezatapopt is described as a "first-in-class precision oncology small molecule…that selectively targets mutated p53 Y220C proteins." It "selectively bind[s] to the pocket in the p53 Y220C mutant protein, restoring the wild-type…p53 protein structure and tumor-suppressing function."
- ClinicalTrials.gov NCT04585750 — PYNNACLE is a Phase 1/2 tumor-agnostic basket trial in patients with locally advanced or metastatic solid tumors harboring TP53 Y220C.
- Phase 2 expansion enrollment: n=114 (ovarian n=42, lung n=18, breast n=18, endometrial n=18, other n=18).
- Most recent data cutoff reported by PMV: August 4, 2025 — safety population of 109 patients on rezatapopt 2000 mg daily monotherapy.
- Regulatory: FDA Fast Track designation granted. NDA submission planned Q1 2027 for platinum-resistant/refractory ovarian cancer.
- Recent J Med Chem paper: "Rezatapopt (PC14586): A First-in-Class Small Molecule p53 Y220C Mutant Protein Stabilizer in Clinical Trials" (https://pubs.acs.org/doi/10.1021/acs.jmedchem.5c00670).
- Trial protocol: Ann Oncol 2024 691TiP abstract and Future Oncology 2025 protocol paper (https://www.tandfonline.com/doi/abs/10.1080/14796694.2025.2557176).
**Notes:** All elements verified — drug target (Y220C), mechanism (reactivator/stabilizer), Phase 2 status, and PYNNACLE trial existence. This is the lead Y220C-directed clinical asset.

---

### Claim 11: wwPDB validation reports are publicly available for every PDB entry; format and content
**Source in reports:** Report 2 Validation section, Resource Selection table cites "RCSB PDB and wwPDB validation reports" as the structural-truth layer (`citeturn20view4`, `citeturn37view0`).
**Status:** Verified.
**Evidence:** wwPDB validation page (https://www.wwpdb.org/validation/validation-reports): "Validation information and reports for released PDB entries are available from the entry pages" at all four wwPDB partner sites (RCSB PDB, PDBe, PDBj, EMDB). Reports are provided in PDF (human-readable, includes 2D plots and summary tables) and XML (machine-readable, parseable into pipelines) formats. Coverage spans all released entries. Content includes:
- X-ray: resolution-dependent metrics (Rfree, Rwork, RSRZ outliers, clashscore, Ramachandran, sidechain rotamer outliers, ligand geometry/RSCC).
- NMR: restraint analysis, model ensemble metrics.
- 3DEM (cryo-EM): FSC curves, half-map metrics, atom inclusion, mask analysis.
**Notes:** Standardized across all wwPDB partner sites; reports are regenerated when entries are updated/versioned. Publicly downloadable via FTP/HTTP. Fully suitable for the report's use case (filtering target structures and as part of a reproducibility manifest).

---

### Claim 12: RCSB PDB / wwPDB target structures are CC0 — "CC0 public-domain dedication for archive data and APIs"
**Source in reports:** Report 1 Dataset Inventory table for "RCSB PDB / wwPDB target structures": "CC0 public-domain dedication for archive data and APIs" (`citeturn37search0`, `citeturn37search7`).
**Status:** Partially verified — the CC0 claim is correct for archive data and for most API data, but there is a documented exception for externally integrated data sources surfaced via the RCSB APIs.
**Evidence:** RCSB PDB policies page (https://www.rcsb.org/pages/policies):
> "data files contained in the PDB archive are available under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
And for APIs:
> "Data provided by RCSB PDB programmatic APIs are available under the same license unless they originate from an integrated external resource"
**Notes:** The report's wording "CC0 public-domain dedication for archive data and APIs" is essentially correct but slightly understates the exception. A more precise rephrasing would be: "CC0 for archive data and for native RCSB API data; integrated external data (e.g., from external annotation providers surfaced through RCSB APIs) retains the external provider's license." For the BOINC project's purposes — distributing PDB structures themselves to volunteers — CC0 applies cleanly, since structure coordinate/metadata files are native PDB archive data. The exception only matters if the project's API consumption pulls in annotations from external integrated resources (e.g., some sequence or domain annotations from UniProt, InterPro, Pfam, etc.), which would carry their respective licenses.

---

## Summary

| # | Claim | Status |
|---|---|---|
| 1 | PDB 7RPZ = high-res KRAS G12D–MRTX1133 (GDP-bound, 1.30 Å) | Verified |
| 2 | PDB 6GJ7 = KRAS G12D pocket with distinct ligand class | Partially verified (G12D yes, but GTP-mimetic state, not GDP — adds orthogonality but should be noted) |
| 3a | PDB 6OIM = KRAS G12C + AMG 510 (sotorasib) | Verified |
| 3b | PDB 6UT0 = KRAS G12C + MRTX849 (adagrasib) | Verified |
| 4 | MRTX1133 = non-covalent KRAS G12D inhibitor; PDAC regression demonstrated | Verified |
| 5 | MRTX1133 clinical status (extra question) | Verified — discontinued by BMS in 2025 due to suboptimal PK |
| 6 | MRTX1133 combinations with EGFR / PI3Kα improve activity | Verified |
| 7 | KRAS mutated in 93% of PDAC (TCGA) | Verified |
| 8 | KRAS G12D ~35% of PDAC, most common subtype | Partially verified — "most common" correct; modal literature value is ~40% (range 35–45%), so report's 35% is at low end. Internal docs at ~40% are better aligned with consensus. |
| 9a | Boeckler 2008 PNAS established Y220C pocket | Verified |
| 9b | Wassman 2013 Nat Comms identified Y220C pocket | Partially verified — Wassman 2013 paper exists and identifies a p53 cryptic pocket, but it is the L1/S3 pocket relevant to multiple mutants (including R175H), NOT a Y220C-specific pocket. Misattribution if framed as Y220C. |
| 9c | PDB 5G4N = early Fersht-lab Y220C fragment | Partially verified — Y220C yes; ligand is difluorinated PhiKan083 derivative (lead-optimization, not fragment). |
| 9d | PDB 7JWU = Y220C entry | FALSE — 7JWU is human ALDH1A1, not p53 Y220C. PDB-ID error. |
| 10 | PMV Pharma rezatapopt / PC14586 PYNNACLE Phase 2 Y220C trial | Verified |
| 11 | wwPDB validation reports publicly available, PDF + XML | Verified |
| 12 | RCSB PDB / wwPDB CC0 license for archive and APIs | Partially verified — CC0 applies cleanly to archive data and native API data; externally integrated data via RCSB APIs retains source license. |

Counts: 9 Verified, 5 Partially verified, 1 False (PDB 7JWU misidentification).

## Key findings worth flagging upstream

1. PDB 6GJ7 is GppCp-bound (GTP-mimetic / active state), not GDP-bound — its use alongside 7RPZ (GDP-bound) as orthogonal validation is fine but should explicitly acknowledge the nucleotide-state difference, not just the chemotype difference.
2. MRTX1133 is no longer in clinical development (BMS terminated in early 2025, suboptimal PK). The BOINC project framing should describe the molecule as preclinical proof-of-concept for a now-validated pocket, not as a current clinical asset awaiting a successor.
3. PDB 7JWU is not a p53 Y220C entry — it's ALDH1A1. Any internal note citing 7JWU as Y220C should be corrected. Real Y220C anchors are 2VUK (PhiKan083), 5ABA, 5AOK, 5G4N/5G4O (fluorinated PhiKan083), 5O1C/5O1H/5O1I (MB aminobenzothiazole series), 8A32 (JC769 iodophenol-based).
4. KRAS G12D in PDAC: consensus is ~40% (range 35–45%); the 35% figure used in Report 2 is defensible as low end of the range but not modal. Internal docs at ~40% are better aligned.
5. Wassman 2013 Nat Comms is a cryptic-pocket paper, but the pocket is L1/S3 across multiple p53 mutants, not Y220C-specific. The Y220C anchor is Boeckler 2008 PNAS.
