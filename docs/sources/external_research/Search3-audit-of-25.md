# Problems Found in `25_full_audit_synthesis.md`

Date reviewed: 2026-05-22  
Scope: Review of the uploaded audit synthesis as a planning/control document. This is **not** a full re-audit of every underlying scientific claim. It focuses on internal consistency, open risks, correction workflow, and high-risk claims that could break downstream work.

## Overall verdict

Use the document as an **internal reliability map**, not as a final source of truth. The plan is directionally useful, but it still has unresolved contradictions and stale/high-risk items. The most important fixes are:

1. Reconcile the headline claim count and total scope.
2. Stop treating "logged" items as resolved.
3. Split correction status into `Fixed`, `Flagged`, `Logged only`, and `Needs re-verification`.
4. Quarantine all PDB IDs until they are validated against RCSB/wwPDB.
5. Re-check current software/platform/license claims before they drive build or deployment decisions.
6. Replace the "safe to cite" section with a source-linked, versioned evidence table.

## Severity key

| Severity | Meaning |
|---|---|
| P0 / Blocking | Do not rely on the plan as a control document until fixed. |
| P1 / High | Likely to cause bad decisions, bad citations, or rework. |
| P2 / Medium | Cleanup needed for clarity, auditability, or future maintenance. |

---

## P0 / Blocking problems

| ID | Problem | Evidence in the plan | Why it matters | Recommended fix |
|---|---|---|---|---|
| P0-01 | Headline claim count contradicts the totals table. | Headline says `~620 distinct factual claims audited`; totals row says `~760`, and the A-M rows sum to roughly that larger number. | The most visible metric in the document is wrong, which weakens trust in the audit. | Change the headline to `~760` or add a reconciliation note explaining why the headline intentionally excludes some claims. |
| P0-02 | The plan overclaims that all material false claims were fixed or flagged. | Bottom line says all material false claims were either fixed in-place or flagged, but multiple entries say `Logged`, `not yet fixed`, or `not individually fixed`. Examples include PEGPH20 in `01_disease.md`, ESPAC-5F OS, and the `21_local_test_plan.md` 8AZV issue. | A logged issue is not the same as a fixed or visible warning. This creates false closure. | Replace the bottom-line sentence with: `All identified material false claims have been fixed, flagged, or logged for follow-up. Logged-only items remain unresolved.` |
| P0-03 | "Logged" is not a resolution state. | The document repeatedly uses `Logged` for known problems without assigning owner, source file location, deadline, or closure test. | Logged-only issues can be forgotten and later cited as if resolved. | Add a tracking table with columns: `Issue ID`, `Source doc`, `Exact location`, `Status`, `Owner`, `Evidence URL`, `Fix required`, `Closure criterion`. |
| P0-04 | Several document confidence ratings are too high given unresolved issues. | `21_local_test_plan.md` is marked `High` while 8AZV is still flagged but not rewritten. `31_mutant_p53_structural_biology.md` is marked `Medium`, but the PDB column still needs full RCSB re-verification before pipeline use. | Users may assume a high-confidence file is operationally safe when it still contains unresolved blockers. | Split confidence into two fields: `Narrative confidence` and `Pipeline/readiness confidence`. For PDB-driven docs, mark pipeline readiness `Blocked` until PDB manifest validation is complete. |
| P0-05 | The p53 structural-biology problem is still only partially contained. | Audit K reports 13 wrong PDB IDs and says the PDB column needs full RCSB re-verification. | A header warning does not prevent pipeline use, copying IDs into scripts, or reintroducing wrong structures downstream. | Quarantine all PDB IDs in `31_mutant_p53_structural_biology.md`; replace the table column with `UNVERIFIED_PDB_ID` until each row has RCSB title, ligand ID, mutation, construct, resolution, assembly, and validation date. |
| P0-06 | The KRAS G12D apo-structure guidance is not strong enough. | 8AZV is correctly flagged as not G12D apo, but the proposed alternatives include 4DSO or ligand-stripped 8AZY. 8AZY is a KRAS-G12D + BI-2865 complex, and 4DSO is a Ras small-molecule ligand structure rather than a clean default apo control. | The plan could replace one bad structure choice with another underdocumented structure choice. | Require a structure-selection mini-audit for every control structure: mutation, nucleotide state, ligand state, construct boundaries, missing residues, biological assembly, and rationale. Do not name 4DSO or stripped 8AZY as defaults without that manifest. |
| P0-07 | Current fpocket licensing appears ambiguous or incorrectly corrected. | The plan says `fpocket = GPL-3` and treats that as corrected. Current Discngine/fpocket `LICENSE` and README identify MIT licensing; older SourceForge-era materials may differ. | A wrong license conclusion can create unnecessary restrictions or, worse, miss actual obligations if the wrong source/version is bundled. | Replace `fpocket = GPL-3` with a version-pinned license statement: `fpocket license must be determined from the exact source/version packaged. Current Discngine/fpocket master appears MIT; preserve LICENSE files for any bundled binary/source.` |
| P0-08 | OpenFE / Apple Silicon correction appears stale. | The plan says OpenFE requires Rosetta 2 on Apple Silicon. Current OpenFE docs provide a macOS arm64 installer and say macOS x86_64 is no longer supported. | Local test plans based on Rosetta-only assumptions may waste time or install the wrong stack. | Update to: `OpenFE supports macOS arm64 installation for local preparation/testing. Production RBFE should still be run on Linux/CUDA or a validated HPC/container path. No Apple Metal OpenMM backend should be assumed.` |
| P0-09 | The "safe to cite" section includes claims that still need qualification. | Examples: MRTX1133 is listed as discontinued due to suboptimal PK; zenocutuzumab is summarized as approved for `NRG1+ tumors including PDAC`; fpocket is listed as GPL-3. | A section labeled "safe to cite" invites downstream reuse without rechecking nuance. | Rename the section to `Lower-risk claims after audit` and add a `primary source` column, `verified as of` date, and caveat for each claim. |
| P0-10 | The plan lacks a publication gate. | It says human verification is required before external-facing use, but does not define a gate, checklist, or blocking criteria. | Future writing can still slip through with uncited or stale claims. | Add a rule: `No external-facing claim may ship unless it has a primary-source URL, verification date, and claim owner. PDB/FDA/license/platform claims require primary-source verification within 30 days of publication.` |

---

## P1 / High-priority problems

| ID | Problem | Evidence in the plan | Why it matters | Recommended fix |
|---|---|---|---|---|
| P1-01 | The totals/scope description is inconsistent. | The introduction refers to external reports A-C; the totals row says `2 external reports`. The totals row also says `9 deep-dive docs + 5 synthesis/tech docs + 2 external reports`, which does not map cleanly onto the A-M audit list. | Ambiguous audit scope makes it hard to know what was actually covered. | Add a `Corpus audited` appendix listing every file/report exactly once, with document path, audit ID, claim count, and status. |
| P1-02 | Approximate counts and ranges make the metrics hard to audit. | Rows include `~75`, `2-3`, `~6`, etc.; totals are presented as percentages. | It is unclear whether percentages are computed from exact counts or approximations. | Keep approximate counts in narrative only. For the table, use exact integers or add a footnote that the percentages are approximate and computed from rounded estimates. |
| P1-03 | The plan does not define `Verified`, `Partial`, `False`, or `Unverifiable`. | The table uses these labels but there is no rubric. | Different reviewers may classify the same claim differently. | Add a classification rubric with examples and required evidence type for each class. |
| P1-04 | Materiality is not defined. | The document distinguishes material false claims from partial issues, but no threshold is specified. | Low-level numerical drift and mission-critical false claims are mixed together. | Define materiality tiers: `Scientific conclusion-changing`, `pipeline-breaking`, `regulatory/compliance`, `citation/attribution`, `minor numeric drift`, `wording precision`. |
| P1-05 | Correction evidence is not auditable. | Many items say `Fixed`, `Fixed via replace_all`, or `Flagged`, but no commit hash, diff, or final text is shown. | A reviewer cannot verify whether a fix landed correctly or introduced new errors. | For every fixed item, record commit hash or file diff, final corrected sentence, and reviewer/date. |
| P1-06 | Flagged-in-header is too weak for high-risk machine-readable fields. | The p53 doc keeps wrong PDB IDs in tables but warns in the header. | Agents, scripts, and humans may copy the table entries while missing the warning. | For high-risk fields, replace wrong values with `DO_NOT_USE_UNVERIFIED` or move them to a quarantine appendix. |
| P1-07 | The plan does not distinguish narrative trust from operational use. | A document can be good enough to read but unsafe for docking, licensing, or clinical-status decisions. | Users may reuse content in the wrong context. | Add `Allowed uses`: `background reading`, `internal draft`, `grant/proposal`, `pipeline input`, `external publication`. Mark each doc accordingly. |
| P1-08 | Many volatile claims lack a `verified as of` date. | FDA approvals, clinical trial status, BOINC Central capabilities, OpenFE support, Enamine size, AlphaFold weights, and corporate status are time-sensitive. | These claims can become stale quickly. | Add `verified_as_of` dates and recheck intervals. Use shorter intervals for FDA/trial/software/platform claims. |
| P1-09 | Clinical approval wording needs tighter indication boundaries. | Zenocutuzumab is summarized as approved for `NRG1+ tumors including PDAC`. | FDA indications are tumor- and line-of-therapy-specific; broad shorthand can overstate label scope. | Use exact indication language: advanced/unresectable/metastatic NRG1 fusion-positive NSCLC or pancreatic adenocarcinoma after prior systemic therapy; add the May 2026 cholangiocarcinoma indication if relevant. |
| P1-10 | MRTX1133 termination rationale is too specific without source hierarchy. | The plan says discontinued by BMS in Jan 2025 due to suboptimal PK. ClinicalTrials.gov lists termination due to formulation challenges; NCI says the study ended before phase 2. | The plan should not present a secondary-report explanation as the official registry reason. | Rewrite as: `The MRTX1133 study was terminated before phase 2; the registry reason is formulation challenges, with secondary reporting citing variable/suboptimal PK.` |
| P1-11 | "Safe to cite" is not source-linked. | The safe-to-cite section lists many numbers and claims without primary-source links in the synthesis itself. | The section cannot function as a citation-ready reference table. | Convert it into a table with `claim`, `primary source`, `exact source text/field`, `verified as of`, `caveat`, and `reuse status`. |
| P1-12 | Partial items are deferred without triage. | The plan says ~145 partial items were not individually edited because doing so would require larger rewrites. | Some partials may be harmless, but others could affect conclusions. | Triage partials into `must fix`, `fix opportunistically`, and `acceptable with caveat`. |
| P1-13 | The plan lacks automated validation for known failure modes. | Lessons learned identify repeated failures in PDB IDs, FDA status, licenses, software compatibility, and compute math. | The next generation of content can repeat the same mistakes. | Add preflight checks: RCSB API for PDB IDs; FDA/Drugs@FDA for approvals; ClinicalTrials.gov for trial status; GitHub/conda package metadata for licenses; unit tests for compute-budget arithmetic. |
| P1-14 | The compute-budget correction needs a reproducible calculation. | The plan says naive VS arithmetic was off by ~3,500x and fixed. | Without the actual formula, this class of error may recur. | Add a small calculation block: `core_hours = compounds * seconds_per_compound / 3600`, plus assumptions for cores, parallelism, and overhead. |
| P1-15 | BOINC/volunteer-computing operational claims need capacity caveats. | Claims like hundreds of jobs/sec dispatch and Docker support are listed as safe without deployment assumptions. | BOINC feasibility depends on job size, validation, bandwidth, host mix, wrappers, and signing/operations maturity. | Add a capacity-model appendix with workload unit size, input/output bytes, validation model, expected host failure rate, and scheduler throughput assumptions. |
| P1-16 | License compliance is reduced to individual package labels. | The plan lists licenses for tools and data but does not specify distribution mode. | Compliance depends on whether binaries, containers, source, data, or web services are redistributed. | Add a license matrix with columns: `component`, `version`, `source`, `license`, `distribution mode`, `obligations`, `allowed in BOINC app?`, `allowed in Docker image?`. |
| P1-17 | Dataset claims are treated as static. | Dataset sizes and counts are included in "safe to cite." | Archive sizes and file counts change. | Add source snapshots or API query outputs for dataset counts, with date and exact query. |
| P1-18 | The plan mixes disease biology, computational infrastructure, and compliance in one status model. | All docs are assigned one confidence label. | A document may be clinically accurate but legally risky, or scientifically accurate but pipeline-unsafe. | Use separate ratings: `clinical`, `structural`, `computational`, `platform`, `license/compliance`, `publication readiness`. |

---

## P2 / Medium-priority cleanup

| ID | Problem | Why it matters | Recommended fix |
|---|---|---|---|
| P2-01 | The term `FDA-approved` is used where `accelerated approval` or exact indication language would be better. | Regulatory precision matters for clinical claims. | Use `FDA accelerated approval`, `regular approval`, or `investigational`, as applicable. |
| P2-02 | The plan sometimes uses shorthand like `NRG1+` instead of `NRG1 fusion-positive`. | `NRG1+` is ambiguous and can be interpreted too broadly. | Use `NRG1 fusion-positive` for zenocutuzumab claims. |
| P2-03 | Dates are sometimes vague or unsupported. | Examples include `Jan 2025`, `March 2026`, `Apr 2026 update`. | Add exact date, source, and whether date refers to announcement, registry update, publication, or access date. |
| P2-04 | "High-confidence verified claims worth knowing" mixes final conclusions with caveated items. | A user may not notice which items still carry caveats elsewhere. | Add a `reuse_status` field: `OK internal`, `OK external with citation`, `needs caveat`, `do not reuse`. |
| P2-05 | Warnings are not standardized. | Different docs may use different warning language or visibility. | Create a standard warning block template for unverifiable/high-risk sections. |
| P2-06 | PDB errors are described, but no canonical replacement workflow is specified. | Reviewers may pick replacement structures ad hoc. | Add a structure-selection SOP: query, verify mutation/ligand/nucleotide, inspect biological assembly, download validation report, record selection rationale. |
| P2-07 | The plan has no regression-prevention mechanism. | Fixed errors can reappear in future agent-generated drafts. | Maintain a `known_bad_claims.md` denylist and a `must_verify_claim_types.md` checklist. |
| P2-08 | Source hierarchy is implicit. | Primary sources, secondary reporting, and internal notes are blended. | Define hierarchy: regulatory registry/FDA/RCSB/GitHub LICENSE > peer-reviewed paper > company press release > secondary media > model-generated summary. |
| P2-09 | The document does not distinguish `unverifiable` from `not yet checked`. | These require different actions. | Use separate labels: `Unverifiable after search`, `Not checked`, `Source unavailable`, `Needs expert judgment`. |
| P2-10 | Some status claims are brittle because they depend on current web state. | Websites, GitHub repos, package metadata, and FDA pages change. | Archive evidence snapshots or store source excerpts in the audit appendix. |

---

## Specific wording replacements

### Replace the headline

Current:

```md
~620 distinct factual claims audited across ~10,000 lines of source content.
```

Recommended:

```md
~760 distinct factual claims audited across ~10,000 lines of source content.
```

If some audits are intentionally excluded from the headline, add a reconciliation note explaining exactly which ones.

### Replace the bottom line

Current:

```md
All material false claims that were identified have been either fixed in-place or flagged with explicit verification warnings.
```

Recommended:

```md
Identified material false claims have been fixed, flagged in affected documents, or logged for follow-up. Items marked "logged" are not resolved until the affected source file is edited or carries a visible warning.
```

### Replace the fpocket license claim

Current:

```md
fpocket = GPL-3 (corrected)
```

Recommended:

```md
fpocket license is version/source-dependent. Current Discngine/fpocket appears MIT-licensed, but any BOINC/container redistribution must pin the exact source/version and preserve the corresponding LICENSE file.
```

### Replace the OpenFE / Apple Silicon claim

Current:

```md
OpenFE requires Rosetta 2 emulation on Apple Silicon.
```

Recommended:

```md
OpenFE currently supports macOS arm64 installation for local preparation/testing workflows. Production RBFE should be validated on Linux/CUDA or an equivalent reproducible HPC/container path. Do not assume an upstream OpenMM Apple Metal backend.
```

### Replace the MRTX1133 clinical-status wording

Current:

```md
MRTX1133 clinically discontinued by BMS Jan 2025 due to suboptimal PK.
```

Recommended:

```md
The MRTX1133 clinical study was terminated before phase 2; the official registry reason is formulation challenges, while secondary reporting has cited variable/suboptimal PK.
```

### Replace the zenocutuzumab wording

Current:

```md
Zenocutuzumab FDA approval Dec 2024 for NRG1+ tumors including PDAC.
```

Recommended:

```md
Zenocutuzumab-zbco received FDA accelerated approval on Dec. 4, 2024 for adults with advanced, unresectable, or metastatic NRG1 fusion-positive NSCLC or pancreatic adenocarcinoma after prior systemic therapy. On May 8, 2026, FDA also approved it for advanced, unresectable, or metastatic NRG1 fusion-positive cholangiocarcinoma after prior systemic therapy.
```

### Replace the PDB-use guidance

Recommended new rule:

```md
No PDB ID may be used in a docking, MD, or validation workflow unless it appears in a checked structure manifest containing: PDB ID, RCSB title, mutation, nucleotide state, ligand identity, ligand role, organism, construct/residue range, resolution/method, biological assembly, validation date, and reviewer.
```

---

## Proposed revised status model

Use this status model instead of binary "fixed/logged" language.

| Status | Meaning | Allowed reuse |
|---|---|---|
| `Fixed in source` | The source document was edited and the corrected text is recorded. | Internal and external reuse after citation check. |
| `Flagged in source` | A visible warning exists in the affected document, but the underlying content may remain. | Internal use only; no pipeline use. |
| `Logged only` | The issue is known but not visible in the affected source document. | Do not cite or reuse until fixed/flagged. |
| `Needs primary-source re-verification` | The claim depends on volatile or high-risk facts. | No external use until rechecked. |
| `Quarantined` | Known-bad or high-risk structured data has been removed from normal workflow. | No reuse except for audit/debugging. |
| `Resolved` | Fixed, source-linked, reviewed, and regression-protected. | Reuse allowed according to confidence class. |

---

## Minimum closure checklist

Before treating the plan as reliable, close these items:

- [ ] Reconcile `~620` vs `~760`.
- [ ] Reconcile `external reports A-C` vs `2 external reports`.
- [ ] Add exact corpus inventory.
- [ ] Add definitions for `Verified`, `Partial`, `False`, and `Unverifiable`.
- [ ] Add materiality tiers.
- [ ] Convert all `Logged` items to tracked issue IDs.
- [ ] Lower or split confidence ratings for docs with unresolved blockers.
- [ ] Quarantine p53 PDB IDs until manifest-verified.
- [ ] Recheck `21_local_test_plan.md` structure choices before any docking/MD workflow.
- [ ] Replace fpocket licensing language with version-pinned licensing.
- [ ] Update OpenFE Apple Silicon guidance.
- [ ] Narrow zenocutuzumab indication wording.
- [ ] Nuance MRTX1133 termination wording.
- [ ] Add evidence URLs and `verified as of` dates to every safe-to-cite claim.
- [ ] Add a publication gate for PDB/FDA/license/platform/corporate/cell-line claims.
- [ ] Add regression-prevention files: `known_bad_claims.md`, `must_verify_claim_types.md`, and `structure_manifest.csv`.

---

## Source links to use in the next pass

These are the primary or near-primary sources most relevant to the high-risk issues above:

- OpenFE installation and macOS arm64 installer: https://docs.openfree.energy/en/stable/installation.html
- OpenMM platform installation guidance: https://github.com/openmm/openmm/blob/master/docs-source/usersguide/application/01_getting_started.rst
- fpocket current LICENSE: https://raw.githubusercontent.com/Discngine/fpocket/master/LICENSE
- fpocket current README license note: https://raw.githubusercontent.com/Discngine/fpocket/master/README.md
- ClinicalTrials.gov MRTX1133 NCT05737706: https://clinicaltrials.gov/study/NCT05737706
- NCI MRTX1133 trial page: https://www.cancer.gov/research/participate/clinical-trials-search/v?id=NCI-2023-02950
- FDA zenocutuzumab Dec. 4, 2024 approval: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-zenocutuzumab-zbco-non-small-cell-lung-cancer-and-pancreatic
- FDA zenocutuzumab May 8, 2026 cholangiocarcinoma approval: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-zenocutuzumab-zbco-advanced-unresectable-or-metastatic-cholangiocarcinoma
- RCSB 8AZV: https://www.rcsb.org/structure/8AZV
- RCSB 8AZY: https://www.rcsb.org/structure/8AZY
- RCSB 4DSO: https://www.rcsb.org/structure/4DSO
- RCSB 9BR4: https://www.rcsb.org/structure/9BR4

---

## Final recommended disposition

Label the current synthesis:

```md
Status: Internal audit map only. Not publication-ready. Not pipeline-ready for PDB-dependent workflows.
```

Promote it to publication-supporting status only after the P0 items are closed and the `safe to cite` section is converted into a versioned evidence table.
