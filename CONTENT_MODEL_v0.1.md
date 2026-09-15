# Psi-Continuum Website — Content Model v0.1

**Status:** Draft  
**Version:** 0.1  
**Scope:** `learning_page` only

This document begins the content-model specification for the educational layer of the Psi-Continuum website. Other content types will be specified incrementally.

---

## 1. Core Principle

> **A learning page is designed around the result of learning, not around the amount of material presented.**

The purpose of a `learning_page` is not merely to expose the reader to information. It should help the reader move through four stages:

```text
recognize → understand → explain → apply
```

A page is therefore a guided learning route with explicit learning objectives and checks of understanding.

---

## 2. Educational Role

A `learning_page` explains one coherent topic or a tightly connected set of concepts.

It should:

- begin from motivation and intuition;
- introduce formal definitions only after the physical idea is clear;
- develop mathematics step by step;
- explain the meaning of every important symbol and quantity;
- connect the topic to observations or real scientific use where appropriate;
- identify common misconceptions;
- explicitly connect prerequisite knowledge to the current topic;
- test conceptual understanding and application, not only recall;
- provide targeted remediation when a key concept is not understood;
- identify the next useful topic;
- provide traceable sources and further reading.

The educational layer must teach standard cosmology on its own terms. It must not be structured as an argument intended to convince the reader of Psi-Continuum.

---

## 3. Standard Learning Route

The default structure of a `learning_page` is:

```text
1. Why does this matter?
        ↓
2. What are we trying to understand?
        ↓
3. Explanation without mathematics
        ↓
4. Intuitive example / analogy
        ↓
5. Precise physical definition
        ↓
6. Mathematics step by step
        ↓
7. Meaning of symbols and quantities
        ↓
8. Worked example / observational connection
        ↓
9. Common misunderstanding
        ↓
10. Connection to prerequisite knowledge
        ↓
11. Checkpoint
        ↓
12. Diagnosis of misunderstood concepts
        ↓
13. Targeted re-explanation
        ↓
14. Final assessment
        ↓
15. What to study next
        ↓
16. Sources and further reading
```

Not every page must use identical visible headings, but the underlying pedagogical responsibilities should remain present when relevant.

---

## 4. Layered Explanation

Difficult concepts should be explainable at several levels rather than only once.

Recommended layers:

1. **Intuitive layer** — what the concept means in ordinary language.
2. **Physical layer** — the precise physical meaning.
3. **Mathematical layer** — equations and derivation, developed step by step.
4. **Applied layer** — how the concept is used with observations, models, or calculations.

An analogy is a teaching aid, not a substitute for the physical definition. The page should make clear where an analogy stops being exact.

---

## 5. Learning Objectives

Every `learning_page` must define explicit `learning_objectives`.

Objectives should describe what the reader should be able to **do** after completing the page.

Example for a future page on the Hubble function:

```yaml
learning_objectives:
  - explain_what_H_means
  - distinguish_H0_from_Hz
  - interpret_H_at_given_redshift
  - connect_H_to_expansion_history
```

Avoid objectives that merely describe exposure, such as `read_about_H` or `know_the_formula`.

Preferred verbs include:

- explain;
- distinguish;
- interpret;
- calculate;
- connect;
- apply;
- identify;
- justify.

---

## 6. Assessment Principle

Assessment must test understanding rather than simple memory of the page.

A weak question asks the reader to recall notation or repeat a sentence.

A stronger question asks the reader to interpret a situation, distinguish related concepts, use an equation, identify a misconception, or transfer the idea to a new example.

The assessment model is:

```text
explanation
    ↓
understanding
    ↓
checkpoint
    ↓
diagnose misconception
    ↓
targeted re-explanation
    ↓
retry
    ↓
final assessment
```

---

## 7. Objective Coverage

A numerical score alone is not sufficient evidence of understanding.

Each essential `learning_objective` must be assessed at least once.

A reader should not be treated as having mastered a page merely because the total score is high while a foundational objective remains misunderstood.

The system should therefore track assessment coverage by objective as well as an overall score.

Example:

```yaml
assessment:
  checkpoint: true
  final_quiz: true
  pass_score: 80
  require_objective_coverage: true
  retry: targeted
```

`pass_score` is a useful summary threshold, but it does not override failure on an essential learning objective.

---

## 8. Targeted Retry

When a reader fails a question, the preferred response is not to repeat the whole page.

The failed question should be associated with one or more `learning_objectives`. The system can then:

1. identify the concept that was not understood;
2. show a shorter alternative explanation;
3. provide another example if useful;
4. ask a new question testing the same objective.

This creates a remediation loop:

```text
misunderstanding → diagnosis → re-explanation → new attempt
```

The retry question should test the same concept without simply repeating the original wording.

---

## 9. Proposed Metadata

Initial metadata for a learning page:

```yaml
---
id: hubble-function
title: The Hubble Function H(z)
type: learning_page
section: learn
status: draft
level: foundation
order: 4

prerequisites:
  - redshift
  - scale-factor

learning_objectives:
  - explain_what_H_means
  - distinguish_H0_from_Hz
  - interpret_H_at_given_redshift
  - connect_H_to_expansion_history

related:
  - cosmological-distances

research:
  - PSI-LATE-01

scitrace:
  - MODEL-H-01

assessment:
  checkpoint: true
  final_quiz: true
  pass_score: 80
  require_objective_coverage: true
  retry: targeted
---
```

This schema is provisional. Implementation details should not be frozen until it has been tested on real learning pages.

---

## 10. Sources and Literature

Every substantial learning page should provide sources and further reading.

References should be organized by purpose rather than presented as an undifferentiated bibliography.

Proposed structure:

```yaml
references:
  essential:
    - ...
  textbook:
    - ...
  primary:
    - ...
  further_reading:
    - ...
```

### Essential

A small number of sources most useful for understanding the page.

### Textbook

Established textbook treatments that provide systematic background and derivations.

### Primary

Primary scientific papers, official data releases, collaboration papers, standards, or other first-party scientific sources supporting specific claims.

### Further reading

Material for readers who want a deeper treatment beyond the learning objectives of the page.

Important factual claims — especially observational values, dataset descriptions, historical claims, and model-dependent statements — should be traceable to appropriate sources near the relevant discussion when practical. A long bibliography at the end is not a substitute for claim-level traceability where it matters.

---

## 11. Scientific Integrity

A learning page should clearly distinguish among:

- established knowledge;
- definitions and mathematical identities;
- model assumptions;
- observational evidence;
- model-dependent inference;
- open questions;
- Psi-Continuum-specific research;
- speculation.

The educational layer must not present a hypothesis as established knowledge or hide important assumptions for the sake of simplicity.

Simplification is allowed; distortion is not.

---

## 12. Relationship to Research and SCITRACE

A learning page may point forward into active research, but educational content and research claims remain separate responsibilities.

Conceptually:

```text
Learn
  │ explains the concept
  ↓
Research
  │ uses the concept in a scientific investigation
  ↓
SCITRACE
    records equations, data, implementation, validation and results
```

This allows a student to move from understanding a concept to seeing how it is actually used in a traceable research workflow.

---

## 13. Initial Acceptance Criteria for `learning_page`

Before a learning page is considered ready for publication, it should satisfy the following questions:

- Is the purpose of the topic clear?
- Can the central idea be understood before the formal mathematics begins?
- Are the physical definition and the analogy clearly separated?
- Is the mathematics developed in understandable steps?
- Are symbols and quantities explained?
- Are prerequisites explicit?
- Are common misconceptions addressed?
- Are learning objectives explicit and testable?
- Does assessment cover every essential learning objective?
- Does assessment require reasoning or application where appropriate?
- Is there a targeted path for correcting misunderstanding?
- Are sources appropriate and traceable?
- Is established cosmology clearly separated from Psi-Continuum-specific interpretation?
- Is the next learning step clear?

---

## 14. Next Validation Step

The `learning_page` model should next be tested against one real chapter rather than expanded abstractly.

Recommended test case:

**The Hubble Function H(z)**

The test should determine whether the proposed structure and metadata are actually useful while writing and learning real cosmology. Fields that do not help should be removed; missing pedagogical requirements should be added before the model is generalized to other content types.

---

## Current Status

`learning_page` is the first specified content type in Content Model v0.1.

The model remains a draft until it has been exercised on a real educational chapter and its assessment workflow.