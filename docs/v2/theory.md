---
layout: default
title: Theory Overview
---

# Theory Overview

## Psi-Continuum v2

Psi-Continuum v2 (ΨCDM) is a minimal one-parameter phenomenological extension of
the standard ΛCDM cosmological model at the **background expansion level**.

It introduces a single smooth late-time deformation of the Hubble expansion,
governed by the dimensionless parameter **ε₀**, while preserving all
early-Universe physics and standard perturbation dynamics.

---

## Background Expansion

The modified Hubble expansion rate is defined as:

```text
H_Ψ(z) = H_Λ(z) · (1 + ε₀ / (1 + z))
```


A visual comparison between ΛCDM and ΨCDM is shown below:

<p align="center"> <img src="https://psi-continuum.org/docs/v2/pic/hubble_function.png" alt="Psi-Continuum Hubble function"> </p>

This parametrisation:

- reduces exactly to ΛCDM when **ε₀ = 0**,
- produces percent-level deviations only at low redshift,
- suppresses all deviations as z → ∞,
- leaves early-Universe observables (CMB, primordial BAO) unchanged.

---

## Scope of the Model

Psi-Continuum v2 is intentionally restricted to the **late-time background expansion**.

It does **not** introduce:

- modifications of gravity,
- additional dynamical fields,
- changes to perturbation equations,
- or alterations of early-Universe physics.

---

## Included Functionality

This package provides a fully reproducible late-time cosmology pipeline,
including:

- ΛCDM and ΨCDM background expansion models
- Distance measures:
  H(z), E(z), d_L(z), D_M/r_d, D_H/r_d, D_V/r_d
- Pantheon+ High-Fidelity SNe Ia likelihood (full covariance)
- 32 cosmic-chronometer H(z) measurements
- SDSS DR12 and DESI DR2 Gaussian BAO likelihoods
- Full joint χ² framework (SN + CC + BAO)
- ε₀ scans, Δχ² profiling, and ΛCDM comparison
- Publication-grade figure generator
- Command-line interface (**psi-cli**) for running the complete pipeline

All numerical results reported in the accompanying paper are fully reproducible
using this software.

---

## Associated Publications

- Psi-Continuum v2 preprint
  https://doi.org/10.5281/zenodo.17879744

- Psi-Continuum v2 software archive
  https://doi.org/10.5281/zenodo.17928837

---

## Project Status

Psi-Continuum v2 is a final archived research release.

The code and documentation are frozen for long-term reproducibility and citation.
Further theoretical developments will be released separately as
**Psi-Continuum v3**.
