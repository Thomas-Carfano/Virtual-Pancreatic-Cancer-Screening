# Must-Verify Claim Types — Publication Gate Checklist

> Categories of claim that require primary-source verification before any external-facing publication. For each category, the **canonical primary source** is named, along with a sample query to use.
>
> Use this list when drafting external-facing content (papers, partnership letters, grant applications, public project descriptions). If your draft contains a claim in any of these categories, verify it within the re-verification window listed in `PROJECT/25_full_audit_synthesis.md` § Publication gate.

## Pre-publication verification checklist

Run this checklist on any document going to external readers:

- [ ] Every PDB ID is in `structure_manifest.csv` with RCSB title and validation date
- [ ] Every FDA approval has an exact indication and approval-date URL
- [ ] Every clinical trial has an NCT number and a date for the cited data
- [ ] Every software-version-dependent claim names the version and a release date
- [ ] Every tool license is verified at the project's LICENSE file
- [ ] Every dataset size has a date and source URL
- [ ] Every corporate status (acquired, IPO'd, divested) has a SEC/IR-page citation
- [ ] Every lab attribution matches the author affiliations on the cited paper
- [ ] Every cell-line mutation status matches Cellosaurus
- [ ] Every numerical claim with three-or-more-digit precision (e.g., "23.31 GB", "62% ORR", "6.45% APC") has a primary-source citation
- [ ] No claim contradicts an entry in `known_bad_claims.md`

## Categories and canonical sources

### 1. PDB IDs and structural biology

**Canonical source:** RCSB PDB (https://www.rcsb.org/structure/[ID])

**Verify:**
- Title of entry (does it match the protein + ligand + mutation you claim?)
- Bound ligand chemical-component ID (3-letter code)
- Protein mutation
- Nucleotide state (GDP / GTP / GppCp / apo)
- Resolution + method (X-ray / cryo-EM / NMR)
- Biological assembly (monomer / dimer / etc.)
- Deposition + release dates

**Sample query:** load https://www.rcsb.org/structure/9BR4 and verify the title contains "rezatapopt" and the ligand list contains the rezatapopt heavy-atom ID.

**Re-verify window:** 30 days before publication.

### 2. FDA approvals and clinical regulatory status

**Canonical source:** drugs@fda + FDA approval announcement pages (oncology specifically: https://www.fda.gov/drugs/resources-information-approved-drugs/oncology-cancer-hematologic-malignancies-approval-notifications)

**Verify:**
- Exact indication language (line-of-therapy, biomarker requirement, prior-therapy condition)
- Approval type (accelerated vs full / regular)
- Approval date
- Companion diagnostic (if any)

**Common errors to avoid:**
- Conflating "approved" with "approved for [the tumor type you're discussing]"
- Conflating "tumor-agnostic" approval with practical efficacy in a specific tumor (cf. DESTINY-PanTumor02 PDAC cohort)
- Using "FDA-approved" without specifying accelerated vs regular

**Sample query:** "FDA zenocutuzumab approval 2024" → land on https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-zenocutuzumab-zbco-non-small-cell-lung-cancer-and-pancreatic and quote the exact indication.

**Re-verify window:** 30 days before publication.

### 3. Clinical trial status and outcomes

**Canonical source:** ClinicalTrials.gov (https://clinicaltrials.gov/study/[NCT-id])

**Verify:**
- Trial phase
- Enrollment / status (recruiting / active not recruiting / completed / terminated / withdrawn)
- Termination reason if any (NOT just secondary-press explanation)
- Primary + secondary endpoints
- Latest data-cut date

**Common errors to avoid:**
- Stating ORR / DCR without trial-arm and patient-count caveats
- Citing secondary press as the official trial reason (cf. MRTX1133: registry says "formulation challenges"; press cites "PK")
- Conflating different cohort sizes between AMPLIFY-201 (2P) and AMPLIFY-7P (7P)

**Sample query:** "NCT05737706 MRTX1133" → land on ClinicalTrials.gov, capture status + termination reason from the registry record itself.

**Re-verify window:** 90 days before publication; 30 days for terminated / discontinued claims.

### 4. Software versions, capabilities, and licenses

**Canonical sources:**
- GitHub releases page (`github.com/<org>/<repo>/releases`)
- Project documentation (often `docs.<project>.org` or in-repo `README.md`)
- LICENSE file (verify directly via `raw.githubusercontent.com/<org>/<repo>/master/LICENSE` or equivalent)

**Verify:**
- Exact version number
- Supported platforms (CUDA / OpenCL / HIP / CPU / Metal / arm64 / etc.)
- License type (Apache-2.0 / MIT / GPL-2.0 / LGPL / dual / etc.)
- Distribution mode considerations (bundling, containerization, source vs binary)

**Common errors to avoid:**
- Trusting an intermediate audit that didn't open the LICENSE file directly (cf. fpocket: was briefly stated as GPL-3 based on one audit before final verification confirmed MIT)
- Trusting agent-generated platform compatibility claims (cf. "OpenMM has Apple Metal backend" — does not exist)
- Confusing version-specific behavior with project-wide behavior

**Sample query:** for fpocket: open https://raw.githubusercontent.com/Discngine/fpocket/master/LICENSE and read the actual license header.

**Re-verify window:** Before any installation; 90 days for tool selection in draft plans.

### 5. Compound library and dataset sizes

**Canonical sources:**
- Project websites + most recent peer-reviewed publication
- For ZINC: https://zinc.docking.org + Tingle & Irwin 2023 paper
- For Enamine REAL: https://enamine.net/compound-collections/real-compounds
- For TCGA / GDC: https://portal.gdc.cancer.gov/projects/[project] (or API)
- For RCSB PDB: https://www.rcsb.org/stats

**Verify:**
- Exact compound count or file size
- Date of the size measurement
- 2D vs 3D vs make-on-demand vs in-stock distinction

**Common errors:**
- Quoting a peer-reviewed number as if it's current (ZINC22 has grown since the 2023 paper)
- Confusing Enamine REAL (~94.5B Apr 2026) with REAL-Space (different) or with REAL-Database (different again)
- Confusing PDC "managed" vs "cumulative downloaded" volumes

**Re-verify window:** 90 days before any compute-budget calculation.

### 6. Corporate status (acquisitions, IPOs, divestitures)

**Canonical sources:**
- Company investor-relations page
- SEC EDGAR filings (https://www.sec.gov/edgar)
- Stock exchange listing (NASDAQ, NYSE) — confirms whether company still trades independently

**Verify:**
- Whether the company exists as an independent entity
- Acquisition status + date + acquirer
- Stock ticker

**Common errors:**
- Wholesale fabrication of acquisitions (cf. "PMV (now Pfizer)" — never happened; PMV remains NASDAQ:PMVP)
- Outdated "now owned by X" claims that don't reflect subsequent divestitures

**Re-verify window:** 30 days before any external claim involving corporate identity.

### 7. Lab attributions and institutional affiliations

**Canonical source:** The cited paper's author-affiliation footnote at the front of the PDF.

**Verify:**
- First author's affiliation (this is who "did the work")
- Senior author's affiliation
- The relevant collaboration institutions

**Common error:**
- Misattributing collaborative work to a famous lab when the work was actually led elsewhere (cf. F@h KRAS-VHL — was Xuhui Huang/UW-Madison, not Chodera/MSKCC)

**Sample query:** Pull the cited paper's PDF; check the affiliation footnotes on page 1.

**Re-verify window:** Before any partnership-pitch email.

### 8. Cell-line mutation status

**Canonical source:** Cellosaurus (https://www.cellosaurus.org/[CVCL-id]) — also cross-check DepMap.

**Verify:**
- KRAS / TP53 / CDKN2A / SMAD4 status at the exact allele level
- Whether the literature claim is current or has been superseded

**Common error:**
- Trusting older textbook/literature claims that Cellosaurus has since flagged (cf. Hs 766T = KRAS Q61H, not WT)

**Re-verify window:** Once per project; cite Cellosaurus version.

### 9. Numerical claims with 3-or-more-digit precision

Any claim like "62.5% ORR" or "23.31 GB" or "6.45% APC" or "1,583 GB" should be tied to a specific primary source. Suspicious-looking precision is a hallucination tell.

**Sample query:** for "1,583 GB RCSB PDB 2025 archive" → land on https://www.rcsb.org/stats/data_storage_growth and confirm.

**Re-verify window:** 30 days before publication.

### 10. Compute budget math

For any claim of "N CPU-hours" or "N CPU-years": verify the underlying arithmetic.

**Sample sanity-check:**
- `compounds × seconds_per_compound / 3600 = core-hours`
- `core-hours / 8760 = core-years`
- Apply realistic parallelism and overhead factors before claiming "feasible at N hosts × M hours/day"

**Common error:** Unit confusion (cf. "10B × 5s = 50B core-hours" — actually 50B CPU-seconds = ~14M core-hours, 3,500× off).

**Sample query:** plug the numbers into Python and re-derive.

---

## Anti-patterns to watch for

Errors recur in the following surface forms. Watch for them in any agent-generated text:

- **"Updated" or "current" without a date.** Anything claimed as "current" should have a date or it can be silently stale.
- **A confident specific number with no source.** E.g., "62% ORR" without a trial-name + cohort-size citation.
- **"FDA-approved" with no indication.** Always specify tumor type and line-of-therapy.
- **"The X lab at Y published Z."** Verify lab + institution against author affiliations.
- **A PDB ID quoted in plain text without an entry-title or ligand check.** PDB IDs are the most error-prone category.
- **"Acquired by" or "now owned by" without IR/SEC link.** Corporate fabrications.
- **"This file runs on Mac M1/M2/M3/M4."** Apple Silicon claims default to over-optimistic.
- **Round-number claim count.** If a doc claims "~620 claims audited" but the totals row sums to 760, one of them is wrong.
