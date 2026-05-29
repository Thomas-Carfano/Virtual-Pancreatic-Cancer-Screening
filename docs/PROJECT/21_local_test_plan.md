# Local Test Plan — Run the Science End-to-End Before Submitting Anywhere

> Goal: prove the pipeline produces real, validated science on one MacBook before we point any volunteer compute at it. Everything in this plan runs on the user's MacBook Pro M4 Max (128 GB RAM, 16 cores, Apple Silicon GPU, macOS 26.5). No cloud required for tier-1 validation; tier-2 expansion uses cloud sparingly.

## What "test locally" actually means

The full PancScan@home pipeline has 6 stages (`PROJECT/20_synthesis.md`). Not all of them run on a single laptop, even a powerful one. Here's the mapping:

| Stage | Tool | Runs on M4 Max? | If yes, how |
|---|---|---|---|
| 1. Target ensemble (AlphaFold3/Boltz-1 + AlphaFlow + MD) | OpenMM, Boltz-1 | **Yes (mostly)** | **OpenMM has NO native Apple Metal backend** — upstream platforms are CUDA, HIP, OpenCL, CPU, Reference. On M-series Macs use the **OpenCL platform** or the third-party `philipturner/openmm-metal` plugin (translates OpenCL kernels to Metal). Boltz-1 via PyTorch MPS works. |
| 2. Active-learning virtual screening (Vina + Uni-Dock + MolPAL) | AutoDock Vina + RDKit | **Yes** | Vina is C++/native, 16 cores; MolPAL is Python |
| 3. GNINA CNN rescore | GNINA | **Hard** | CUDA-specific; runs via Docker (slow on Mac) — workaround below |
| 4. Boltz-2 affinity | Boltz-2 | **Yes (with caveats)** | PyTorch MPS works for most ops; rough edges on `linalg_svd` and float64 may force CPU fallback for some inputs |
| 5. Short MD validation | OpenMM | **Yes (via OpenCL or metal plugin)** | Same caveat as Stage 1 — use OpenMM OpenCL platform or `openmm-metal` plugin |
| 6. OpenFE RBFE | OpenFE | **Native arm64; no GPU acceleration on Apple Silicon** | OpenFE installs cleanly on osx-arm64 (an earlier draft erroneously claimed Rosetta 2 was required — that's not true). The real constraint is that OpenFE's GPU-accelerated FEP backend is CUDA-only; on Apple Silicon it falls back to OpenMM's CPU/OpenCL platform, so wall-time per lead is multiple hours to a day. Cloud GPU (~$50–100/lead) is still more efficient at Tier 3. |

**Verdict:** the entire pipeline can run locally, with Stage 3 (GNINA) being the only painful spot. For the initial test we can substitute GNINA's CNN rescore with **Vina's built-in scoring + Vinardo + Smina/Vina hybrid scoring**, which captures most of the value at <2× cost. Tier-2 we either move GNINA to a Docker x86_64 image (Rosetta translation, slow but functional) or rent a small cloud GPU for one batch as a sanity check.

## Tier 0 — the smallest possible end-to-end test (~1 day of work, ~1 hour of compute)

This is the minimum proof that the science works. Everything beyond is just scaling.

### Setup

1. **Conda/mamba** — install via Homebrew Cask: `brew install --cask miniforge` (note: Miniforge is distributed as a Cask, not a Formula; conda-forge upstream actually recommends the official PKG installer from https://github.com/conda-forge/miniforge over Homebrew because Homebrew auto-updates can destroy environments). Use mamba for speed.
2. **Make a project conda env**:
   ```bash
   mamba create -n pancscan python=3.11 -y
   mamba activate pancscan
   mamba install -c conda-forge -c bioconda \
     openbabel rdkit autodock-vina pymol-open-source openmm \
     numpy pandas matplotlib jupyterlab biopython mdanalysis -y
   pip install meeko prolif spyrmsd
   ```
3. **Verify Vina runs**: `vina --help` should return the CLI.
4. **Verify OpenMM platforms**: `python -c "from openmm import Platform; [print(Platform.getPlatform(i).getName()) for i in range(Platform.getNumPlatforms())]"` — on stock conda-forge install on Apple Silicon you should see `CPU`, `OpenCL`, `Reference`. **There is no native `Metal` platform in upstream OpenMM.** If you install the third-party `philipturner/openmm-metal` plugin you'd see an `OpenCL`/`Metal` entry; otherwise use `OpenCL` for GPU acceleration on M-series Macs.

### Test target

- **PDB 7RPZ** — KRAS G12D + MRTX1133 (full-length, GDP-bound, Switch-II pocket open).
- Source: `wget https://files.rcsb.org/download/7RPZ.pdb` (no auth, public).
- Preparation: strip waters, retain Mg²⁺ + GDP, separate ligand (MRTX1133) into its own .sdf, convert protein to .pdbqt via Meeko.

### Test ligand set

| Ligand | Why | Source |
|---|---|---|
| **MRTX1133** (native, extracted from 7RPZ) | Positive control — must re-dock <2 Å | 7RPZ |
| **Sotorasib (AMG 510)** | KRAS G12C-specific — should NOT bind G12D pocket well; tests selectivity | PDB 6OIM |
| **Adagrasib (MRTX849)** | Same as sotorasib — G12C control | PDB 6UT0 |
| **Imatinib** | Random kinase inhibitor; should rank low | PubChem CID 5291 |
| **Aspirin** | Decoy negative; should rank near worst | PubChem CID 2244 |
| **~995 DUD-E decoys** | Property-matched decoys to MRTX1133 | DUD-E auto-generator |

Total: ~1,000 ligands. At ~5 sec/ligand × 1 conformation on Vina with 16 cores, the full run is **~10 minutes**.

### What success looks like

1. **MRTX1133 self-docking RMSD < 2.0 Å** vs the crystal pose. If this fails, the pipeline is broken — stop and debug.
2. **MRTX1133 ranks in top 1%** (top 10 of 1000) of the screened set.
3. **Aspirin ranks below the median.** If aspirin scores high, our scoring is broken or the pocket is too permissive.
4. **Sotorasib + adagrasib score lower than MRTX1133** — they're built for G12C's covalent cysteine handle, not G12D's aspartate. (They may still rank high because the pocket is similar; observe.)
5. **Visualize MRTX1133 pose in PyMOL** — confirm:
   - Salt bridge to **D12** (the mutant aspartate) — the defining interaction
   - H-bond network with **Y96, H95** (Switch-II)
   - No steric clash with G10/T58 floor

If all 5 pass, the local pipeline works and we can expand.

### Deliverables of Tier 0

- A Jupyter notebook (`pancscan/notebooks/tier0_kras_g12d_smoke_test.ipynb`) that:
  1. Downloads PDB 7RPZ and prepares it
  2. Builds the 1,000-ligand test set
  3. Runs Vina with appropriate grid
  4. Reports scores + RMSD for positive controls
  5. Renders the top pose in 3D
- A short pass/fail report at `pancscan/reports/tier0_smoke_test.md`

## Tier 1 — small-but-real screen (~1 week of work, ~1 day of compute)

Once Tier 0 passes, expand to:

- **Targets:** add KRAS G12D apo + 1–2 cryptic-pocket-open conformations from short MD (Stage 1). **⚠️ PDB ID for "G12D apo" is NOT yet selected — do not default to 8AZV (which is actually KRAS + BI-2865 inhibitor complex, NOT apo), 7T47 (KRAS G12D + MRTX1133 + GppCp, holo not apo), 4DSO (Ras + GSP/GTP-analog + benzamidine, not apo), or stripped 8AZY (G12D + BI-2865 — stripping the ligand leaves a cavity-conditioned receptor, NOT a true apo state).** A proper G12D apo source must be selected via the structure-selection SOP in `sources/verifications/structure_manifest.csv` — likely generating MD-derived apo conformers rather than relying on a holo crystal with the ligand removed.
- **Ligands:** ZINC22 "in-stock, lead-like" subset (~5 million compounds).
- **Pipeline stages:** Vina docking → top 1% → Vina rescore with Vinardo → top 0.1% → Boltz-2 affinity prediction.
- **Active learning:** dock random 1% (50K), train a Chemprop GNN surrogate, predict top 1% of remaining 99%, dock those.
- **Expected runtime:** 16 cores × 24 hr = ~384 core-hours; with active learning we touch ~100K ligands directly → ~2.5 days wall-clock on the M4 Max.
- **Validation:** MRTX1133 + RMC-9805 still in top 1% across the larger set. Any "fragment hits" — molecules sharing the D12 salt-bridge + Switch-II H-bond pattern — flagged for follow-up.

### Deliverables of Tier 1

- A reproducible pipeline: `pancscan/pipelines/tier1_zinc22_lead_like.py`
- A hit-list .parquet file with top 5,000 ranked compounds + their poses
- A brief writeup at `pancscan/reports/tier1_results.md`

## Tier 2 — short MD validation of top hits (~1 week, ~3 days of compute)

For the top ~100 Tier-1 hits:
- Build an OpenMM system: KRAS G12D + ligand + Mg²⁺ + GDP + solvent box
- Run 50 ns MD per complex on Apple Metal (~6 hr per complex; in 100s of complexes that's 600 GPU-hr)
- Compute MM-GBSA or simple binding pocket residence time
- Rank by stability + favorable interaction patterns
- Top 10–30 → flag for free-energy validation in Tier 3

## Tier 3 — gold-standard binding free energies (cloud or LANCs)

For the top 10–30 leads:
- OpenFE relative binding free energy (RBFE) against MRTX1133 as reference
- Each calculation ~12–48 GPU-hr; on M4 Max via Metal it's slow but works (~48–96 hr each)
- For 20 leads = ~3–8 days continuous; or move to a single rented H100 instance for ~$50–100 total
- This is the only stage where renting cloud genuinely beats the M4 Max

## Tier 4 — extending beyond KRAS G12D (only after Tier 0–3 prove out)

Same pipeline, swap targets:
- KRAS G12V (PDB to identify), G12R, Q61H
- Mutant p53 hotspots: Y220C (PDB 8A32 — rezatapopt complex), R175H, R273H, R248Q
- Each new target is ~1 person-week of work for someone who's been through the first cycle.

## How this maps to the eventual BOINC project

The local pipeline IS the BOINC app. Once Tier 0+1 work locally, packaging it as a Docker container and a BOINC workunit is mostly a system-integration exercise, not a science exercise:

- The `vina dock --receptor X --ligand Y` invocation becomes a workunit's compute step
- The 1,000-ligand batch becomes the workunit input
- The score JSON becomes the workunit output
- The validator becomes "did this volunteer's scores match a trusted re-run within tolerance?"
- The assimilator appends scores to the central hit DB

So the bulk of the *risk* in this project is in the local pipeline. Once that's right, the BOINC packaging is real engineering but well-understood.

## Hardware we have vs the typical volunteer host

For context (`PROJECT/03_boinc.md`): the median BOINC volunteer in 2026 has ~4–8 CPU cores, 8–32 GB RAM, often a mid-range GPU. The user's M4 Max is **~3–4× more capable** than median in everything except discrete GPU compute (where it's competitive with a mid-range NVIDIA card via MPS, but lacks CUDA-specific kernels).

Implication: anything that runs comfortably on the M4 Max will run on most volunteers' hardware. Anything that struggles here (e.g., AlphaFold3 inference on big systems, FEP on slow Mac MPS) will be a problem on volunteers and we'll need to design workunits with a memory/runtime cap.

## What happens if Tier 0 fails

That's *the* high-value information. The most common failure modes:

| Symptom | Likely cause | Fix |
|---|---|---|
| MRTX1133 docks but RMSD > 2 Å | Wrong protonation or wrong box | Use PROPKA / ProtoSS for protein protonation; tighten box around native ligand |
| MRTX1133 scores well but pose is upside-down | Vina scoring favors lipophilic contacts over the D12 salt bridge | Add explicit H-bond constraint or use GNINA CNN rescore |
| Aspirin scores top-10 | Pocket box too generous; permissive scoring | Restrict search box; use exhaustiveness 16+ |
| All ligands score similar | GDP/Mg²⁺ stripped accidentally | Re-check structure prep |
| OpenMM fails on Metal | Platform mismatch | Fall back to OpenCL or CPU; will be slower but always works |

## Open questions before starting

1. **Conda vs venv vs Pixi.** Conda/mamba is industry standard for Python+native binaries. Pixi is newer + faster but less battle-tested. Recommend **mamba** (via miniforge) for now.
2. **PyMOL vs ChimeraX vs Mol\*.** PyMOL has the best scripting; ChimeraX renders better; Mol* is web-only and great for sharing. Recommend **PyMOL** for scripting and **ChimeraX** for hero renders.
3. **Where to put the working directory.** Suggest `/Volumes/Storage April 2026/PancreaticCancer/pancscan/` — same volume as everything else. ~168 GB free is plenty for Tier 0–2; Tier 3+ may want SSD speed for FEP I/O (worth moving to internal disk).

## Next concrete step

If the user is ready to start:

1. `brew install miniforge` (one command)
2. Create the `pancscan` env (one block)
3. Download PDB 7RPZ
4. Run a 5-minute Vina self-docking of MRTX1133 to confirm the toolchain works

That's the floor. Everything else builds from there.
