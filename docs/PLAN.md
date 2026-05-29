# PancScan@home
### A volunteer-computing project against pancreatic cancer

| | |
|---|---|
| **Author** | Thomas Carfano (tomcarfano@gmail.com) |
| **Date** | 2026-05-22 |
| **Status** | Planning document. Nothing has been built yet. |
| **License** | All code MIT/Apache; all data CC0 or CC-BY; all preprints on bioRxiv. No IP retained. |
| **What I'm asking you for** | An expert eye on the science and engineering. The seven questions in §8 are where your feedback most changes the plan. |
| **How to read this** | The 80-word pitch is in §1. If that interests you, §2–5 are the substance. Skim §6–7 for risks and scope. §8 is the ask. §9 documents what's been verified. |
| **Supporting research** | ~85,000 words across 25 deep-dive documents in `PROJECT/`; verification record at `PROJECT/25_full_audit_synthesis.md`. |

---

## 1. At a glance

I'm self-funding an open, BOINC-style volunteer-compute project that will run ultra-large virtual screening (≥10⁹ compounds) against the highest-leverage druggable pancreatic-cancer targets — starting with the KRAS G12D switch-II pocket — and feed every hit back to the public as open data. Everything published goes onto bioRxiv. All code is MIT/Apache. The science begins on my laptop, scales to BOINC Central, then to a dedicated server. I'm asking you to find errors in the plan and tell me where it should change before any code is written.

---

## 2. Why pancreatic cancer, and why now

### 2.1 The disease

Pancreatic ductal adenocarcinoma (PDAC) became the **3rd leading cause of US cancer death in 2026** (~67,530 new cases per the American Cancer Society 2026 *Cancer Facts & Figures*), with 5-year survival ~13% across all stages. It is genetically simple: ~93% of tumors carry mutated *KRAS* (G12D in ~40% of cases), with frequent additional hits in *TP53* (~65–75%), *CDKN2A* (~42%), and *SMAD4* (~30%). Two structural features make it uniquely hard to treat:

- **The desmoplastic stroma.** 80–90% of a PDAC tumor by volume is not cancer cells — it's a collagen + hyaluronan scaffold that physically blocks ~80–90% of drug molecules from reaching the malignant cells. This is why standard chemotherapy works so poorly.
- **Immune cold.** PDAC has only ~2–3 mutations per megabase (vs ~10–100 in melanoma), few neoantigens, and active immune exclusion. Single-agent checkpoint inhibitors fail outside the ~1% MSI-high subset.

### 2.2 What changed

For 30 years KRAS was considered undruggable. As of 2026:

- **G12C is FDA-approved** (sotorasib 2021, adagrasib 2022, divarasib in Phase 3) — but only ~1–2% of PDAC carries G12C, so this is mostly NSCLC/CRC.
- **G12D is now drug-able** but the field is still finding the right molecule. MRTX1133 was the structural proof-of-concept (Wang et al. *J Med Chem* 2022; KD ~0.2 pM; 700× selectivity over WT). The Phase 1/2 study (NCT05737706) was **terminated before Phase 2** in early 2025; the **registry reason on ClinicalTrials.gov is "formulation challenges," while secondary reporting has cited variable/suboptimal pharmacokinetics**. Either way, MRTX1133 remains the canonical preclinical proof-of-concept for the G12D switch-II pocket and the best self-docking positive control for our pipeline. Live G12D-targeted clinical assets from other sponsors: **RMC-9805 / zoldonrasib** (Revolution Medicines; Phase 1 ORR 30%, DCR 80%), **ASP3082** (Astellas), **HRS-4642** (Hengrui), **INCB161734** (Incyte).
- **Pan-RAS** **RMC-6236 / daraxonrasib** is in Phase 3 (RASolute 302/303) and could shift the entire PDAC standard of care in the next 12–24 months.
- **Personalized neoantigen vaccines** produced real signals: BioNTech/Genentech's autogene cevumeran (Rojas et al. *Nature* 2023, NCT04161755) gave 8 of 16 PDAC patients durable T-cell responses with no recurrence at 3+ years.
- **Adoptive T-cell therapy against mutant KRAS G12D** produced a 72% partial response in one metastatic PDAC patient (Leidner et al. *NEJM* 2022, HLA-C\*08:02).

### 2.3 What's still compute-bottlenecked

Three problems are well-defined, computationally tractable, and not currently being solved by any volunteer-compute project for PDAC:

1. **New chemical matter against KRAS G12D, G12V, G12R, Q61H** — ultra-large library screens against MD-derived conformational ensembles.
2. **KRAS inhibitor resistance prediction** — long-timescale MD on KRAS + drug + emerging secondary mutations, before clinical resistance is observed.
3. **Mutant p53 hotspot stabilizers**, especially R175H — cryptic-pocket discovery + ensemble docking against a target with no approved drug.

These map naturally onto two volunteer-compute platforms that have a 20-year track record of producing peer-reviewed cancer science: BOINC (massive virtual screening pattern — FightAIDS@home, OpenPandemics) and Folding@home (all-atom MD pattern — recent KRAS-VHL E3 ligase work by Qiu et al. *JACS Au* 2024 at the Huang lab, UW-Madison).

---

## 3. What I'm proposing

### 3.1 Two tracks that feed each other

| Track | What it does | Where it runs | Time to first result |
|---|---|---|---|
| **A: Folding@home partnership** | Long-timescale all-atom MD on KRAS G12D + drug + emerging resistance mutations; cryptic-pocket discovery on mutant p53 R175H | Existing F@h infrastructure (~1.2M volunteer GPUs) | 3–6 months after partnership letter |
| **B: PancScan@home** | Ultra-large virtual screening (≥10⁹ compounds) against an expanding panel of PDAC drug targets | New BOINC project, pilot-hosted on **BOINC Central** then on dedicated server | 6–9 months to public alpha |

Track A produces MD-derived conformational ensembles. Track B screens compounds against those ensembles. Top Track B hits get returned to F@h for pose-dynamics validation. Both are open data.

### 3.2 The 6-stage pipeline (all open-source)

```
Stage 1 → Target ensemble        AlphaFold3 / Boltz-1 + AlphaFlow + OpenMM MD       (CPU+GPU)
Stage 2 → Virtual screening      AutoDock Vina + Uni-Dock-GPU + MolPAL active learn (CPU+GPU)
Stage 3 → CNN rescoring          GNINA (server-side only — GPL via OpenBabel)       (GPU)
Stage 4 → Affinity prediction    Boltz-2  (Pearson 0.62 vs FEP+ 0.72, 1000× cheaper)(GPU)
Stage 5 → MD validation          OpenMM   (10–100 ns / lead-pose)                   (GPU)
Stage 6 → Free-energy ranking    OpenFE RBFE  (RMSE 1.73 kcal/mol vs commercial FEP)(cloud)
```

Stages 1–4 fit volunteer compute. Stage 5 fits Folding@home better. Stage 6 is best run on rented cloud GPUs (~$50–100/lead; ~$15K/yr total).

### 3.3 Why active learning is the difference between feasible and infeasible

Naive math: 10¹⁰ compounds × 1 conformation × 5 sec/CPU-core ≈ 14M core-hours (≈ 1,600 core-years).

With active learning (Graff et al. MolPAL pattern; Gentile et al. Deep Docking):

1. Dock a random 1% of the library (~100M compounds).
2. Train a graph-neural-network surrogate on those scores.
3. Predict scores for the remaining 99%.
4. Re-dock the predicted top 1%.
5. Iterate 3–5 rounds.

Recovery: **~90% of the true top hits in <5% of the compute**. At 50K active volunteer hosts × 8 hr/day, a 10B-compound screen drops from infeasible to ~175 days; the ZINC22 in-stock subset (~5B) to ~3 months. This is the load-bearing assumption; if it fails, the project fails.

---

## 4. Targets and validation

### 4.1 Target tiers

**Tier 1 (months 1–6): KRAS G12D switch-II pocket.**
- **Anchor:** PDB **7RPZ** — KRAS G12D + MRTX1133 + GDP + Mg²⁺, 1.30 Å (Wang et al. 2022).
- **Orthogonal:** PDB **6GJ7** — KRAS G12D + BI-2852 + GppCp (GTP-mimetic active state), 1.67 Å. Orthogonality spans both ligand chemotype and nucleotide state.
- **Positive controls for docking validation:** MRTX1133, RMC-9805, BI-2852.

**Tier 2 (months 6–12).** KRAS G12V (~30% PDAC), G12R (~12%), Q61H. Mutant p53 Y220C (~1.5% — small population but the only mutation with a clinical-stage selective binder, **rezatapopt** at PMV Pharmaceuticals; PYNNACLE Phase 2 NCT04585750; anchor PDB **9BR4**). Mutant p53 R175H (~3% PDAC overall; the largest structural mutant with no approved drug — the real prize).

**Tier 3 (year 2+).** Mutant p53 R273H, R248Q/W (contact mutants; covalent docking arm). MYC indirect targets (BRD4, CDK9). Stromal targets (FAP via FAP-2286 and small-molecule FAP inhibitors; CXCR4; HAS2/HAS3).

Combined, Tiers 1+2 cover **~85% of PDAC mutational diversity**.

### 4.2 The 4-layer validation ladder

Both external research reports I commissioned and our own analysis converged on this structure. A hit must pass at least 3 of 4 layers before any wet-lab follow-up.

| Layer | What it checks | Tools / data |
|---|---|---|
| **1. Structural truth** | Redock the crystallographic ligand into the prepared receptor; recover <2 Å RMSD and key contacts (D12 salt bridge, Y96/H95 H-bonds for KRAS G12D) | PDB 7RPZ + 6GJ7 + wwPDB validation reports |
| **2. Curated actives discrimination** | Top compounds enriched over property-matched inactives — **never treat "not reported" as inactive** | ChEMBL + BindingDB + PubChem BioAssay (curated KRAS gold-standard set we'll publish openly) |
| **3. Benchmark calibration (with explicit caveats)** | Engine + pipeline sanity check | DUD-E only. **NOT LIT-PCBA** — the 2025 SieveStack audit (arXiv:2507.21404) documented severe data leakage; a memorization-only baseline matches state-of-the-art deep models on it. |
| **4. Orthogonal biology** | Top chemotypes plausible in PDAC biology | TCGA-PAAD + CPTAC + DepMap + PRISM + AACR Project GENIE BPC PANC v1.0 |

### 4.3 Numerical success criteria

- MRTX1133 self-docking RMSD < 2.0 Å vs 7RPZ crystal pose
- Curated actives enriched in top 1%: EF1% > 5, BEDROC > 0.4
- Cross-conformer rank correlation > 0.7 (concordance across the conformational ensemble)
- Top-100 novel hits sent to wet-lab partner: ≥5% confirmed binding (industry benchmark for ultra-large VS)

---

## 5. Engineering plan

### 5.1 Compute budget (engineering estimate, not vendor benchmark)

For PancScan@home v1 (KRAS G12D + G12V tier-1 panel, 50M-compound active-learning screen):

| Resource | Annual need |
|---|---|
| CPU-core-hours | ~2.4M |
| GPU-hours | ~80K |
| Cloud (OpenFE RBFE on top 30–100 leads) | ~$15K |
| Storage (compound library + hit DB + structures) | ~5 TB |
| Egress bandwidth | ~50 TB/yr |
| BOINC server (Hetzner / OVH bare-metal) | ~$200/mo |

At ~50K active volunteer hosts (mid-tier BOINC scale; between historical FightAIDS@home and OpenPandemics): production tranche of 5M-compound screen completes in **~1–2 weeks wall-clock**. User-funded all-in: **~$10–20K/yr**. Wet-lab confirmation of top hits, if separately commissioned: +$50–200K.

### 5.2 Tools, licenses, GPL boundaries

| Layer | Tool | License | Notes |
|---|---|---|---|
| Receptor source | RCSB PDB | CC0 | wwPDB validation reports for QC |
| Compound libraries | ZINC22 (~37B 2D / ~4.5B 3D) + Enamine REAL (~94.5B as of Apr 2026) | Public | Make-on-demand |
| Ligand/receptor prep | RDKit + Meeko (Forli lab) | BSD / open | Centralized; volunteers get prepared inputs |
| CPU docking | AutoDock Vina 1.2.x | Apache 2.0 | The volunteer kernel |
| GPU docking | AutoDock-GPU / Uni-Dock-GPU | GPL-2/LGPL-2.1 | Second wave |
| CNN rescore | gnina | Dual GPL/Apache (**GPL via OpenBabel**) | **Keep server-side only** — separable from the Apache Vina volunteer binary |
| Pocket detection | P2Rank + fpocket | MIT (both) | QC + target triage |
| Affinity prediction | Boltz-2 | MIT | Pearson 0.62 at 1000× lower cost than FEP |
| MD | OpenMM | MIT + LGPL | On Apple Silicon use OpenCL platform (no native Metal in upstream OpenMM) |
| Free energy | OpenFE 1.7 | open | RMSE 1.73 kcal/mol on Dec 2025 ChemRxiv public benchmark |

GPL boundary management is real and explicit: if we ship a single bundled binary that combines Vina (Apache) + gnina (GPL via OpenBabel), the whole thing becomes GPL. We avoid this by keeping gnina server-side rescoring only — volunteers run Apache-licensed Vina, never the GPL pipeline.

### 5.3 Local-first deployment on Apple Silicon

My machine is a MacBook Pro M4 Max — 128 GB unified memory, 16 cores, Apple Silicon GPU. About 3–4× more capable than the median BOINC volunteer host in everything except CUDA-specific compute. The full pipeline runs locally, with these realistic caveats:

| Stage | M4 Max behavior |
|---|---|
| 1. Boltz-1 + OpenMM ensemble | Native; Boltz via PyTorch MPS, OpenMM via OpenCL platform |
| 2. Vina + RDKit screening | Native; 16 cores; fast |
| 3. gnina rescore | Painful locally (CUDA-specific); use Docker x86_64 or substitute Vinardo for early validation |
| 4. Boltz-2 affinity | Native PyTorch MPS; some ops fall back to CPU (linalg_svd, float64) |
| 5. OpenMM MD validation | Native; OpenCL platform on Apple Silicon |
| 6. OpenFE RBFE | Native arm64 (Rosetta 2 NOT required); but FEP backend is CUDA-only, so falls back to OpenMM CPU/OpenCL — multiple hours/day per lead; cloud GPU more efficient |

**Tier 0 = a 10-minute end-to-end smoke test.** Dock MRTX1133 (extracted from PDB 7RPZ) + sotorasib + adagrasib + aspirin + ~995 DUD-E decoys (property-matched to MRTX1133) against KRAS G12D. Pass criteria: MRTX1133 self-docks <2 Å, ranks top 1%, pose shows D12 salt bridge + Y96/H95 H-bonds; aspirin ranks below median. **If Tier 0 fails, the project is broken — stop and debug.**

Subsequent tiers scale: Tier 1 (5M ZINC22 in-stock subset, ~2.5 days on M4 Max); Tier 2 (short MD validation of top 100); Tier 3 (OpenFE on top 30, cloud GPU).

**The local pipeline is the BOINC app.** Once Tier 0 + 1 work locally, packaging for BOINC is system integration, not science.

### 5.4 Deployment path

| Phase | Where | Why |
|---|---|---|
| **0. Local** | M4 Max | Prove the science with one machine before pointing any volunteer compute at it |
| **1. Pilot Zero** | **BOINC Central** (https://boinc.berkeley.edu/central/) | Free hosting, no server ops; supports Docker apps + AutoDock as of March 2026 |
| **2. Own server** | Hetzner DE bare-metal (via `boinc-server-docker`) | Once admission to BOINC Central is sorted and we know the workunit shapes |
| **3. Scale** | Science United integration | Volunteers choose "cancer research" science area; system routes work |

---

## 6. Roadmap

| Month | Phase | Concrete deliverables |
|---|---|---|
| 1 | Foundation | Brand + domain; freeze target panel; assemble KRAS G12D conformer ensemble; curate KRAS gold-standard active/inactive set; **send F@h partnership letter to Huang lab (UW-Madison, the actual KRAS-VHL authors), copy Chodera (MSKCC) and Bowman (UW/Penn)**; investigate BOINC Central admission |
| 2 | Local build | Tier 0 smoke test on M4 Max; build Docker app (Vina + Boltz-2 inference; gnina server-side only); workunit generator + validator + assimilator |
| 3 | Local Tier 1 | 5M-compound ZINC22 in-stock subset with active learning; positive control validation; baseline benchmark publication |
| 4 | Pilot Zero | Submit to BOINC Central; closed alpha with ~10 friendly testers |
| 5 | Public alpha | Project website; Discord; Science United integration; first announcement |
| 6–9 | Production Tier 1 | KRAS G12D + G12V (~250K ligands × 3 conformers, ~25–35K CPU-hours); Boltz-2 layer |
| 9–12 | Tier 2 | G12R, Q61H, mutant p53 Y220C (rezatapopt + 9BR4 validation), R175H ensemble docking |
| 12–18 | Wet-lab partner | PanCAN / academic / CRO partnership; top-100 hit assay; first open hit-list bioRxiv preprint |
| 18+ | Tier 3 + new tracks | Contact mutants (covalent docking); MYC indirect; stromal targets; layer in neoantigen prediction track, TCR-pMHC track, KRAS resistance MD via F@h partnership |

---

## 7. Scope and risks

### 7.1 What's deliberately not in scope

- **NOT a wet lab.** No synthesis, assays, or animal studies — those are a wet-lab partner's job. We feed wet labs better starting points.
- **NOT patient-facing.** No clinical decision support; no diagnostic tool. We never distribute patient-identifiable data to volunteers.
- **NOT closed.** No patents. No proprietary tools. If a hit becomes a drug, it gets there through downstream partners. The data is the gift.
- **NOT trying to outcompute pharma.** Industry has more compute and better chemists. Our differentiators are openness, library scale that few academics can afford, and rigorous public benchmarks (especially given the LIT-PCBA failure).
- **NOT a one-target project.** The first target (KRAS G12D) is the validation; the long-term value is reusable infrastructure for any open PDAC drug-discovery problem.

### 7.2 Risk register

| Risk | Mitigation |
|---|---|
| Vina/GNINA/Boltz-2 scoring too noisy to find real hits | 4-layer validation ladder; ensemble docking; positive-control rediscovery required before trusting novel hits; top 0.01% rescored with OpenFE RBFE |
| Numerical inconsistency across heterogeneous volunteer hardware | Start replication 2–3× with plan-class-specific validators (no CPU↔GPU cross-comparison until empirically equivalent); use BOINC's adaptive replication primitives |
| Volunteer recruitment stalls | Science United integration; PanCAN outreach partnership; publish real interim results every 6 months |
| BOINC Central admission falls through | Stand up own server via `boinc-server-docker` on Hetzner — adds ~2 months but path is well-documented |
| Field overtakes us (daraxonrasib succeeds and resistance becomes the new problem) | We pivot Track 4 (KRAS resistance prediction MD) to primary. If daraxonrasib fails, Track 1 (G12D VS) is even more important. Both scenarios keep the project relevant. |
| GPL contagion via gnina | gnina kept server-side rescoring only; volunteer binaries are Apache-only |
| Compromised server distributes malware via volunteer hosts | BOINC standard: code-signing key on offline physically-secured machine; immutable file model; canary tier before broad release |
| Agent-generated content in our research base has errors | All claims verified across 14 independent audits — ~50 material false claims found and corrected before this plan was written; verification record in `PROJECT/25_full_audit_synthesis.md` |
| Public communications drift into unsupported "cure-language" | Project framing is "open hit discovery against KRAS G12D and adjacent PDAC targets" — every public release pairs scientific claims with the validation layer they passed |

---

## 8. What I need from reviewers

These are the seven questions where your input changes the plan:

1. **Is KRAS G12D virtual screening still the right primary target in 2026?** With daraxonrasib (RMC-6236) in Phase 3 and RMC-9805 producing real G12D-specific signals, has the field moved past the need for new chemical matter against the switch-II pocket? Or is the post-resistance landscape going to demand exactly the kind of open hit library we'd produce?
2. **Are the compute budgets realistic?** Is 50K active volunteer hosts achievable for a new PDAC project in the current volunteer-compute landscape? Is the active-learning recovery rate (~90% top hits at <5% compute) achievable on a target as complex as KRAS G12D, or is that benchmark from easier targets?
3. **Are there better open-source tools** than what I've selected (Vina + GNINA + Boltz-2 + OpenFE)? Specifically: is there a better pose-prediction or scoring tool that has emerged in late 2025 / early 2026 I should know about?
4. **Is BOINC Central a viable Pilot Zero path?** Has anyone you know launched a project through them recently? What's the admission process actually like?
5. **Is the 4-layer validation ladder rigorous enough?** Specifically — given the LIT-PCBA failure, what's the next-most-rigorous public benchmark for ultra-large VS that we should adopt? Should we build our own KRAS-focused benchmark and publish it openly?
6. **Is mutant p53 R175H cryptic-pocket discovery feasible?** The structural biology is less mature than KRAS. If we can't get a co-crystal, can MD-derived ensembles produce a docking target worth screening against, or is this premature?
7. **Are there any KRAS / PDAC / drug-discovery / BOINC facts in this document that you know to be wrong?** The verification record is exhaustive but agent-generated content has a documented ~7% false-claim baseline; expert eyes catch what we missed.

---

## 9. Verification status

This plan is built on ~85,000 words of structured research across 25 deep-dive documents. Every specific factual claim — PDB IDs, drug names, trial outcomes, dataset sizes, compute benchmarks, tool licenses, lab attributions — was checked against authoritative sources across **14 independent audits** (May 2026), totaling **~760 verifiable claims**.

| Status | Count | % |
|---|---|---|
| Verified clean | ~532 | 70% |
| Partial / nuanced / dated | ~145 | 19% |
| Materially false at first generation | ~50 | 7% |
| Unable to verify | ~28 | 4% |

All ~50 material false claims have been either corrected in-place or flagged with explicit verification warnings at the top of the affected document. Examples of what was caught and corrected:

- F@h KRAS-VHL E3 ligase work attributed to the wrong lab (Chodera/MSKCC) — corrected to Huang/UW-Madison (Qiu et al. *JACS Au* 2024)
- "PMV Pharmaceuticals (now Pfizer)" — wholesale fabricated; PMV remains independent
- "OpenMM has Apple Metal backend" — does not exist upstream; corrected
- Sotorasib/adagrasib framed as FDA-approved for PDAC — only NSCLC + CRC; corrected
- MRTX1133 framed as a current clinical asset — discontinued by BMS January 2025; corrected
- Multiple wrong PDB IDs in the p53 document (e.g., 7JWU was claimed as Y220C but is actually ALDH1A1) — corrected or flagged
- US PDAC incidence stated as ~64,000 / 4th leading — actually ~67,530 / 3rd leading; corrected

**One area needs further re-verification before pipeline use:** the medicinal-chemistry PDB-ID tables in `PROJECT/31_mutant_p53_structural_biology.md` Sections 6 and 14. The agent that generated that document hallucinated ~13 PDB IDs; the most consequential ones have been corrected (most importantly: PDB 8A32 contains a Joerger/SGC iodophenol stabilizer, not rezatapopt — the verified rezatapopt anchor is **PDB 9BR4**), but the broader MDM2-inhibitor and contact-mutant entries still need RCSB lookup before any downstream use.

**Full record:** `PROJECT/25_full_audit_synthesis.md` and per-audit files at `sources/verifications/A_*.md` through `N_*.md`.

---

## 10. Selected references

**KRAS biology and drugs**
- Wang, X. et al. "Identification of MRTX1133, a Noncovalent, Potent, and Selective KRAS G12D Inhibitor." *J Med Chem* 2022, 65(4):3123–3133.
- Hallin, J. et al. "Anti-tumor efficacy of a potent and selective non-covalent KRASG12D inhibitor." *Nature Medicine* 2022.
- Ostrem, J. M. L. et al. *Nature* 2013 (Switch-II pocket discovery; Shokat lab).
- The Cancer Genome Atlas Research Network. "Integrated Genomic Characterization of Pancreatic Ductal Adenocarcinoma." *Cancer Cell* 2017.

**KRAS-VHL E3 ligase MD on Folding@home (the precedent)**
- Qiu, Y. et al. *JACS Au* 2024, DOI 10.1021/jacsau.4c00503 (Huang lab, UW-Madison + HKUST collaborators).
- F@h blog 2025-09-18: https://foldingathome.org/2025/09/18/catching-kras-in-the-act-simulations-reveal-new-paths-for-targeted-protein-degradation/

**Mutant p53**
- Boeckler, F. M. et al. *PNAS* 2008, 105:10360 (Y220C cavity; PDB 2VUK).
- Rezatapopt / PC14586 *J Med Chem* (PMV Pharmaceuticals).

**Vaccines and adoptive cellular therapy**
- Rojas, L. A. et al. *Nature* 2023 (autogene cevumeran; NCT04161755).
- Leidner, R. et al. *NEJM* 2022 (mutant KRAS G12D TCR-T).

**Ultra-large virtual screening**
- Lyu, J. et al. *Nature* 2019 (138M docking).
- Sadybekov, A. A. et al. *Nature* 2022 (V-SYNTHES, 11B library).
- Tingle, B. I. & Irwin, J. J. *J Chem Inf Model* 2023 (ZINC22).
- Gentile, F. et al. *ACS Cent Sci* 2020 (Deep Docking).
- Graff, D. E. et al. *Chemical Science* 2021 (MolPAL).
- McNutt, A. T. et al. *J Cheminform* 2021 (GNINA).
- Eberhardt, J. et al. *J Chem Inf Model* 2021 (AutoDock Vina 1.2).

**Benchmark integrity**
- Huang, A.; Knight, I. S.; Naprienko, S. "Data Leakage and Redundancy in the LIT-PCBA Benchmark." arXiv:2507.21404, 2025.
- Mysinger, M. M. et al. *J Med Chem* 2012 (DUD-E).

**Structure prediction**
- Abramson, J. et al. *Nature* 2024 (AlphaFold 3; weights released Nov 2024).
- Wohlwend, J. et al. 2024 (Boltz-1, MIT).
- "Boltz-2: Open-source biomolecular foundation model with affinity prediction." 2025.

**Volunteer computing**
- Anderson, D. P. "BOINC: A Platform for Volunteer Computing." 2019, arXiv:1903.01699.

**Epidemiology**
- American Cancer Society. *Cancer Facts & Figures 2026.*
- Rahib, L. et al. *Cancer Research* 2014 (PC #2 cancer killer by 2030 projection).
- Placido, D. et al. *Nature Medicine* 2023 (EHR deep-learning PC risk prediction).

A fuller bibliography is in the deep-dive documents listed in §11.

---

## 11. Project documentation

| File | Coverage |
|---|---|
| [`PROJECT/01_disease.md`](PROJECT/01_disease.md) | PDAC biology and treatment overview |
| [`PROJECT/02_targets.md`](PROJECT/02_targets.md) | Drug targets and computational bottlenecks |
| [`PROJECT/03_boinc.md`](PROJECT/03_boinc.md) | BOINC, WCG, Folding@home, Rosetta@home landscape |
| [`PROJECT/04_proposal.md`](PROJECT/04_proposal.md) | Original two-track proposal |
| [`PROJECT/10_epidemiology.md`](PROJECT/10_epidemiology.md) | SEER stats, demographic disparities (~4,900 words) |
| [`PROJECT/11_risk_factors.md`](PROJECT/11_risk_factors.md) | Hereditary syndromes + modifiable risk (~4,400 words) |
| [`PROJECT/12_diagnosis_staging.md`](PROJECT/12_diagnosis_staging.md) | AJCC TNM, NCCN resectability, CA 19-9 limits (~8,800 words) |
| [`PROJECT/13_treatment_landscape.md`](PROJECT/13_treatment_landscape.md) | Surgery + chemo + radiation + targeted therapy (~4,800 words) |
| [`PROJECT/14_immunotherapy.md`](PROJECT/14_immunotherapy.md) | Vaccines, CAR-T, TCR-T, oncolytic viruses (~5,400 words) |
| [`PROJECT/15_targeted_therapy.md`](PROJECT/15_targeted_therapy.md) | KRAS variants, mutant p53, DDR, single-cell biology (~6,900 words) |
| [`PROJECT/16_research_models.md`](PROJECT/16_research_models.md) | Cell lines, organoids, KPC mice, PDX, scRNA atlases (~5,600 words) |
| [`PROJECT/17_computational_methods.md`](PROJECT/17_computational_methods.md) | Ultra-large VS state of the art, AF3/Boltz-1/Boltz-2, active learning, OpenFE (~5,000 words) |
| [`PROJECT/20_synthesis.md`](PROJECT/20_synthesis.md) | Recommendation after the deep-dive pass |
| [`PROJECT/21_local_test_plan.md`](PROJECT/21_local_test_plan.md) | M4 Max-specific local pipeline |
| [`PROJECT/22_boinc_technical_spec.md`](PROJECT/22_boinc_technical_spec.md) | Workunit sizing, validator design, security model |
| [`PROJECT/23_external_research_verification.md`](PROJECT/23_external_research_verification.md) | Audit of two user-supplied deep-research reports |
| [`PROJECT/24_internal_doc_audit.md`](PROJECT/24_internal_doc_audit.md) | First internal audit pass |
| [`PROJECT/25_full_audit_synthesis.md`](PROJECT/25_full_audit_synthesis.md) | **Canonical verification record across all 14 audits** |
| [`PROJECT/30_kras_structural_biology.md`](PROJECT/30_kras_structural_biology.md) | Atom-level KRAS biology + drug binding (~7,300 words) |
| [`PROJECT/31_mutant_p53_structural_biology.md`](PROJECT/31_mutant_p53_structural_biology.md) | Atom-level mutant p53 (~10,500 words; PDB column flagged for re-verification) |
| [`sources/external_research/`](sources/external_research/) | Two independent deep-research reports (preserved) |
| [`sources/verifications/`](sources/verifications/) | Per-audit detailed claim records (A through N) |

---

## 12. Operational decisions still open

Not blocking external review, but flagging:

- **Brand name and domain** — PancScan@home vs PDAC@home vs OpenPanc vs PancCure
- **Server hosting** — Hetzner DE (recommended) vs OVH FR vs self-hosted
- **Wet-lab partner** — PanCAN Know-Your-Tumor vs academic pharmacology lab vs CRO
- **License granularity** — Apache 2.0 for the core (patent grant); MIT for analysis scripts
- **KRAS G12V parallelization** — start day-one alongside G12D, or sequence after G12D Tier 1 succeeds
- **Custom KRAS benchmark** — build and publish our own openly, to plug the gap LIT-PCBA can no longer fill (+1–2 months but a useful public deliverable)

---

## Closing note

This is one person's plan, self-funded, with the explicit goal of producing real scientific value while being radically open. It is informed by ~85,000 words of structured research, two independent external research reports, and 14 verification audits — but it has never been built and never been peer-reviewed. Every confident-sounding claim above is a hypothesis until external review validates it.

If you see something wrong — even small — please flag it. If you see a better direction (a higher-impact target, a better tool, a deal-breaking blocker we've missed) — please say so. The plan exists to be revised.

— Thomas Carfano (tomcarfano@gmail.com)
