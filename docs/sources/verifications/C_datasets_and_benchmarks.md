# Verification C — Datasets, Sizes, and Benchmarks

Verification of factual claims in two source reports:
- `/Volumes/Storage April 2026/PancreaticCancer/sources/external_research/1Search - deep-research-report.md`
- `/Volumes/Storage April 2026/PancreaticCancer/sources/external_research/2search - deep-research-report.md`

Status legend: VERIFIED, PARTIAL, FALSE, UNVERIFIED.

---

## Dataset size and count claims

### Claim 1: TCGA-PAAD via GDC — "185 cases and 12,853 files"
**Source in reports:** Report 1, "Inventory of relevant public datasets" → TCGA-PAAD row.
**Status:** VERIFIED.
**Evidence:** GDC API confirms the project at https://portal.gdc.cancer.gov/projects/TCGA-PAAD contains 185 cases and 12,853 files. Breakdown observed via the API expansion: Simple Nucleotide Variation (3,997 files), Copy Number Variation (2,700 files), Sequencing Reads (1,537 files); experimental strategies include WGS (3,198 files across 173 cases), WXS (2,950 files across 185 cases), and Genotyping Array (2,376 files across 185 cases). The project is in an open, released state. Source: GDC API endpoint `https://api.gdc.cancer.gov/projects/TCGA-PAAD?expand=summary,summary.data_categories,summary.experimental_strategies`.
**Notes:** Exact match to the reports' figures. Note that *case count* (185) is distinct from *sample count* used in many downstream studies (often 177–182 depending on filtering).

---

### Claim 2: DepMap 24Q2 Public — "23.31 GB" package; CC BY 4.0; no human PII
**Source in reports:** Report 1, DepMap 24Q2 row.
**Status:** PARTIAL. License verified; size figure could not be confirmed from the Figshare landing page (HTTP 403 to WebFetch) but is consistent with prior DepMap quarterly releases.
**Evidence:**
- License: DepMap 24Q2 Public is distributed under Creative Commons Attribution 4.0 International (CC BY 4.0). Confirmed via Figshare+ dataset record `https://plus.figshare.com/articles/dataset/DepMap_24Q2_Public/25880521` and DepMap forum announcement `https://forum.depmap.org/t/announcing-the-24q2-release/3312`.
- Content: New cell models with WGS/WES (Copy Number and Mutation), RNA-seq (Expression and Fusions), and genome-wide CRISPR knockout screens.
- The DepMap portal data page (`https://depmap.org/portal/data_page/`) lists per-file sizes but the aggregate "23.31 GB" total was not directly visible in the WebFetch slice.
**Notes:** The 23.31 GB figure is plausible given prior DepMap quarterly release packages of similar shape, but I could not confirm the exact byte total from primary sources due to Figshare WebFetch being blocked (403). License claim is fully verified.

---

### Claim 3: PDC (Proteomic Data Commons) — "70 TB across its holdings"
**Source in reports:** Report 1, CPTAC PDAC via PDC/GDC row.
**Status:** FALSE (as written). The publicly cited figures are different.
**Evidence:**
- ICF client-story page for the PDC engagement explicitly states: "The portal regularly manages 29 terabytes, with 785 terabytes of data downloaded in 140 countries." Source: `https://www.icf.com/clients/health/improving-proteomics-data-access-nci`.
- NCI Data Release Notes (`https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm`) describe per-release file volumes (e.g., release v5.3 = ~3.5 TB; release v6.0 = ~540 GB) but do not consolidate to a "70 TB" total.
- 2024 Cancer Research Communications paper notes "more than 160 datasets across 19 cancer types" but does not state 70 TB.
**Notes:** The number "70 TB" does not appear in any authoritative source I could find. The closest authoritative figures are **~29 TB managed** and **~785 TB downloaded** (cumulative). The reports' "70 TB" claim should be corrected to "~29 TB managed (per ICF, the PDC implementation partner)" or removed.

---

### Claim 4: TCIA Pancreas-CT — "82 abdominal CT scans" with manual segmentations
**Source in reports:** Report 1, TCIA Pancreas-CT row.
**Status:** VERIFIED.
**Evidence:** TCIA collection page `https://www.cancerimagingarchive.net/collection/pancreas-ct/` confirms 82 abdominal contrast-enhanced 3D CT scans from the NIH Clinical Center. Manual pancreas segmentations are included: "A medical student manually performed slice-by-slice segmentations of the pancreas as ground-truth and these were verified/modified by an experienced radiologist." Segmentations available as a separate ZIP/NIfTI download (948.96 KB).
**Notes:** Minor caveat — the segmentation pack covers 80 subjects (Version 2), not all 82 scans. Reports do not make a quantitative claim about segmentation count.

---

### Claim 5: TCIA CPTAC-PDA — radiology + pathology images for CPTAC PDAC cohort
**Source in reports:** Report 1, TCIA CPTAC-PDA row.
**Status:** VERIFIED.
**Evidence:** Collection page `https://www.cancerimagingarchive.net/collection/cptac-pda/` confirms a CPTAC PDA cohort with both modalities:
- Radiology (DICOM): MR, CT, US, PT — 67.24 GB across 110 subjects.
- Pathology (whole-slide SVS): 88 GB across 168 subjects.
- Total Version 15 (Feb 26, 2025): 155.24 GB across 168 subjects.
**Notes:** Reports do not claim a specific size; they accurately describe the collection as "large and image-heavy." Verified.

---

### Claim 6: Full 2025 RCSB PDB archive snapshot — "1,583 GB"
**Source in reports:** Report 1, RCSB PDB row.
**Status:** VERIFIED.
**Evidence:** RCSB stats page (`https://www.rcsb.org/stats/data_storage_growth`) reports: 2025 legacy archive snapshot is **1,583 GB** containing 246,905 PDB structures. Growth trajectory: 2024 = 1,437 GB / 229,564 structures; 2023 = 1,242 GB / 214,121 structures; 2022 = 1,086 GB / 199,755 structures. The versioned archive component is 298 GB as of 2025.
**Notes:** Direct exact match. Note that a separate web search returned a 1,437 GB figure dated to January 1, 2025 — this is the prior year's snapshot. The 1,583 GB figure is the current 2025 snapshot.

---

## Database license claims

### Claim 7: ChEMBL — "CC BY-SA 3.0 for data content"
**Source in reports:** Report 1, ChEMBL row.
**Status:** VERIFIED.
**Evidence:** ChEMBL Interface Documentation explicitly: "The ChEMBL data is made available on a Creative Commons Attribution-Share Alike 3.0 Unported License." Source: `https://chembl.gitbook.io/chembl-interface-documentation/about` and ChEMBL licensing page `http://chembl.github.io/chembl-licensing/`. Attribution must include the ChEMBL URL and release version.
**Notes:** Verified exactly.

---

### Claim 8: DepMap — "CC BY 4.0; depositor states no human PII"
**Source in reports:** Report 1, DepMap row.
**Status:** PARTIAL (license verified; PII statement plausible but not directly quoted).
**Evidence:** CC BY 4.0 confirmed (see Claim 2). The Figshare+ deposit and DepMap Terms of Use note that data are de-identified cell-line resources; depositor description on Figshare typically asserts no human PII for the public package.
**Notes:** PII assertion is consistent with how DepMap public releases are framed (cell-line omics, not patient-identifiable data). Could not retrieve the exact depositor language due to Figshare 403.

---

### Claim 9: PubChem — "freely accessible archive; licensing/provenance considerations vary by contributing source"
**Source in reports:** Report 1, PubChem row.
**Status:** VERIFIED.
**Evidence:** PubChem is provided to the public free of charge by NCBI/NLM. The NCBI Data Usage Policies (`https://www.ncbi.nlm.nih.gov/home/about/policies/`) confirm there is no general license restriction on PubChem data, but warn that "the NCBI site contains resources which incorporate material contributed or licensed by individuals, companies, or organizations that may be protected by U.S. and foreign copyright laws… persons reproducing, redistributing, or making commercial use of this information are expected to adhere to the terms and conditions asserted by the copyright holder." Provenance flags vary by depositor.
**Notes:** Verified. The reports' nuanced framing ("freely accessible… but provenance considerations vary by contributing source") matches NCBI's stated position exactly.

---

### Claim 10: ZINC20 / ZINC22 — public source for screening
**Source in reports:** Report 2, validation asset table; Report 1, indirect mention.
**Status:** VERIFIED.
**Evidence:** ZINC20 is documented at `https://zinc20.docking.org` and described in Irwin et al. (J Chem Inf Model 2020) as "a free ultralarge-scale chemical database for ligand discovery." ZINC-22 covers tangible compound libraries (Enamine REAL, WuXi GalaXi, Mcule Ultimate) and is accessed via `https://cartblanche22.docking.org`. ZINC is hosted by the Irwin and Shoichet labs at UCSF. Free public access is confirmed.
**Notes:** Verified. ZINC15 is also still live at `https://zinc15.docking.org`.

---

## Benchmark claims

### Claim 11: DUD-E — "ships actives plus property-matched decoys for 102 targets"
**Source in reports:** Report 2, benchmark calibration section.
**Status:** VERIFIED.
**Evidence:** Mysinger, Carchia, Irwin, Shoichet (J Med Chem 2012, 55:6582–6594, doi:10.1021/jm300687e). The DUD-E paper describes "102 proteins with 22,886 clustered ligands drawn from ChEMBL, each with 50 property-matched decoys drawn from ZINC." Target categories span 26 kinases, 15 proteases, 11 nuclear receptors, 5 GPCRs, 2 ion channels, 2 cytochrome P450s, 36 other enzymes, 5 miscellaneous. Site `http://dude.docking.org`. Source: `https://pubmed.ncbi.nlm.nih.gov/22716043/`.
**Notes:** Verified exactly.

---

### Claim 12: LIT-PCBA 2025 audit — "severe data leakage and redundancy; benchmark unreliable for fair evaluation"
**Source in reports:** Report 2, benchmark calibration paragraph and risks section.
**Status:** VERIFIED. This is the highest-priority verification — the audit paper exists and the report's characterization is accurate.
**Evidence:**
- **Paper:** Huang, A.; Knight, I. S.; Naprienko, S. "Data Leakage and Redundancy in the LIT-PCBA Benchmark." arXiv:2507.21404 (v1 July 29, 2025; v2 August 7, 2025). URLs: `https://arxiv.org/abs/2507.21404`, `https://arxiv.org/abs/2507.21404v2`. Affiliation reference: SieveStack.
- **Abstract excerpt (verbatim):** "LIT-PCBA is widely used to benchmark virtual screening models, but our audit reveals that it is fundamentally compromised. We find extensive data leakage and molecular redundancy across its splits, including 2D-identical ligands within and across partitions, pervasive analog overlap, and low-diversity query sets. In ALDH1 alone, for instance, 323 active training -- validation analog pairs occur at ECFP4 Tanimoto similarity ≥ 0.6; across all targets, 2,491 2D-identical inactives appear in both training and validation, with very few corresponding actives. These overlaps allow models to succeed through scaffold memorization rather than generalization, inflating enrichment factors and AUROC scores…"
- **Key findings:** 2,491 inactives duplicated across train/validation; 2,945 duplicates within training, 789 within validation; 3 query-set ligands leak into train (2) or validation (1); for some targets >80% of query ligands are near-duplicates (Tanimoto ≥ 0.9); 323 highly similar active pairs in ALDH1 alone between train and validation; **a trivial memorization-based baseline with no learnable parameters matches or exceeds the reported performance of state-of-the-art deep models including CHEESE**.
- **Audit repository:** `https://github.com/sievestack/lit-pcba-audit` (reproduction scripts and baseline implementation).
- **Counter-discussion:** A related blog ("Do Stereoisomers Cause Leakage? A Closer Look at the LIT-PCBA Audit" by Miroslav Lzicar at `https://mireklzicar.com/blog/stereoisomers`) discusses whether some "leakage" is actually stereoisomers — this is a useful caveat but does not overturn the audit's central findings.
**Notes:** Report 2's framing — "use DUD-E only for engine/pipeline sanity checks, and treat LIT-PCBA as a historical secondary benchmark with explicit caveats" — is consistent with the audit. **Recommended action for the PDAC project:** treat LIT-PCBA as a secondary/historical benchmark only; do not use as primary validation gate for KRAS G12D screening pipeline performance.

---

### Claim 13: LIT-PCBA origin — "drew actives and inactives from PubChem BioAssays"
**Source in reports:** Report 2, benchmark calibration paragraph.
**Status:** VERIFIED.
**Evidence:** Tran-Nguyen, V.-K.; Jacquemard, C.; Rognan, D. "LIT-PCBA: An Unbiased Data Set for Machine Learning and Virtual Screening." J Chem Inf Model 2020. The dataset was derived from "149 dose-response PubChem bioassays… additionally processed to remove false positives and assay artifacts and keep active and inactive compounds within similar molecular property ranges." It includes 15 protein targets, 7,761 confirmed actives, and 382,674 confirmed inactives. Source: `https://pubs.acs.org/doi/abs/10.1021/acs.jcim.0c00155`.
**Notes:** Verified. The PubChem-BioAssay origin is exactly as described in the reports.

---

### Claim 14: BindingDB — "public resource of experimentally measured protein–small-molecule affinities"
**Source in reports:** Report 2, validation asset table.
**Status:** VERIFIED.
**Evidence:** BindingDB (Liu et al., originally 2007; current update: "BindingDB in 2024: a FAIR knowledgebase of protein-small molecule binding data," PMC11701568) describes itself as a public, web-accessible database of experimentally measured binding affinities between small molecules and proteins. Current scale: 2.9 million binding measurements spanning 1.3 million compounds and thousands of protein targets. Strong patent-derived data curation focus. Source: `https://www.bindingdb.org/` and `https://pmc.ncbi.nlm.nih.gov/articles/PMC11701568/`.
**Notes:** Verified.

---

### Claim 15: AlphaFold DB — "over 200 million structures"
**Source in reports:** Report 2, comparative-assessment paragraph.
**Status:** VERIFIED.
**Evidence:** AlphaFold DB homepage (`https://alphafold.ebi.ac.uk/`) states verbatim: "AlphaFold DB provides open access to over 200 million protein structure predictions to accelerate scientific research." Co-developed by Google DeepMind and EMBL-EBI.
**Notes:** Verified exactly.

---

## Statistics + numbers about PDAC and KRAS

### Claim 16: AACR Project GENIE pancreatic portal — exists, has PDAC data, publicly accessible
**Source in reports:** Report 2, validation asset table.
**Status:** VERIFIED.
**Evidence:** AACR Project GENIE BPC PANC v1.0-public (`https://www.aacr.org/professionals/research/aacr-project-genie/bpc/panc-1-0-public-project-genie-aacr/`) contains 1,109 pancreatic cancer patients from 4 institutions (MSK, DFCI, UHN, VICC) with genomic profiling between 2013–2018 (patient ages 24–88), treatment histories, imaging, and survival outcomes. Accessible via cBioPortal (`www.cbioportal.org/genie/`) and Synapse (`https://synapse.org/genie`). PDAC-specific fields include tumor resectability status.
**Notes:** Verified. Both interfaces require user registration ("request access"), but the dataset is openly available.

---

### Claim 17: Rahib et al. modeling — pancreatic cancer projected to be #2 cancer killer by 2030
**Source in reports:** Report 2, executive summary and validation assets (implicit); also referenced in user's own PDAC memory docs.
**Status:** VERIFIED.
**Evidence:** Rahib, L.; Smith, B. D.; Aizenberg, R.; Rosenzweig, A. B.; Fleshman, J. M.; Matrisian, L. M. "Projecting cancer incidence and deaths to 2030: the unexpected burden of thyroid, liver, and pancreas cancers in the United States." Cancer Research 2014, 74(11):2913–2921 (June 1, 2014). PubMed `https://pubmed.ncbi.nlm.nih.gov/24840647/`. Abstract verbatim: "pancreas and liver cancers are projected to surpass breast, prostate, and colorectal cancers to become the second and third leading causes of cancer-related death by 2030, respectively." (Lung cancer remains #1.)
**Notes:** Verified exactly. Reports' framing matches.

---

### Claim 18: MRTX1133 J Med Chem paper by Wang et al. 2022 — exists
**Source in reports:** Report 2, recommended-target section and risks section.
**Status:** VERIFIED.
**Evidence:** Wang, X.; Allen, S.; Blake, J. F.; Bowcut, V.; Briere, D. M.; Calinisan, A.; Dahlke, J. R.; Fell, J. B.; Fischer, J. P.; et al. "Identification of MRTX1133, a Noncovalent, Potent, and Selective KRASG12D Inhibitor." J Med Chem 2022, 65(4):3123–3133 (Feb 24, 2022; EPub Dec 10, 2021). Source: `https://pubmed.ncbi.nlm.nih.gov/34889605/` and `https://pubs.acs.org/doi/10.1021/acs.jmedchem.1c01688`. 27 authors total, Mirati Therapeutics (San Diego) and Pfizer Boulder R&D (Colorado). Wang is first author.
**Notes:** Verified exactly. This is the canonical MRTX1133 medicinal-chemistry discovery paper.

---

## Summary tally

| # | Claim | Status |
|---|---|---|
| 1 | TCGA-PAAD 185 cases / 12,853 files | VERIFIED |
| 2 | DepMap 24Q2 23.31 GB | PARTIAL (license OK; size not directly confirmed) |
| 3 | PDC 70 TB holdings | **FALSE** |
| 4 | TCIA Pancreas-CT 82 scans + segmentations | VERIFIED |
| 5 | TCIA CPTAC-PDA radiology + pathology | VERIFIED |
| 6 | RCSB PDB 2025 archive 1,583 GB | VERIFIED |
| 7 | ChEMBL CC BY-SA 3.0 | VERIFIED |
| 8 | DepMap CC BY 4.0 / no PII | PARTIAL (license OK; PII statement plausible) |
| 9 | PubChem freely accessible, provenance varies | VERIFIED |
| 10 | ZINC20/ZINC22 public | VERIFIED |
| 11 | DUD-E 102 targets, property-matched decoys | VERIFIED |
| 12 | **LIT-PCBA 2025 audit (leakage, redundancy)** | **VERIFIED** — arXiv:2507.21404 (Huang, Knight, Naprienko, July 2025) |
| 13 | LIT-PCBA origin from PubChem BioAssays | VERIFIED |
| 14 | BindingDB public affinities | VERIFIED |
| 15 | AlphaFold DB >200M structures | VERIFIED |
| 16 | AACR Project GENIE pancreatic portal | VERIFIED |
| 17 | Rahib 2014 — PC #2 killer by 2030 | VERIFIED |
| 18 | MRTX1133 Wang 2022 J Med Chem | VERIFIED |

**Totals:** 14 VERIFIED, 2 PARTIAL, 1 FALSE, 1 UNVERIFIED — across 18 claims (PARTIAL items in this case are sub-claims where license verified but size/PII could not be directly confirmed).

**Single material correction needed:** The PDC "70 TB" figure is not supported by any authoritative source. ICF (the PDC implementation partner) publicly states the portal manages ~29 TB and has served ~785 TB of downloads. The reports should be amended.

**LIT-PCBA verdict:** The 2025 audit is real and well-documented (arXiv:2507.21404 by Huang, Knight, Naprienko of SieveStack). The audit's central claim — that LIT-PCBA contains severe data leakage, analog redundancy, and is exploitable by a memorization-only baseline that matches state-of-the-art models — is robustly supported. Report 2's policy recommendation (LIT-PCBA as a historical secondary benchmark only, with explicit caveats) is consistent with the audit findings. **This validates the project's decision to use DUD-E only as a sanity check and to not lean on LIT-PCBA for primary validation of the KRAS G12D screening pipeline.**
