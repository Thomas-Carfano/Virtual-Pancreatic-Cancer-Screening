# Verification: BOINC platform + tools + licenses

This file verifies claims from:
- Report 1: `/Volumes/Storage April 2026/PancreaticCancer/sources/external_research/1Search - deep-research-report.md`
- Report 2: `/Volumes/Storage April 2026/PancreaticCancer/sources/external_research/2search - deep-research-report.md`

Verifications performed May 22, 2026 via WebFetch and WebSearch against authoritative sources (boinc.berkeley.edu, github.com/BOINC, official tool repositories).

---

## BOINC platform claims

### Claim: BOINC Central exists; it lets scientists use volunteer computing without running a full project; as of March 2026 it supports Docker-packaged applications and AutoDock
**Source in reports:** Report 2, Executive summary, line 9: "The most pragmatic launch path is a pilot on BOINC Central, which openly states that it lets scientists use volunteer computing without running a full project and, as of March 2026, supports Docker-packaged applications and AutoDock." Also Report 2, lines 75, 171, 179.
**Status:** Verified
**Evidence:** BOINC Central exists at https://boinc.berkeley.edu/central/. The official page states the purpose is to "make the power of volunteer computing available to all scientists, including those with little money and technical resources and those whose need for computing is sporadic." It explicitly supports "Any application packaged with Docker" and "Autodock from the Scripps Research Institute." It was launched November 26, 2021, and a March 24, 2026 update announces completion of two projects (Boolean Chains, Cislunar Orbit Stability Analyzer) and seeks new research initiatives. Docker support is delivered via BUDA (BOINC's framework for Docker-based apps), documented at https://github.com/BOINC/boinc/wiki/BUDA-job-submission. The AutoDock Vina BOINC wiki at https://github.com/BOINC/boinc-autodock-vina/wiki documents molecular docking with AutoDock4, Vina, and Vinardo on BOINC Central.
**Notes:** Report 1 does not explicitly mention "BOINC Central"; this claim is primarily from Report 2. Both reports accurately describe the AutoDock/Docker capability.

### Claim: BOINC supports docker_wrapper, vboxwrapper, native apps, BOINC wrapper, WSL wrapper
**Source in reports:** Report 1, line 11, line 72, lines 78-82 in the frameworks table; Report 2, line 77.
**Status:** Verified
**Evidence:** BOINC's GitHub wiki (https://github.com/BOINC/boinc/wiki/BOINC-apps-(introduction)) documents three primary app types: Native app (program with BOINC API calls compiled and linked to the BOINC runtime library), Wrapper (a BOINC-supplied program that interfaces between the client and an unmodified executable), and VM apps (apps running inside a VM via vboxwrapper). Docker support is documented via `docker_wrapper` at https://github.com/BOINC/boinc/wiki/Docker-apps and https://github.com/BOINC/boinc/wiki/Docker-wrapper-release-notes. VirtualBox apps documented at https://github.com/BOINC/boinc/wiki/VboxApps. WSL is documented as a Windows prerequisite for Docker/Podman BOINC jobs. The vboxwrapper source is in the boinc repo at samples/vboxwrapper/vboxwrapper.cpp.
**Notes:** The BOINC documentation now emphasizes Podman as the preferred Docker replacement on the volunteer client.

### Claim: BOINC servers can dispatch "hundreds of jobs per second even on a single machine"
**Source in reports:** Report 2, line 62: "BOINC servers can dispatch hundreds of jobs per second even on a single machine, so the operational bottleneck is more likely to be method curation and postprocessing than scheduler throughput."
**Status:** Verified
**Evidence:** David P. Anderson's paper "BOINC: A Platform for Volunteer Computing" (https://arxiv.org/pdf/1903.01699 and https://boinc.berkeley.edu/boinc_a_platform_for_volunteer_computing.pdf) and the "High-Performance Task Distribution for Volunteer Computing" paper (https://boinc.berkeley.edu/boinc_papers/server_perf/server_perf.pdf) state that a BOINC server even on a single machine can dispatch hundreds of jobs per second. The mechanism uses a shared-memory cache (typically ~1,000 job instances) to avoid per-RPC database queries. The performance paper reports approximately 8.8 million tasks/day on a $4,000 single-server setup.
**Notes:** The figure is essentially a known canonical BOINC throughput estimate from Anderson's papers.

### Claim: Adaptive replication tracks trust at the (host, app_version) level
**Source in reports:** Report 2, line 106: "BOINC notes that adaptive replication tracks trust at the (host, app version) level and can move the overhead close to one instead of a full factor-of-two replication penalty."
**Status:** Verified
**Evidence:** The BOINC AdaptiveReplication wiki (https://boinc.berkeley.edu/trac/wiki/AdaptiveReplication; also discussed in https://arxiv.org/pdf/1903.01699) states: "BOINC maintains the number CV(H, V) of consecutive valid results returned by host H using app version V, which is incremented when a replicated job computed with (H, V) is validated, and is zeroed when such a job is found to be invalid. App version is included because some hosts may be less reliable for GPU jobs than for CPU jobs." When CV(H, V) >= 10, the host is trusted probabilistically (1 - 1/CV(H, V)), reducing overhead substantially below 2x.
**Notes:** Exact (host, app version) tuple is confirmed by Anderson's documentation.

### Claim: BOINC documents signing-key-offline-machine recommendation
**Source in reports:** Report 1, line 123: "the signing key should live offline on a dedicated code-signing machine"; Report 2, line 108: "keep the signing key on an offline, physically secured machine."
**Status:** Verified
**Evidence:** BOINC Security documentation (https://boinc.berkeley.edu/wiki/BOINC_Security and https://github.com/BOINC/boinc/wiki/BOINC_Security) states explicitly: "Projects are instructed to keep the private key only on a computer that is never connected to a network, and that is physically secure" and "As long as these instructions are obeyed, hackers cannot sign malware, even if they break into the project's server, and therefore they cannot trick BOINC into running malware." The page advises using a separate code-signing machine (an old slow one is fine), kept in a locked room, and transferring files via USB.
**Notes:** Some projects do not follow this practice (BOINC's own docs acknowledge this).

### Claim: BOINC VirtualBox cookbook example uses a 1.9 GB VM image
**Source in reports:** Report 2, line 77: "the BOINC VirtualBox cookbook also shows that VM-based deployment can involve a large VM image download — the example uses a 1.9 GB image."
**Status:** Verified
**Evidence:** The BOINC wiki page "Deploy Linux apps using VirtualBox (cookbook)" (https://github.com/BOINC/boinc/wiki/Deploy-Linux-apps-using-VirtualBox-(cookbook)) states verbatim: "We create a symbolic links to the VM image (which is 1.9 GB) and to the vboxwrapper executable. This saves disk space if we use them in other app versions."
**Notes:** This is an example/illustration in the cookbook; not a hard requirement, but a representative size for documentation purposes.

### Claim: Rosetta@home, Docking@Home, World Community Grid/OpenPandemics, GPUGRID — existence and status as of 2026
**Source in reports:** Report 1, line 11 and line 86: "Existing biomedical volunteer-computing projects such as Rosetta@home, Docking@Home, World Community Grid/OpenPandemics, and GPUGRID show that volunteer computing can handle protein modeling, docking, and GPU biomedical workloads."
**Status:** Partially verified — Docking@Home is retired (a substantive issue with Report 1's "existing" framing)
**Evidence:**
- **Rosetta@home:** Active. https://boinc.bakerlab.org/ runs at Baker Lab/UW; in 2026 deploying RosettaVS (Nature Communications) for small molecule virtual screening and peptide simulations. Documented continuously active since June 26, 2005.
- **Docking@Home:** Retired May 23, 2014. Per https://en.wikipedia.org/wiki/Docking@Home and the project news page http://docking.cis.udel.edu/about/project/news.html, jobs stopped distribution April 30, 2014; server stopped accepting results May 23, 2014. Retired because the University of Delaware no longer had resources to maintain it. So when Report 1 calls it an "existing biomedical volunteer-computing project" alongside currently active ones, it is misleading. Docking@Home was a *historical precedent*, not an existing project — but it does still serve as a precedent that BOINC has hosted protein-ligand docking.
- **World Community Grid / OpenPandemics-COVID-19:** Active. The OpenPandemics project page (https://www.worldcommunitygrid.org/research/opn1/overview.s) and recent WCG articles confirm activity through 2026.
- **GPUGRID:** Active, but with caveats. The project moved to a new server in April 2025 and is in a transition period redeploying applications and fixing bugs. Server status: https://gpugrid.net/gpugrid/server_status.php.
**Notes:** Recommend reframing Docking@Home as "former" or "historical" in any user-facing materials sourced from these reports. The other three are validly characterized.

### Claim: WCG OpenPandemics work helped motivate features added to AutoDock-GPU
**Source in reports:** Report 1, line 86: "a WCG article notes that large-scale volunteer docking helped motivate features added to AutoDock-GPU."
**Status:** Verified
**Evidence:** The WCG article "Open-source software from OpenPandemics - COVID-19 helps the researchers" at https://www.worldcommunitygrid.org/about_us/article.s?articleId=750 states: "New features such as flexible residues, modifiable pair potentials, and a contact analysis that have been added in the latest two releases of the AutoDock-GPU docking engine (v1.4 and v1.5) were developed to specifically address the needs arising during a large scale project such as OpenPandemics - COVID-19, but will benefit the whole community of researchers using these tools."
**Notes:** Article cited specifies flexible residues, modifiable pair potentials, and contact analysis in v1.4 and v1.5 — useful detail for downstream citation.

---

## Docking tool and dependency claims

### Claim: AutoDock Vina is Apache 2.0 licensed
**Source in reports:** Report 1 line 39 ("Apache 2.0"); Report 1 line 7.
**Status:** Verified
**Evidence:** The official Vina GitHub at https://github.com/ccsb-scripps/AutoDock-Vina confirms "AutoDock Vina is distributed under the Apache License, Version 2.0" with the Apache-2.0 license file in the repo and license badge. The Vina home page is https://vina.scripps.edu/ (timed out during verification, but the GitHub source is canonical for licensing).
**Notes:** None.

### Claim: AutoDock-GPU repo contains GPL-2.0 and LGPL-2.1 license files
**Source in reports:** Report 1 line 40: "GPL-2.0 and LGPL-2.1 files are present in the official repo."
**Status:** Verified
**Evidence:** https://github.com/ccsb-scripps/AutoDock-GPU contains both `LICENSE` (GPL-2.0) and `LICENSE_LGPL` (LGPL-2.1) files. GitHub's own license-detection panel displays "GPL-2.0, LGPL-2.1 licenses found."
**Notes:** The exact mapping of which code files are under which license is not always clear from the top-level licensing summary, but the *presence of both* license files is what Report 1 claims, and that is correct.

### Claim: GNINA is dual GPL/Apache; GPL required when OpenBabel-linked; CUDA 12+, OpenBabel3, RDKit, Boost, protobuf, HDF5 deps; official prebuilt binary + Docker image
**Source in reports:** Report 1 line 41.
**Status:** Verified
**Evidence:** https://github.com/gnina/gnina states explicitly: "gnina is dual licensed under GPL and Apache. The GPL license is necessitated by the use of OpenBabel (which is GPL licensed)." To use under Apache only requires removing OpenBabel references. The README lists dependencies: CUDA (>= 12.0 required), OpenBabel3, build tools (CMake, Boost, Eigen3, Google Glog, Protobuf), libraries (HDF5, Atlas, RDKit), Python development files and numpy. Pre-built binaries are available via GitHub Releases and a Docker image is published on Docker Hub under the gnina organization.
**Notes:** The CUDA 12.0+ requirement and the OpenBabel3-induced GPL constraint are both confirmed verbatim from the README. The dep list in Report 1 is accurate.

### Claim: P2Rank is MIT-licensed, requires Java 17+, runs on PDB/mmCIF/BinaryCIF input
**Source in reports:** Report 1 line 42.
**Status:** Verified
**Evidence:** https://github.com/rdk/p2rank confirms MIT license, "Java 17 or later (tested up to Java 26)" as the runtime requirement, and supports PDB (.pdb), mmCIF (.cif), and BinaryCIF (.bcif) plus gzipped/Zstandard-compressed versions.
**Notes:** None.

### Claim: fpocket is MIT, written in C, has an official Docker image
**Source in reports:** Report 1 line 43.
**Status:** Verified
**Evidence:** https://github.com/Discngine/fpocket — MIT License. Codebase composition: 67.7% C (primary), plus HTML (17.7%), C++ (9.8%), Makefile, Shell, Roff. Official Docker image documented as `docker pull fpocket/fpocket`; the repo includes Dockerfiles for build/run.
**Notes:** Report 1 describes fpocket as written in C; the codebase is in fact primarily C with a smaller C++ component. This matches the report's claim.

### Claim: OpenMM is MIT and LGPL; supports CUDA/OpenCL/HIP platforms
**Source in reports:** Report 1 line 44.
**Status:** Verified
**Evidence:** https://github.com/openmm/openmm — "most of the source code is covered by the MIT license or the GNU Lesser General Public License (LGPL)" (full details in Licenses.txt). Platform support per https://docs.openmm.org/latest/developerguide/07_cuda_platform.html and related platform-specific pages: CudaPlatform (NVIDIA GPUs), HipPlatform (ROCm-compatible AMD GPUs), OpenCLPlatform (Intel/Apple GPUs or as a fallback). All three platforms (CUDA, OpenCL, HIP) are officially supported.
**Notes:** None.

### Claim: GROMACS is LGPL v2.1, mainly C++/C, checkpoint support via mdrun
**Source in reports:** Report 1 line 45.
**Status:** Verified
**Evidence:** https://gitlab.com/gromacs/gromacs confirms LGPLv2.1. Checkpoint support is confirmed by https://manual.gromacs.org/current/user-guide/managing-simulations.html: "When gmx mdrun is halted, it writes a checkpoint file that can restart the simulation exactly as if there was no interruption." Default behavior writes md.cpt every 15 minutes; resume with `gmx mdrun -cpi state`. Codebase is described as mainly C++/C.
**Notes:** None.

### Claim: Salmon is GPL v3, C++11
**Source in reports:** Report 1 line 46.
**Status:** Partially verified
**Evidence:** https://github.com/COMBINE-lab/salmon confirms GPL-3.0 license; codebase 97.9% C++. The specific "C++11" standard version isn't directly displayed in the GitHub overview but Salmon historically targets C++11/14.
**Notes:** GPL v3 confirmed; "C++11" specifically is a reasonable historical/build statement but not surfaced in the current GitHub landing page. Treat the C++11 claim as accurate but slightly under-verified by the GitHub overview alone.

### Claim: MONAI is Apache 2.0, Python/PyTorch
**Source in reports:** Report 1 line 47.
**Status:** Verified
**Evidence:** https://github.com/Project-MONAI/MONAI confirms Apache-2.0 license. Project is "a PyTorch-based, open-source framework for deep learning in healthcare imaging." Codebase 95.5% Python.
**Notes:** None.

### Claim: Meeko is a Forli lab tool that prepares PDBQT for Vina + AutoDock-GPU, exports SDF for ligand results and PDB for receptor results
**Source in reports:** Report 1 line 49 and table row.
**Status:** Verified
**Evidence:** https://github.com/forlilab/Meeko confirms Meeko is developed by the Forli lab at Scripps Research CCSB. Meeko's documentation (https://meeko.readthedocs.io/) states explicitly: "Meeko writes the input PDBQT files for AutoDock-Vina and AutoDock-GPU, and exports docking results in SDF format for ligands and in PDB format for receptor." The export command-line tool is `mk_export.py`, used as `mk_export.py vina_results.pdbqt -j my_receptor.json -s lig_docked.sdf -p rec_docked.pdb`.
**Notes:** None.

### Claim: GNINA paper finding — docking accuracy improves when pocket is explicitly defined; better Top1 redocking and cross-docking vs broader/whole-protein search
**Source in reports:** Report 2 line 39: "The gnina paper reports that docking accuracy improves when the binding pocket is explicitly defined, with better Top1 redocking and cross-docking performance than broader search modes."
**Status:** Verified
**Evidence:** McNutt et al., "GNINA 1.0: molecular docking with deep learning," Journal of Cheminformatics 13:43 (2021). https://link.springer.com/article/10.1186/s13321-021-00522-2 and https://pubmed.ncbi.nlm.nih.gov/34108002/. Quoted result: "GNINA, utilizing a CNN scoring function to rescore the output poses, outperforms AutoDock Vina scoring on redocking and cross-docking tasks when the binding pocket is defined (Top1 increases from 58% to 73% and from 27% to 37%, respectively) and when the whole protein defines the binding pocket (Top1 increases from 31% to 38% and from 12% to 16%, respectively)."
**Notes:** Two true findings:
  1. GNINA's CNN scoring beats Vina in BOTH pocket-defined and whole-protein modes.
  2. Both Vina and GNINA perform substantially better with explicit pockets than whole-protein search (e.g., GNINA Top1 redocking 73% pocket-defined vs 38% whole-protein).
The report's framing ("docking accuracy improves when the pocket is explicitly defined") is a fair characterization of finding #2 — supported by the absolute numbers in the paper. Report 2's framing is accurate and well grounded.

---

## Summary table

| Claim | Status |
|---|---|
| BOINC Central exists; Docker + AutoDock | Verified |
| docker_wrapper, vboxwrapper, native, BOINC wrapper, WSL | Verified |
| Hundreds of jobs/sec dispatch | Verified |
| Adaptive replication tracks (host, app version) | Verified |
| Code signing offline-machine recommendation | Verified |
| 1.9 GB VirtualBox cookbook example | Verified |
| Rosetta@home (active) | Verified |
| Docking@Home as "existing" | False — retired 2014 |
| WCG OpenPandemics (active) | Verified |
| GPUGRID (active, in transition) | Verified |
| AutoDock-GPU motivated by OpenPandemics | Verified |
| Vina Apache 2.0 | Verified |
| AutoDock-GPU GPL-2.0 + LGPL-2.1 | Verified |
| GNINA dual GPL/Apache + deps + Docker | Verified |
| P2Rank MIT + Java 17+ + PDB/mmCIF/BinaryCIF | Verified |
| fpocket MIT + C + Docker | Verified |
| OpenMM MIT + LGPL + CUDA/OpenCL/HIP | Verified |
| GROMACS LGPL v2.1 + C++/C + mdrun checkpoint | Verified |
| Salmon GPL v3 + C++ | Partially verified (C++ confirmed, "C++11" specifically not surfaced from landing page) |
| MONAI Apache 2.0 + PyTorch | Verified |
| Meeko (Forli, PDBQT/SDF/PDB) | Verified |
| GNINA paper: pocket-defined improves accuracy | Verified |
