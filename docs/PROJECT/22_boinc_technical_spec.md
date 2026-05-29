# BOINC Technical Specification — Integrating Two External Research Reports

> The user obtained two independent deep-research reports (saved at `sources/external_research/1Search - deep-research-report.md` and `sources/external_research/2search - deep-research-report.md`) before this session. Together they represent hundreds of grounded web searches across BOINC, virtual screening, KRAS biology, and PDAC public data. This doc reconciles them against our work and extracts the concrete engineering specifications they add.

## Convergence — both reports independently agreed with our plan

| Decision | Our plan | External reports | Status |
|---|---|---|---|
| #1 PDAC target | KRAS G12D switch-II pocket | KRAS G12D switch-II pocket | **Triple-confirmed** |
| Primary BOINC workload | Ultra-large virtual screening | Ensemble virtual screening | **Triple-confirmed** |
| Production docking kernel | AutoDock Vina (+ GNINA rescore) | AutoDock Vina first, AutoDock-GPU + GNINA second | **Triple-confirmed** |
| Receptor anchor structure | PDB 7RPZ (KRAS G12D + MRTX1133) | PDB 7RPZ | **Triple-confirmed** |
| Deployment style | Native binaries; Docker selectively | Native first, Docker/VM fallback | **Triple-confirmed** |
| Data on volunteers | Public-only (PDB + ZINC22 + ChEMBL/PubChem) | Public-only; no patient data on volunteers | **Triple-confirmed** |
| Architecture | Central prep → BOINC funnel → central rescoring | Same three-tier funnel | **Triple-confirmed** |

Two independent research efforts arriving at the same engineering choices as our own analysis is the best external validation we could ask for. Where they differ is in the *level of operational detail* — which is what this document captures.

## What the external reports add

### 1. BOINC Central as a free pilot host

Report 2 (§Executive summary, §Roadmap) calls out **BOINC Central** — a service that lets scientists use volunteer computing without running a full BOINC project. As of March 2026 it supports **Docker-packaged applications and AutoDock**.

**Implication for our plan:** before we stand up our own BOINC server (`PROJECT/04_proposal.md` § Track B, month 1), we should consider a **Pilot Zero on BOINC Central**. Time-to-first-volunteer compute would be weeks, not months. Same architecture, much less ops.

Action: investigate BOINC Central admission requirements and what AutoDock app they ship.

### 2. Specific work-unit specifications

Both reports converge on tight numbers that we lacked:

| Lane | Ligands/WU | Wall time target | Input size | Output size |
|---|---|---|---|---|
| **CPU alpha (Vina)** | ~500 | 30–90 min | ~5 MB (after sticky-file reuse) | ~0.5 MB |
| **GPU beta (AutoDock-GPU / GNINA)** | ~5,000 | 10–30 min | ~20 MB | ~1 MB |
| **Redundancy canary** | Identical, replicated | Same | Same | Same — for host trust |

**Ligand bucketing rule:** target wall time, not compound count. Bucket by heavy-atom count + rotatable-bond count + protonation/tautomer state count, because these are the three big drivers of Vina's per-ligand runtime.

### 3. Sticky files for receptor reuse

Receptor grids, conformer bundles, target metadata: **download once per volunteer host, reuse across many work units**. BOINC's `sticky_file` + locality scheduling exist exactly for this. Without it, ~3 receptor conformers × tens of thousands of work units × N volunteers = enormous wasted bandwidth.

Practical rule: anything reused across ≥10 work units gets sticky-cached. Ligand batches change per WU; receptor grids do not.

### 4. Compute budgets (engineering estimates, not benchmarks)

From report 1 §Recommended pilots:

| Tranche | Scale | Compute |
|---|---|---|
| **Validation burn-in** | 50K ligands × 2 targets × quorum 2 | ~5,000 CPU-hr |
| **Production Pilot 1** | 250K ligands × 3 targets | ~25,000–35,000 CPU-hr |
| **GPU rescoring of shortlist** | Top 10–20K ligands × 2–3 receptor states | ~500–1,000 GPU-hr |
| **Pilot scale (5M compounds)** | 15M docking evaluations | 30K CPU WUs OR 3K GPU WUs |
| **Expansion (50M compounds)** | 150M evaluations | 300K CPU WUs OR 30K GPU WUs |

Volunteer scale needed: **~300–1,000 CPU volunteers** + **~50–150 GPU volunteers**. At ~3,000 donated core-hours/day, the Pilot 1 production tranche is **~1–2 weeks wall time**.

That's a believable mid-tier BOINC project — comparable to early FightAIDS@home (`PROJECT/03_boinc.md` §6). Achievable.

### 5. The 4-layer validation ladder

Report 2 §Validation lays this out cleanly and matches what we'd been calling "positive controls + benchmark + biology check" — but more structured:

**Layer 1: Structural truth.**
- Redock the crystallographic ligand back into the prepared receptor
- Primary: PDB **7RPZ** (KRAS G12D + MRTX1133) — already our anchor
- **NEW:** orthogonal — PDB **6GJ7** (KRAS G12D pocket structure with a distinct ligand class)
- Use wwPDB validation reports for both
- Reject any receptor-prep settings that can't recover the native pose

**Layer 2: Retrospective ligand discrimination.**
- Curated KRAS gold standard from **ChEMBL** + **BindingDB** + **PubChem BioAssay**
- Strict categorization: **confirmed actives** vs **assay-matched inactives** vs **unknowns**
- **Never** treat "not reported" as inactive (huge source of false confidence)

**Layer 3: Benchmark calibration — with explicit caveats.**
- **DUD-E**: useful only for engine/pipeline sanity checks, NOT KRAS-specific proof
- **LIT-PCBA**: ⚠️ a 2025 audit found severe data leakage and redundancy. Use only as historical secondary benchmark; do NOT cite as decisive evidence of screening quality.
- This is new for us — our existing docs (`PROJECT/17_computational_methods.md`) don't flag the LIT-PCBA issue. Updating below.

**Layer 4: Orthogonal biological relevance.**
- Join ranked hits against PDAC public biology
- **TCGA-PAAD / NCI PDAC study** (185 cases, 12,853 files) — confirm target centrality
- **CPTAC PDAC** via PDC (~29 TB managed per ICF, the PDC implementation partner — ~785 TB cumulative downloads; PDAC subset smaller) — proteogenomic context. [Note: external reports cited "70 TB," which `PROJECT/23_external_research_verification.md` could not confirm against any authoritative source.]
- **DepMap 24Q2 Public** (23.31 GB, CC BY 4.0) — cell-line dependency structure
- **PRISM** — public drug-response context for known analogs
- **AACR Project GENIE pancreatic portal** — variant landscape cross-check (**this one is new to our plan**)

**Success criteria:** a compound that ranks high on only one layer gets downgraded. Robust hits should be plausible across at least 3 of 4 layers.

### 6. Validator implementation specifics

For each returned work unit, the validator should compare:

- **Ligand IDs and receptor version IDs** — exact match
- **Docking metadata** (parameters, seed) — exact match
- **Score vectors** — within tolerance windows (1 kcal/mol class)
- **Pose hashes or contact fingerprints** — within an allowed equivalence threshold

Replication strategy (BOINC primitive: adaptive replication):
1. Start conservative: replication factor 2–3 with plan-class-specific validators
2. Do **NOT** cross-compare CPU lane vs GPU lane outputs until you've empirically shown they're numerically equivalent
3. Once a `(host, app_version)` pair has clean validation history, allow adaptive replication to drop overhead toward 1

If floating-point differences across hardware matter, use **homogeneous redundancy**: only compare outputs from hardware in the same homogeneity class.

### 7. Security model

Report 1 §Security and report 2 §Security/governance both stress:

- **Code-signing key on offline, physically secured machine.** Never on the BOINC server itself. This is BOINC's standard defense against a compromised server turning volunteer hosts into malware delivery.
- **File model is immutable** — every signed app version has a fixed hash
- **Tokenized upload protections** + **output-size limits**
- **Sandbox** apps via unprivileged account on volunteer machines
- **Never execute user-supplied code paths on the server** (especially Python eval traps in result parsing)
- Promote every release through a **canary tier** before broad exposure

VM-fallback caveat: report 1 cites a BOINC VirtualBox cookbook example with a **1.9 GB VM image**. That's broad-volunteer-unfriendly. Stick to native binaries; VM only for exceptional cases.

### 8. Software stack (consolidated)

Both reports converge on the same stack we'd specified. Adding their license + role detail:

| Layer | Tool | License | Role |
|---|---|---|---|
| Receptor source | RCSB PDB + wwPDB validation reports | CC0 archive | Primary structural truth |
| Ligand library | ZINC20/ZINC22 subsets + ChEMBL + PubChem (curated) | Public; ChEMBL is CC BY-SA 3.0 | Make-on-demand + bioactivity priors |
| Ligand/receptor prep | RDKit + **Meeko** (Forli lab) | BSD / open | PDBQT inputs for Vina/AD-GPU; SDF outputs; centralize this |
| CPU docking | **AutoDock Vina 1.2.x** | Apache 2.0 | The volunteer kernel |
| GPU docking | **AutoDock-GPU** | GPL-2 / LGPL-2.1 | Batched GPU lane (later phase) |
| Secondary rescoring | **gnina** | Dual GPL / Apache | CNN-based; keep centralized (avoids GPL pulling Vina lane) |
| Pocket detection | **P2Rank** (MIT) + **fpocket** (MIT — verified at https://github.com/Discngine/fpocket/blob/master/LICENSE; an earlier audit pass incorrectly flagged this as GPL-3 and a subsequent verification confirmed MIT) | MIT | Target triage; small CPU jobs |
| Server orchestration | Nextflow + Docker / Apptainer | Apache | Reproducible central workflows only — NOT volunteer payload |
| MD refinement (later) | OpenMM, optionally GROMACS | MIT / LGPL | After hit-list pruning to ~100 leads |

Note the GPL boundary: **gnina is GPL**; if we use it volunteer-side we have to ship it as a separable executable, not link it into a larger Apache-licensed binary. Safer to keep gnina centralized for rescoring of returned poses.

### 9. Pilot roadmap from the external reports

Report 1's roadmap (June 2026 → March 2027) and report 2's roadmap (June 2026 → June 2027) align closely. Distilled:

| Month | Phase | What |
|---|---|---|
| Month 1 (Jun 2026) | Foundation | Target freeze, public KRAS structure set assembly, validation set curation, BOINC server bootstrap |
| Months 2–3 | Core engineering | Ligand prep + workunit packer, native CPU Vina app, validator, assimilator, central rescoring |
| Months 4–5 | Alpha | Limited pilot on **BOINC Central** or private testers; analyze redundancy and error rates |
| Months 6–7 | Scale-up | Add GPU lane; run 5M-compound pilot screen |
| Months 8–10 | Public launch | Public documentation, volunteer onboarding, 50M-compound production campaign |
| Months 11–13 | Translation | Release ranked hit package, benchmark report, hand off shortlist for experimental testing |

This is slower than our `PROJECT/04_proposal.md` roadmap suggested (which had a public launch at month 4). The external reports' pacing is probably more realistic — the user's M4 Max work in `PROJECT/21_local_test_plan.md` can compress the alpha phase but not the scale-up.

### 10. Success metrics

| Dimension | Metric | Target |
|---|---|---|
| Structural quality | Redocking RMSD + contact recovery on PDB 7RPZ/6GJ7 | <2 Å, D12 + Y96 contacts preserved |
| Screening performance | EF1%, EF5%, BEDROC, PR-AUC, ROC-AUC on curated KRAS sets | Materially better than random; stable across reruns |
| Biological coherence | Agreement with TCGA/CPTAC/DepMap/PRISM | Top chemotypes plausible in PDAC context |
| BOINC operations | Validator pass rate, error rate, turnaround, bandwidth per 1M dockings | <5% invalid after burn-in; manageable bandwidth |
| Volunteer health | Active hosts, retention, median WUs/host | Stable or growing after public launch |
| Reproducibility | Concordance across app versions, reruns, central rescoring | Rankings stable under pinned environment |

## Where our docs need updating (deltas only)

### `PROJECT/17_computational_methods.md` — add LIT-PCBA caveat
LIT-PCBA was originally drawn from PubChem BioAssays and looked attractive as a public benchmark. The 2025 audit (cited in external report 2) found severe data leakage + redundancy. **Use as historical secondary only; never as decisive evidence.** Our existing 17_computational_methods.md treats it as a credible benchmark. Flag this.

### `PROJECT/30_kras_structural_biology.md` — add PDB 6GJ7 as orthogonal target
We already use **7RPZ** as the anchor (KRAS G12D + MRTX1133). Both external reports recommend **6GJ7** as the orthogonal pocket-validation target — distinct ligand class, distinct binding mode. Add to the receptor ensemble for Tier 0 validation (`PROJECT/21_local_test_plan.md`).

### `PROJECT/21_local_test_plan.md` — adopt the work-unit sizing
Our local test plan ran ~1000 ligands as Tier 0. Scale-up to BOINC Central pilot should use the report's **500-ligand CPU work units** as the volunteer-facing unit shape from day one. Same scoring, same outputs — sized so each volunteer's 30–90 min runtime is what they actually see.

### `PROJECT/04_proposal.md` and `PROJECT/20_synthesis.md` — pilot phase
The original plan went own-BOINC-server immediately. Updated plan: **Pilot Zero on BOINC Central first** (fastest path to first volunteer compute), then own server only after Pilot Zero proves operations. Doesn't change the long-term shape, just the first 2–3 months.

## New tasks unlocked by the external reports

1. **Investigate BOINC Central admission**: what does it take to get our app onboarded? What AutoDock version do they support? What's their workunit packaging convention?
2. **Curate the KRAS gold-standard set**: pull KRAS-bound actives from ChEMBL + BindingDB + PubChem BioAssay; classify into confirmed actives / matched inactives / unknowns. This is a discrete project that doesn't require BOINC and can happen in parallel with local pipeline work.
3. **Audit LIT-PCBA**: read the 2025 audit paper, decide whether any subset is still usable, document our position publicly so other researchers don't trip on the same data leakage.
4. **AACR Project GENIE pancreatic portal pull**: verify the variant landscape against TCGA-PAAD; identify any high-frequency variants we should add to the target panel beyond KRAS G12D.

## Open questions the external reports don't resolve

1. **How does BOINC Central actually work for new science projects?** Both reports cite it as fastest path but neither has admission details for new researchers. Worth a direct inquiry.
2. **Numerical consistency across heterogeneous hardware.** Vina is largely deterministic with a fixed seed, but cross-arch floating-point differences exist (ARM vs x86 vs CUDA vs OpenCL). Need real data — and homogeneous redundancy until we have it.
3. **GNINA GPL contagion.** If we ship a single binary that combines Vina (Apache 2.0) + GNINA scoring (GPL via OpenBabel), the whole thing becomes GPL. Mitigation: ship as separable executables.
4. **Replacement for LIT-PCBA.** No clean replacement benchmark exists for ultra-large VS calibration. May need to build our own KRAS-focused benchmark from ChEMBL/BindingDB, publish it openly.

## Bottom line

The two external reports give us ~80% of a build-spec we didn't have. Combined with our existing science deep dives (~80,000 words) and local pipeline plan, we now have what's needed to actually start writing code. The technical risks are well-understood; the science risks are well-understood; the deployment path has two parallel options (BOINC Central pilot, own-server scale-up); the validation strategy is rigorous and 4-layered.

Best next concrete deliverables — when the user is ready:

1. **A KRAS gold-standard active/inactive set** curated from ChEMBL/BindingDB/PubChem. No BOINC needed.
2. **A working Vina pipeline locally** on the M4 Max (`PROJECT/21_local_test_plan.md` Tier 0), validated against MRTX1133 self-docking AND a 6GJ7 ligand.
3. **A BOINC Central admission inquiry** — find out what onboarding actually requires.

Each of these can happen independently, in parallel.
