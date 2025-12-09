# Quick Start Guide

This guide walks you through the minimal steps to install Psi-Continuum v2,
download required datasets, and run the full analysis pipeline.

## 1. Install the package

```bash
pip install psi-continuum-v2
```

## 2. Download datasets

```bash
psi-download-data
```

## 3. Run the full analysis pipeline

```bash
psi-run-all
```

All results will appear in `results/`.

## 4. Use the interactive CLI menu

```bash
psi-cli
```

---

## 📄 **docs/installation.md**

```markdown
# Installation

Psi-Continuum v2 requires:

- Python 3.10+
- NumPy ≥ 1.23
- SciPy ≥ 1.9
- Matplotlib ≥ 3.6

Install from PyPI:

```bash
pip install psi-continuum-v2
```

Or install from source:

```bash
git clone https://github.com/dmitrylife/psi-continuum-v2
cd psi-continuum-v2
pip install .
```

---

## 📄 **docs/cli.md**

```text
# Command Line Interface (CLI)
```

Psi-Continuum v2 installs several useful CLI tools.

## `psi-cli` – interactive menu

```bash
psi-cli
```

Functions:

- 1. Download datasets
- 2. Check datasets
- 3. Run full analysis pipeline
- 4. Open documentation
- 5. Show project paths

```bash
psi-download-data
```

---

```bash
psi-check-data
```

Validate that all datasets are present and usable.

```bash
psi-check-data
```

---

`psi-run-all`

Run the complete pipeline:

- model tests
- SN test
- H(z) test
- BAO tests
- joint likelihood
- ε₀ scan
- publication figures

---

## 📄 **docs/api.md**

```text
# Python API Reference
```

## Background models

```python
from psi_continuum_v2.cosmology.background.lcdm import E_LCDM, H_LCDM
from psi_continuum_v2.cosmology.background.psicdm import E_PsiCDM, H_PsiCDM
```

### Likelihoods

```python
from psi_continuum_v2.cosmology.likelihoods.sn_likelihood import chi2_sn_full_cov
from psi_continuum_v2.cosmology.likelihoods.hz_likelihood import chi2_hz
from psi_continuum_v2.cosmology.likelihoods.bao_likelihood import chi2_bao
from psi_continuum_v2.cosmology.likelihoods.joint_likelihood import build_joint_chi2
```

Data loaders

```python
from psi_continuum_v2.cosmology.data_loaders.pantheonplus_loader import load_pantheonplus_hf
```

More sections may be added as the API grows.

---

## 📄 **docs/data_format.md**

```text
# Data Format & Files
```

The pipeline uses four datasets:

### Pantheon+ SH0ES (SN Ia)
Files:
- `Pantheon+SH0ES.dat`
- `Pantheon+SH0ES_STAT+SYS.cov`

### H(z) Compilation
- `HZ_compilation.csv`

### SDSS DR12 BAO
- `sdss_DR12Consensus_bao.dat`
- `BAO_consensus_covtot_dM_Hz.txt`

### DESI DR2
- `desi_gaussian_bao_ALL_GCcomb_mean.txt`
- `desi_gaussian_bao_ALL_GCcomb_cov.txt`

All datasets are downloaded to:

`data/`
