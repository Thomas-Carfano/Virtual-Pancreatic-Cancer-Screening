# Synthesis: What 8 Deep Dives Changed About the Project

> This document integrates the eight deep-dive research files (`10_*` through `17_*`) into a refined recommendation. The original proposal (`04_proposal.md`) still stands — this sharpens the pipeline, expands the target panel, adds three new tracks the field has revealed are computationally bottlenecked, and gives realistic budget numbers.

## TL;DR

1. **Keep the two-track plan.** Folding@home partnership for molecular dynamics + a new BOINC project (PancScan@home) for ultra-large virtual screening.
2. **The pipeline is now specific.** A 6-stage cascade — AlphaFold3/Boltz-1 → MD ensembles → active-learning Vina/Uni-Dock → GNINA CNN rescoring → Boltz-2 affinity → OpenFE RBFE — built entirely from open-source tools and feasible at ~50K active volunteer hosts.
3. **Active learning is load-bearing.** Without it, 70B compounds × 50 conformations is infeasible. With it (dock 1%, predict 99%), it's ~100× cheaper and runs in months not decades.
4. **Three target families, not one.** KRAS variants (G12D, G12V, G12R, Q61H — together ~85% of PDAC), mutant p53 hotspots (R175H, R248Q/W, R273H, R282W, G245S — together ~50% of PDAC), and MYC-pathway proxies (BRD4, CDK9). All have open structural data and unsolved drug discovery problems.
5. **Three NEW computational tracks the deep dives surfaced** that weren't in the original proposal: personalized neoantigen prediction, TCR-pMHC modeling for KRAS×HLA combinatorics, and KRAS-inhibitor resistance prediction. These extend PancScan@home from "virtual screening" into a small portfolio of related compute campaigns.
6. **Budget is real and modest.** ~2.4M CPU-core-hours/yr + ~80K GPU-hours/yr + ~$15K cloud/yr at ~50K hosts. Achievable.

## What stays the same from `04_proposal.md`

- Two-track approach (F@h partnership + own BOINC).
- Open everything — MIT/Apache code, CC0 data, bioRxiv preprints.
- Ultra-large virtual screening is the right BOINC workload (proven by FightAIDS@home, OpenPandemics).
- World Community Grid stays a backup path, not primary — they're not currently soliciting external proposals (`PROJECT/03_boinc.md` §2).
- Wet-lab validation is downstream; we feed wet labs better starting points.

## What's sharper now

### 1. The PancScan@home pipeline (from `PROJECT/17_computational_methods.md`)

Pipeline as 6 stages, all open-source. Each stage filters down to the next:

```
┌─────────────────────────────────────────────────────────────────┐
│  Stage 1: Target structure ensemble                             │
│  AlphaFold3 / Boltz-1 → AlphaFlow → short OpenMM MD             │
│  Output: 20–100 conformations per target (CPU+GPU)              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  Stage 2: Active-learning virtual screening                     │
│  AutoDock Vina (CPU) + Uni-Dock-GPU + MolPAL / Deep Docking     │
│  Dock 1% of library → train surrogate → predict top 1% of rest  │
│  Output: top ~0.01% (~10M compounds from 100B) (CPU+GPU)        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  Stage 3: GNINA CNN rescoring                                   │
│  Rescore top hits with CNN-based scoring                        │
│  Output: top ~100K compounds (GPU)                              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  Stage 4: Boltz-2 affinity prediction                           │
│  MIT open-source 2025 model — Pearson ~0.62 vs FEP ~0.72 at     │
│  1000× lower cost. Reshapes everything downstream of docking.   │
│  Output: top ~5K compounds (GPU)                                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  Stage 5: Short MD binding validation                           │
│  10–100 ns MD per ligand-conformation pair to confirm pose      │
│  Output: top ~500 compounds (GPU heavy — F@h fit)               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  Stage 6: OpenFE RBFE                                           │
│  Open Free Energy Consortium — RMSE 1.73 kcal/mol parity with   │
│  commercial FEP+. Run on ~30–100 leads.                         │
│  Output: ranked leads → wet lab (cloud-rented or large GPUs)    │
└─────────────────────────────────────────────────────────────────┘
```

Stages 1–4 fit volunteer compute cleanly. Stage 5 fits Folding@home better (their MD strength). Stage 6 likely runs on rented cloud GPUs — only hundreds of jobs, so ~$15K/year is enough.

### 2. Why active learning matters

Naive docking math: 10B compounds × 1 conformation × 5 sec/CPU = 50B CPU-seconds ≈ **~14M core-hours** (≈ 1,600 core-years). (Earlier draft said "50B core-hours ≈ 5M CPU-years" — unit error of ~3,500× corrected per audit L. The qualitative point — that naive docking against an ultra-large library is infeasible without active learning — stands.) With 50K volunteer hosts running ~8 hr/day, that's still ~340 years.

Active learning (MolPAL / Deep Docking pattern):
- Dock random 1% (~100M)
- Train a graph-neural-network surrogate on those scores
- Predict scores for the remaining 99%
- Re-dock the predicted top 1% (~100M)
- Iterate 3–5 rounds

Recovery: ~90% of true top hits in <5% of the compute. The 5M CPU-years drops to ~250K core-years — and at 50K hosts × 8 hr/day, that's ~5 years for a 10B library, ~3 months for ZINC22 in-stock subset (~5B). Tractable.

### 3. Hybrid CPU+GPU workunits

Different stages prefer different hardware. We don't pick "CPU-first" or "GPU-first" — we let workunits self-assign.

| Stage | Hardware | Per-WU runtime | Credit weight |
|---|---|---|---|
| 1 (AlphaFold/Boltz/MD) | GPU + 8–32GB RAM | ~30–60 min | 10× |
| 2 (Vina) | CPU, low RAM | ~10–20 min | 1× |
| 2 (Uni-Dock-GPU) | GPU | ~5–15 min | 1.5× |
| 3 (GNINA rescore) | GPU | ~5–10 min | 2× |
| 4 (Boltz-2 affinity) | GPU + 8GB RAM | ~5–15 min | 3× |

This matches BOINC's existing credit model and lets volunteers contribute whatever hardware they have.

## What's new — three additional tracks the deep dives surfaced

The original proposal was virtual-screening focused. The deep dives revealed three more compute-bottlenecked PDAC problems that fit volunteer compute and tap the same infrastructure. These become parallel "tracks" of PancScan@home, sharing the BOINC server, app sandbox, and validation infrastructure.

### Track 2 — Personalized neoantigen prediction (from `PROJECT/14_immunotherapy.md`)

**The clinical fact.** Autogene cevumeran (BioNTech/Genentech personalized mRNA neoantigen vaccine) gave 8/16 PDAC patients durable T-cell responses with no recurrence at 3+ years. ELI-002 (Elicio KRAS amphiphile vaccine) showed 99% mKRAS-specific T-cell response in AMPLIFY-7P. The 2022 NEJM landmark case showed TCR-T against mutant KRAS G12D produced a 72% partial response in a metastatic patient.

**The compute bottleneck.** Every personalized neoantigen vaccine needs:
1. Predict which patient mutations generate strong MHC-binding peptides (NetMHCpan, MHCflurry).
2. Predict immunogenicity (BigMHC, PRIME, others).
3. Rank peptides for inclusion in the vaccine.

Current prediction accuracy plateaus around AUROC 0.85 because training data is small. Volunteer compute could:
- Run massive in-silico expansion of MHC × peptide pairs to generate synthetic training data.
- Train ensembles of MHC-binding predictors with hyperparameter searches at scale.
- Maintain an open neoantigen prediction service that any researcher can call.

**Workload.** Mostly inference + hyperparameter search (CPU+GPU). Small per-WU runtime (~1–5 min). Validates against autogene cevumeran responder/non-responder data once published.

### Track 3 — TCR-pMHC modeling for KRAS × HLA combinatorics

**The clinical fact.** Mutant KRAS (G12D, G12V) generates a neoantigen peptide that's presented by HLA class I in some patients. The Rosenberg NEJM 2022 case used HLA-C\*08:02 to present the KRAS G12D peptide. But which HLA alleles can present which mutant KRAS peptides? And how strongly?

**The compute bottleneck.** ~6000 common HLA alleles × ~10 KRAS mutation variants × ~10 surrounding peptide windows = ~600K HLA-peptide pairs to model with high-fidelity structural prediction (AlphaFold-Multimer, RoseTTAFold-All-Atom). Then TCR specificity prediction adds another layer.

**Why this matters.** A complete HLA × mKRAS map would tell which patients are candidates for off-the-shelf KRAS TCR-T (most economical immunotherapy modality) and which need fully personalized vaccines. This could expand the population eligible for the NEJM-style response from ~3% (HLA-C\*08:02 carriers) to potentially 40%+ of PDAC patients.

**Workload.** AlphaFold-Multimer-style structure prediction per HLA-peptide pair (GPU, ~5–30 min per WU). Embarrassingly parallel.

### Track 4 — KRAS-inhibitor resistance prediction

**The clinical fact.** RMC-6236 (daraxonrasib) achieved 29% ORR across any RAS mutation in 2025 trials; RMC-9805 (G12D-specific) hit 30% ORR in Phase 1. The drugs are working. But resistance is starting to be observed — switch-II pocket secondary mutations, KRAS amplification, RTK reactivation, lineage switching (`PROJECT/15_targeted_therapy.md` §2.5).

**The compute bottleneck.** We want to know, *before* clinical resistance emerges:
- Which secondary KRAS mutations will confer resistance to G12C inhibitors, G12D inhibitors, and pan-RAS tri-complex inhibitors?
- Which bypass pathways are accessible from a given baseline mutation?
- Which combination drugs would resist resistance?

**Method.** Long-timescale all-atom MD on KRAS variant + drug + secondary mutation complexes, looking for energetically-accessible resistance configurations. Folding@home is perfect for this (their KRAS-VHL E3 ligase work in 2024–25 is exactly the same flavor of question).

**Workload.** MD trajectories of ~100 ns – 1 µs per mutation × drug combination. GPU-heavy, ideal F@h work. We don't host this — we partner with F@h (Track A of `04_proposal.md`) and contribute funding + a curated mutation list.

## Refined target panel

The original proposal said "KRAS G12D switch-II pocket + published cryptic sites." The deep dives expanded this:

### Tier 1 (months 1–6, initial PancScan@home)
| Target | PDAC frequency | Why now |
|---|---|---|
| KRAS G12D switch-II + cryptic sites | ~40% | MRTX1133 / RMC-9805 prove the pocket is real; resistance is forming and combination drugs needed |
| KRAS G12V switch-II | ~30% | Similar pocket; no approved drug yet |

### Tier 2 (months 6–12, after pipeline is proven)
| Target | PDAC frequency | Why |
|---|---|---|
| KRAS G12R | ~12% | PDAC-enriched; no approved drug |
| KRAS Q61H | ~5% | Distinct from G12; rare in lung, common-ish in PDAC |
| Mutant p53 R175H | ~3% PDAC (~5–6% of TP53-mutant PDAC; largest structural-mutant) | Structural mutant; ZMC1 + cryptic-pocket work suggests druggable. (Earlier draft said "~10%" — corrected per audit L; literature consensus is ~3% PDAC overall) |
| Mutant p53 R273H | ~7% | Contact mutant; restoration via APR-246 partially works |
| Mutant p53 R248Q/W | ~7% | Contact mutant |
| Mutant p53 Y220C | ~1% (smallest but reference) | Use as positive control — rezatapopt is a known binder |
| Mutant p53 G245S | ~3% | Structural mutant |

### Tier 3 (year 2+)
| Target | Rationale |
|---|---|
| BRD4 / CDK9 (MYC indirect) | MYC is undruggable directly; BET / CDK9 hit MYC indirectly |
| FAP (stromal) | FAP-targeted radioligand therapy (FAPI-PET, FAP-2286, etc.) shows PDAC stroma uptake; small-molecule FAP inhibitors active. (Earlier draft cited zenocutuzumab here — that's wrong: zenocutuzumab is an NRG1-fusion HER2×HER3 bispecific, NOT a stromal drug. Corrected per audit L.) |
| CXCR4 | Stromal axis; mobilization of effector T cells |
| HAS2/HAS3 (hyaluronan) | PEGPH20 failed as a drug; small-molecule HAS inhibitors are open |
| Claudin 18.2 (allosteric binders) | Zolbetuximab proves the target is real |

This panel covers ~85% of PDAC mutational diversity in tier 1+2 and addresses both tumor-cell-intrinsic (KRAS, p53, MYC) and microenvironmental (FAP, CXCR4, HAS, claudin) drug-discovery problems.

## Budget — realistic numbers

From `PROJECT/17_computational_methods.md`, the computational methods deep dive estimated:

| Resource | Annual need (PancScan@home v1, KRAS G12D + G12V) |
|---|---|
| CPU-core-hours | ~2.4M |
| GPU-hours | ~80K |
| Cloud (OpenFE RBFE on top leads) | ~$15K |
| Storage (compound library + hit DB + structures) | ~5 TB |
| Bandwidth (workunit distribution) | ~50 TB/yr egress |
| BOINC server (Hetzner / OVH bare-metal) | ~$200/month |

At ~50K active volunteer hosts (a believable mid-sized BOINC project, between FightAIDS@home and OpenPandemics in scale), this is feasible in a single year.

User-funded costs (server + cloud + storage): roughly **$5K–10K/year for server + cloud, $5K–10K/year for storage/CDN**. Total all-in: **$10K–20K/yr** to run PancScan@home v1 end-to-end. Wet-lab validation (if not partnered) adds another ~$50K–200K depending on assay tier.

(For comparison: a single relative-binding-free-energy calculation in commercial Schrödinger FEP+ costs ~$50–100 of cloud GPU and ~1 hr researcher time. We'd be running thousands of these for free via OpenFE.)

## What we should NOT do

Discovered during the deep dives:

- **Don't try to train ML models from scratch on volunteer compute.** Latency, churn, and heterogeneity make distributed gradient training infeasible (Petals/Hivemind work for inference, not training). If we need a trained model, train it on a single big GPU box; volunteer compute runs inference at scale.
- **Don't promise a clinical decision-support tool.** PDAC is too heterogeneous, our outputs are too far upstream, and we don't have access to patient-level data. We're a discovery engine, not a diagnostic.
- **Don't replicate Folding@home's MD pipeline.** They've spent 20 years optimizing it. Partner instead.
- **Don't go after MSI-high PDAC alone.** It's ~1% of PDAC and already has pembrolizumab. The compute leverage is in the 99% MSI-stable population.
- **Don't try to win on chemistry quality vs. pharma.** Their compute is bigger and their chemists are better. We win on *openness, scale, and breadth*. The data + code + hit lists going into the open archive is the product.

## Where the deep dives raised new questions

Things I should investigate further before committing:

1. **Can we get patient-derived organoid screen data?** The Tuveson lab and HUB Organoid Biobank have hundreds of PDOs with drug-screening data (`PROJECT/16_research_models.md` §3). If even subset is public or share-able, our virtual hits could be ranked against organoid responses — much higher signal-to-noise than computational scoring alone.
2. **How accessible is autogene cevumeran responder data?** Anonymized peptide-level immunogenicity data would massively improve neoantigen prediction (Track 2). Worth contacting BioNTech / MSKCC.
3. **Is there a NOD biobank we could partner with for early-detection ML?** END-PAC, PRECEDE, and various academic biobanks exist (`PROJECT/11_risk_factors.md`). A long-term play.
4. **PANORAMA / PANDA CT radiomics datasets** — public, sized for ML, and pancreatic-CT-focused. If we wanted to add a fifth track (radiomics), this is the substrate.

## Updated roadmap

### Month 1
- [ ] **Project brand + domain.** Pick a name (PancScan@home is fine, alternatives include PancCure@home, PDAC@home, OpenPanc).
- [ ] **Send Folding@home partnership pitch** to **Huang (UW-Madison — the lab that actually ran the 2024–25 KRAS-VHL F@h work)**, Chodera (MSKCC), Bowman (Wash U / Penn), and F@h leadership. Specifically propose KRAS G12D + drug + secondary-mutation MD as a campaign. Use Track 4 (resistance prediction) as the scientific hook.
- [ ] **Stand up `boinc-server-docker`** on Hetzner / OVH. Get a hello-world workunit through end-to-end.
- [ ] **Build initial KRAS G12D conformational ensemble.** Use published MD trajectories from Bowman/Chodera labs as seed; expand with AlphaFold3 + AlphaFlow.

### Month 2
- [ ] Build the **docking app** (Stage 2): AutoDock Vina + Uni-Dock-GPU + GNINA, packaged in Docker for Linux x86_64, Windows x86_64, macOS arm64.
- [ ] Build the **workunit pipeline**: generator, validator, assimilator. Use BOINC's standard replication-consensus model.
- [ ] Stage **ZINC22 "in-stock"** subset (~5B → ~55B as of Sept 2025) chunked into 10K-compound batches.
- [ ] Public hit-list Postgres + downloadable Parquet snapshots.

### Month 3
- [ ] **Closed beta** with ~10 friendly volunteers; 10K workunits end-to-end.
- [ ] **Positive controls**: confirm MRTX1133, RMC-6236, RMC-9805 rank in top 1% on our KRAS G12D pipeline. Confirm rezatapopt ranks in top 1% on p53 Y220C.
- [ ] **Project website**, Discord/forum, license docs.

### Month 4 — public launch
- [ ] Register with **Science United**.
- [ ] List on **boinc.berkeley.edu/projects.php**.
- [ ] Press: r/BOINC, Hacker News, PanCAN Discord, Wikipedia article.
- [ ] Goal: 1K active volunteers by month 5, 10K by month 9, 50K by year 2.

### Months 5–9 — scale + Tier 2 targets
- [ ] Add KRAS G12V/G12R/Q61H targets.
- [ ] Add mutant p53 R175H, R273H, R248Q targets.
- [ ] Layer **Boltz-2 affinity** (Stage 4) as a workunit type.
- [ ] Begin **active learning** loops (Deep Docking / MolPAL).

### Months 9–18 — open the new tracks
- [ ] **Track 2 (Neoantigen prediction)** — build MHC-binding workunits using NetMHCpan / MHCflurry. Reach out to BioNTech / MSKCC about responder data.
- [ ] **Track 3 (TCR-pMHC modeling)** — build HLA-peptide structural prediction workunits.
- [ ] **Track 4 (KRAS resistance MD)** — feed F@h with our curated mutation panel (assuming the F@h partnership lands).

### Year 2+
- [ ] **Wet-lab partner** for top-100 hit validation. PanCAN, an academic pharmacology lab, or a CRO.
- [ ] **First open hit-list bioRxiv preprint.** Standard "ultra-large VS against KRAS G12D + cryptic sites" paper.
- [ ] **NOD risk-prediction collaboration** (longer-term — needs EHR access).
- [ ] **CT radiomics pilot** on PANORAMA/PANDA (longer-term — needs ML training infrastructure off-volunteer).

## Final notes

The deep dives confirmed every claim from `04_proposal.md` and sharpened them substantially. The biggest single change: the field is moving fast enough that by the time PancScan@home v1 launches (month 4), daraxonrasib will likely have Phase 3 readouts and we'll know whether pan-RAS inhibition is broadly working in PDAC. If it is, resistance prediction (Track 4) becomes the highest-leverage thing we can do. If it isn't, we need new chemical matter against KRAS G12D — which is exactly what Track 1 (virtual screening) provides.

Either way, this project has the right shape for the moment.

---

## Cross-references

For depth on any topic, see the corresponding deep-dive file:

- Epidemiology, "silent disease" — `PROJECT/10_epidemiology.md`
- Hereditary + modifiable risk — `PROJECT/11_risk_factors.md`
- Diagnosis + staging — `PROJECT/12_diagnosis_staging.md`
- Surgery + chemo + radiation — `PROJECT/13_treatment_landscape.md`
- Immunotherapy + cellular therapy — `PROJECT/14_immunotherapy.md`
- Targeted therapy + subtypes + scRNA — `PROJECT/15_targeted_therapy.md`
- Research models (wet + in silico) — `PROJECT/16_research_models.md`
- Computational drug discovery state of the art — `PROJECT/17_computational_methods.md`
