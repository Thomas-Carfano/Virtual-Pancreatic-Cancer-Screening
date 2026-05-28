# Data dictionary

Definitions for every data file and column produced by PancScan, including units and how each
value is computed. All tabular files are UTF-8 CSV with a header row. See [METHODS.md](METHODS.md)
for the methodology and [README.md](README.md) for the project overview.

## Conventions & units

- **affinity / score** — AutoDock Vina predicted binding free energy, in **kcal/mol**. More
  negative = predicted tighter binding. Approximate (±~3 kcal/mol error); compare in aggregate,
  not by single-compound rank.
- **RMSD** — root-mean-square deviation between two 3D poses, in **ångström (Å)**; heavy atoms only,
  symmetry-corrected. Lower = closer to the reference (crystal) pose. <2 Å = successful redock.
- **SMILES** — canonical molecular structure string (RDKit canonicalization).
- **Broad ID** (`BRD-...`) — stable Broad Institute compound identifier (Drug Repurposing Hub).
- **PDB ID** — 4-character RCSB Protein Data Bank structure code (e.g. `7RPZ`).
- **CCD** — PDB Chemical Component Dictionary ligand code (e.g. `6IC` = MRTX1133; may be 5 chars).
- **ChEMBL ID** — stable identifier from the ChEMBL bioactivity database.
- **pChEMBL** — −log10(molar activity); pChEMBL ≥ 6 means ≤ 1 µM (potent).

---

## Input library — `libraries/repurposing_hub/compounds.csv`

The screened compound set: deduplicated, salt-stripped, MW-filtered Broad Drug Repurposing Hub.

| Column | Type | Description |
|---|---|---|
| `id` | string | Broad compound ID (`BRD-...`). Primary key. |
| `smiles` | string | Canonical SMILES (largest fragment; salts removed). |
| `label` | string | Drug name (`pert_iname` from the Repurposing Hub). |

---

## Screening results — `libraries/repurposing_hub/screen_*/results.csv`

One row per attempted compound (appended live; supports resume). `screen_KRAS_G12D/`,
`screen_PARP1/`, `screen_KRAS_G12V/` etc.

| Column | Type | Description |
|---|---|---|
| `id` | string | Compound ID (matches `compounds.csv`). |
| `smiles` | string | SMILES docked. |
| `label` | string | Drug name (or `active`/`decoy` in enrichment runs). |
| `prep_ok` | bool | Did 3D prep (protonation/embed/PDBQT) succeed? |
| `dock_ok` | bool | Did Vina dock successfully? If `False`, see `error`. |
| `affinity` | float (kcal/mol) | **Best (most negative) Vina score** across passes. The primary ranking value. |
| `affinity_mean` | float (kcal/mol) | Mean score across exhaustiveness passes. |
| `affinity_std` | float (kcal/mol) | Std-dev across passes (pose-search stability; large = undersampled). |
| `n_passes` | int | Number of docking passes that produced a score. |
| `affinities_by_pass` | string | Per-pass scores, `;`-separated. |
| `error` | string | Failure reason when `dock_ok=False` (else blank). |

### `results_ranked.csv`
Same columns, filtered to `dock_ok=True` and **sorted by `affinity` ascending** (best first). This
is the ranked screen output.

### `run_manifest.json`
Run metadata: `date`, `config` (full dock config used), `exhaustiveness_schedule`, `compounds_total`,
`succeeded/failed`, `ranked_total`, `wall_seconds_this_run`, and `best` (top-ranked compound record).

---

## Curated candidates — `candidates/`

Human-facing deliverable. See `candidates/README.md` and per-target `HANDOFF.md`.

### `candidates/<TARGET>/top50.csv` and `top25_selective.csv`
| Column | Type | Description |
|---|---|---|
| `rank` | int | 1 = best predicted binder. |
| `drug_name` | string | Common drug/compound name. |
| `broad_id` | string | Broad compound ID. |
| `smiles` | string | Canonical SMILES. |
| `affinity_kcal_mol` | float | Best Vina score (kcal/mol). |

`top50.csv` = overall top 50 for that target. `top25_selective.csv` = top 25 that are **NOT** also
high-ranked on the other target (more target-specific leads).

### `candidates/cross_target_overlap.csv`
Drugs in the top-100 of **both** KRAS G12D and PARP1 (often generic shape-fitters; includes
olaparib/EB-47 as sanity controls).

| Column | Type | Description |
|---|---|---|
| `drug_name`, `broad_id`, `smiles` | string | Compound identity. |
| `g12d_affinity` | float (kcal/mol) | Score vs KRAS G12D. |
| `parp1_affinity` | float (kcal/mol) | Score vs PARP1. |

---

## Target validation — `tier2/targets/<TARGET>/validation_report.json`

Native-redock validation for each screening target.

| Field | Type | Description |
|---|---|---|
| `target` | string | Internal target label. |
| `cif` | string | Source mmCIF filename (RCSB). |
| `chain` | string | Chain(s) used as receptor (e.g. `A`, or `A,C` for tri-complexes). |
| `ligand_ccd` | string | PDB CCD code of the native ligand redocked. |
| `receptor_residues` | int | Number of residues in the prepared receptor. |
| `ligand_atoms` | int | Heavy-atom count of the native ligand. |
| `template_prep` | bool | Bond-order template prep succeeded (vs fallback). |
| `redock_score_kcal_mol` | float | Vina score of the redocked native ligand. |
| `redock_heavy_rmsd_angstrom` | float (Å) | Pose accuracy vs crystal. <2 Å = pass. |
| `passed` | bool | RMSD < 2 Å AND score < −7 kcal/mol. |

### `tier2/targets/<TARGET>/dock_config.json`
Reusable docking configuration: `receptor_pdbqt` (path), `box` (`center_x/y/z`, `size_x/y/z` in Å),
and `vina` parameters (`exhaustiveness`, `num_modes`, `cpu`, `seed`).

---

## Enrichment reports — `*/enrichment_report.json`

Blind-test validation that the engine separates known binders from decoys.

| Field | Type | Description |
|---|---|---|
| `n_actives` | int | Known active compounds docked. |
| `n_decoys` | int | Property-matched decoy compounds docked. |
| `n_failed_docks` | int | Compounds that failed prep/dock (excluded). |
| `roc_auc` | float (0–1) | Area under ROC curve. 0.5 = random, 1.0 = perfect ranking. |
| `ef_1pct` / `ef_5pct` / `ef_10pct` | float (×) | Enrichment factor in top 1/5/10% (1.0 = random). |
| `bedroc_alpha20` | float (0–1) | Early-recognition-weighted enrichment (α=20). |
| `mean_affinity_actives` | float (kcal/mol) | Mean score of actives. |
| `mean_affinity_decoys` | float (kcal/mol) | Mean score of decoys. |
| `separation_kcal_mol` | float | decoy_mean − active_mean (positive = actives bind better). |
| `verdict` | string | Plain-language interpretation (strong/modest/weak/none). |

---

## Tier 0 reports — `reports/tier0_report.json`

Original proof-of-concept: re-dock MRTX1133 into KRAS G12D (PDB 7RPZ). Fields include the
acceptance criteria (`ligand_code_6IC_present`, `rmsd_under_2_angstrom`, etc.), the docking box,
all Vina pose scores, `rmsd_top_pose_vs_crystal_angstrom`, and overall `passed`.

---

## Provenance of identifiers (for linking / enrichment by crawlers)

- Compounds → resolvable at the Broad Drug Repurposing Hub and (via name/SMILES) PubChem/ChEMBL.
- Targets → `https://www.rcsb.org/structure/<PDB_ID>`.
- Ligand CCDs → `https://www.rcsb.org/ligand/<CCD>`.
- ChEMBL targets used: KRAS = `CHEMBL2189121`, PARP1 = `CHEMBL3105`.
