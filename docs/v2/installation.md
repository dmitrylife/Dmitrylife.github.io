---
layout: default
title: Installation
---

# Installation

This page describes how to install the **Psi-Continuum v2** software package.

⚠️ **Archived release**  
These instructions correspond to the **final archived software version v0.2.3**.
The installation procedure is frozen and will not change.

---

## Requirements

Psi-Continuum v2 requires:

- **Python ≥ 3.10**
- **NumPy ≥ 1.23**
- **SciPy ≥ 1.9**
- **Matplotlib ≥ 3.6**

The package is platform-independent and runs on Linux, macOS, and Windows.

---

## Installation from PyPI (recommended)

Install the package directly from PyPI:

```bash
pip install psi-continuum-v2
```

Note:

    - The PyPI package contains **code only**.
    - Observational datasets are **not included**.
    - Generated results (`results/`) are **not included**.

All required datasets must be downloaded separately using the built-in tools
(see the Quick Start section).

---

## Installation from Source (optional)

For reproducibility checks or inspection of the source code, you may install
directly from the GitHub repository.

```bash
git clone https://github.com/dmitrylife/psi-continuum-v2
cd psi-continuum-v2
pip install .
```

This installs the same frozen version of the package as distributed via PyPI.

---

## Next Steps

After installation

10. Download the required datasets:

```bash
psi-download-data
```

20. Verify dataset integrity:

```bash
psi-check-data
```

30. Run the full analysis pipeline:

```bash
psi-run-all
```

See the **Quick Start Guide** for a complete reproducible workflow.
