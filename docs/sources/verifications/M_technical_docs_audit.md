# M — Technical Docs Audit: 21_local_test_plan.md + 22_boinc_technical_spec.md

**Date:** May 22, 2026
**Files audited:**
- `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/21_local_test_plan.md`
- `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/22_boinc_technical_spec.md`

**Scope:** Verify every concrete technical claim — tool capabilities, version numbers, hardware specs, runtime estimates, license claims, URLs. Apple Silicon claims are highest-priority since they drive the user's actual machine setup.

**Legend:**
- ✅ Verified
- ⚠️ Partially verified / important caveat
- ❌ False / misleading
- 🔵 Unable to verify

---

## Part 1 — `21_local_test_plan.md` (Apple Silicon + Local Pipeline)

### Apple Silicon platform claims (highest-stakes section)

#### 1. "OpenMM has Apple Metal backend" (lines 11, 15, 16)
**Status: ❌ Misleading.**

Upstream OpenMM platforms are **CUDA, HIP, OpenCL, CPU, Reference** — there is **no native "Metal" platform** in the official OpenMM distribution. Apple Silicon users run OpenMM via the **OpenCL** platform (which Apple still provides via its deprecated-but-functional OpenCL compatibility layer) or **CPU**.

A third-party plugin (`philipturner/openmm-metal`) does exist and adds a "Metal" platform — but it works by translating OpenCL kernels to Apple's Metal API via Apple's `cl2Metal` (i.e., it is functionally OpenCL-on-Metal, not native Metal kernels). Performance roughly tracks OpenCL on Apple GPUs; not the "free 2-3× speedup" implied by "Metal backend." The plugin's v1.0 tag works but newer versions fail tests on Intel Macs.

The verification command in the doc (line 37) expecting "Metal" in the platform list will **return False** on a stock conda-forge OpenMM install. The user will see `Reference`, `CPU`, `OpenCL` (if drivers OK). Action: rewrite as "OpenMM via OpenCL on Apple Silicon (or experimental third-party Metal plugin)."

Sources:
- https://docs.openmm.org/latest/userguide/library/04_platform_specifics.html
- https://github.com/philipturner/openmm-metal
- https://github.com/openmm/openmm/issues/3639

#### 2. "Boltz-1/2 via PyTorch MPS works (slower than NVIDIA but usable)" (lines 11, 14)
**Status: ⚠️ Partially verified.**

MPS support **exists via a community PR** (jwohlwend/boltz #527 — colbyford). Caveats from that PR and from Rowan's Boltz-2 FAQ:
- At the time of the Rowan FAQ (mid-2025): "no support for Apple Silicon MPS hardware acceleration" — fixed by the PR after that
- The PR notes that `aten::linalg_svd` falls back to CPU on MPS, `pin_memory` is unused, and some `float64` ops are not supported on MPS
- It "folds successfully" but is not a first-class supported configuration

So "works (slower)" is true with the PR merged, but "PyTorch MPS works" understates the friction. The user will hit op-not-supported fallbacks. Sources:
- https://github.com/jwohlwend/boltz/pull/527
- https://www.rowansci.com/blog/boltz2-faq
- https://macinchem.org/2025/06/17/boltz-on-apple-silicon/

#### 3. "GNINA CUDA-specific; runs via Docker (slow on Mac)" (line 13)
**Status: ✅ Verified.**

GNINA requires CUDA (compute capability ≥ 3.5) and there is no native Mac/Metal port. Docker image exists but on Apple Silicon would require x86_64 emulation (Rosetta 2 for Docker), no GPU access from Mac to Docker, so it's CPU-only emulated — very slow. The doc's recommendation to substitute Vinardo/Smina hybrid scoring locally is sensible. Source: https://github.com/gnina/gnina

#### 4. "AutoDock Vina runs on Apple Silicon natively" (implicit from line 12)
**Status: ✅ Verified.**

`vina_1.2.6_mac_aarch64` binaries are officially built by GitHub Actions and shipped via Releases (PR #340 era). Native ARM64 supported. Source: https://github.com/ccsb-scripps/AutoDock-Vina/releases

#### 5. "OpenFE RBFE on M4 Max via Metal slow but works (~48-96 hr each)" (lines 16, 111)
**Status: ❌ False (Metal claim) / ⚠️ Apple Silicon support is limited.**

Per OpenFE official installation docs: **"Installing on Macs with Apple Silicon requires creating an x86_64 environment, as one of the requirements is not yet available for Apple Silicon."** OpenFE 1.7.0+ made CUDA the **default** platform. There is **no Metal backend** for OpenFE — it relies on OpenMM, and OpenMM has no Metal backend (see #1 above).

So on M4 Max, you run OpenFE via Rosetta 2 (x86_64 emulation), on the OpenMM CPU platform (or OpenCL via emulation, even slower). That's not "slow but works via Metal" — it's emulated x86 + CPU-only OpenMM. Realistic per-edge time will be **substantially worse than 48-96 hr** on a real GPU edge (3-6 hr on H100); CPU-only on emulated x86_64 could be 5-10× slower again. Plausible: many days to a week per edge.

The doc's recommendation to rent an H100 instance for Tier 3 (line 112) is the right call; the "Metal" claim should be removed entirely.

Source: https://docs.openfree.energy/en/v1.2.0/installation.html

#### 6. "Apple Metal backend; consumer-Mac sweet spot" for MD (line 15)
**Status: ❌ Misleading.**

Same root issue as #1: no Apple Metal backend exists in OpenMM. On Apple Silicon, MD runs via OpenCL (works, ~1.5-3× slower than equivalent NVIDIA GPU based on community benchmarks) or CPU. Calling Mac a "consumer-Mac sweet spot" for MD overstates it — Macs are *adequate* for short MD, but a $400 used RTX 3060 would beat the M4 Max GPU at OpenMM throughput.

#### 7. "MD 100 ns ~12 hr on consumer GPU" (Tier 2, ~line 102 implication)
**Status: ⚠️ Plausible but system-dependent.**

The doc says 50 ns / 6 hr per complex on Apple Metal (line 102). For a small ligand-protein system (KRAS = ~170 residues + ligand + solvent box ≈ 30-50K atoms), the SaladCloud OpenMM benchmark on consumer GPUs shows 200-400 ns/day for similar systems on RTX 3060/4060-class hardware. Apple M4 Max GPU is roughly RTX 3060-level for OpenCL workloads, so 50 ns / 6 hr (= 200 ns/day) is **plausible** for a moderate-size protein-ligand system. ✓

Source: https://blog.salad.com/openmm-gpu-benchmark/

### Installation / packaging claims

#### 8. `brew install miniforge` (line 26, 162)
**Status: ❌ Wrong command syntax.**

Miniforge is a **Cask** in Homebrew, not a Formula. Correct command: `brew install --cask miniforge`. Without `--cask`, the install will fail with "No available formula with the name 'miniforge'."

Also note: the **Miniforge developers do not recommend installing via Homebrew** because Homebrew's auto-update of miniforge can destroy all conda environments. The conda-forge team recommends the official PKG installer (signed/notarized with NumFOCUS certificates as of 2026). The doc should warn about this.

Sources:
- https://formulae.brew.sh/cask/miniforge
- https://github.com/conda-forge/miniforge/issues/576

#### 9. `mamba install -c conda-forge -c bioconda openbabel rdkit autodock-vina pymol-open-source openmm` (line 31)
**Status: ✅ Verified (mostly conda-forge, not bioconda).**

All packages exist on conda-forge or bioconda:
- `openbabel` — conda-forge (yes) and bioconda
- `rdkit` — conda-forge (canonical home)
- `autodock-vina` — bioconda ✓ (https://anaconda.org/bioconda/autodock-vina)
- `pymol-open-source` — conda-forge
- `openmm` — conda-forge (canonical home — note: bioconda does NOT host openmm)

The command works because `-c conda-forge -c bioconda` allows packages from either. The channel ordering with conda-forge first is correct best practice. ✓

#### 10. `pip install meeko prolif spyrmsd` (line 34)
**Status: ✅ Verified.** All three are on PyPI. https://pypi.org/project/meeko/, https://pypi.org/project/prolif/, https://pypi.org/project/spyrmsd/

#### 11. PDB 7RPZ download URL `https://files.rcsb.org/download/7RPZ.pdb` (line 42)
**Status: ✅ Verified.** URL works; returns the X-ray crystal structure of KRAS G12D + MRTX-1133, 1.30 Å resolution, includes GDP and Mg²⁺. Sources: https://www.rcsb.org/structure/7RPZ; https://www.rcsb.org/docs/programmatic-access/file-download-services

#### 12. DUD-E "auto-generator for property-matched decoys" (line 54)
**Status: ✅ Verified.** Online DUD-E decoy generator at http://decoys.docking.org accepts any user-supplied ligand list and generates property-matched decoys. (Original DUD/DUD-E papers by Mysinger, Carchia, Irwin & Shoichet.)

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3405771/

### Structure / target claims

#### 13. PDB 7RPZ — "KRAS G12D + MRTX1133 (full-length, GDP-bound, Switch-II pocket open)" (line 41)
**Status: ⚠️ Mostly correct, minor nuance.**

7RPZ is KRAS G12D + MRTX-1133 + GDP + Mg²⁺, 1.30 Å, deposited 2020. "Full-length" — the construct in 7RPZ is the catalytic domain (residues ~1-169), which is the standard "full-length minus HVR" used in essentially all KRAS crystal structures. Calling it "full-length" is shorthand that's accepted in the field; pedantically the HVR (hypervariable region, residues 170-188) is not in the structure. Acceptable for the audience.

#### 14. PDB 8AZV "KRAS G12D apo" (line 86)
**Status: ❌ False.**

8AZV is **KRAS (not specifically G12D) in complex with BI-2865**, not an apo structure. The 8AZV series (8AZR, 8AZV, 8AZX, 8AZY=G12D+BI-2865, 8AZZ=G12V+BI-2865) are all BI-2865 complexes. There is no "8AZV apo G12D" — this is a factual error. **Alternative apo G12D structures**: 4DSO (G12D-GDP, apo of pocket), or use 7T47 (KRAS G12D + GppCp + MRTX-1133) and strip the ligand. The doc's parenthetical alternative "7T47" is itself a holo MRTX-1133 structure (G12D + GppCp + MRTX1133), not apo.

The correct citation pattern for "G12D apo" depends on what "apo" means — strictly GDP-bound without inhibitor: many structures (4DSO, 4OBE, etc.). Just-protein apo (no nucleotide): very rare for KRAS due to crystallization.

Sources:
- https://www.rcsb.org/structure/8AZV
- https://www.rcsb.org/structure/8AZY (the G12D one with BI-2865)
- https://www.rcsb.org/structure/7T47

#### 15. PDB 6OIM (sotorasib/AMG 510 + KRAS G12C) (line 51)
**Status: ✅ Verified.** Crystal structure of human KRAS G12C covalently bound to AMG 510. https://www.rcsb.org/structure/6OIM

#### 16. PDB 6UT0 (adagrasib/MRTX849 + KRAS G12C) (line 52)
**Status: ✅ Verified.** Crystal structure of clinical development candidate MRTX849 covalently bound to KRAS G12C in the switch-II pocket. https://www.rcsb.org/structure/6UT0

### Performance / runtime claims

#### 17. "~5 sec/ligand × 1 conformation on Vina with 16 cores" → "~10 min for 1000 ligands" (line 56)
**Status: ⚠️ Order-of-magnitude OK, but ambiguous wording.**

The "5 sec/ligand" figure for Vina is roughly right for a typical drug-like molecule with default exhaustiveness=8 on a single CPU thread. With 16 cores in parallel: 1000 × 5 = 5000 sec single-threaded, ÷ 16 ≈ 312 sec ≈ 5 min. Or if "5 sec on 16 cores" is meant per-ligand, then 1000 × 5 = 5000 sec ≈ 83 min. The "10 min" total in the doc is consistent with the first interpretation (5 sec per ligand single-threaded, parallelized across 16 cores). Plausible for small ligands; will run longer for >40-atom ligands or larger search boxes.

#### 18. "Tier 1 ~384 core-hours wall-clock on M4 Max, ~2.5 days" (line 89)
**Status: ⚠️ Math is approximately consistent.**

16 cores × 24 hr = 384 core-hours. 384 core-hours / 16 cores = 24 hr wall-clock, but the doc says "~2.5 days wall-clock" because of active learning (Chemprop training, batched re-docking, top-1% extraction). Reasonable for a screening workflow with AL overhead. The 100K-ligand effective screen (vs 5M nominal) implies ~98% of compounds are predicted-not-docked, which matches MolPAL-style AL workflows.

#### 19. "Median BOINC volunteer hardware in 2026: ~4-8 CPU cores, 8-32 GB RAM, often a mid-range GPU" (line 136)
**Status: 🔵 Unable to verify precisely.**

BOINC project stats sites (boincstats.com, gridcoinstats.eu) report aggregate hardware but no single authoritative "median BOINC volunteer in 2026" exists in public sources. Order of magnitude is reasonable (most volunteers run on home PCs which in 2026 are 6-16 cores Intel/AMD or M-series Mac; 16-32 GB RAM is typical for modern home builds). The "mid-range GPU" claim is harder — many volunteers run CPU-only.

#### 20. "M4 Max is ~3-4× more capable than median in everything except discrete GPU compute" (line 136)
**Status: ⚠️ Defensible but unverifiable claim.**

M4 Max has 16 cores (12P+4E), 128 GB RAM, ~38 TOPS NPU, ~14 TFLOP GPU. Versus a median home PC with 8 cores, 16-32 GB RAM, and an RTX 4060 (~15 TFLOP), the M4 Max is roughly 2× on CPU (more cores + higher per-core), 4× on RAM, comparable on raw GPU TFLOPS but lacks CUDA/cuDNN kernels and is OpenCL-only. "3-4× more capable" is generous on the CPU side; the GPU caveat is well-flagged.

### Other claims in 21_local_test_plan.md

#### 21. "Conda/mamba is industry standard for Python+native binaries. Pixi is newer + faster but less battle-tested" (line 154)
**Status: ✅ Fair assessment.** Conda/mamba (via miniforge) is indeed the de facto standard for cheminformatics/structural biology Python stacks. Pixi is real and gaining adoption but younger.

#### 22. "PyMOL has the best scripting; ChimeraX renders better; Mol* is web-only" (line 155)
**Status: ✅ Reasonable summary.** Mol* runs in browser (web-only or web+desktop bundles); PyMOL has decades of script library; ChimeraX is the successor to Chimera with improved rendering and is open-source academic.

---

## Part 2 — `22_boinc_technical_spec.md` (BOINC Platform Synthesis)

### BOINC Central claims (Section 1)

#### 23. "BOINC Central supports Docker-packaged applications and AutoDock as of March 2026" (lines 23-26)
**Status: ✅ Verified.**

BOINC Central is operated by BOINC at Berkeley and uses BUDA (BOINC Universal Docker App) framework for Docker-based science apps. Currently supports AutoDock4, Vina, and Vinardo. Boolean Chains and Cislunar Orbit Stability Analyzer projects used BUDA. Source: https://boinc.berkeley.edu/central/

#### 24. Reference to `marius311/boinc-server-docker` (implied/external)
**Status: ✅ Verified — repo exists.** Multi-container Docker BOINC server, Debian Stretch + PHP 7 + MariaDB 10. Source: https://github.com/marius311/boinc-server-docker

### Work-unit shape claims (Section 2)

#### 25. "CPU lane Vina: ~500 ligands, 30-90 min, ~5 MB in / 0.5 MB out" (line 36)
**Status: 🔵 Defensible engineering estimate; not a benchmark.**

The doc itself flags these as "engineering estimates, not benchmarks" (header of §4). Math sanity:
- 500 ligands × ~5 sec/ligand (single core) = 2500 sec = ~42 min ✓ in the 30-90 min window for typical hosts
- Sticky-file reuse: receptor grid ~5-10 MB, shared once → per-WU bandwidth ~0.5-2 MB for ligand batch only ✓
- Output ~0.5 MB: top-N poses + scores in compressed JSON/SDF, plausible

These are sensible defaults for a BOINC CPU lane.

#### 26. "GPU lane: ~5,000 ligands, 10-30 min, ~20 MB in / 1 MB out" (line 36)
**Status: 🔵 Defensible.** Vina-GPU 2.1 achieves ~21× speedup on average, ~50× max. So 5000 ligands × 0.1-0.25 sec/ligand on GPU ≈ 500-1250 sec = 8-21 min. ✓ Source: https://www.biorxiv.org/content/10.1101/2023.11.04.565429v1

### Compute budget claims (Section 4)

#### 27. "Validation burn-in: 50K ligands × 2 targets × quorum 2 = ~5K CPU-hr" (line 53)
**Status: ⚠️ Math close.**

50K × 2 = 100K ligand-target pairs × quorum 2 = 200K dockings. At 5 sec/ligand single-core = 10⁶ sec = 277 CPU-hours. With exhaustiveness=16 and larger drug-like ligands, 5× slower → ~1400 CPU-hr. To reach 5000 CPU-hr requires ~25 sec/ligand single-core or larger ligands. The 5K figure is in the right ballpark for the described scale **if** you assume harder/slower ligands. ⚠️ Worth noting it's at the high end.

#### 28. "Production Pilot 1: 250K ligands × 3 targets = ~25-35K CPU-hr" (line 54)
**Status: ⚠️ Math close on similar assumptions.** 750K dockings × ~120 sec/ligand single-core = 25,000 CPU-hr ✓ if ligands are larger/slower. Same caveat — these are upper-bound estimates.

#### 29. "300-1000 CPU volunteers + 50-150 GPU volunteers; ~1-2 weeks wall time" (line 59)
**Status: ✅ Plausible.** At 3000 donated core-hours/day (300 active volunteers × 10 hr/day donated): 25,000 CPU-hr ÷ 3000 = 8.3 days. So 1-2 weeks is consistent. ✓

### Validation layer claims (Section 5)

#### 30. PDB 6GJ7 as orthogonal target (line 70)
**Status: ✅ Verified.**

6GJ7 is "Crystal structure of KRAS G12D (GPPCP) in complex with 22" — referred to in literature as a switch-II pocket structure with a distinct ligand class from MRTX1133. Useful as orthogonal validation. Source: https://www.rcsb.org/structure/6GJ7

#### 31. TCGA-PAAD "185 cases / 12,853 files" (line 86)
**Status: ✅ Verified (185 cases); ⚠️ file count unverified.**

TCGA-PAAD has 185 patients / 186 carcinomas — confirmed across multiple sources. The "12,853 files" figure is the GDC file count for TCGA-PAAD; not independently verified in this audit but consistent with prior audits in the project. Important caveat from the literature: ~19% of TCGA-PAAD "RNA-seq profiles" correspond to non-PDAC neoplasms or normal/inflamed pancreas — needs curation per the Cancer Cell paper. https://pubmed.ncbi.nlm.nih.gov/30669703/

#### 32. "CPTAC PDAC via PDC (~29 TB managed per ICF)" (line 87)
**Status: 🔵 Unable to verify in this audit.**

The doc itself flags that the "70 TB" external-report figure was downgraded to "29 TB managed per ICF" based on audit 23. Not directly verifiable in public web sources in this round; defer to prior audit.

#### 33. DepMap 24Q2 "23.31 GB, CC BY 4.0" (line 88)
**Status: ⚠️ Partially verified.**

DepMap 24Q2 Public release is real, CC BY 4.0 confirmed. The exact 23.31 GB figure is not directly stated in DepMap's release page but is plausible for the full release tarball. Source: https://forum.depmap.org/t/announcing-the-24q2-release/3312

#### 34. AACR Project GENIE pancreatic portal (line 90)
**Status: ✅ Verified.**

AACR Project GENIE has a pancreatic cancer cohort: BPC Pancreas v1.0-public (1,109 patients); the public release 18.0 includes 10,684 pancreatic samples from 10,227 patients. KRAS, TP53, CDKN2A, SMAD4 are the most frequently mutated. Source: https://www.aacr.org/professionals/research/aacr-project-genie/

### License claims (Section 8)

#### 35. "AutoDock Vina 1.2.x — Apache 2.0" (line 132)
**Status: ✅ Verified.** Vina 1.2 source code released under Apache License v2.0. Source: https://github.com/ccsb-scripps/AutoDock-Vina/blob/develop/LICENSE

#### 36. "AutoDock-GPU — GPL-2 / LGPL-2.1" (line 133)
**Status: ✅ Verified.** AutoDock-GPU is dual-licensed GNU GPL v2 and LGPL v2.1. Source: https://github.com/ccsb-scripps/AutoDock-GPU/blob/develop/LICENSE

#### 37. "gnina — Dual GPL / Apache; GPL via OpenBabel; must keep server-side rescoring" (line 134, 139)
**Status: ✅ Verified.** GNINA is dual licensed under GPL and Apache; the GPL is required because gnina links OpenBabel which is GPL. The doc's recommendation to ship gnina as a separate executable to avoid GPL contagion onto the Apache Vina lane is sound legal practice. Source: gnina/gnina GitHub LICENSE, OpenBabel GitHub.

#### 38. "ChEMBL is CC BY-SA 3.0" (line 130)
**Status: ✅ Verified.** ChEMBL data is released under CC BY-SA 3.0. (Long-standing fact, well documented.)

#### 39. "Meeko (Forli lab) — BSD" (line 131)
**Status: ✅ Verified.** Meeko at https://github.com/forlilab/Meeko is developed by the Forli lab at Scripps CCSB; license is permissive (BSD-style).

#### 40. "P2Rank + fpocket — MIT" (line 135)
**Status: ⚠️ Partially verified.**
- P2Rank: MIT license — verified at https://github.com/rdk/p2rank
- fpocket: Actually **GNU GPL v3**, not MIT — verified at https://github.com/Discngine/fpocket

The doc treats both as MIT in the same row. **fpocket is GPL-3.** This matters: if fpocket runs volunteer-side bundled with Apache code, you have a GPL contagion problem analogous to gnina. Mitigation: keep fpocket centralized for target triage as the doc already implies (it's labeled "small CPU jobs").

#### 41. "OpenMM — MIT / LGPL" (line 137)
**Status: ⚠️ Partially correct.** OpenMM uses the **MIT** license for most of the codebase but **LGPL** for some plugins (e.g., the AMOEBA force-field plugin). The "MIT / LGPL" dual-listing is reasonable shorthand.

### History claims (BOINC ecosystem)

#### 42. Rosetta@home "active since 2005" (implied throughout)
**Status: ✅ Verified.** Launched June 26, 2005 by Baker Lab, UW. Still active. https://en.wikipedia.org/wiki/Rosetta@home

#### 43. Docking@Home "retired May 2014"
**Status: ✅ Verified.** Stopped distributing jobs April 30, 2014; server stopped accepting results May 23, 2014. https://en.wikipedia.org/wiki/Docking@Home

#### 44. WCG OpenPandemics motivated AutoDock-GPU v1.4-v1.5 features
**Status: ✅ Verified.** Forli Lab + WCG tech team built AutoDock-GPU features (flexible residues, modifiable pair potentials, contact analysis) that landed in v1.4 and v1.5 for OpenPandemics-COVID-19. Source: https://www.worldcommunitygrid.org/about_us/article.s?articleId=750

#### 45. GPUGRID "in transition since April 2025"
**Status: ✅ Verified.** GPUGRID moved to a new server April 10, 2025; website still in transition. Source: https://www.gpugrid.net/gpugrid/

### Pocket-conditioned generative models (passing reference)

#### 46. Pocket2Mol, TargetDiff, DiffSBDD — real pocket-conditioned generative models
**Status: ✅ Verified.** All three are real, well-cited pocket-conditioned generative models for structure-based drug design:
- Pocket2Mol — SE(3)-equivariant autoregressive (Peng et al. ICML 2022)
- TargetDiff — E(3)-equivariant diffusion model (Guan et al. ICLR 2023)
- DiffSBDD — E(3)-equivariant diffusion for ligand generation (Schneuing et al., Nature Comp Sci 2024)

These aren't mentioned by name in the doc actually but were in the audit-prompt list. Confirmed real. (PocketFlow also real, not flagged here.)

### URLs and external references

#### 47. https://github.com/marius311/boinc-server-docker
**Status: ✅ Verified.** Exists, actively maintained, README intact.

#### 48. https://github.com/ccsb-scripps/AutoDock-Vina
**Status: ✅ Verified.** Canonical Vina repo.

#### 49. https://github.com/gnina/gnina
**Status: ✅ Verified.** Canonical gnina repo.

#### 50. https://github.com/openmm/openmm
**Status: ✅ Verified.** Canonical OpenMM repo.

#### 51. https://github.com/forlilab/Meeko
**Status: ✅ Verified.** Canonical Meeko repo.

#### 52. https://hub.docker.com/r/fpocket/fpocket
**Status: ✅ Verified.** Image exists at fpocket/fpocket (4.0.0 tag confirmed). Source: https://hub.docker.com/r/fpocket/fpocket

---

## Summary table

| Category | Total checked | ✅ | ⚠️ | ❌ | 🔵 |
|---|---|---|---|---|---|
| Apple Silicon platform | 7 | 2 | 2 | 3 | 0 |
| Installation / packaging | 5 | 4 | 0 | 1 | 0 |
| Structures (PDB) | 4 | 3 | 0 | 1 | 0 |
| Performance / runtime | 4 | 0 | 3 | 0 | 1 |
| BOINC Central / WU shapes | 4 | 1 | 0 | 0 | 3 |
| Compute budgets | 3 | 1 | 2 | 0 | 0 |
| Validation layers | 5 | 2 | 2 | 0 | 1 |
| Licenses | 7 | 4 | 3 | 0 | 0 |
| BOINC history | 4 | 4 | 0 | 0 | 0 |
| URLs + repos | 6 | 6 | 0 | 0 | 0 |
| Generative models (ref) | 1 | 1 | 0 | 0 | 0 |
| **Total** | **52** | **28** | **12** | **5** | **5** |

---

## Top errors (must fix before user runs the pipeline)

### 🚨 #1 — `brew install miniforge` won't work (line 26, 162)
**Fix:** Change to `brew install --cask miniforge`. Better: warn user that Homebrew install of miniforge is discouraged by upstream (auto-updates can destroy environments) and recommend the official PKG installer from https://github.com/conda-forge/miniforge/releases instead.

### 🚨 #2 — OpenMM "Apple Metal backend" does not exist in upstream (lines 11, 15, 16, 37)
**Fix:**
1. Remove "Apple Metal backend" language. Replace with: "OpenMM runs on Apple Silicon via the OpenCL platform (out-of-the-box) or via the experimental third-party `philipturner/openmm-metal` plugin if you want Metal-API-via-OpenCL translation."
2. Fix the verification command (line 37): expecting `Metal` in `Platform.getPlatform(i).getName()` will return False on stock install. Expected platforms: `Reference`, `CPU`, `OpenCL`.
3. The Tier 2 MD plan ("Run 50 ns MD per complex on Apple Metal") becomes "...on Apple GPU via OpenCL platform" or "...on CPU platform if OpenCL drivers misbehave."

### 🚨 #3 — OpenFE does NOT support Apple Silicon natively (lines 16, 111)
**Fix:**
1. Note that OpenFE installation on Apple Silicon currently **requires an x86_64 conda environment** (Rosetta 2 emulation) — one of its dependencies is not yet ARM-native. Per OpenFE docs verbatim.
2. Remove "via Metal slow but works (~48-96 hr each)" — there is no Metal path. Realistic local Apple Silicon time is x86_64-emulated + OpenMM CPU platform; could be many days per edge.
3. The recommendation to rent an H100 for Tier 3 (the doc already says this) is the right call. Strengthen it: "Tier 3 RBFE is the **one stage** where you should not attempt local Apple Silicon execution. Plan for cloud GPU from day one."

### 🚨 #4 — PDB 8AZV is NOT "KRAS G12D apo" (line 86)
**Fix:** 8AZV is KRAS (wildtype-ish) + BI-2865. For "apo G12D," use **8AZY** (G12D + BI-2865) and strip the ligand to make an "apo" mock, OR use **4DSO** / **4OBE** (G12D-GDP without inhibitor). The doc's alternative 7T47 is also a holo MRTX1133 structure, not apo. Suggested fix: cite **4DSO** (KRAS G12D, GDP-bound, no inhibitor) as the apo reference, with cryptic-pocket-open conformations generated by short MD as already planned.

### 🚨 #5 — fpocket is GPL-3, not MIT (line 135)
**Fix:** Update the license table: P2Rank is MIT, fpocket is **GPL-3**. Same GPL-contagion logic as gnina applies: if fpocket runs volunteer-side, it must be a separable executable. The doc already implies "small CPU jobs" centrally, which sidesteps the issue — make that explicit.

---

## Lesser issues (flag but not blockers)

- **Boltz MPS support** is real but not first-class — expect operator fallbacks to CPU (linalg_svd, float64). The doc's "usable" framing is right; mention the rough edges.
- **Vina docking time "5 sec/ligand"** is OK as an average but varies 2-10× with ligand size, exhaustiveness, and box volume. Hedge the language.
- **Median BOINC volunteer hardware** specifics are educated guesses, not measured — fine to keep as estimates but flag as such.
- **CPTAC PDC "29 TB"** is correct relative to the audit-23 correction from 70 TB, but the underlying figure is still hard to pin to an authoritative source in 2026 — best treat as "order of magnitude."

---

## What the doc gets right

- The 4-layer validation ladder (structural truth → retrospective ligand discrimination → benchmark calibration → biological orthogonality) is well-organized and matches best practice.
- The LIT-PCBA caveat about the 2025 audit (data leakage) is good — important to flag publicly.
- The GPL boundary discussion for gnina (line 139, 192) is technically correct and the mitigation (separable executables) is sound.
- Sticky files for receptor grid reuse (Section 3) is the right BOINC primitive for this workload.
- The 4-tier local plan structure (Tier 0 smoke → Tier 1 small screen → Tier 2 MD → Tier 3 FEP cloud) is sound and the failure-mode table (line 144-150) shows good operational thinking.
- PDB anchors (7RPZ, 6GJ7, 6OIM, 6UT0) are all real and well-chosen.
- BOINC history claims (Rosetta@home, Docking@Home, OpenPandemics, GPUGRID transition) all verified accurate.
- License claims for Vina (Apache 2.0), AutoDock-GPU (GPL/LGPL), gnina (dual GPL/Apache), Meeko (BSD), ChEMBL (CC BY-SA 3.0) all verified accurate.

---

## Bottom line

**28/52 claims verified outright (54%); 12/52 with caveats (23%); 5/52 false (10%); 5/52 unverifiable (10%).**

The doc is technically substantive and mostly correct on BOINC, licenses, history, and structure references. The **highest-risk class of errors is the Apple Silicon claims**: 3 of 7 are factually wrong in ways that will directly impact the user's machine setup. Specifically:
1. OpenMM "Apple Metal backend" — does not exist as described; this is the most consequential error
2. OpenFE "via Metal" — does not exist; OpenFE on Apple Silicon requires x86_64 emulation
3. `brew install miniforge` — wrong syntax; need `--cask`
4. PDB 8AZV is not G12D apo
5. fpocket is GPL-3 not MIT (license-contagion implications)

Fixing these five errors before the user runs Tier 0 is critical — otherwise the very first `mamba install ... openmm` step plus the verification command will produce confusing results, and the user will quietly assume they have GPU acceleration when they don't.

**Sources (most-cited):**
- https://docs.openmm.org/latest/userguide/library/04_platform_specifics.html
- https://github.com/philipturner/openmm-metal
- https://docs.openfree.energy/en/v1.2.0/installation.html
- https://formulae.brew.sh/cask/miniforge
- https://github.com/jwohlwend/boltz/pull/527
- https://github.com/ccsb-scripps/AutoDock-Vina/releases
- https://www.rcsb.org/structure/7RPZ
- https://www.rcsb.org/structure/8AZV
- https://github.com/Discngine/fpocket
- https://boinc.berkeley.edu/central/
