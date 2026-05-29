# Proposal: PancScan@home + Folding@home partnership

> A two-track volunteer compute initiative against pancreatic cancer. One track (PancScan@home) is new, differentiated, and 100% under our control. The other (Folding@home partnership) is fast, leverages existing infrastructure, and feeds our track scientifically.

## TL;DR

**Track A — Folding@home partnership (start week 1).** Email Folding@home leadership + the **Xuhui Huang lab (UW-Madison)** — who actually ran the 2024–25 KRAS-VHL E3 ligase MD on F@h that the Sept 2025 F@h post (https://foldingathome.org/2025/09/18/catching-kras-in-the-act-simulations-reveal-new-paths-for-targeted-protein-degradation/) describes (~1.5 ms total MD; 6 metastable encounter states; 3 with favorable PROTAC linker geometries; primary publication Qiu et al., JACS Au 2024, DOI 10.1021/jacsau.4c00503). Other reasonable copy-to addresses: John Chodera (MSKCC, separate F@h KRAS work and broader FEP expertise) and Greg Bowman (UW/Penn, cryptic-pocket work). Propose a PDAC campaign: long-timescale all-atom MD on KRAS G12D bound to MRTX1133, RMC-6236, and emerging G12D degraders, plus on MYC-MAX, mutant p53 Y220C, and FAP. Time to first result: 3–6 months. We fund and contribute, F@h hosts.

**Track B — PancScan@home: a new BOINC virtual-screening project (start week 2; MVP at month 4).** Stand up a BOINC server that distributes ultra-large virtual screening (10B–70B compounds, ZINC22 + Enamine REAL) against an ensemble of PDAC drug targets — starting with KRAS G12D Switch-II pocket and published cryptic sites, then expanding to pan-KRAS allosteric sites, mutant p53, MYC-MAX, and stromal targets (FAP, CXCR4). The output is a continuously growing open hit-list database, freely downloadable. Use AutoDock Vina + GNINA (CNN rescoring) under the hood, both fully open source.

**Why two tracks?** They feed each other. F@h trajectories produce protein conformation ensembles (the "structures") that PancScan@home screens compounds against. Top PancScan@home hits get fed back to F@h for binding-mode dynamics. Each gets stronger when the other works.

## 1. Why this specific combination

From the research:
- [B1] KRAS / pan-RAS cryptic-pocket MD is a top-3 compute bottleneck → F@h is already doing it → partner, don't duplicate.
- [B3] Pan-KRAS allosteric virtual screening (~3.5T poses) is the **single biggest** under-resourced PDAC compute problem and is a *perfect* fit for BOINC's batch-parallel pattern (proven by FightAIDS@home and OpenPandemics). No existing volunteer-compute project does this for PDAC. **This is our differentiated opening.**
- [B2] MYC cryptic-pocket VS and [A8] mutant-p53 stabilizer VS plug straight into the same PancScan@home infrastructure once it works for KRAS — same docking app, just swap the target.
- Open compound libraries (ZINC22, Enamine REAL) are already free. Open targets (PDB + F@h-derived ensembles) will be free. Open docking tools (AutoDock Vina, GNINA, DiffDock) are free. Nothing about this requires proprietary anything.

## 2. PancScan@home — concrete design

### Scientific scope (Phase 1, months 1–6)
- **Primary target:** KRAS G12D Switch-II pocket — most common PDAC oncogenic mutation, structurally well-characterized (PDB 7RPZ etc.), MRTX1133 is a known binder for benchmarking.
- **Conformational ensemble:** Initial seed of ~20–50 conformations from published MD studies (Bowman lab, Chodera lab, AlphaFold conformational ensembles). Expand via F@h partnership.
- **Compound library:** Start with **ZINC22 "in-stock + on-demand"** subset (~5B compounds), then full ZINC22 (~37B), then Enamine REAL (~70B) as we scale.
- **Docking engine:** [AutoDock Vina](https://vina.scripps.edu/) (rigid-receptor, fast) for primary screening; [GNINA](https://github.com/gnina/gnina) CNN-rescoring on top of Vina poses to improve hit-rate (literature shows 2–3× enrichment).
- **Output:** Public hit-list database — every compound's best Vina score + GNINA rescore + the receptor conformation it bound, sortable + downloadable.

### Phase 2–3 expansion (months 6–12+)
- More targets: KRAS G12V/G12R/Q61H, pan-KRAS allosteric sites, mutant p53 (Y220C, R175H, R248Q), MYC-MAX dimer interface, FAP, CXCR4, hyaluronic-acid synthesis enzymes (HAS2/HAS3).
- More compound libraries: full Enamine REAL, [Pubchem](https://pubchem.ncbi.nlm.nih.gov/), [ChEMBL](https://www.ebi.ac.uk/chembl/), [DrugBank](https://go.drugbank.com/) repurposing set.
- ML rescoring layer (DiffDock-L, Boltz-1, etc.) on top hits.

### Compute architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     PancScan@home server                    │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐    │
│  │  Compound    │  │   Target     │  │  Work Generator │    │
│  │  Library DB  │  │  Conformer   │──▶│   (creates WUs)│    │
│  │  (ZINC22+)   │  │   DB (MD)    │  │                 │    │
│  └──────────────┘  └──────────────┘  └────────┬────────┘    │
│                                                │             │
│                          ┌─────────────────────▼──────────┐  │
│                          │ BOINC scheduler / transitioner │  │
│                          └────────┬────────────────────┬──┘  │
└───────────────────────────────────┼────────────────────┼─────┘
                                    │                    │
              ┌─────────────────────▼──┐    ┌────────────▼─────┐
              │ Volunteer host (Win)   │ ...│ Volunteer (Linux) │
              │ Docker app: Vina+GNINA │    │                    │
              │ 10k compounds × 1 conf │    │                    │
              └─────────────────────┬──┘    └────────────┬──────┘
                                    │                    │
                          ┌─────────▼────────────────────▼──┐
                          │  Validator (replicate × 2)      │
                          └─────────────────┬───────────────┘
                                            │
                          ┌─────────────────▼───────────────┐
                          │  Assimilator → Hit DB           │
                          │  (Postgres, public read-only)   │
                          └─────────────────┬───────────────┘
                                            │
                          ┌─────────────────▼───────────────┐
                          │  pancscan.org/hits  (public)    │
                          └─────────────────────────────────┘
```

Workunit shape:
- Inputs: 1 target conformation (`.pdbqt`, ~50 KB), 1 batch of 10k compounds (`.smi` + `.sdf`, ~5 MB compressed)
- Process: ~10 min – 1 hr on a consumer CPU; faster on GPU via GNINA-CUDA
- Output: ranked poses + scores (~2 MB compressed)
- Validation: each workunit replicated to 2 volunteers; top-hit scores must match within tolerance

Server: single beefy machine (or small cluster) running [`boinc-server-docker`](https://github.com/marius311/boinc-server-docker). Estimated initial cost: well under $1k/month for storage + bandwidth. Can scale on Hetzner / OVH / Backblaze B2 for storage.

### Openness commitments
- All code MIT-licensed, GitHub.
- All hit data CC0 (public domain), downloadable as Parquet + Postgres dumps.
- All target conformations contributed back to public archives (PDB-Dev for MD ensembles, OPM, etc.).
- All workunit scripts and apps reproducible via Docker.
- Pre-print every analysis on bioRxiv before paywalled submission.

## 3. Track A — Folding@home partnership pitch

A draft email + scientific proposal to send in week 1. Targets:
- **Xuhui Huang (UW-Madison)** — actually ran the F@h KRAS-VHL E3 ligase work (Qiu et al. JACS Au 2024)
- John Chodera (MSKCC, choderalab.org) — separate F@h KRAS work, deep FEP expertise
- Greg Bowman (Wash U / U Penn, bowmanlab) — cryptic pockets
- Vijay Pande / F@h leadership

The pitch is short: *"We are self-funding a PDAC-focused volunteer compute initiative. We will stand up a virtual-screening BOINC project (PancScan@home) but recognize Folding@home is the right home for MD. Would you be open to a PDAC campaign (KRAS G12D + degraders, p53, MYC, FAP) where we contribute funding + a wet-lab partner pipeline and you host the dynamics? Our VS output will feed your MD inputs and vice versa."*

Draft sits at `PROJECT/05_fah_letter.md` (next).

## 4. Roadmap

### Month 1
- [ ] Send Folding@home partnership pitch (Track A).
- [ ] Stand up `boinc-server-docker` on a Hetzner / OVH box, get a hello-world workunit running.
- [ ] Acquire / build initial KRAS G12D conformational ensemble (start with published MD trajectories from Bowman/Chodera labs; PDB).
- [ ] Stage ZINC22 "in-stock" subset (~5B) — chunk into 10k-compound batches.

### Month 2
- [ ] Build the Docker app: AutoDock Vina + GNINA rescoring + score export. Cross-platform: Linux x86_64, Windows x86_64, macOS arm64 (Vina builds clean).
- [ ] Implement workunit lifecycle: generator, validator, assimilator. Write replication / consensus logic.
- [ ] Public hit-list Postgres + downloadable Parquet snapshots.

### Month 3
- [ ] Closed beta with ~10 friendly volunteers; run 10k WUs end-to-end. Benchmark throughput.
- [ ] Compare Vina top hits against known KRAS G12D binders (MRTX1133, RMC-6236) as positive controls.
- [ ] Set up project website (pancscan.org or similar), Discord / forum, license docs.

### Month 4 — public launch
- [ ] Register with [Science United](https://scienceunited.org/) so volunteers can opt in via "cancer research" category.
- [ ] Submit to BOINC project list ([boinc.berkeley.edu/projects.php](https://boinc.berkeley.edu/projects.php)).
- [ ] Press: r/BOINC, Hacker News, PanCAN, Wikipedia.
- [ ] Goal: 1,000 active volunteers by month 5, 10,000 by month 9.

### Months 5–12
- [ ] Add KRAS G12V / G12R / Q61H, mutant p53 Y220C, MYC-MAX, FAP, CXCR4 as targets.
- [ ] Add full Enamine REAL.
- [ ] Layer DiffDock / Boltz-1 rescoring on top hits.
- [ ] Identify wet-lab partner (PanCAN consortium, academic pharmacology lab, or contract research org) to assay top 100–1000 hits.
- [ ] First open hit-list publication on bioRxiv.

## 5. Verification — how we'd know this is producing real value

- **Validation positive controls.** Known PDAC-target binders (MRTX1133 for KRAS G12D, etalanetug for KRAS, PC14586 for p53 Y220C) must rank in the top 1% of compounds when fed through our pipeline. If they don't, the scoring is wrong, not the chemistry.
- **Re-discovery of published hits.** Compounds that other labs have reported as KRAS / p53 / MYC binders should appear among our top hits. Reproducing known science validates the pipeline before we trust novel hits.
- **Wet-lab assay rate.** Of the top 100 novel hits we send to a wet-lab partner, what % show binding (e.g., DSF, ITC, SPR) above background? Target: ≥5% (industry benchmark for ultra-large VS).
- **Volunteer health.** Active hosts per week. Validator consensus rate. Workunit error rate. (BOINC has built-in metrics.)
- **Citation footprint.** Are other PDAC researchers using our open hit-list? Track downloads + citations of our preprints + GitHub forks.

## 6. What this proposal explicitly is NOT

- **Not a wet-lab.** We don't synthesize compounds, run assays, or do animal studies. We feed wet labs better starting points.
- **Not patient-facing.** No clinical decision support. No patient data handling (HIPAA out of scope).
- **Not closed.** No IP, no patents, no proprietary tools. If a hit becomes a drug, it gets there through downstream partners. The data is the gift.
- **Not "trying to outcompute Big Pharma."** Pharma has billions of compute hours but locks results. The differentiator here is *openness at scale* — and the long tail of academic / startup chemists who can't access pharma-scale screens.

## 7. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Vina+GNINA scoring is too inaccurate to find real hits | Use ensemble docking against MD-derived conformations (proven to help); validate against known binders before trusting novel hits; rescore top 0.01% with ML methods (DiffDock, Boltz). |
| F@h declines to partner | Track B (PancScan@home) is fully independent. F@h partnership is upside, not dependency. |
| Volunteer recruitment stalls | Science United integration; partner with PanCAN for outreach; the project is intrinsically interesting (a famously deadly cancer + visible "i'm contributing" metrics). |
| BOINC ops burden exhausts the maintainer | Use boinc-server-docker (already containerized); start small (10k WU/day) and scale only when stable; build community early so non-maintainers can submit fixes. |
| Top hits sit in a database that nobody uses | Active outreach: bioRxiv preprint at month 9, presentations at AACR / ASCO GI, partnerships with PanCAN's Know-Your-Tumor for translation. |
| Volunteers attack / poison results | BOINC's built-in replication-then-consensus model handles this; cross-validate suspicious results on a trusted server before promoting to hit DB. |

## 8. Open questions for the next session

1. Domain name + brand. PancScan@home? PDAC@home? PancCure? — pick one.
2. Server location. Hetzner DE? OVH? Self-hosted on the user's storage? (Probably Hetzner — better uptime, EU data-residency, cheap.)
3. Initial target panel — KRAS G12D only first, or also G12V/G12R for parallelism?
4. Wet-lab partner. PanCAN consortium? An academic pharmacology lab? Contract research org?
5. Funding the partner. The user is funding compute; a wet-lab partner may require its own funding stream. Talk to PanCAN about co-funding.
