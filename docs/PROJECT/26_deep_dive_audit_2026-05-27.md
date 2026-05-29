# PancreaticCancer Deep-Dive Audit - 2026-05-27

Status: audit report only. No source documents, code, docking outputs, or generated artifacts were edited during this pass.

Target: `/Volumes/Storage April 2026/PancreaticCancer`

Scope: `PLAN.md`, supporting docs in `PROJECT/` and `sources/`, the `pancscan/` docking code/results, and project hygiene. This is a factual research/project audit, not medical advice.

## Executive Summary

`PLAN.md` is the strongest document in the project and has already incorporated several important corrections: 2026 ACS incidence/death estimates, the MRTX1133 trial termination caveat, p53 9BR4 as the rezatapopt anchor, OpenMM platform caveats, BOINC Central feasibility language, and dataset-size caveats. It is close to being externally shareable as a concept document.

The project is not yet safe to use as a docking pipeline source of truth. The blockers are concentrated in three places:

- `PLAN.md` line 175 describes a broader Tier 0 gate than the code/report actually ran.
- `PROJECT/31_mutant_p53_structural_biology.md` still contains wrong PDB workflows in the body even though its header warns against them.
- `pancscan/tier1/screen/run_full/results.csv` is a partial, single-pass run, not a completed Tier 1 gate.

The existing audit infrastructure is unusually useful. `sources/verifications/known_bad_claims.md`, `must_verify_claim_types.md`, `structure_manifest.csv`, and `PROJECT/25_full_audit_synthesis.md` already identify many of the right hazards. The next improvement should be closure discipline: either fix the flagged docs, mark them as background-only, or block downstream use through a machine-readable checklist.

## Current Confidence By Surface

| Surface | Confidence | Notes |
|---|---:|---|
| `PLAN.md` | Medium-high after targeted fixes | Good narrative and mostly current facts; one important Tier 0 overclaim remains. |
| `PROJECT/` docs | Mixed | Useful background, but several docs still contain stale claims or known-bad PDB IDs. Treat as background-only unless line-verified. |
| `sources/verifications/` | High as audit evidence | Strong denylist/manifest structure; unresolved logged-only items remain open. |
| `pancscan` Tier 0 | Medium-high for self-dock only | The 7RPZ/MRTX1133 self-dock result is meaningful, but it does not prove decoy enrichment or cross-ligand specificity. |
| `pancscan` Tier 1 | Low-medium | Code is directionally sensible, but current artifacts show a partial one-pass run and no completed manifest/report. |
| Repo hygiene | Low | The target is not a Git repo, has no `.gitignore`, and generated artifacts are mixed with source. |

## Source Verification Spot Checks

| Claim type | Current authoritative check | Audit result |
|---|---|---|
| US pancreatic cancer 2026 incidence/deaths | ACS `Cancer Facts & Figures 2026` reports 67,530 new cases and 52,740 deaths. Source: [ACS 2026 PDF](https://www.cancer.org/content/dam/cancer-org/research/cancer-facts-and-statistics/annual-cancer-facts-and-figures/2026/2026-cancer-facts-and-figures.pdf). | `PLAN.md` is aligned. |
| 5-year survival around 13% | ACS survival table for diagnoses 2015-2021 lists all SEER stages combined at 13%. Source: [ACS survival rates](https://www.cancer.org/cancer/types/pancreatic-cancer/detection-diagnosis-staging/survival-rates.html). | `PLAN.md` is aligned. |
| MRTX1133 trial status | ClinicalTrials.gov API for `NCT05737706`: `overallStatus=TERMINATED`, `whyStopped=Formulation challenges`, completion date 2025-03-10, last update 2025-04-06. Source: [ClinicalTrials.gov NCT05737706](https://clinicaltrials.gov/study/NCT05737706). | `PLAN.md` is aligned if it keeps the registry reason separate from secondary PK reporting. |
| Sotorasib/adagrasib FDA scope | FDA pages support CRC indications with EGFR antibodies; they do not make these PDAC approvals. Sources: [sotorasib + panitumumab FDA](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-sotorasib-panitumumab-kras-g12c-mutated-colorectal-cancer), [adagrasib + cetuximab FDA](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-adagrasib-cetuximab-kras-g12c-mutated-colorectal-cancer). | Any supporting doc saying or implying approved PDAC use needs qualification. |
| Zenocutuzumab/Bizengri | FDA granted accelerated approval for NRG1-fusion NSCLC and pancreatic adenocarcinoma on 2024-12-04 and approved cholangiocarcinoma on 2026-05-08. Sources: [FDA NSCLC/PDAC approval](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-zenocutuzumab-zbco-non-small-cell-lung-cancer-and-pancreatic), [FDA cholangiocarcinoma approval](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-zenocutuzumab-zbco-advanced-unresectable-or-metastatic-cholangiocarcinoma), [FDA Bizengri snapshot](https://www.fda.gov/drugs/drug-trials-snapshots/drug-trials-snapshots-bizengri). | Current `PLAN.md` framing is acceptable if it remains NRG1-fusion-specific. |
| p53 8A32 vs 9BR4 | RCSB/data API: 8A32 title is Y220C with iodophenol stabilizer JC769 and nonpolymer KVA; 9BR4 title is Y220C with PC-9859/rezatapopt-series ligand. Sources: [RCSB 8A32](https://www.rcsb.org/structure/8A32), [RCSB 9BR4](https://www.rcsb.org/structure/9BR4). | `PLAN.md` is mostly fixed; `PROJECT/31...` body is not. |
| BOINC Central feasibility | BOINC Central states it supports Docker-packaged apps and AutoDock/Vina-style workloads, and its March 2026 news cites 450 CPU-years for a completed project. Sources: [BOINC Central](https://boinc.berkeley.edu/central/), [About BOINC Central](https://boinc.berkeley.edu/central/about.php). | Feasible as an integration path; not proof of admission or production readiness. |
| OpenMM/OpenFE platform caveats | OpenMM latest docs list `Reference`, `CPU`, `CUDA`, `OpenCL`, and `HIP`, not native Metal. OpenFE stable docs list macOS arm64 installer support, but recommend Linux/NVIDIA GPUs for production OpenMM protocols. Sources: [OpenMM docs](https://docs.openmm.org/latest/userguide/application/02_running_sims.html), [OpenFE install docs](https://docs.openfree.energy/en/stable/installation.html). | `PLAN.md` and `21_local_test_plan.md` are directionally aligned. |
| Dataset sizes | Enamine official REAL Database page lists 13.6B enumerated database molecules; Enamine quick facts list over 94.5B REAL compounds; ZINC-22 peer-reviewed paper lists >37B 2D and >4.5B 3D. Sources: [Enamine REAL Database](https://enamine.net/compound-collections/real-compounds/real-database), [Enamine REAL quick facts](https://enamine.net/?catid=2&highlight=WyJxdWljayJd&id=1911%3Atest-real-compounds&view=article), [ZINC-22 JCIM](https://pubs.acs.org/doi/10.1021/acs.jcim.2c01253). | Supporting docs with `70B` or `55B ZINC22` are stale. |

Chrome was used for live-page inspection where useful; the RCSB page title for 8A32 rendered correctly in Chrome. ClinicalTrials.gov's rendered page did not expose the key fields reliably in the browser snapshot, so the official ClinicalTrials.gov API was used for the exact status fields.

## P0 Findings

### P0-01 - p53 structural-biology doc still contains unsafe PDB workflows

Evidence:

- `PROJECT/31_mutant_p53_structural_biology.md:6` warns that 8A32 is not rezatapopt and that 9BR4 should be used instead.
- The same file still says 8A32 is rezatapopt at `:52`, `:209`, `:283`, `:315`, `:330`, `:348`, `:358`, `:473`, `:480`, `:562`, `:656`, `:674`, `:676`, `:686`, and `:761`.
- It still references other known-bad PDB IDs, including `4LO8` at `:205` and `:814`, and `7XZS` at `:319`, `:494`, `:664`, and `:775`.
- `sources/verifications/known_bad_claims.md:79-81` already records that 8A32 is KVA/JC769, 4LO8 is not p53, and 7XZS is Ricin A chain.
- `sources/verifications/structure_manifest.csv:8` records 9BR4 as the rezatapopt/Y220C anchor; `:12` quarantines the unresolved KRAS-G12D-apo target.

Impact:

Anyone using `PROJECT/31_mutant_p53_structural_biology.md` as a pipeline recipe can prepare the wrong receptor/ligand pair, then falsely validate p53 docking against a non-rezatapopt complex. This is the highest-risk accuracy defect because it turns a documented caveat into a direct workflow contradiction.

Recommended fix:

Quarantine `PROJECT/31_mutant_p53_structural_biology.md` from all pipeline use until every PDB row is either manifest-verified or replaced with `UNVERIFIED_PDB_ID`. For Y220C validation, replace "rezatapopt into 8A32" with "9BR4/PC-9859/rezatapopt-series validation" throughout. Also fix `PROJECT/21_local_test_plan.md:119`, which still lists "PDB 8A32 -- rezatapopt complex".

### P0-02 - `PLAN.md` Tier 0 description overclaims what the current Tier 0 implementation proves

Evidence:

- `PLAN.md:175` says Tier 0 docks MRTX1133 plus sotorasib, adagrasib, aspirin, and about 995 DUD-E decoys, with rank/contact/median criteria.
- `pancscan/tier0_smoke_test.py:3-15` describes a narrower smoke test: redock MRTX1133 from 7RPZ, check receptor/ligand prep, run Vina, compute RMSD/scores, and write reports.
- `pancscan/reports/tier0_report.md:11-20` lists only 6IC/GDP/Mg presence, RMSD under 2 Angstrom, and top score under -8 kcal/mol.
- `pancscan/reports/tier0_report.md:23-24` reports top score -14.66 kcal/mol and RMSD 0.506 Angstrom, which supports self-docking only.

Impact:

The current Tier 0 PASS is real but narrower than the plan says. An external reviewer can reproduce the mismatch immediately. More importantly, the current PASS does not show negative-control discrimination, aspirin below median, DUD-E enrichment, sotorasib/adagrasib behavior, or specific D12/Y96/H95 contact recovery.

Recommended fix:

Before sharing `PLAN.md`, either downgrade line 175 to match the current artifact ("Tier 0 self-dock smoke test") or implement the broader Tier 0 gate and generate a new report that includes the extra ligands, decoys, rank statistics, and contact checks.

## P1 Findings

### P1-01 - Tier 1 `run_full` is partial, single-pass, and below the current "strong" gate

Evidence:

- Intended enrichment set: `pancscan/tier1/enrichment/enrichment_compounds.csv` has 640 rows: 40 actives and 600 decoys.
- Current output: `pancscan/tier1/screen/run_full/results.csv` has 205 rows: 40 actives and 165 decoys attempted; 193 successful docks and 12 failures.
- All successful rows have `n_passes=1`, despite `pancscan/tier1/batch_dock.py:8-16` documenting a multi-pass schedule and `:148-149` defaulting to `8,16,32`.
- `pancscan/tier1/batch_dock.py:214-223` should write `results_ranked.csv` and `run_manifest.json` after normal completion, but `screen/run_full/` currently contains only `results.csv` at top level.
- Current metrics calculated from `results.csv`: ROC-AUC 0.757, EF1% 4.825, EF5% 2.895, EF10% 2.171, mean active affinity -9.00 kcal/mol, mean decoy affinity -7.57 kcal/mol.
- `pancscan/tier1/analyze_enrichment.py:82-89` defines "STRONG enrichment" as AUC >= 0.70 and EF1 >= 5. The current EF1 is just below that threshold.

Impact:

The partial result shows a real signal, but it is not a completed Tier 1 gate. Calling the folder `run_full` risks overclaiming. The current artifact cannot support production screening or external claims about enrichment.

Recommended fix:

Rename this output as a partial run or resume/complete all 640 compounds. Use the documented multi-pass schedule or explicitly document why a one-pass bulk-screen mode is being used. Run `analyze_enrichment.py`, preserve `results_ranked.csv`, `run_manifest.json`, `enrichment_report.json`, and publish the final pass/fail criteria in a report.

### P1-02 - KRAS G12D apo/ensemble source is still unresolved

Evidence:

- `sources/verifications/structure_manifest.csv:12` marks `KRAS-G12D-apo` as `UNVERIFIED` / `NEEDS SELECTION`.
- `PROJECT/21_local_test_plan.md:85` correctly warns not to default to 8AZV, stripped 8AZY, 4DSO, or 7T47.
- `PLAN.md:45`, `:62`, `:67`, `:123`, and `:196` depend on MD-derived conformational ensembles and cross-conformer behavior.

Impact:

The current 7RPZ self-dock is a good holo-pose validation, but it does not solve apo/ensemble selection. Any Tier 1+ claim about conformational ensembles or cryptic-pocket screening is premature until the target-source SOP is closed.

Recommended fix:

Add a structure-selection note for KRAS G12D apo: accepted starting structures, ligand-stripping policy, MD equilibration protocol, and validation criteria. Keep `KRAS-G12D-apo` quarantined in `structure_manifest.csv` until this is done.

### P1-03 - Supporting docs still contain stale or known-bad claims that conflict with the cleaner `PLAN.md`

Examples:

- `PROJECT/02_targets.md:40`, `:76`, and `:85` still use Enamine REAL `70B`.
- `PROJECT/04_proposal.md:9` and `:26` still frame screening around `10B-70B` / `~70B`.
- `PROJECT/20_synthesis.md:9` and `:222` still contain `70B` arithmetic and `ZINC22 ... ~55B`.
- `PROJECT/11_risk_factors.md:204` and `:240` still say "Placek" for the Nature Medicine EHR paper; `known_bad_claims.md:96` says correct first author is Placido.
- `PROJECT/15_targeted_therapy.md:277` says Collisson was `Cell`; `known_bad_claims.md:94` says it was `Nature Medicine`.
- `PROJECT/15_targeted_therapy.md:280` says Puleo has 4 subtypes while listing 5 subtype names; `known_bad_claims.md:95` records 5.
- `PROJECT/12_diagnosis_staging.md:276` says G12D is targetable with "recent-generation MRTX1133 and similar inhibitors entering trials"; this needs the MRTX1133 termination nuance.

Impact:

The project has two competing truth layers: a cleaner top-level plan and older supporting docs with leftover errors. External readers will not know which layer to trust.

Recommended fix:

Add a banner to stale supporting docs: "Background-only; superseded by PLAN.md and sources/verifications." Then batch-correct the small high-visibility items above. For anything not fixed, add explicit local caveats at the claim, not only in the audit files.

### P1-04 - The publication gate is documented but not operationalized

Evidence:

- `PROJECT/25_full_audit_synthesis.md:58-59` identifies unresolved p53/PDB blockers.
- `PROJECT/25_full_audit_synthesis.md:83`, `:90`, and `:96` summarize unresolved dataset, PDB, FDA, and platform corrections.
- `sources/verifications/must_verify_claim_types.md:74-77` correctly calls out trial-status source hierarchy, including MRTX1133.

Impact:

The audit system knows what is risky, but nothing prevents `PLAN.md` or a supporting doc from reintroducing a known-bad claim. This matters because the project has already produced multiple rounds of corrections and contradictions.

Recommended fix:

For the next implementation pass, create a lightweight prepublication checklist or script that fails on known-bad strings in externally shared files. At minimum, keep a manual "must pass before sharing" table in the new report queue and mark each blocker closed with file/line evidence.

## P2 Findings

### P2-01 - Enrichment provenance text is misleading after capping actives

Evidence:

- `pancscan/tier1/enrichment/provenance.md:5` says the output has 40 actives.
- `pancscan/tier1/enrichment/provenance.md:9` says 422 drug-like actives come from a G12D assay.
- `pancscan/tier1/build_enrichment_set.py:149-153` calculates `n_g12d` before applying the `actives_cap`, then truncates actives.
- `pancscan/tier1/build_enrichment_set.py:217-222` writes the pre-cap `n_g12d` count under the capped active section.

Impact:

The provenance is not false if read as "available before cap," but the placement makes it look like the 40 selected actives include 422 G12D-assay actives, which is impossible.

Recommended fix:

Report both numbers explicitly: `N G12D-assay drug-like actives available before cap` and `M of selected 40 actives are G12D-assay actives`.

### P2-02 - Ligand prep falls back silently in cases that should be audited

Evidence:

- `pancscan/tier1/prepare_ligand.py:44-55` returns the input SMILES if Dimorphite-DL protonation fails.
- `pancscan/tier1/prepare_ligand.py:69-72` falls back to the original SMILES if the protonated SMILES cannot be parsed.
- `pancscan/tier1/prepare_ligand.py:86-92` suppresses MMFF/UFF optimization exceptions and proceeds with ETKDG geometry.

Impact:

This is reasonable for a robust screening prototype, but production runs need failure telemetry. Otherwise protonation failures, salt/multicomponent issues, and unoptimized geometries can enter the ranking without being visible in `results.csv`.

Recommended fix:

Add structured prep flags to result rows: `protonation_fallback`, `original_smiles_used`, `optimization_failed`, `salt_or_multicomponent_detected`, and `prep_warning`. Do not make these fatal by default; make them visible and filterable.

### P2-03 - Generated artifacts are mixed with source and there is no repo hygiene boundary

Evidence:

- The target is not a Git repo.
- No `.gitignore` was found under the target.
- A scan found 413 generated or machine-local artifacts under `pancscan/`, including `.pdbqt`, `.sdf`, `.pdb`, `__pycache__`, `.pyc`, `.DS_Store`, and docking outputs.
- `pancscan/README.md:97-105` acknowledges `data/` and `reports/` are created at runtime, but the current tree keeps generated docking artifacts in-place.

Impact:

Without Git, `.gitignore`, or a source/data boundary, it is hard to tell what is canonical code, what is evidence, and what is disposable run output. This increases the chance of stale reports being reused.

Recommended fix:

Initialize a repo or move source code into a repo-managed subdirectory. Add `.gitignore` rules for `__pycache__/`, `*.pyc`, `.DS_Store`, routine PDBQT/SDF/PDB outputs, temporary docking logs, and bulk screening folders unless explicitly promoted to `reports/` as evidence.

### P2-04 - `pancscan/README.md` has a package-name inconsistency

Evidence:

- `pancscan/environment.yml:8-10` correctly says the conda-forge package is `vina`, not `autodock-vina`.
- `pancscan/README.md:83` suggests `mamba install -c conda-forge autodock-vina`.

Impact:

This is a setup-paper-cut, not a scientific blocker. It will still waste time when the environment is rebuilt on Apple Silicon.

Recommended fix:

Change the troubleshooting command to `mamba install -c conda-forge vina` and keep the `environment.yml` note as the source of truth.

### P2-05 - Current Tier 1 outputs do not preserve enough run metadata

Evidence:

- `pancscan/tier1/dock_config.json:14-19` records default Vina settings, but the actual run output does not include a top-level manifest.
- `pancscan/tier1/screen/run_full/results.csv` records `n_passes=1`, but not the command line, host, Vina version, worker count, wall time, resume history, or failure summary.
- `pancscan/tier1/batch_dock.py:215-223` would write some of this after normal completion, but the current run appears interrupted or incomplete.

Impact:

The result cannot be audited as a completed experiment. Partial CSVs are still useful, but they should identify themselves as partial and resumable.

Recommended fix:

Write an initial `run_manifest.json` before docking starts and update it atomically during/after the run. Include `status`, `started_at`, `updated_at`, `command`, `git_or_tree_hash` if available, input CSV hash, config hash, row counts, failed IDs, and completion state.

## P3 / Positive Findings

- The Tier 0 self-dock result is meaningful for the exact question it tested: `pancscan/reports/tier0_report.md:23-24` reports a strong 7RPZ/MRTX1133 pose recovery.
- `pancscan/tier0_smoke_test.py:241-255` explicitly addresses the earlier bond-order/protonation pitfall and uses an RCSB ideal ligand template before Meeko PDBQT generation.
- `pancscan/tier1/analyze_enrichment.py` has a clear, simple enrichment-gate structure and calculates ROC-AUC, EF, BEDROC, and score separation.
- Static syntax checks of Python files under `pancscan/` passed during the audit.
- `PLAN.md:269` openly warns that the p53 PDB tables still require re-verification before pipeline use. That caveat should stay until the p53 docs are fully corrected.

## Recommended Remediation Queue

### Before External Sharing

1. Fix or downgrade `PLAN.md:175` so the Tier 0 description matches the actual Tier 0 artifact.
2. Quarantine or repair `PROJECT/31_mutant_p53_structural_biology.md`; do not let it function as a recipe until every PDB row is manifest-verified.
3. Fix `PROJECT/21_local_test_plan.md:119` from "8A32 -- rezatapopt complex" to the manifest-approved 9BR4 framing.
4. Add "background-only / superseded by PLAN.md" banners to stale supporting docs, or batch-correct the high-risk stale claims listed above.
5. Keep the MRTX1133 wording source-hierarchical: registry reason is formulation challenges; secondary reporting may discuss PK.
6. Keep FDA approval scope explicit: sotorasib/adagrasib are not PDAC approvals; zenocutuzumab is NRG1-fusion-specific.

### Before Pipeline Use

1. Complete or relabel the Tier 1 `run_full` output.
2. Preserve final Tier 1 artifacts: `results_ranked.csv`, `run_manifest.json`, `enrichment_report.json`, logs, and exact command line.
3. Decide and document the KRAS G12D apo/ensemble source; keep the manifest quarantine until then.
4. Add prep warnings for ligand protonation/optimization fallbacks.
5. Add a PDB manifest validator before any p53 workflow can run.
6. Establish Git/source hygiene before more generated artifacts accumulate.

### Nice-To-Have After Blockers

1. Add a small regression test for `analyze_enrichment.py` using a synthetic CSV with known AUC/EF.
2. Add a row-count consistency check: intended enrichment set count vs current results count.
3. Add a `make audit-claims` or equivalent grep check for known-bad claim strings.
4. Create a `reports/` index that distinguishes evidence reports from draft planning notes.

## Safe-To-Share Checklist For `PLAN.md`

- [ ] Tier 0 wording matches the current self-dock report, or a new expanded Tier 0 report exists.
- [ ] p53 Y220C validation points to 9BR4, and any mention of 8A32 clearly says it is KVA/JC769, not rezatapopt.
- [ ] MRTX1133 is described as a terminated clinical study/preclinical proof-of-concept, with the ClinicalTrials.gov reason separated from secondary reporting.
- [ ] G12C drugs are scoped to FDA-approved indications and not implied as PDAC approvals.
- [ ] Zenocutuzumab is scoped to NRG1-fusion tumors.
- [ ] Dataset-size numbers are dated and source-specific: Enamine REAL Database vs REAL Space vs ZINC-22 2D/3D.
- [ ] BOINC Central is described as a feasible integration target, not a secured deployment.
- [ ] The document says supporting docs are background-only unless claim-verified.
- [ ] The document includes a short "not clinical advice / research plan only" note before public sharing.

## Checks Run During This Audit

- Broad `rg` stale-claim searches across `PLAN.md`, `PROJECT/`, and `sources/`.
- Exact line-reference searches for Tier 0, p53 PDB IDs, dataset-size claims, MRTX1133, FDA-approval scope, and known typo/citation issues.
- Static AST parse of Python files under `pancscan/`; all parsed successfully.
- CSV inspection of `pancscan/tier1/enrichment/enrichment_compounds.csv` and `pancscan/tier1/screen/run_full/results.csv`.
- Manual calculation of Tier 1 metrics from the current `results.csv`.
- Generated-artifact scan under `pancscan/`.
- Official-source spot checks using ACS, ClinicalTrials.gov, FDA, RCSB/data API, BOINC Central, OpenMM/OpenFE docs, Enamine, and ZINC-22.

## Source Links

- [ACS Cancer Facts & Figures 2026](https://www.cancer.org/research/cancer-facts-statistics/all-cancer-facts-figures/2026-cancer-facts-figures.html)
- [ACS Cancer Facts & Figures 2026 PDF](https://www.cancer.org/content/dam/cancer-org/research/cancer-facts-and-statistics/annual-cancer-facts-and-figures/2026/2026-cancer-facts-and-figures.pdf)
- [ACS pancreatic cancer survival rates](https://www.cancer.org/cancer/types/pancreatic-cancer/detection-diagnosis-staging/survival-rates.html)
- [ClinicalTrials.gov NCT05737706](https://clinicaltrials.gov/study/NCT05737706)
- [ClinicalTrials.gov NCT04585750](https://clinicaltrials.gov/study/NCT04585750)
- [FDA sotorasib + panitumumab CRC approval](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-sotorasib-panitumumab-kras-g12c-mutated-colorectal-cancer)
- [FDA adagrasib + cetuximab CRC approval](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-adagrasib-cetuximab-kras-g12c-mutated-colorectal-cancer)
- [FDA zenocutuzumab NSCLC/pancreatic adenocarcinoma approval](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-zenocutuzumab-zbco-non-small-cell-lung-cancer-and-pancreatic)
- [FDA zenocutuzumab cholangiocarcinoma approval](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-zenocutuzumab-zbco-advanced-unresectable-or-metastatic-cholangiocarcinoma)
- [FDA Bizengri drug snapshot](https://www.fda.gov/drugs/drug-trials-snapshots/drug-trials-snapshots-bizengri)
- [RCSB 7RPZ](https://www.rcsb.org/structure/7RPZ)
- [RCSB 8A32](https://www.rcsb.org/structure/8A32)
- [RCSB 9BR4](https://www.rcsb.org/structure/9BR4)
- [BOINC Central](https://boinc.berkeley.edu/central/)
- [About BOINC Central](https://boinc.berkeley.edu/central/about.php)
- [OpenMM running simulations/platforms](https://docs.openmm.org/latest/userguide/application/02_running_sims.html)
- [OpenFE installation docs](https://docs.openfree.energy/en/stable/installation.html)
- [Enamine REAL Database](https://enamine.net/compound-collections/real-compounds/real-database)
- [Enamine REAL quick facts](https://enamine.net/?catid=2&highlight=WyJxdWljayJd&id=1911%3Atest-real-compounds&view=article)
- [ZINC-22 JCIM paper](https://pubs.acs.org/doi/10.1021/acs.jcim.2c01253)
