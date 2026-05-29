# BOINC, World Community Grid & Folding@home — Landscape and Launch Paths

> What it takes to launch a volunteer-compute cancer project in 2026, what already exists, and how to choose a path.

## 1. BOINC platform — how it actually works

**Architecture.** BOINC is a distributed-computing middleware for harnessing idle consumer hardware (Windows, macOS, Linux, Android, FreeBSD). Client/server:

- **Client.** Volunteers run "BOINC Manager," which downloads work units, runs computation, uploads results.
- **Server.** Linux + Apache + PHP + MySQL. Minimum 64-bit CPU, 8 GB RAM, 40 GB disk. Modern deployments use [`boinc-server-docker`](https://github.com/marius311/boinc-server-docker).
- **Daemons.** Transitioner (workunit state machine), Feeder (DB → scheduler), Validator (consensus / sanity-check results), Assimilator (process validated results), Work Generator (create workunits from inputs).

**Work unit lifecycle.** Researcher defines workunits (templated XML) and apps (executables / Docker containers for each OS). Results are automatically replicated across multiple volunteers for validation. Apps run sandboxed.

**GPU support.** Native CUDA + OpenCL. GPUs need ≥256 MB VRAM and CUDA compute capability ≥1.0. Linux/macOS GPU detection works when BOINC runs as a service; Windows requires non-PAE mode.

**Project listing / volunteer routing.** Anyone can host a BOINC project — no approval. But to reach volunteers you want listing on [boinc.berkeley.edu/projects.php](https://boinc.berkeley.edu/projects.php) and integration with **[Science United](https://scienceunited.org/intro.php)**, an NSF-funded account manager that lets volunteers pick a *science area* (e.g., "cancer research") and have compute routed automatically. Science United keeps volunteers' personal data; projects get anonymous accounts.

## 2. World Community Grid — gate-keeping, cancer history, PDAC status

**Org.** Founded by IBM in 2004. Transferred September 2021 to [Krembil Research Institute](https://www.worldcommunitygrid.org/about_us/article.s?articleId=732) (University Health Network, Toronto). Directed by Dr. Igor Jurisica.

**Gate-keeping.** During the Krembil transition (2021–2024) WCG paused new project proposals. As of 2025–2026, WCG is not actively soliciting external proposals; future projects likely require formal partnership with Krembil. Historical partners have all been established academic institutions (Scripps, Princess Margaret, Ontario Cancer Inst.).

**Cancer projects WCG has hosted:**

1. **Help Conquer Cancer** (2007–~present, low activity) — protein crystallography for cancer initiation.
2. **Mapping Cancer Markers** (2013–active) — DNA/protein marker discovery across lung, ovarian, prostate, **pancreatic**, breast tissue samples. Pancreatic tissue is included but no PDAC-specific breakthrough has been published.
3. **Smash Childhood Cancer** (2016–2024) — pediatric drug-target ID; results now feed the $25M CRUK Cancer Grand Challenge KOODAC consortium.
4. **OpenPandemics: COVID-19** (2020–2024) — virtual screening of small molecules against SARS-CoV-2 3CL protease. Flavonoid hits published 2021–22. Useful template for a PDAC analog.
5. **FightAIDS@home Phase 2** (also Scripps) — 20B+ docking comparisons against HIV. Found a novel capsid pocket binder.

**Verdict.** No WCG project has been PDAC-targeted. Mapping Cancer Markers brushes against PDAC but isn't focused on it. Proposing a new PDAC-specific WCG project is possible but slow (12–24 months) and requires Krembil partnership.

## 3. Folding@home — non-BOINC, but the strongest cancer dynamics platform

**Org.** ~1.2M active volunteers (2025). Custom P2P architecture, not BOINC. GPU-heavy.

**What it does.** All-atom molecular dynamics simulations. Markov State Models from distributed trajectories. Drug-target conformational ensembles.

**Cancer / PDAC work.** [Xuhui Huang's lab at UW-Madison](https://wisc.edu/) (with HKUST collaborators) ran ~1.5 ms of all-atom MD on KRAS–VHL E3 ligase complexes on F@h in 2024–25, mapping 6 metastable encounter states (3 with favorable PROTAC linker geometries) — published as Qiu et al. *JACS Au* 2024 (DOI 10.1021/jacsau.4c00503) and summarized on the F@h blog Sept 2025. Directly relevant to KRAS-driven PDAC. Memorial Sloan Kettering's [Chodera lab](https://choderalab.org/) is a separate F@h power-user with deep FEP and ML-potential expertise. F@h has also done kinase activation, Alzheimer's, Parkinson's.

**Partnership model.** Informal — researchers contact F@h leadership (Pande / Chodera / Shukla labs); no formal gate. Projects added to the queue based on scientific merit.

**Verdict.** Highest-leverage partner for PDAC molecular dynamics. Already has KRAS precedent. Onboarding takes 3–6 months, not 12–24.

## 4. Rosetta@home

BOINC-based protein design (Baker Lab, University of Washington). Past cancer work: IL-2 receptor agonist (Neoleukin-2/15) for immunotherapy; Mdm2/Mdmx blockers for the p53 pathway. Strong for *de novo* therapeutic protein design (CAR-T scaffolds, checkpoint variants), narrower for screening / dynamics. Plausible for a PDAC neoantigen / mini-binder design subproject.

## 5. Other volunteer platforms

- **GPUGrid.net** — GPU MD, 15+ years active, 2000+ publications. Drug discovery for HIV / cancer.
- **Petals / Hivemind / Learning@home** — inference + fine-tuning of large models on volunteer GPUs. *Not* useful for training-from-scratch — see Section 7.
- **Charity Engine, etc.** — general compute brokers; less cancer-specific.

## 6. Workload patterns that have worked at volunteer-compute scale

1. **Massive virtual screening (100M+ docking runs).**
   - FightAIDS@home: 20B+ docking comparisons → novel HIV capsid pocket binder ([Springer 2022](https://link.springer.com/article/10.1007/s10822-022-00446-5)).
   - OpenPandemics: SARS-CoV-2 3CL protease screen → flavonoid + dual-action antiviral hits.
   - **PDAC fit:** **Excellent.** KRAS / p53 / MYC / stromal targets against Enamine REAL or ZINC22 maps perfectly.

2. **All-atom molecular dynamics & ensemble sampling.**
   - F@h: KRAS dynamics, kinase ensembles, neurodegeneration aggregation.
   - GPUGrid: cancer / HIV MD.
   - **PDAC fit:** **Excellent**, but F@h already does this — better to partner than to duplicate.

3. **Distributed protein design.**
   - Rosetta@home: Neoleukin, Mdm2 binders.
   - **PDAC fit:** Moderate (neoantigen mini-binders, CAR-T scaffolds).

4. **Markov State Models from distributed trajectories.**
   - F@h: every MSM kinase paper since ~2015.
   - **PDAC fit:** Layer on top of (2).

## 7. Workload patterns that have NOT worked

1. **Large-scale ML training from scratch.** Volunteer networks have 10–100 ms latency, heterogeneous compute, frequent churn. Gradient descent needs tight synchronization. Petals / Hivemind run at inference / fine-tuning speed only. **Implication:** training a giant drug-response model from scratch on volunteer compute is a research project, not a deliverable.

2. **Genomic / population-genetics analysis.** Patient genomic data is sensitive (HIPAA / GDPR), requires institutional oversight, complex pipelines, tight I/O. No volunteer project has done this at scale.

3. **Real-time / interactive simulations.** Volunteer compute can't guarantee latency or availability.

## 8. Launch-path comparison

| Path | Time to first result | Sci control | Ops burden | Openness | Impact ceiling |
|---|---|---|---|---|---|
| **(a) Propose to WCG** | 12–24 mo | Medium | Low | Gated (institutional partnership) | Very high (1M+ volunteers, brand) |
| **(b) Propose to Folding@home** | 3–6 mo | High | Medium | Open | Very high (1.2M, KRAS precedent) |
| **(c) Stand up own BOINC server** | 2–4 mo | Full | High | Open | Medium (10k–100k initially) |
| **(d) Non-BOINC ML platform (Petals/Hivemind)** | 1–2 mo | High | Medium | Open | Low (inference / fine-tuning only) |

## 9. Top 3 ranked paths

### 1. Folding@home partnership for PDAC molecular dynamics (FASTEST)
- **Pros.** Existing infrastructure, KRAS precedent (Huang/UW-Madison, Chodera/MSKCC), 1.2M GPUs, no formal gate.
- **Cons.** Less branding control; we follow F@h's app/workflow conventions.
- **Action.** Email F@h leadership + **Huang lab (UW-Madison)** and Chodera lab (MSKCC) proposing a PDAC kinase / KRAS-degrader / cryptic-pocket campaign.

### 2. Stand up own BOINC virtual-screening project ("PancScan@home") (BEST DIFFERENTIATION)
- **Pros.** Full scientific & branding control. Differentiated from F@h (F@h does MD, not VS at billion-compound scale). Open everything. Reusable platform for future PDAC targets.
- **Cons.** Real ops burden; need to recruit volunteers (via Science United).
- **Action.** Build BOINC server via `boinc-server-docker`. Wrap an open docker app (e.g., AutoDock Vina + GNINA). Stage compound batches from Enamine REAL + ZINC22. Stage targets from PDB + MD ensembles. Beta with 10k workunits → register with Science United.

### 3. Propose to WCG (BACKUP)
- **Pros.** Highest volunteer ceiling, institutional cachet, peer-review mandate.
- **Cons.** 12–24 mo timeline, gatekeeping, no PDAC precedent.
- **Action.** Establish partnership with Krembil; only after we have an MVP from path 1 or 2 to point at.

## 10. Sources

- [BOINC](https://boinc.berkeley.edu/)
- [BOINC server cookbook (GitHub wiki)](https://github.com/BOINC/boinc/wiki/Create-a-BOINC-server-(cookbook))
- [boinc-server-docker](https://github.com/marius311/boinc-server-docker)
- [BOINC Docker apps wiki](https://github.com/BOINC/boinc/wiki/Docker-apps)
- [BOINC GPU computing](https://github.com/BOINC/boinc/wiki/GPU_computing)
- [Science United](https://scienceunited.org/intro.php)
- [World Community Grid](https://www.worldcommunitygrid.org/)
- [WCG at Krembil — transition announcement](https://www.worldcommunitygrid.org/about_us/article.s?articleId=732)
- [WCG — Mapping Cancer Markers](https://www.worldcommunitygrid.org/research/mcm1/overview.s)
- [WCG — Help Conquer Cancer](https://www.worldcommunitygrid.org/research/hcc1/overview.s)
- [WCG — Smash Childhood Cancer](https://www.worldcommunitygrid.org/research/scc1/faq.s)
- [WCG — OpenPandemics](https://www.worldcommunitygrid.org/research/opn1/faq.s)
- [Folding@home](https://foldingathome.org/)
- [Folding@home — KRAS research (Sept 2025)](https://foldingathome.org/2025/09/18/catching-kras-in-the-act-simulations-reveal-new-paths-for-targeted-protein-degradation/)
- [Folding@home — Cancer](https://foldingathome.org/diseases/cancer/)
- [Rosetta@home](https://boinc.bakerlab.org/)
- [Rosetta protein design at IPD](https://www.ipd.uw.edu/news-pages/the-power-of-charity-for-protein-design/)
- [FightAIDS@home](https://www.scripps.edu/fightaidsathome/index.html)
- [FightAIDS@home publication (Springer 2022)](https://link.springer.com/article/10.1007/s10822-022-00446-5)
- [OpenPandemics — Forli lab results](https://forlilab.org/openpandemics-covid-19/)
- [GPUGrid.net](https://gpugrid.org/)
- [Petals (ACL 2023)](https://arxiv.org/pdf/2209.01188)
- [Hivemind (GitHub)](https://github.com/learning-at-home/hivemind)
- [Wikipedia — BOINC](https://en.wikipedia.org/wiki/Berkeley_Open_Infrastructure_for_Network_Computing)
- [Wikipedia — Volunteer computing](https://en.wikipedia.org/wiki/Volunteer_computing)
