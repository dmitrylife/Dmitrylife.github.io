---
layout: default
title: Psi–Continuum State-Space Diagnostics (v5)
---

{% include audit-01-notice.html %}


> ⚠️ **Status Notice**

> Psi–Continuum Cosmology v5 represents the archived background-level
> formulation of the macroscopic state–space framework.

> The results and diagnostics presented in v5 remain fully reproducible
> and internally consistent within the adopted fixed reference background.

> Version v5 does not include nuisance-parameter marginalization
> or extended statistical inference procedures. Its purpose is strictly diagnostic:
> to organize late-time expansion data within a macroscopic state–space
> description relative to a chosen ΛCDM baseline.

> Subsequent developments will address extended statistical treatments
> and broader parameter handling as standalone methodological studies.

# Psi–Continuum State-Space Diagnostics (v5)

A lightweight, reproducible diagnostic package for macroscopic state–space analysis of late–time cosmic expansion.

### 📦 Software package

- **PyPI:** [psi-continuum-statespace](https://pypi.org/project/psi-continuum-statespace/)
- **Source code:** [github.com/dmitrylife/psi-continuum-statespace](https://github.com/dmitrylife/psi-continuum-statespace)

### 📄 Scientific reference

This page documents the diagnostic software companion to the article:

**Psi–Continuum Cosmology v5**  
*A Macroscopic State–Space Response Framework for Late–Time Cosmic Expansion*

- **Preprint (Zenodo DOI):**  
  [https://doi.org/10.5281/zenodo.18088720](https://doi.org/10.5281/zenodo.18088720)
  
---

## Purpose

The `psi-continuum-statespace` package provides a purely diagnostic, background–level implementation of the macroscopic state–space framework introduced in *Psi–Continuum Cosmology v5*.

Install directly from PyPI:

```bash
pip install psi-continuum-statespace
```

Example usage (interactive shell):

```bash
psi-statespace interactive
```

The software is designed to:

- construct the macroscopic state–space coordinate **Ψ(z)**,
- visualize state–space trajectories derived from background expansion histories,
- assess the internal consistency of independent late–time observational datasets.

The package **does not introduce new cosmological models**, does not modify
gravitational dynamics, and does not perform parameter estimation.

---

## Conceptual scope

The state–space framework implemented here is:

- **macroscopic** — formulated at the background level,
- **diagnostic** — descriptive rather than predictive,
- **model–independent** — defined via ratios of expansion histories,
- **reproducible** — fully determined by frozen background APIs.

Within this formulation:

- ΛCDM appears as the **instantaneous–response limit** in state space,
- late–time acceleration corresponds to **small, smooth deformations**
  organized as trajectories in Ψ(z).

---

### Clarifications

> **Technical clarifications:**  
> Additional explanations regarding reference background,
> parameter fixing, and normalization conventions are available  
> [here](/clarifications/).

---

## Relation to Psi–Continuum v2

This package relies on the **frozen background–level API** of
**Psi–Continuum Cosmology v2** for computing reference expansion histories.

No modifications to the v2 implementation are introduced.

The v5 framework should be understood as a **macroscopic reinterpretation**
of late–time background information, not as an extension of the underlying
cosmological model.

---

## Reproducibility

All figures and diagnostics presented in the v5 article are reproducible
using the public release of this package.

The figures included in the publication are provided separately in the
`publication/` directory of the repository for reference.

---

## Intended audience

This software is intended for:

- researchers in observational and phenomenological cosmology,
- readers of *Psi–Continuum Cosmology v5*,
- users interested in alternative **organizational languages** for late–time
  expansion data.

It is **not** intended as a general–purpose cosmological analysis pipeline.

---

## Citation

If you use this diagnostic framework or reproduce results from the article,
please cite:

> Dmitry V. Klimov (2025).  
> *Psi–Continuum Cosmology v5:  
> A Macroscopic State–Space Response Framework for Late–Time Cosmic Expansion*.  
> Zenodo. https://doi.org/10.5281/zenodo.18088720

