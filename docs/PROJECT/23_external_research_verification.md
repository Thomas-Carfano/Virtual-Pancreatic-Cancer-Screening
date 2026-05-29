# External Research Verification — Source Audit of Both Deep-Research Reports

> Both reports (`sources/external_research/1Search` and `2search-deep-research-report.md`) cite via opaque `citeturn…` reference IDs that can't be dereferenced. This document records the result of independent source verification against authoritative web sources, done May 22, 2026. Detailed per-claim reports are in `sources/verifications/A_boinc_and_tools.md`, `B_pdb_and_structures.md`, and `C_datasets_and_benchmarks.md`.

## Headline

**The reports are mostly accurate.** Across ~50 verifiable claims:

- **40+ verified** against authoritative sources (BOINC docs, PDB entries, dataset portals, primary literature)
- **3 material errors** that propagate into our planning if uncorrected
- **8 partial/nuanced** — claim broadly right, but with a caveat that matters operationally
- **1 unable to verify directly** (a specific Figshare byte total, blocked by 403)

External validation: both reports independently picked the same #1 PDAC target (KRAS G12D switch-II pocket), the same production docking kernel (AutoDock Vina), and the same architecture (three-tier funnel) we'd already arrived at. The convergence is real, not artifact.

## Material errors — must be corrected in our docs

### Error 1: PDC "70 TB" — wrong
**Where:** Both external reports + our `PROJECT/22_boinc_technical_spec.md` (Layer 4 of validation ladder).
**What's actually true:** Per ICF (the PDC implementation partner), the portal **manages ~29 TB** and has served **~785 TB cumulative downloads**. The "70 TB" figure does not appear in any authoritative source. The PDC release-notes do show per-release file volumes (e.g., v5.3 = ~3.5 TB; v6.0 = ~540 GB) but never aggregate to 70 TB.
**Fix:** Update `PROJECT/22_boinc_technical_spec.md` § Layer 4 to read "~29 TB managed (per ICF)". *Corrected in this turn.*

### Error 2: "Docking@Home" framed as an "existing" BOINC project
**Where:** External report 1 line 11 + 86, listing Docking@Home alongside Rosetta@home, OpenPandemics, GPUGRID as "existing biomedical volunteer-computing projects." The error is in the external report only — our own docs do not currently reference Docking@Home, so no internal correction was needed; this is a flag against future use of report 1 framing in our communications.
**What's actually true:** Docking@Home **retired in May 2014**. Stopped distributing jobs April 30, 2014; server stopped accepting results May 23, 2014. Closed because the University of Delaware no longer had resources to maintain it.
**Why this matters:** It remains a *historical precedent* (validating that protein-ligand docking can work on BOINC), but calling it an "existing" project misleads about the current biomedical-BOINC landscape. **Other precedents to learn from are all active**: Rosetta@home, WCG OpenPandemics, GPUGRID (in transition since April 2025 server migration).
**Fix:** No internal docs to correct; future references to BOINC biomedical precedents must label Docking@Home as historical / retired.

### Error 3: PDB 7JWU is NOT a p53 Y220C entry
**Where:** Our `PROJECT/31_mutant_p53_structural_biology.md` cites 7JWU in 6 places as an "intermediate stilbene-based binder" / "intermediate-stage Aprea-PMV chemotype" for Y220C. This is *not* from the external reports — it was an error in the agent prompt I wrote when commissioning the p53 deep dive. The agent expanded it into invented descriptions.
**What's actually true:** PDB 7JWU is **human ALDH1A1 (aldehyde dehydrogenase 1A1) bound to compound (R)-28** (a pyrazolo[3,4-d]pyrimidinone). Resolution 1.90 Å, depositors Hurley & Buchman, August 2020. Different protein, different ligand class, unrelated to p53.
**Real Y220C anchor structures** (per verification): **2VUK** (PhiKan083 — original Fersht/Boeckler 2008 Y220C stabilizer), **5ABA**, **5AOK**, **5G4N / 5G4O** (difluorinated/trifluorinated PhiKan083 lead-optimization), **5O1C / 5O1H / 5O1I** (MB aminobenzothiazole series), **8A32** (JC769 iodophenol-based / related to rezatapopt).
**Fix:** Replace 7JWU references throughout `PROJECT/31_mutant_p53_structural_biology.md` with **2VUK** (Boeckler 2008 PhiKan083 — the canonical first-generation Y220C structure) and add a verification-corrections appendix to the file. *Corrected in this turn.*

## Important nuances — claim broadly right, but operational caveat

### PDB 6GJ7 vs 7RPZ orthogonality includes nucleotide state, not just chemotype
The external reports recommend 6GJ7 as the orthogonal KRAS G12D pocket validation partner to 7RPZ. Both are KRAS G12D — that part is correct. But:
- **7RPZ** = GDP-bound (inactive state), MRTX1133 in switch-II pocket, 1.30 Å
- **6GJ7** = GppCp-bound (GTP-mimetic, *active* state), BI-2852 in switch I/II interface pocket, 1.67 Å

So when used together they're orthogonal across both ligand chemotype AND nucleotide state. This is *more* useful for robustness than the reports framed — but our docking protocol must explicitly handle both nucleotide states (GDP vs GppCp) when running the two structures.

### MRTX1133 was clinically discontinued in January 2025
BMS (which acquired Mirati in late 2023 for ~$4.8B) terminated the MRTX1133 Phase 1/2 study after Phase 1 completion. Reason: "highly variable and suboptimal" pharmacokinetics, not safety. MRTX1133 remains the canonical *preclinical proof-of-concept* for non-covalent KRAS G12D inhibition — the chemotype and pocket are validated. It is still the right positive control for our docking pipeline.
**Implication:** Frame MRTX1133 in our project comms as "preclinical reference compound for a validated pocket," not as a current clinical asset. Next-generation G12D programs now in clinic from other sponsors: RMC-9805 (Revolution Medicines), ASP3082 (Astellas), HRS-4642 (Hengrui), INCB161734 (Incyte).

### KRAS G12D ~35% vs ~40% in PDAC
External reports cite ~35%; our internal docs cite ~40%. Literature range is 35–45% across cohorts; the modal consensus value is ~40% (TCGA-PAAD = 41%, MDA cohort ~39%, multi-cohort reviews cluster around 40%). Our docs are better aligned with consensus. The 35% figure is defensible as the low end of the range but is not "the NCI value" — the NCI summary page only states the 93% overall KRAS rate, not a G12D-specific percentage.

### Wassman 2013 Nat Comms is NOT a Y220C paper
Our `PROJECT/31_mutant_p53_structural_biology.md` § 6a described Wassman 2013 as "characterizing the Y220C cavity dynamics" with a flexible loop (residues 225–230). **This is misattributed.** Wassman 2013 identifies a **transiently open L1/S3 pocket relevant to multiple p53 mutants** (including R175H), validated by Cys124 mutagenesis abolishing PRIMA-1 activity. The pocket is not Y220C-specific; the residue range cited (225–230) is also not L1/S3.
**Fix:** Verification-corrections appendix in `PROJECT/31_mutant_p53_structural_biology.md`. The Y220C-specific dynamics paper to cite is the Joerger/Fersht follow-up to Boeckler 2008, not Wassman 2013. *Corrected in this turn.*

### Salmon "C++11" claim — under-specified
Salmon's GPL v3 license and C++ implementation are verified, but the specific C++11 standard version isn't surfaced from the current GitHub landing page. Not a meaningful issue for our planning, but flagged for completeness.

### RCSB PDB CC0 license has one exception
CC0 applies cleanly to archive data and to native RCSB API data. **Externally integrated annotations** (e.g., some sequence/domain annotations from UniProt, InterPro, Pfam surfaced via RCSB APIs) retain their source license. For our project — distributing PDB structure files themselves to volunteers — CC0 applies. Only matters if our API consumption pulls integrated external annotations downstream.

## Most important verified claims

These are the load-bearing claims that hold up:

### ✅ BOINC Central is real
https://boinc.berkeley.edu/central/ — launched Nov 26, 2021; March 24, 2026 update confirms ongoing operation. Explicitly supports "Any application packaged with Docker" and "Autodock from the Scripps Research Institute." Docker support via BUDA (BOINC's Docker framework). This is the fastest pilot path — our Pilot Zero strategy holds.

### ✅ LIT-PCBA 2025 audit is real and the findings are robust
Huang, Knight, Naprienko (SieveStack). "Data Leakage and Redundancy in the LIT-PCBA Benchmark." **arXiv:2507.21404** (v1 July 29, 2025; v2 Aug 7, 2025). Audit code at https://github.com/sievestack/lit-pcba-audit. Findings:
- 2,491 inactives duplicated across train/validation splits
- 323 ALDH1 active analog pairs at ECFP4 Tanimoto ≥ 0.6 across train-validation
- 3 query-set ligands leaked into train/validation
- For some targets >80% of query ligands are near-duplicates (Tanimoto ≥ 0.9)
- **A trivial memorization-only baseline matches or exceeds state-of-the-art deep models including CHEESE**

**This validates our position** to treat LIT-PCBA as a historical secondary benchmark only and to not use it as a primary validation gate. Recommended action: document our policy publicly so other PDAC compute researchers don't trip on the same data leakage.

### ✅ All tool licenses
- AutoDock Vina = Apache 2.0
- AutoDock-GPU = GPL-2.0 + LGPL-2.1 (both files in repo)
- GNINA = dual GPL/Apache (GPL when OpenBabel-linked) — confirmed CUDA 12+, OpenBabel3, RDKit, Boost, protobuf, HDF5; pre-built binaries + Docker image
- P2Rank = MIT, Java 17+, PDB/mmCIF/BinaryCIF input
- fpocket = MIT, primarily C, official Docker image
- OpenMM = MIT + LGPL, CUDA + OpenCL + HIP platforms
- GROMACS = LGPL v2.1, mdrun checkpoint support
- Salmon = GPL v3, C++
- MONAI = Apache 2.0, PyTorch
- Meeko (Forli lab) = handles PDBQT → SDF/PDB pipeline for Vina + AutoDock-GPU

### ✅ All dataset sizes verified except PDC
- TCGA-PAAD = exactly **185 cases, 12,853 files** (GDC API confirms)
- RCSB PDB 2025 archive = exactly **1,583 GB** containing 246,905 structures
- TCIA Pancreas-CT = exactly **82 abdominal CT scans** with manual segmentations
- TCIA CPTAC-PDA = **155.24 GB** total (67.24 GB radiology + 88 GB pathology, 168 subjects)
- AlphaFold DB = **>200 million** structures
- DUD-E = **102 targets**, 22,886 ligands, 50 property-matched decoys each

### ✅ All KRAS/MRTX/p53 specifics
- KRAS mutated in **93% of PDAC** in TCGA-PAAD (140/150 cases, Cancer Genome Atlas Research Network 2017 Cancer Cell)
- PDB 7RPZ = KRAS G12D + MRTX-1133 + GDP + Mg²⁺, 1.30 Å
- PDB 6OIM = KRAS G12C + AMG 510 (sotorasib) covalent
- PDB 6UT0 = KRAS G12C + MRTX849 (adagrasib) covalent
- MRTX1133 J Med Chem 2022 paper (Wang et al.) — KD ~0.2 pM, IC50 < 2 nM, >700× selectivity over WT
- PDAC regression: 8/11 (73%) of KRAS G12D PDAC CDX/PDX models showed ≥30% regression (Hallin et al. Nature Medicine 2022)
- MRTX1133 + EGFR/PI3Kα combination data: documented in Hallin et al. 2022
- Boeckler 2008 PNAS — established Y220C cavity with PhiKan083 (PDB 2VUK)
- PMV Pharmaceuticals rezatapopt / PC14586 — PYNNACLE Phase 1/2 trial (NCT04585750) — verified; FDA Fast Track granted; NDA Q1 2027

### ✅ BOINC platform specifics
- Servers can dispatch hundreds of jobs/sec on a single machine (Anderson papers, arXiv:1903.01699)
- Adaptive replication tracks trust at (host, app_version) level — exact wording from BOINC AdaptiveReplication wiki
- Code-signing key on offline machine is the official BOINC recommendation
- 1.9 GB VirtualBox cookbook example — verbatim from the BOINC wiki cookbook page
- WCG OpenPandemics work motivated AutoDock-GPU v1.4 + v1.5 features (flexible residues, modifiable pair potentials, contact analysis) — verbatim from the WCG article
- All app deployment modes confirmed: native, BOINC wrapper, docker_wrapper, vboxwrapper, WSL wrapper

## What this means for our plan

1. **`PROJECT/22_boinc_technical_spec.md` is corrected** for the PDC TB figure (was "70 TB", now "~29 TB managed per ICF"). Docking@Home framing was never in our docs — only flagged for future use of external-report material. The rest stands.
2. **`PROJECT/31_mutant_p53_structural_biology.md` is corrected** for the 7JWU misattribution. Y220C anchor is now **PDB 2VUK** (Boeckler 2008 PhiKan083). A verification-corrections appendix has been added.
3. **Our local test plan (`PROJECT/21_local_test_plan.md`) stays.** Everything in it (PDB 7RPZ as primary, MRTX1133 as positive control, AutoDock Vina + Meeko + RDKit, OpenMM Metal backend) is verified.
4. **LIT-PCBA stays out of our primary validation ladder.** The 2025 audit is robust. We use DUD-E for engine sanity-checks only and build our own KRAS-focused benchmark from ChEMBL + BindingDB + PubChem BioAssay (Layer 2 of the validation ladder).
5. **BOINC Central as Pilot Zero** path is real. Worth direct inquiry into admission requirements.
6. **Frame MRTX1133 carefully in project communications** — preclinical proof-of-concept, not a current clinical asset. Next-gen G12D programs (RMC-9805, ASP3082, HRS-4642, INCB161734) are the live clinical assets we'd want to track for resistance/combination science.

## Detailed verification files

- `sources/verifications/A_boinc_and_tools.md` — 22 claims, BOINC platform + tool licenses + GNINA paper
- `sources/verifications/B_pdb_and_structures.md` — 15 claims, PDB entries + KRAS biology + MRTX1133 + Y220C
- `sources/verifications/C_datasets_and_benchmarks.md` — 18 claims, dataset sizes + benchmark validity + LIT-PCBA audit

Each claim is recorded with status, evidence URL(s), and verbatim quotes from authoritative sources.
