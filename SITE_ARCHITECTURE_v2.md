# Psi-Continuum — Site Architecture v2

**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-10

---

## 1. Purpose

`psi-continuum.org` is a scientific and educational platform for studying modern cosmology, documenting active research, and exposing the traceable structure of scientific results.

The website is not designed as a promotional site for a single theory.

Its long-term structure consists of three primary layers:

**Learn ↔ Research ↔ SCITRACE**

- **Learn** explains established cosmology and scientific methods.
- **Research** contains active and archived scientific investigations.
- **SCITRACE** exposes how scientific results are connected to equations, data, code, validation, inference, and robustness tests.

Supporting sections provide notes, project information, and archival material.

---

## 2. Core Architectural Principles

### 2.1 Structure before implementation

The information architecture is defined before pages, components, or interactive functionality are implemented.

Technology must follow the scientific structure rather than determine it.

### 2.2 Separation of responsibilities

Educational material, active research, and research traceability must remain conceptually distinct.

A page should have one primary scientific responsibility.

### 2.3 Stable semantic URLs

Public URLs should describe the meaning of content rather than its current technical implementation.

Preferred examples:

```text
/learn/expansion/hubble-function/
/learn/observations/bao/
/research/psi-late-01/
/research/archive/v2/
/scitrace/master/
```

URLs should remain stable whenever possible.

### 2.4 Content independent of presentation

Scientific and educational content should be stored primarily as structured Markdown and metadata.

Layouts, navigation, styling, and interactive interfaces should be separated from scientific content.

This allows the presentation layer to evolve without rewriting the scientific record.

### 2.5 Historical integrity

Published or frozen scientific records must not be silently rewritten.

Corrections, audits, reinterpretations, and later developments should be linked to the original record rather than replacing it.

### 2.6 Research does not exist to validate Psi-Continuum

The educational and research architecture must allow the data to support, constrain, or reject any proposed interpretation.

A null result is a valid scientific result.

---

## 3. Top-Level Information Architecture

```text
psi-continuum.org
│
├── Home
├── Learn
│   ├── Foundations
│   ├── Expansion
│   ├── Geometry and GR
│   ├── ΛCDM
│   ├── Observations
│   ├── Statistics and Inference
│   └── From Data to Research
├── Research
│   ├── Active Research
│   │   └── PSI-LATE-01
│   └── Archive
│       ├── v2
│       ├── v2 Audit
│       ├── v3
│       ├── v4
│       └── v5
├── SCITRACE
│   ├── About
│   ├── Specification
│   └── Master
├── Notes
└── About
```

This is a logical architecture. The physical repository structure may differ when technically justified.

---

## 4. Learn

### 4.1 Purpose

`Learn` is the educational layer of Psi-Continuum.

Its purpose is to teach the foundations required to understand modern observational cosmology and eventually follow a real cosmological analysis.

It must not function as an introduction whose purpose is to convince the reader of the Psi-Continuum framework. Standard cosmology comes first.

### 4.2 Learning path

```text
What is cosmology?
        ↓
Observing the Universe
        ↓
Redshift
        ↓
Scale factor a(t)
        ↓
Expansion rate H(t) and H(z)
        ↓
FLRW geometry
        ↓
Friedmann equations
        ↓
ΛCDM
        ↓
Cosmological distances
        ↓
SN Ia / BAO / H(z) / CMB
        ↓
Uncertainties and covariance
        ↓
χ² and likelihood
        ↓
Parameter inference
        ↓
Model comparison
        ↓
Robustness
        ↓
Real research
```

The exact curriculum may evolve, but prerequisite relationships must remain explicit.

### 4.3 Educational principle

> Do not merely tell the reader what we know. Show how we know it.

The material should explain how observations, assumptions, mathematics, and inference lead to conclusions.

### 4.4 Standard learning-page structure

```text
Title
Purpose
Prerequisites
What is observed?
Physical idea
Mathematical formulation
Meaning of quantities
Worked or conceptual example
Common misconceptions
Connection to observations
Connection to research
Further reading
Next topic
```

---

## 5. Research

`Research` contains actual scientific investigations. Educational explanation and scientific claims must not be confused.

Each research program should have a stable research identifier.

### 5.1 Active research

**PSI-LATE-01 — A Traceable Reconstruction of Late-Time Cosmic Expansion**

```text
Data provenance
      ↓
ΛCDM baseline validation
      ↓
Reconstruction
      ↓
Inference
      ↓
Robustness
      ↓
Physical interpretation
```

Guiding principle:

> Detect Ψ(z) first; interpret Ψ(z) only after robustness.

### 5.2 Research identifiers

```yaml
research_id: PSI-LATE-01
title: A Traceable Reconstruction of Late-Time Cosmic Expansion
status: active
```

Research identifiers should remain stable even if titles change.

### 5.3 New results

A new scientific result does not automatically require a new top-level page. Results belong to a research program and should be represented through that program and, where appropriate, through SCITRACE.

---

## 6. Research Archive

The archive preserves the historical development of the project. Archived material is part of the scientific record and should not be presented as current research.

```text
/research/archive/v2/
/research/archive/v2-audit/
/research/archive/v3/
/research/archive/v4/
/research/archive/v5/
```

Historical records may link to preprints, frozen documentation, repositories, software releases, datasets, audits, and later corrections or reinterpretations.

The original record remains identifiable.

---

## 7. SCITRACE

SCITRACE is the traceability layer of the platform.

```text
Question
   ↓
Hypothesis
   ↓
Equation
   ↓
Data + provenance
   ↓
Validation
   ↓
Transformation / Model
   ↓
Observable
   ↓
Likelihood
   ↓
Inference
   ↓
Robustness
   ↓
Result
```

Traceability should also work in reverse:

```text
Result
   ↓
Inference
   ↓
Likelihood
   ↓
Observable
   ↓
Code
   ↓
Data
   ↓
Equation
```

### 7.1 SCITRACE principles

- No result without a trace.
- Specification before implementation.
- Data are part of the scientific argument.
- Every transformation is explicit.
- Code and mathematics must correspond.
- Validation precedes inference.
- No interpretation before robustness.
- Negative results are results.
- Scientific records are immutable.
- Human-readable and machine-readable.
- Maximum transparency. Minimum prose.

### 7.2 Relationship with the website

SCITRACE must not initially dictate the technology of the entire website. The first implementation may consist of structured metadata and generated human-readable pages.

Interactive graph interfaces may be added later without changing the scientific content model.

---

## 8. Notes

`Notes` contains exploratory conceptual material, including physical analogies, mathematical observations, possible interpretations, unresolved questions, and speculative connections.

A note is not automatically a scientific result.

Notes should clearly distinguish:

```text
established result
inference
working hypothesis
speculation
open question
```

Where a note becomes part of a formal research program, the corresponding research or SCITRACE object should be created explicitly.

---

## 9. About

`About` explains the purpose of Psi-Continuum, authorship, research philosophy, project history, open-science principles, contact information, repositories, and persistent identifiers.

It should not duplicate the scientific content of `Research` or educational content of `Learn`.

---

## 10. Content Types

```text
landing
learning_page
research_project
archive_record
scitrace_document
note
about
```

Additional types should be introduced only when a genuine structural need appears.

---

## 11. Page Metadata

Example learning page:

```yaml
---
title: The Hubble Function
type: learning_page
section: learn
status: published
order: 4

prerequisites:
  - redshift
  - scale-factor

related:
  - cosmological-distances

research:
  - PSI-LATE-01

scitrace:
  - MODEL-H-01
---
```

Example research page:

```yaml
---
title: A Traceable Reconstruction of Late-Time Cosmic Expansion
type: research_project
research_id: PSI-LATE-01
status: active
---
```

Metadata schemas will be specified separately before large-scale implementation.

---

## 12. Content Relationships

Possible relationships include:

```text
requires
next
previous
related
explains
used_in
research
scitrace
supersedes
audited_by
```

Example:

```text
Learn: BAO
    │
    ├── requires → Cosmological Distances
    ├── requires → Redshift
    ├── used_in → PSI-LATE-01
    └── scitrace → DATA-BAO-01
                    LIKE-BAO-01
```

This relationship model may later support automatic navigation and knowledge graphs.

---

## 13. URL Policy

Public URLs should be semantic, lowercase, stable, independent of file extensions, and independent of implementation technology.

Preferred:

```text
/learn/expansion/hubble-function/
```

Avoid:

```text
/page17.html
/new-hubble-page-final/
/v3-new-doc2/
```

Published URLs should not be changed without a strong reason. When a URL must change, a redirect should be provided where technically possible.

---

## 14. Repository Principles

The repository should gradually move toward a structure similar to:

```text
/
├── _layouts/
├── _includes/
├── assets/
├── learn/
├── research/
├── scitrace/
├── notes/
├── data/
└── architecture/
```

This is a target structure, not an instruction to move existing files immediately.

Existing stable pages should be migrated only after the content model and routing strategy are validated.

---

## 15. Technology Policy

The scientific architecture must remain independent of the website framework.

The current static-site approach may remain in use while it satisfies project requirements.

A more complex backend or frontend should be introduced only when required by functionality such as interactive SCITRACE graphs, advanced search, dynamic data exploration, user-specific functionality, or computational notebooks and services.

Technology must solve an identified problem.

**Complexity is not itself progress.**

---

## 16. Source of Truth

**GitHub = scientific source of truth**

**SCITRACE = specification + traceability + validation**

**psi-continuum.org = human interface**

The public website presents the scientific record but does not replace the version-controlled source.

---

## 17. Expansion Rules

### New educational topic
Add it to the appropriate `Learn` path and declare its prerequisites and relationships.

### New research program
Assign a stable research ID and place it under `Research`.

### New dataset
Do not create a top-level website section merely because a dataset was added. Connect it to the relevant research program and SCITRACE record.

### New scientific result
Attach it to the research program and its trace.

### New interpretation
Do not silently rewrite earlier results. Create a new interpretation, note, research object, or version as appropriate.

### Superseded work
Move its public role to the archive while preserving the original record.

---

## 18. Migration Principle

The current website will not be reorganized all at once.

```text
Architecture
      ↓
Content model
      ↓
Metadata schema
      ↓
Layouts
      ↓
Navigation
      ↓
Learn foundation
      ↓
Research structure
      ↓
SCITRACE integration
      ↓
Migration of legacy content
```

At each stage the public website should remain functional.

---

## 19. Educational and Scientific Integrity

The educational layer must clearly distinguish:

- established cosmological knowledge;
- conventional assumptions;
- observational evidence;
- model-dependent inference;
- open scientific problems;
- Psi-Continuum-specific research;
- speculative interpretation.

Psi-Continuum-specific concepts must not be presented as established cosmological facts.

This distinction is a permanent architectural requirement.

---

## 20. Long-Term Goal

The long-term goal is a website on which a reader can:

1. learn the foundations of cosmology;
2. understand how cosmological observations are obtained;
3. understand how models are confronted with data;
4. follow a real research program;
5. inspect the provenance of a scientific result;
6. trace that result back to equations, data, code, and validation;
7. distinguish established knowledge from active research and speculation.

The desired reader journey is:

```text
Learn
  ↓
Understand
  ↓
Inspect real data
  ↓
Follow research
  ↓
Trace a result
  ↓
Evaluate the scientific argument
```

The platform should therefore teach not only cosmology, but also how cosmological knowledge is constructed.

---

## 21. Current Status

This document defines the first architectural direction for the next generation of `psi-continuum.org`.

It does not authorize immediate restructuring of existing public URLs or historical records.

The next design task is:

**Content Model and Metadata Specification v0.1**

Only after that specification is reviewed should implementation of the new site structure begin.
