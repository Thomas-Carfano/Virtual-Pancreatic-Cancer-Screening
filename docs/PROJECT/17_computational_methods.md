# 17. Computational Methods for Drug Discovery — State of the Art (2026)

*A survey calibrated to volunteer-compute feasibility, written for the PancScan@home self-funded BOINC-style project on pancreatic ductal adenocarcinoma (PDAC).*

---

## 1. The Modern Computational Pipeline — From Target to Lead

A contemporary structure-based drug discovery (SBDD) pipeline in 2026 looks fundamentally different from the one that existed when BOINC-era projects like Rosetta@home and Folding@home were designed. The qualitative shift is that *all five tiers below are now numerically tractable on the same compound space, in cascade form, given enough compute*:

| Tier | Method class | Output | Compute order |
|---|---|---|---|
| 1. Target prep | AlphaFold3 / Boltz-2 / ensemble MD | Druggable receptor model | 10–10⁴ GPU-hr |
| 2. Pocket finding | PocketMiner, P2Rank, fpocket | Ranked binding sites | seconds–minutes |
| 3. Ultra-large VS | Vina-GPU / Uni-Dock / V-SYNTHES | 10⁴–10⁶ top scorers from 10⁹–10¹⁰ pool | 10³–10⁶ CPU-hr |
| 4. ML rescoring + active learning | GNINA, RTMScore, Boltz-2 affinity, MolPAL | Re-rank top 10⁴ → 10² | 10²–10⁴ GPU-hr |
| 5. Physics validation | MD, MM/GBSA, FEP, ABFE | ΔG ± 1 kcal/mol | 10²–10⁴ GPU-hr per cohort |

The pipeline is read top-to-bottom: each tier has roughly 10× higher cost per compound and roughly 10² lower throughput than the tier above it. Volunteer compute is best matched to **tiers 3, 4, and the cheapest end of tier 5** — exactly the regime where 10⁵ heterogeneous CPU/GPU workers each completing 10²–10³ small jobs/day can outstrip a small academic cluster by 2–3 orders of magnitude.

The critical realization that distinguishes 2026 from 2020 is *the cascade*. A workflow that only docks 10⁹ compounds and ranks by Vina score has been outperformed in retrospective head-to-heads by workflows that dock 10⁷ and rescore with GNINA or Boltz-2 affinity, because rank correlation with experimental affinity is dominated by the scoring function, not the breadth of search. This shapes everything below.

---

## 2. Ultra-Large Virtual Screening — Recent History and Hit Rates

The "ultra-large" era began with **Lyu et al. 2019** (*Nature*), where Shoichet, Irwin and colleagues docked 138 million make-on-demand compounds against the dopamine D4 receptor and 99 million against AmpC β-lactamase using DOCK3.7. From the D4 screen, 549 compounds were synthesized; **30 had submicromolar activity** out of 81 novel chemotypes, including a 180 pM subtype-selective agonist. The headline finding was that hit rates *rose monotonically with docking score* — i.e., the score is informative even at billion-scale ranking, validating the conceit of ultra-large VS.

**Sadybekov, Katritch et al. 2022** (*Nature*) extended this with V-SYNTHES, a synthon-based hierarchical enumeration of the Enamine REAL Space at 11 billion compounds — using "molecular puzzle pieces" instead of enumerating the full product space. V-SYNTHES is reported to be ~5,000× faster than brute-force docking of the same space, hit rates were comparable, and it found nanomolar cannabinoid CB2 ligands. **V-SYNTHES2 (Katritch lab, 2024–2025)** is now operating at 36 billion+.

**Gorgulla et al.** built **VirtualFlow** (Nature 2020) into the canonical open-source ultra-large VS platform. **VirtualFlow 2.0** (bioRxiv 2023) added adaptive sampling and now claims access to 69 billion molecules. VirtualFlow's design — a SLURM-based fan-out of containerized Vina/Smina/QuickVina jobs — is the closest extant template for a BOINC-style fan-out and is genuinely open-source under MIT-like terms.

Reported hit rates across these studies, on novel chemotypes pursued to assay, cluster around **10–35% submicromolar from the top 0.01–0.05% of docked compounds**, which is roughly 10–100× the experimental HTS rate at the same library size and the same target. This is the empirical justification for the entire enterprise.

---

## 3. Compound Libraries — What Exists in 2026

| Library | Size (2026) | Type | Cost / availability |
|---|---|---|---|
| **Enamine REAL Space** | ~83–95 billion (Sep 2025 update) | Make-on-demand, ~80% delivered in 3–4 weeks | Free download for academia; per-compound synthesis $$$ |
| **ZINC22 / ZINC-22** | ~55 billion 2D / ~6 billion 3D (Nov 2025) | Curated tangible compounds | Free; Tingle & Irwin, UCSF |
| **WuXi GalaXi** | ~8 billion | Vendor-specific make-on-demand | Commercial |
| **Mcule** | ~75 million in-stock + larger virtual | Mostly in-stock | Free academic browse |
| **PubChem** | ~119 million | Real compounds with annotations | Free |
| **ChEMBL** | ~2.5 million bioactive | With measured activity | Free |
| **DrugBank** | ~14,000 drug-like + approved | Curated, repurposing | Free academic |
| **GDB-17** | ~166 billion (enumerated, mostly not tangible) | Combinatorial enumeration | Free |

For PancScan@home, the practical screening space is *ZINC22 3D (~6B) plus a sampled slice of Enamine REAL*. We will not screen 95B even if we had the compute — the cost-per-synthesis sets a useful natural cap, since you cannot follow up more than a few hundred compounds.

SMARTS-level filters always applied: **PAINS-A/B/C** (Pan-Assay Interference, Baell & Holloway 2010), **REOS** (Walters, Murcko), and "Rule of Five" with relaxed thresholds for kinase / GTPase scaffolds. These remove roughly 5–15% of any docked top list.

---

## 4. Docking Engines — Open-Source Emphasis

| Engine | Platform | Speed (consumer GPU/CPU) | Open source | Best use |
|---|---|---|---|---|
| **AutoDock Vina 1.2.x** | CPU | ~5–30 s/ligand, default exhaustiveness 8 | Yes, Apache | Baseline, reproducibility |
| **AutoDock-GPU** | GPU | ~0.5–2 s/ligand | Yes | Mid-scale rigid-receptor |
| **Vina-GPU 2.1** (Ding et al.) | GPU | 21× avg / 50× peak over CPU Vina | Yes | Drop-in Vina acceleration |
| **Uni-Dock** (DP Tech) | GPU | ~0.1 s/ligand on V100 (vina); 0.5 s (ad4) | Yes (Apache) | Ultra-large fan-out |
| **Smina** | CPU | Similar to Vina, more flexible scoring | Yes | Custom scoring R&D |
| **GNINA** | CPU/GPU | ~0.5–2 s/pose CNN rescore | Yes | CNN scoring on Vina-style poses |
| **QuickVina-W / QVina-GPU** | CPU/GPU | 3–10× Vina | Yes | Throughput-favored |
| **DOCK 3.8** (Shoichet) | CPU | ~1–5 s/ligand on flexible Vina-like | Free for academia | The historical ultra-large engine |
| **DOCK 6** | CPU | Slower, ~10–30 s/ligand | Free for academia | RNA targets, anchor-and-grow |
| **rDock** | CPU | ~5–10 s/ligand | Yes (LGPL) | Fragment / pharmacophore |
| **idock / idock-CUDA** | CPU/GPU | ~1–3 s/ligand | Yes | Lightweight |
| **DiffDock-L** | GPU | ~3–10 s/ligand (40 steps) | Yes | Pocket-agnostic diffusion |
| **EquiBind / TankBind** | GPU | <1 s/ligand | Yes | Fast pose proposal; weak ranking |
| **Glide SP/XP** | CPU | Glide-SP ~10–30 s; XP much slower | No (Schrödinger commercial) | Benchmark reference |
| **GOLD** | CPU | ~30 s/ligand | No (CCDC commercial) | Benchmark reference |

**Critical 2025 benchmark finding**: A large LIT-PCBA evaluation (15 targets, 578K ligand-target pairs) showed that **AutoDock-GPU poses rescored with GNINA** (i.e., AutoDock-GNINA) was the strongest single workflow with median EF1% of 2.14, beating DiffDock-L on most targets. Pure diffusion docking *underperforms classical search + ML rescoring* on the screening-power task at billion scale — and this is the empirical basis for our recommended pipeline.

For PancScan@home, the workhorse stack is:
- **Vina-GPU 2.1 or Uni-Dock** as primary search (volunteer GPUs)
- **AutoDock Vina 1.2.x CPU** as fallback for CPU-only workers
- **GNINA-CNN rescoring** at the top 0.1% tier
- **Boltz-2 affinity head** at the top 0.001% tier

---

## 5. Structure Prediction — The AlphaFold Lineage and Successors

The receptor model problem is now substantially solved for most pancreatic-cancer targets (KRAS WT/G12D/G12V/G12C/G12R, EGFR, BRCA, p53, MUC1, mesothelin, c-MET, MEK1/2, AXL, etc.) — but the *druggable conformation* is not. Co-folding accuracy on novel ligand chemotypes still degrades sharply outside the training distribution.

| Model | Year | License | Capability | Compute |
|---|---|---|---|---|
| **AlphaFold2** | 2021 | Apache 2.0 (DeepMind) | Monomer, multimer (separate) | 5–30 min consumer GPU |
| **AlphaFold-Multimer** | 2022 | Apache | Protein complexes | 10–60 min consumer GPU |
| **AlphaFold3** | 2024 (paper) / Nov 2024 (weights, non-commercial) | Non-commercial only | Protein + ligand + DNA/RNA + ions | 5–30 min GPU |
| **OpenFold-3** | 2025 | MIT, open-weight | AF3 reproduction | Comparable to AF3 |
| **Protenix** (ByteDance) | 2025 | Apache 2.0 | AF3 reproduction | Comparable |
| **Chai-1** | 2024 | Apache 2.0 | Protein + ligand, no MSA optional | ~5–20 min |
| **Boltz-1** | 2024 | MIT | Protein + ligand + nucleic | ~3–15 min, very memory-efficient |
| **Boltz-2** | 2025 | MIT | Boltz-1 + binding affinity head | 1000× faster than FEP |
| **RoseTTAFold-All-Atom** | 2023–24 | Free academic | All-atom, ligand-capable | ~5–30 min |
| **ESMFold** | 2022 | MIT | Sequence-only protein | 1–5 min |
| **AlphaFlow / ESMFlow** | 2024 | MIT | Conformational ensembles | 1–10× single fold |
| **PocketMiner** (Bowman lab) | 2023 | MIT | Cryptic-pocket residue prediction | Seconds |
| **P2Rank** | 2018–25 | Apache | Pocket detection from structure | Seconds |
| **PocketFlow / DiffSBDD** | 2023–24 | MIT | Pocket-conditioned generation | GPU-min |

**For PancScan@home**, the relevant deliverable is *target-conformational ensembles* (TCEs) — not just single AF3 models. The plan: for each PDAC target, generate ~50 AlphaFlow snapshots, run 200 ns each of MD per snapshot, cluster the trajectories, then use the 5–20 most populous receptor conformations as the docking template set. This is *the* compute step most easily parallelized across volunteer GPUs, and it produces a re-usable artifact: a public PDAC TCE dataset.

The dominant 2025–26 trend: **Boltz-2** with its affinity head approaches FEP-quality ranking at ~1000× lower cost (Pearson 0.62 vs FEP 0.72 on the hit-to-lead benchmark, per the MIT/Recursion preprint). It is open under MIT and is the single most consequential ML tool for a volunteer-compute pipeline in 2026.

---

## 6. Molecular Dynamics — Engines, Force Fields, Enhanced Sampling

| Engine | Platform | Performance (RTX 4080-class, 100K atoms) | Open |
|---|---|---|---|
| **OpenMM 8.x** | GPU-first | ~100–200 ns/day | Yes (MIT) |
| **GROMACS 2025** | GPU+CPU | ~150–300 ns/day | Yes (LGPL) |
| **AMBER 24** (pmemd.cuda) | GPU | ~200–400 ns/day | Free academic |
| **NAMD 3** | GPU | ~80–150 ns/day | Free academic |
| **CHARMM** | CPU mostly | ~10–50 ns/day | Free academic |
| **Anton 3** | Custom ASIC (D.E. Shaw) | ~50–100 µs/day | Not available to volunteers |

**Folding@home pattern** — short (10–100 ns) trajectories fanned out across many GPUs, then statistically combined via **Markov State Models** (MSMs; Pande, Bowman, Noé) — is *exactly* the volunteer-compute idiom. F@h's exascale aggregate during 2020 demonstrated that the pattern scales to ~10⁵ active hosts. Adopting OpenMM with the Folding@home work-unit conventions is the path of least resistance.

Force fields: **AMBER ff14SB** and **ff19SB** for protein, **GAFF2** or **OpenFF 2.x (Sage/Parsley)** for small molecule, **TIP3P** or **OPC** for water. The OPC water model is meaningfully more accurate for binding sites but slightly more expensive (~5%).

Enhanced sampling, ranked by cost-effectiveness for cryptic-pocket discovery:
- **Gaussian-accelerated MD (GaMD)** — cheapest, just a biasing potential
- **Metadynamics** (Parrinello) — requires good CV choice
- **REST2 / replica exchange with solute tempering** — robust, expensive (8–16 replicas)
- **Co-solvent MD** — mix benzene, isopropanol, etc. into the box; very effective for finding cryptic pockets, used heavily by Bowman lab and Sosa group
- **Frame-by-frame fragment hotspot mapping (FTMap)** offline

For PDAC, the **KRAS switch-II cryptic pocket** (G12D / G12C / G12V) is the canonical case study: 100 µs of aggregate sampling across F@h revealed druggable conformations that single-structure docking missed. This is *the* directly relevant precedent.

---

## 7. Free-Energy Methods — When They Pay

| Method | Compute / ligand | Expected accuracy | When to use |
|---|---|---|---|
| **MM/GBSA** | 1–5 GPU-hr | RMSE ~3–5 kcal/mol | Rescore top 10³–10⁴ |
| **MM/PBSA** | 2–10 GPU-hr | RMSE ~2–4 kcal/mol | Rescore top 10²–10³ |
| **RBFE (FEP+)** (Schrödinger) | 20–80 GPU-hr per edge | RMSE ~1 kcal/mol | Top 10²; commercial |
| **RBFE (OpenFE)** | 30–100 GPU-hr per edge | RMSE 1.7 kcal/mol public | Top 10² open pipeline |
| **ABFE (Yank / OpenFE SepTop)** | 100–1000 GPU-hr per ligand | RMSE 1–2 kcal/mol | Top 10–30, lead opt |

**OpenFE 1.7 (Oct 2025)** is the moment open-source RBFE became production-grade. The December 2025 multi-pharma collaborative benchmark (15 companies, ~1700 ligands) reported RMSE 1.73 kcal/mol on the public set with the OpenFE hybrid-topology protocol — matching commercial FEP+ within statistical error. OpenFE 1.7 also added **SepTop ABFE**. Under a permissive license, this is the first time a volunteer-compute project could plausibly run an ABFE campaign at all.

Cost reality for PancScan@home: **RBFE is the lead-optimization stage**, only viable if the project has already converged on a tractable congeneric series (say 20–100 analogs of one hit chemotype). It should never be the primary scoring tier. Per the table, the entire top-30 RBFE campaign costs ~3,000 GPU-hr — i.e., one F@h-class day if 1,000 GPUs participate, which is plausible at a steady-state 10⁵-volunteer scale.

---

## 8. ML Scoring and Generative Design

### Scoring / rescoring
| Tool | Modality | Typical Pearson r vs. exp pKi | License |
|---|---|---|---|
| Vina score | Empirical | ~0.40–0.55 | Apache |
| **GNINA CNN** | 3D CNN, Vina poses | ~0.55–0.65 | Apache |
| **RTMScore** | GNN | ~0.60–0.68 | Open |
| **DeepDock** | GNN | ~0.55–0.65 | Open |
| **OnionNet** / OnionNet-2 | 3D CNN | ~0.60 | Open |
| **Boltz-2 affinity head** | Foundation model | **~0.62 hit-to-lead, ~0.78 on cleaner sets** | MIT |
| FEP+ (commercial) | Physics | ~0.72 hit-to-lead | Schrödinger |

The 2024–25 consensus from HIPPO / OpenAffinity / CASP16-affinity benchmarks: *Boltz-2 is now competitive with physics-based RBFE at 10³× speed*. This is the largest single qualitative change since 2019.

### Generative
- **REINVENT 4** (AZ, 2024) — RNN + RL, four modes (de novo, scaffold, linker, Mol2Mol). Open under Apache.
- **MolMIM** (NVIDIA, 2023) — masked latent generative
- **Pocket2Mol / TargetDiff / DiffSBDD / PocketFlow** — pocket-conditioned, diffusion or flow-matching. Generally MIT.

For PancScan@home, REINVENT 4 + a Boltz-2-affinity reward function is the canonical "design and screen" loop. Pocket-conditioned generation (DiffSBDD) is the more ambitious version but currently has much lower hit rates than dock-then-screen on novel targets.

---

## 9. Active Learning — Making 70 Billion Tractable

The discovery that *you only need to physically dock ~1%* of a billion-scale library to recover ~90% of the top scorers — through pool-based active learning with a surrogate ML model that predicts docking scores — is the operational unlock. **Graff, Shakhnovich & Coley 2021** (*Chemical Science*) demonstrated this for MolPAL, and the **2024 *Nature Communications*** AI-accelerated VS platform paper extended it to billion-scale with confirmed hit recovery rates of 70–90% at 0.1–1% docking budget.

The recipe:
1. Randomly sample 10⁴–10⁵ compounds, dock them
2. Train an inexpensive ML model (Chemprop, RF, etc.) on those scores
3. Predict scores for the entire 10⁹+ library
4. Dock the top 10⁵ predicted compounds
5. Retrain; iterate 5–10 times
6. Final docked set is ~10⁶–10⁷ (1% of pool) but recovers ~90% of true top-10⁴

For a BOINC-style volunteer project, this **reduces the dock-everything compute requirement by ~100×** and is mathematically necessary — without it, screening 10B compounds against 10 PDAC targets at 5 conformations each is 5×10¹² docks, or 25M CPU-years at 5s/dock. With 100× active-learning reduction it becomes 250K CPU-years, which is approximately one year on 10⁵ active volunteer cores at 50% duty cycle. **This is the load-bearing assumption.**

The 2025 Nature Biotechnology antibacterial paper (1.4B compounds, 90× hit-rate improvement, 82 confirmed actives) is the clearest demonstration of the recipe working end-to-end at scale and is the closest precedent to the PancScan@home strategy.

---

## 10. Volunteer Compute Fit — What Runs Where

| Workload | CPU | Consumer GPU | Datacenter GPU | F@h pattern | BOINC pattern |
|---|---|---|---|---|---|
| Vina docking | Great | Great (10–30× faster) | Great | Yes | Yes (Rosetta@home idiom) |
| GNINA CNN rescore | OK | Great | Great | Yes | Yes |
| Boltz-2 inference | Slow | Marginal (8GB tight) | Great (24GB+) | Partial | Partial — needs ≥12 GB VRAM |
| AlphaFold/Boltz fold | Painful | OK (10–30 min) | Great | OK | OK |
| MD short trajectories (10–100 ns) | Bad | **Native fit** | Native fit | **Canonical use case** | Possible via OpenMM |
| MD long (>1 µs) | No | Possible across many WUs | Possible | **F@h's specialty** | F@h pattern |
| FEP / RBFE | No | Marginal | Yes | Hard — checkpointing | Hard |
| ABFE | No | Marginal | Yes | Hard | Hard |
| ML model *training* | No | No (data-bound) | Yes | No | **Does not work** |
| ML model *inference* | OK for trees | Great | Great | Yes | Yes |
| Generative design (REINVENT, DiffSBDD) | Slow | Great | Great | Yes | Yes |
| Active-learning surrogate prediction | OK | Great | Great | Yes | Yes |

The two hard rules:
- **Training big neural models from scratch is wrong on volunteer compute.** Bandwidth and gradient-aggregation latency kill it. Inference is fine.
- **Long-correlation MD trajectories are F@h territory.** They require state-checkpointed work units that the BOINC server reassembles in order.

A self-funded BOINC-style project can ship the docking + ML-inference + short-MD + active-learning pieces immediately. RBFE and ABFE work best via centralized rented A100/H100 nodes (~$1–2/GPU-hr spot) for the final 30–100 ligand campaign — i.e., budget $5,000–$30,000 in cloud spend rather than try to run it on volunteer hardware.

---

## 11. Benchmark Numbers — Per Compound, Per Nanosecond, Per Ligand

| Operation | Hardware | Time | Throughput per node/day |
|---|---|---|---|
| Vina dock, exhaustiveness=8 | 1 CPU core | ~5–30 s | ~3,000–17,000 / day |
| Vina dock | 1 modern desktop (16 cores) | ~0.3–2 s effective | ~50K–280K / day |
| Uni-Dock vina | 1 V100 GPU | ~0.1 s | ~860K / day |
| Vina-GPU 2.1 | RTX 4080 | ~0.5 s | ~170K / day |
| GNINA CNN rescore | RTX 4080 | ~0.5–2 s | ~50K–170K / day |
| DiffDock-L (40 steps) | RTX 4080 | ~3–10 s | ~10K–30K / day |
| AlphaFold2 monomer | RTX 4080 | ~5–30 min | ~50–280 / day |
| Boltz-1 protein+ligand | RTX 4080 | ~3–15 min | ~100–500 / day |
| Boltz-2 affinity | RTX 4080 | ~10–60 s/ligand | ~1,500–8,500 / day |
| OpenMM MD, 100K atoms | RTX 4080 | ~100–200 ns/day | — |
| MD 100 ns, 100K atoms | RTX 4080 | ~12 hr | ~2 / day |
| OpenFE RBFE one edge | A100 | ~30–80 GPU-hr | ~0.3 / day |
| OpenFE ABFE SepTop one ligand | A100 | ~100–500 GPU-hr | ~0.05 / day |

**The headline math: docking 10B compounds × 1 conformation by brute force, no active learning, at 5 s/CPU-core/ligand = 5×10¹⁰ core-seconds ≈ 1.6×10⁶ core-years.** With active learning to 1% it falls to 1.6×10⁴ core-years — feasible at steady-state 10⁵ active CPU cores in two months. With Uni-Dock-GPU on 10⁴ active consumer GPUs at 10⁶ ligands/GPU-day it is ~10 days for the same campaign.

---

## 12. Recommended Pipeline for PancScan@home

The proposed cascade, with explicit volunteer-compute budgets per pancreatic-cancer target:

**Stage A — Target ensembles** (one-time per target, ~5–10 targets)
- AlphaFold3 / Boltz-1 → starting structures, including PocketMiner-flagged cryptic pockets
- AlphaFlow → 50 conformations
- OpenMM short MD: 200 ns × 50 = 10 µs per target, GPU-only work units
- Cluster to 10 representative receptor conformations
- *Compute: ~6,000 GPU-hr/target → ~50 days on 100 volunteer GPUs at 50% duty cycle. Annual: 1 target / 2 months.*

**Stage B — Active-learning ultra-large dock** (per target, per year)
- ZINC22 3D subset (~5B) + Enamine REAL slice (~5B) = 10B compound pool
- 10⁴ random docking seed → Chemprop surrogate
- 5 active-learning iterations, each ~10⁵ Vina dockings against 10 receptor conformations = 10⁶ docks/iter
- Final retained set: top 10⁵ compounds × 10 conformations = 10⁶ poses
- *Compute: ~50K CPU-core-hr/iteration. 5 iterations = 250K core-hr → ~25 days on 10⁴ active CPU cores at 50%.*

**Stage C — ML rescoring**
- GNINA CNN on all 10⁶ poses → re-rank
- Boltz-2 affinity on top 10⁴
- *Compute: ~10K GPU-hr → ~5 days on 100 volunteer GPUs.*

**Stage D — Short-MD validation**
- 100 ns × 3 replicas × top 200 compounds = 600 trajectories
- *Compute: ~600 × 12 = 7,200 GPU-hr → ~6 days on 100 GPUs.*

**Stage E — Free-energy validation** (out-of-band, rented cloud)
- OpenFE RBFE network on top 30 analogs of leading chemotype
- *Compute: ~3,000 GPU-hr A100 → ~$3K–6K cloud spend.*

**Stage F — Outputs**
- All top-1,000 docking poses, all top-200 trajectories, all FEP results published under CC-BY
- Top hits handed to a synthesis partner (Enamine, Mcule REAL) for IC₅₀ confirmation

**Annual aggregate compute requirement** at steady state, assuming 4 targets/year:
- ~2,400,000 CPU-core-hr (≈ 10K cores × 240 hr / 50% duty = feasible at 20K volunteer cores)
- ~80,000 GPU-hr (≈ 200 volunteer consumer GPUs)
- ~$15K cloud RBFE budget

This is achievable at a volunteer base of **~50,000 active hosts** (~half CPU-only desktops, half with consumer GPUs) — a project size comparable to mid-decline-era Rosetta@home, well below F@h's peak.

---

## 13. CPU-First vs GPU-First — The Architecture Decision

The single biggest design decision is the docking work-unit definition. Three options:

1. **CPU-first, Vina 1.2.x.** Maximally compatible (any volunteer machine, ARM included). ~10K–20K docks/host/day on a typical 8-core consumer CPU. Output is poses + Vina score. *Best for the bulk active-learning iterations.*

2. **GPU-first, Vina-GPU 2.1 or Uni-Dock.** ~10⁵–10⁶ docks/host/day on consumer GPUs. Requires CUDA volunteer; ~30% of typical BOINC pool. *Best for stage-C rescoring and stage-D MD.*

3. **Hybrid with credit weighting.** Vina-CPU work units pay the standard, Uni-Dock-GPU work units pay 1.5×, MD work units pay 10×. Volunteers self-select; pool composition stabilizes naturally.

**Recommendation: Hybrid, with CPU-Vina as the default for new volunteers and an opt-in GPU/MD track.** This is what F@h and Rosetta@home converged on, for the same reasons.

A *second* architectural choice: containerization. **Use Singularity/Apptainer images for the science binaries** (Vina, GNINA, OpenMM, Boltz-2) — BOINC's wrapper task can call into a pre-cached image. This is how VirtualFlow 2.0 distributes; the same image is reusable on cluster, cloud, and volunteer host. SiDock@home (the existing BOINC drug-discovery project, active 2021–present) has demonstrated this works at scale of ~10K active hosts.

A *third* architectural choice: dataset hosting. Compound libraries at 5–10B scale are ~1–5 TB compressed and cannot be downloaded by every volunteer. The pattern is: server preprocesses into Vina-ready PDBQT shards of ~10K compounds, each shard ~50 MB, and each work unit downloads one shard + one receptor + returns scores. This is exactly the VirtualFlow → BOINC translation.

---

## 14. Sources

### Ultra-large virtual screening
- Lyu J. et al. *Ultra-large library docking for discovering new chemotypes.* **Nature** 566, 224–229 (2019). https://www.nature.com/articles/s41586-019-0917-9
- Sadybekov A.A., Sadybekov A.V., Liu Y., Iliopoulos-Tsoutsouvas C., Huang X.-P., Pickett J., Houser B., Patel N., Tran N., Tong F., Zvonok N., Jain M.K., Savych O., Vasilyev D.S., Gavrilov K., Gusach A., Levit-Zerdoun E., Marino G., Roth B.L., Sadybekov V., Makriyannis A., Cherezov V., Katritch V. *Synthon-based ligand discovery in virtual libraries of over 11 billion compounds.* **Nature** 601, 452–459 (2022). https://www.nature.com/articles/s41586-021-04220-9
- Sadybekov A.V., Katritch V. *Computational approaches streamlining drug discovery.* **Nature** 616 (2023).
- Gorgulla C. et al. *An open-source drug discovery platform enables ultra-large virtual screens.* **Nature** 580, 663–668 (2020). https://www.nature.com/articles/s41586-020-2117-z
- Gorgulla C. et al. *VirtualFlow 2.0 — The Next Generation Drug Discovery Platform Enabling Adaptive Screens of 69 Billion Molecules.* **bioRxiv** (2023). https://www.biorxiv.org/content/10.1101/2023.04.25.537981v1
- VFVS repository: https://github.com/VirtualFlow/VFVS
- Bender A., Cortés-Ciriano I. *Artificial intelligence in drug discovery: what is realistic?* **Drug Discov Today** (2023).

### Libraries
- Tingle B.I., Tang K.G., Castanon M., Gutierrez J.J., Khurelbaatar M., Dandarchuluun C., Moroz Y.S., Irwin J.J. *ZINC-22 — A Free Multi-Billion-Scale Database of Tangible Compounds for Ligand Discovery.* **J. Chem. Inf. Model.** (2023). https://pubs.acs.org/doi/10.1021/acs.jcim.2c01253
- ZINC22: https://cartblanche.docking.org
- Enamine REAL Space updates: https://www.biosolveit.de/2025/09/23/enamines-real-space-september-2025-update-now-83-billion/
- Mcule: https://mcule.com
- PubChem: https://pubchem.ncbi.nlm.nih.gov

### Docking engines
- Trott O., Olson A.J. *AutoDock Vina.* **J. Comput. Chem.** 31, 455–461 (2010).
- Eberhardt J. et al. *AutoDock Vina 1.2.0.* **J. Chem. Inf. Model.** (2021).
- Tang S. et al. *Vina-GPU 2.1.* **bioRxiv** (2023). https://www.biorxiv.org/content/10.1101/2023.11.04.565429v1
- Yu Y. et al. *Uni-Dock: GPU-accelerated docking enabling ultra-large virtual screening.* **J. Chem. Theory Comput.** (2023).
- McNutt A.T., Francoeur P., Aggarwal R., Masuda T., Meli R., Ragoza M., Sunseri J., Koes D.R. *GNINA 1.0.* **J. Cheminformatics** (2021).
- Corso G. et al. *DiffDock.* **ICLR** (2023); DiffDock-L (2024).
- Bryant P. et al. *Benchmarking GNINA and AutoDock Vina for Precision Virtual Screening Workflow* (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12388557/
- arXiv 2605.01681 *Benchmarking Single-Pose Docking, Consensus Rescoring, and Supervised ML on the LIT-PCBA Library* (2025).

### Structure prediction
- Jumper J. et al. *AlphaFold2.* **Nature** 596 (2021).
- Evans R. et al. *AlphaFold-Multimer.* **bioRxiv** (2021).
- Abramson J. et al. *AlphaFold3.* **Nature** 630 (2024).
- AlphaFold3 code/weights release: November 2024 (non-commercial only).
- OpenFold-3: https://github.com/aqlaboratory/openfold-3
- Protenix (ByteDance) preprint, **bioRxiv** Jan 2025. https://www.biorxiv.org/content/10.1101/2025.01.08.631967v1
- Chai Discovery. *Chai-1: Decoding the molecular interactions of life.* (2024).
- Wohlwend J. et al. *Boltz-1.* (2024). https://gcorso.github.io/assets/boltz1.pdf
- Passaro S., Corso G. et al. *Boltz-2 — Towards Accurate and Efficient Binding Affinity Prediction.* **bioRxiv** 2025.06.14.659707 (2025). https://www.biorxiv.org/content/10.1101/2025.06.14.659707v1
- Krishna R. et al. *RoseTTAFold All-Atom.* **Science** (2024).
- Lin Z. et al. *ESMFold.* **Science** (2023).
- Jing B., Berger B. *AlphaFlow.* (2024).
- Meller A., Ward M., Borowsky J., Kshirsagar M., Lotthammer J., Oviedo F., Lavista Ferres J., Bowman G.R. *Predicting locations of cryptic pockets from single protein structures using the PocketMiner graph neural network.* **Nat. Commun.** 14, 1177 (2023). https://www.nature.com/articles/s41467-023-36699-3
- Krivák R., Hoksza D. *P2Rank.* **J. Cheminformatics** (2018).

### MD
- Eastman P. et al. *OpenMM 8.* **PLOS Comp. Biol.** (2024).
- Abraham M.J. et al. GROMACS 2025 release notes. https://manual.gromacs.org/2025.1/
- Case D.A. et al. *AMBER 24.* (2024).
- AMBER ff14SB: Maier J.A. et al. *J. Chem. Theory Comput.* (2015). ff19SB: Tian C. et al. (2020).
- Izadi S., Anandakrishnan R., Onufriev A.V. *OPC water model.* (2014).
- Bowman G.R. *SARS-CoV-2 Simulations Go Exascale to Capture Spike Opening and Reveal Cryptic Pockets.* (2020). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8249329/
- Bowman G.R., Pande V.S., Noé F. *An Introduction to Markov State Models* (2014).
- Vithani N., Ward M.D., Zimmerman M.I., Novak B., Borowsky J.H., Singh S., Bowman G.R. *Folding@home accelerated cryptic-pocket discovery during the COVID-19 pandemic* (2021).

### Free-energy methods
- OpenFE Consortium. *Large-scale collaborative assessment of binding free energy calculations for drug discovery using OpenFE.* **ChemRxiv** (Dec 2025 / Mar 2026 update). https://chemrxiv.org/doi/10.26434/chemrxiv-2025-7sthd
- OpenFE 1.7 release notes (Oct 2025). https://openfree.energy/science/update/2025/10/23/release-v1.7/
- Mobley D.L., Gilson M.K. *Predicting Binding Free Energies.* **Annu. Rev. Biophys.** (2017).
- Chodera J.D. et al. Yank documentation and gufe protocol stack.
- Wang L. et al. (FEP+) *J. Am. Chem. Soc.* (2015).

### ML potentials and scoring
- Smith J.S., Isayev O., Roitberg A.E. *ANI-1, ANI-2x.* **Chem. Sci.** (2017, 2019).
- Zubatyuk R., Isayev O. *AIMNet2.* **bioRxiv** (2023) / 2025 update. https://pmc.ncbi.nlm.nih.gov/articles/PMC12057637/
- Batatia I. et al. *MACE.* **NeurIPS** (2022); MACE-OFF23. https://arxiv.org/abs/2312.15211
- Batzner S. et al. *NequIP.* (2022); Musaelian A. et al. *Allegro.* (2023).
- Lu W. et al. *RTMScore.* (2022).
- Méndez-Lucio O. et al. *DeepDock.* **Nat. Mach. Intell.** (2021).
- Zheng L. et al. *OnionNet-2.* (2021).

### Generative & active learning
- Loeffler H.H. et al. *Reinvent 4.* **J. Cheminformatics** (2024). https://link.springer.com/article/10.1186/s13321-024-00812-5
- NVIDIA BioNeMo. *MolMIM* (2023).
- Peng X. et al. *Pocket2Mol.* **ICML** (2022).
- Guan J. et al. *TargetDiff.* (2023).
- Schneuing A. et al. *DiffSBDD.* (2023).
- Graff D.E., Shakhnovich E.I., Coley C.W. *Accelerating high-throughput virtual screening through molecular pool-based active learning (MolPAL).* **Chem. Sci.** 12, 7866 (2021). https://pubs.rsc.org/en/content/articlelanding/2021/sc/d0sc06805e
- MolPAL repository: https://github.com/coleygroup/molpal
- Gentile F., Yaacoub J.C., Gleave J., Fernandez M., Ton A.-T., Ban F., Stern A., Cherkasov A. *Deep Docking: AI-enabled VS of ultra-large libraries.* **Nat. Protoc.** (2022). https://www.nature.com/articles/s41596-021-00659-2
- *Deep-learning-based virtual screening of antibacterial compounds.* **Nat. Biotechnol.** (Nov 2025). https://www.nature.com/articles/s41587-025-02814-6
- *An artificial intelligence accelerated virtual screening platform.* **Nat. Commun.** (2024). https://www.nature.com/articles/s41467-024-52061-7

### KRAS-specific
- Maurer T. et al. *KRAS switch-II pocket structures and inhibitors.* (2012, 2017).
- Mattos C. et al. *Multiple secondary KRAS sites.* (2012–2020).
- Wellnhofer; Lyne et al. KRAS computational screens.
- Discovery of Novel Noncovalent KRAS G12D Inhibitors through Structure-Based Virtual Screening and MD. **PubMed 38542866** (2024).
- *Identification of KRAS mutants (G12C, G12D, G12V) inhibitors.* **Future Med. Chem.** (2025).
- *Targeting the untargetable: accelerated discovery of KRAS G12D inhibitors through a deep-learning-enhanced in silico pipeline.* (2025).
- KRASAVA Expert System. **PMC 12786227** (2025).

### Volunteer compute precedents
- Anderson D.P. *BOINC.* (2004) and BOINC manual.
- Larson S.M., Snow C.D., Shirts M.R., Pande V.S. *Folding@home and the worldwide grid.* (2002 to present); F@h exascale: Zimmerman M.I. et al. *Nat. Chem.* (2021).
- DrugDiscovery@home historical records (2007–2012).
- Nikitina N. et al. *Toward Crowdsourced Drug Discovery: Start-Up of the Volunteer Computing Project SiDock@home.* (2021). https://link.springer.com/chapter/10.1007/978-3-030-92864-3_39
- Optimization of the Workflow in a BOINC-Based Desktop Grid for Virtual Drug Screening (2022).

---

*Document prepared for the PancScan@home self-funded volunteer-computing initiative against pancreatic ductal adenocarcinoma. All listed methods are or will be used in service of compute that will be released publicly.*
