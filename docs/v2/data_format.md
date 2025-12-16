---
layout: default
title: Data Format
---

# Data Format & Files

This page describes the observational datasets and file structure required
by the **Psi-Continuum v2** analysis pipeline.

⚠️ **Archived release**  
The data format described here corresponds to the **final archived software
version v0.2.3** and is frozen.

---

## Overview

The pipeline uses four observational datasets:

- Type Ia supernovae (Pantheon+ SH0ES)
- Cosmic-chronometer H(z) measurements
- SDSS DR12 BAO consensus data
- DESI DR2 BAO Gaussian likelihoods

All datasets are required to reproduce the results of the Psi-Continuum v2
publication.

---

## Pantheon+ SH0ES (Supernovae Ia)

Files:

- `Pantheon+SH0ES.dat`
- `Pantheon+SH0ES_STAT+SYS.cov`

These files contain the Pantheon+ High-Fidelity supernova sample and the full
statistical + systematic covariance matrix.

---

## H(z) Compilation (Cosmic Chronometers)

File:

- `HZ_compilation.csv`

This file contains a compilation of 32 H(z) measurements from cosmic
chronometers and related methods.

Source reference:
<https://arxiv.org/pdf/2301.09591>

---

## SDSS DR12 BAO Consensus

Files:

- `sdss_DR12Consensus_bao.dat`
- `BAO_consensus_covtot_dM_Hz.txt`

These files contain the SDSS BOSS DR12 consensus BAO measurements and their
covariance matrix.

---

## DESI DR2 BAO (Gaussian Likelihood)

Files:

- `desi_gaussian_bao_ALL_GCcomb_mean.txt`
- `desi_gaussian_bao_ALL_GCcomb_cov.txt`

These files define the Gaussian BAO likelihood for DESI DR2 used in the
late-time analysis.

---

## Required Directory Structure

All datasets must be placed **exactly** in the following directory structure:

```text
data/
├── bao
│   ├── BAO_consensus_covtot_dM_Hz.txt
│   └── sdss_DR12Consensus_bao.dat
├── desi
│   └── dr2
│       ├── desi_gaussian_bao_ALL_GCcomb_cov.txt
│       └── desi_gaussian_bao_ALL_GCcomb_mean.txt
├── hz
│   └── HZ_compilation.csv
└── pantheon_plus
    ├── Pantheon+SH0ES.dat
    └── Pantheon+SH0ES_STAT+SYS.cov
```

    ## ⚠️ Important

    - File names and directory paths are case-sensitive.
    - The pipeline assumes this exact structure.
    - Renaming files or moving them will result in errors.

---

## Dataset Download

The recommended way to obtain all datasets is via the built-in downloader:

```bash
psi-download-data
```

This command automatically creates the directory structure shown above and
downloads all required files from their official public sources.

---

## Validation

After placing or downloading the datasets, verify their integrity using:

```bash
psi-check-data
```

This command reports missing or incorrectly placed files and provides
clear instructions for correction.

---

## Notes

- Observational datasets are **not included** in the PyPI package.
- The data format is frozen for long-term reproducibility.
- No additional datasets or alternative formats are supported in Psi-Continuum v2.
