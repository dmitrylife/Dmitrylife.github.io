---
layout: default
title: Python API
---

# Python API Reference

This page documents the **public Python API** of the Psi-Continuum v2 package.
The API provides low-level access to background cosmological models,
data loaders, and χ² likelihood functions used internally by the analysis pipeline.

⚠️ **API status:**  
This API corresponds to the **final archived release v0.2.3** and is frozen.
No further extensions or changes are planned for Psi-Continuum v2.

---

## Background Expansion Models

The package provides background-level ΛCDM and ΨCDM expansion functions.

```python
from psi_continuum_v2.cosmology.background.lcdm import E_lcdm, H_lcdm
from psi_continuum_v2.cosmology.background.psicdm import E_psicdm, H_psicdm
```

These functions compute:

- the dimensionless expansion rate E(z)
- the Hubble function H(z)

for ΛCDM and ΨCDM background cosmologies.

---

## Likelihood Functions

Low-level χ² likelihoods are exposed for direct use and testing.

```python
from psi_continuum_v2.cosmology.likelihoods.sn_likelihood import chi2_sn_full_cov
from psi_continuum_v2.cosmology.likelihoods.hz_likelihood import chi2_hz
from psi_continuum_v2.cosmology.likelihoods.bao_likelihood import chi2_bao
from psi_continuum_v2.cosmology.likelihoods.joint_likelihood import build_joint_chi2
```

These functions implement:

- Supernova Ia χ² with full covariance
- Cosmic-chronometer H(z) χ²
- BAO χ² likelihoods
- Construction of a full joint χ² (SN + CC + BAO)

They are primarily intended for reproducibility and validation purposes.

---

## Data Loaders

Dataset loader utilities are provided to read and validate observational data.

```python
from psi_continuum_v2.cosmology.data_loaders.pantheonplus_loader import load_pantheonplus_hf
```

Loaders return structured NumPy arrays and covariance matrices
used internally by the likelihood pipeline.

---

## Recommended Usage

For most users, **direct interaction with the Python API is not required**.

The recommended entry point is the command-line interface:

```bash
psi-cli
```

which ensures consistent data handling, validation, and reproducible execution
of the full analysis pipeline.

---

## Notes

The API is intentionally minimal and background-only.

- No perturbation, gravity modification, or early-Universe modules are included.
- Function signatures and behavior are frozen for long-term reproducibility.
- The API is provided without stability guarantees beyond this archived release.
