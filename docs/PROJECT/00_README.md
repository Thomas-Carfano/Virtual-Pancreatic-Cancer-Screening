# Pancreatic Cancer Volunteer Compute Project

A self-funded effort to design and launch a BOINC-style volunteer computing project that contributes to a cure for pancreatic cancer. Everything here is public and open.

**Lead:** Thomas Carfano (tomcarfano@gmail.com)
**Started:** 2026-05-21

> **📄 Externally-shareable plan: [PLAN.md](../PLAN.md)** at the project root. Self-contained, verification-status documented, ready for expert review. Read this if you are an external reviewer evaluating the project.

## Reading order

### Start here
- **[00_README.md](00_README.md)** — this file
- **[20_synthesis.md](20_synthesis.md)** — what the deep dives changed; **the current recommendation lives here**

### The original v1 (good orientation, but read 20_synthesis.md for current state)
- **[01_disease.md](01_disease.md)** — pancreatic cancer biology for a non-scientist; 9 candidate compute angles
- **[02_targets.md](02_targets.md)** — drug targets, research frontiers, compute bottlenecks
- **[03_boinc.md](03_boinc.md)** — BOINC platform, World Community Grid, Folding@home, Rosetta@home; launch-path comparison
- **[04_proposal.md](04_proposal.md)** — original two-track proposal (F@h partnership + PancScan@home)

### Deep dives (the "ridiculous amount of research" pass)
- **[10_epidemiology.md](10_epidemiology.md)** — SEER stats, demographic disparities, NOD risk window, why PDAC stays silent (~4,900 words)
- **[11_risk_factors.md](11_risk_factors.md)** — hereditary syndromes (BRCA, Lynch, FAMMM, Peutz-Jeghers, hereditary pancreatitis), modifiable risk factors, surveillance protocols (~4,400 words)
- **[12_diagnosis_staging.md](12_diagnosis_staging.md)** — symptoms, CT/MRI/EUS/ERCP, CA 19-9 limitations and replacement panels, AJCC TNM 8th, NCCN resectability, IPMN/MCN/PanIN (~8,800 words)
- **[13_treatment_landscape.md](13_treatment_landscape.md)** — surgery types, adjuvant/neoadjuvant trials (PRODIGE-24, PREOPANC, NAPOLI-3), KRAS inhibitor approvals, MR-LINAC, supportive care (~4,800 words)
- **[14_immunotherapy.md](14_immunotherapy.md)** — why PDAC is immune-cold, checkpoint failures, autogene cevumeran, ELI-002, mesothelin/claudin 18.2 CAR-T, KRAS G12D TCR-T, pelareorep, satricabtagene autoleucel (~5,400 words)
- **[15_targeted_therapy.md](15_targeted_therapy.md)** — KRAS variant-by-variant inhibitor landscape, daraxonrasib Phase 3, mutant p53 reactivators, MYC indirect, DDR/BRCAness, NRG1/NTRK/BRAF/HER2/claudin, molecular subtypes, scRNA-seq + spatial (~6,900 words)
- **[16_research_models.md](16_research_models.md)** — 2D cell lines, patient-derived organoids, KPC mice and GEMM derivatives, PDX, humanized mice, organ-on-chip, in silico datasets (TCGA-PAAD, ICGC, CPTAC, DepMap, scRNA atlases) (~5,600 words)
- **[17_computational_methods.md](17_computational_methods.md)** — ultra-large virtual screening, AlphaFold3/Boltz-1/Boltz-2, active learning, OpenFE, ML potentials, generative models, volunteer-compute fit, throughput benchmarks (~5,000 words)

### Local pipeline + atom-level target foundations (May 22 pivot)
- **[21_local_test_plan.md](21_local_test_plan.md)** — full local-first pipeline for the user's M4 Max (128 GB), tier 0→3 progression, what success looks like
- **[22_boinc_technical_spec.md](22_boinc_technical_spec.md)** — technical specifications distilled from two external deep-research reports (`sources/external_research/`) the user obtained independently; work unit sizing, validator design, 4-layer validation ladder, BOINC Central pilot path, security model
- **[23_external_research_verification.md](23_external_research_verification.md)** — source-by-source audit of both external research reports against authoritative web sources. 40+ verified, 3 material errors found (PDC TB figure, Docking@Home framing, PDB 7JWU misidentification), 8 partial/nuance items. Detailed per-claim verifications in `sources/verifications/`.
- **[24_internal_doc_audit.md](24_internal_doc_audit.md)** — first internal audit pass (audits D–I): docs 10, 11, 12, 13, 14, 15, 16, 17, 30, 31. ~400 claims; ~77% verified, ~16% partial, ~4% materially false. All material errors corrected.
- **[25_full_audit_synthesis.md](25_full_audit_synthesis.md)** — **the canonical verification record.** Full sweep across all 14 audits (A–N), ~785 claims total, ~70% verified, ~19% partial, ~7% materially false. Documents all material errors found, all fixes applied, and a tracking table for "logged" issues still open. Updated 2026-05-22 in response to Search3 external review of the synthesis itself (split confidence ratings into narrative vs pipeline-readiness; added publication gate; quarantined p53 PDB IDs + the missing G12D apo target; corrected fpocket to MIT — an earlier audit briefly carried it as GPL-3 before final-pass verification).
- **Regression-prevention files in `sources/verifications/`:**
  - `known_bad_claims.md` — denylist of facts we've proven wrong
  - `must_verify_claim_types.md` — publication-gate checklist
  - `structure_manifest.csv` — PDB ID provenance table (any PDB ID used in a workflow must appear here with RCSB validation)
- **[30_kras_structural_biology.md](30_kras_structural_biology.md)** — atom-level KRAS biology, switch-II pocket, every PDB ID + binding mode (sotorasib/adagrasib/divarasib/MRTX1133/RMC compounds), docking score interpretation (~7,300 words)
- **[31_mutant_p53_structural_biology.md](31_mutant_p53_structural_biology.md)** — atom-level mutant p53 biology, Y220C pocket, R175H/R273H/R248 hotspots, every clinical-stage reactivator + PDB ID, why p53 is the inverse drug-design problem from KRAS (~10,500 words)

### External research archive
- **[sources/external_research/1Search - deep-research-report.md](../sources/external_research/1Search%20-%20deep-research-report.md)** — independent BOINC + PDAC research report (tool inventory, dataset inventory, recommended pilots)
- **[sources/external_research/2search - deep-research-report.md](../sources/external_research/2search%20-%20deep-research-report.md)** — independent BOINC + PDAC research report (KRAS G12D switch-II pocket recommendation, validation ladder, roadmap)

Total: ~85,000+ words of structured, sourced content across our own deep dives plus ~70 KB of external research reports.

## Working principles

- **Public.** All code MIT/Apache. All data CC0 or CC-BY. All papers preprinted on bioRxiv/arXiv.
- **Free.** No paywalls. No proprietary tooling. Volunteers contribute compute, never pay.
- **Honest.** If a thing doesn't work, we say so. We track real scientific output, not just teraflops.
- **Cumulative.** Every hit, every conformation, every model goes into an open archive other researchers can build on.

## Layout

```
PancreaticCancer/
├── PROJECT/         (this folder — design docs and rationale)
├── sources/         (downloaded references — papers, screenshots, datasets)
└── (future)
    ├── pancscan/    (the compute project itself, when we build it)
    │   ├── server/  (boinc-server-docker configuration)
    │   ├── app/     (cross-platform docker app — Vina + GNINA + Boltz-2)
    │   ├── data/    (target structures, conformer ensembles, hit lists)
    │   ├── workgen/ (work generator, validator, assimilator)
    │   └── web/     (public hit-list website + downloads)
    ├── infra/       (deploy scripts, monitoring, backups)
    └── papers/      (preprints in flight)
```
