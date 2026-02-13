---
layout: default
title: Clarifications
permalink: /clarifications/
---


# Technical Clarifications and Conventions

This page documents technical clarifications regarding definitions,
baseline conventions, and parameter choices used in the Psi–Continuum
framework (v2–v5).

These notes do not modify the published results.
They clarify normalization conventions and modeling scope.

---

## 1. Definition of the Dimensionless Expansion Rate

In v2 the dimensionless expansion rate is defined as

$$
E_{\Lambda\mathrm{CDM}}(z) \equiv \frac{H_{\Lambda\mathrm{CDM}}(z)}{H_0}
$$

This step is purely definitional.

It does **not** assume that H0 is measured in a model-independent way.
In the v2 analysis, H0 is treated as a normalization parameter of a
chosen reference ΛCDM background.

The role of this definition is to express the expansion history in a
dimensionless form relative to a fixed baseline.

---

## 2. Parameter Dependence of E_LCDM(z)

In general,

$$
E_{\Lambda\mathrm{CDM}}(z; \Omega_{m0}, \Omega_\Lambda, \Omega_k) = \sqrt{\Omega_{m0} (1+z)^3 + \Omega_\Lambda + \Omega_k (1+z)^2}
$$

depends on cosmological parameters.

In v2 the analysis is explicitly restricted to spatially-flat ΛCDM:

$$
E_{\Lambda\mathrm{CDM}}(z) = \sqrt{\Omega_{m0} (1+z)^3 + (1 - \Omega_{m0})}
$$

The reference background adopts a fixed parameter pair:

$$
(H_0, \Omega_{m0}) = (70 \, \mathrm{km\, s^{-1} Mpc^{-1}}, 0.3)
$$

This choice is intentional.

The goal of v2 is not to perform a full multi-parameter cosmological
inference, but to test the sensitivity of late-time background datasets
to a single phenomenological deformation parameter ε0 around a fixed,
transparent baseline.

A natural extension would treat (H0, Ω_m0, r_d) as nuisance parameters
and marginalize over their uncertainties.
This is not implemented in v2 in order to isolate deformation effects
clearly and reproducibly.

---

## 3. Nature of the Reference Background

The ΛCDM background used in v2–v5 functions as a **reference
normalization**, not as a claim of parameter optimality.

All comparisons are performed relative to the same baseline.
The deformation parameter ε0 measures structured deviations around
this chosen reference.

Changing the baseline shifts the normalization but does not alter
the diagnostic logic of the framework.

---

## 4. Scope of the Framework

The Psi–Continuum framework:

- operates strictly at the homogeneous background level,
- introduces no new dynamical degrees of freedom,
- does not modify gravitational field equations,
- does not introduce new force carriers or interaction channels.

It provides a macroscopic, response-based organizational language
for late-time expansion data.

All quantitative tests remain confined to the archived and reproducible
software releases associated with each version.

---

If further clarification is required, readers are encouraged to consult:

- Psi–Continuum Cosmology v2 (Zenodo archive)
- Psi–Continuum Cosmology v5 (state–space formulation)
- The associated open-source software repositories

