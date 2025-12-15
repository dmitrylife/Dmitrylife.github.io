---
layout: default
title: Command Line Interface
---

# Command Line Interface (CLI)

Psi-Continuum v2 provides a small set of command-line tools designed for
**reproducible execution** of the full late-time cosmology analysis pipeline.

⚠️ **Archived interface**  
This CLI corresponds to the **final archived release v0.2.3** and is frozen.
No additional options or extensions are planned for Psi-Continuum v2.

---

## Interactive Menu

The primary user entry point is the interactive menu:

```bash
psi-cli
```

This launches a guided interface with the following options:

> 1. "Download datasets"
> 2. "Check datasets"
> 3. "Run full analysis pipeline"
> 4. "Open documentation"
> 5. "Show project paths"

The interactive menu is the recommended starting point for new users.

---

## Built-in Commands

For automated or scripted usage, individual commands are also available.

### Download datasets

```bash
psi-download-data
```

Downloads all required observational datasets into the local `data/` directory.

---

### Check datasets

```bash
psi-check-data
```

Verifies that all required files are present and correctly located.
Reports missing or misnamed files with clear instructions.

---

### Run full analysis pipeline

```bash
psi-run-all
```

- Executes the complete reproducibility pipeline, including:
- background model validation
- Supernova Ia likelihood
- Cosmic-chronometer H(z) likelihood
- BAO likelihoods (SDSS DR12 + DESI DR2)
- joint χ² construction
- ε₀ parameter scan
- generation of all publication figures

---

## Reproducibility Guarantee

All CLI commands reproduce **exactly** the numerical results and figures
reported in the Psi-Continuum v2 publication.

    No additional tuning, parameters, or configuration files are required.

The CLI is intentionally minimal to ensure transparent and repeatable execution.

---

## Notes

- The CLI operates at the background-expansion level only.
- No perturbation or early-Universe modules are included.
- The interface is frozen for long-term archival reproducibility.
