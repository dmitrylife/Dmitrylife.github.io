---
layout: default
title: Overview
---

# Theory Overview

## Psi-Continuum v2 is a minimal one-parameter phenomenological extension of the ΛCDM cosmological model.

It introduces a single smooth late-time deformation of the background expansion, governed by the dimensionless parameter **ε₀**, while preserving all early-Universe physics.

The modified Hubble expansion is:

<p align="center">
  <img src="https://psi-continuum.org/docs/v2/pic/hubble_function.png" alt="Psi-Continuum Hubble function">
</p>

```mathematica
H_{\Psi}(z) = H_{\Lambda}(z)\left(1 + \frac{\varepsilon_{0}}{1+z}\right)
```

which reduces exactly to ΛCDM at **ε₀ = 0** and produces percent-level deviations only at low redshift.

This package includes:

- ΛCDM and ΨCDM background cosmology  
- Distance measures: *H(z), E(z), d_L(z), D_M/r_d, D_H/r_d, D_V/r_d*  
- Pantheon+ HF SNe Ia likelihood (full covariance)  
- 32 cosmic-chronometer H(z) measurements  
- SDSS DR12 and DESI DR2 BAO Gaussian likelihoods  
- Full joint χ² framework (SN + CC + BAO)  
- ε₀ scans, Δχ² profiling, and ΛCDM comparison  
- Publication-grade figure generator  
- Command-line interface (**psi-cli**) for running the entire analysis pipeline  

All results in the accompanying paper are fully reproducible using this package.

Zenodo: <https://doi.org/10.5281/zenodo.17879744>
