---
layout: default
title: Quick Start
---

# Quick Start Guide

This guide walks you through the minimal steps required to install
**Psi-Continuum v2**, download the required datasets, and reproduce
all numerical results and figures reported in the associated publication.

⚠️ **Archived release**  
This guide corresponds to the **final archived software version v0.2.3**.
The workflow described below is frozen and will not change.

---

## 1. Install the package

Install the Psi-Continuum v2 package from PyPI:

```bash
pip install psi-continuum-v2
```

---

## 2. Download required datasets

Download all observational datasets used in the analysis:

```bash
psi-download-data
```

This command creates the local `data/` directory and downloads all the necessary files from the repository.

---

## 3. Quick data status check

Verify that all datasets are present and correctly located:

```bash
psi-check-data
```

The command reports missing or misnamed files with clear instructions.

---

## 4. Run the full analysis pipeline

Execute the complete reproducibility pipeline:

```bash
psi-run-all
```

This reproduces:

- background model validation
- Supernova Ia likelihood results
- H(z) cosmic-chronometer analysis
- BAO likelihoods (SDSS DR12 + DESI DR2)
- joint χ² analysis
- ε₀ parameter scan
- all publication figures

---

## 5. Optional: Interactive CLI menu

For guided exploration, you may also use the interactive menu:

```bash
psi-cli
```

This provides a user-friendly interface to the same workflow steps.

---

## Output

All generated results, figures, and tables are written to the local
`results/` directory.

These outputs correspond **exactly** to the numerical results and figures
reported in the Psi-Continuum v2 publication.
