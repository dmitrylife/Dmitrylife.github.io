---
layout: default
title: Quick start for observers
permalink: /docs/experiments/quick_start.en.html
---

# 🚀 Quick start for amateur astronomers

### This page is a practical companion to the «[Experimental observations](https://psi-continuum.org/docs/experiments/index_en)» section.

Minimal theory — maximum practice.  
If you have a telescope and a camera, you can already participate.

---

## 1️⃣ Choose a target

Select **one object**:

- **RR Lyrae star**
- **Classical Cepheid**

Requirements:
- magnitude range **V ≈ 7–12**
- well observable from your latitude
- **2–3 stable comparison stars** in the same field

> 👉 Recommended targets: [Target list](targets_en)

---

## 2️⃣ Prepare the equipment

Minimum setup:

- telescope with aperture **≥ 15 cm**
- CCD or CMOS camera
- photometric filter **Johnson V**  
  *(Sloan r′ is acceptable if V is unavailable)*
- equatorial mount with tracking

❌ No spectroscopy required  
❌ No absolute photometry required

---

## 3️⃣ Observing cadence

- Frequency: **2–3 sessions per week**
- Total duration: **at least 6–8 weeks**
- Each session:
  - observe the **same target**
  - use the **same filter**
  - keep exposure settings as consistent as possible

---

## 4️⃣ What to measure

Perform **differential photometry**:

- target variable star,
- average of **2–3 comparison stars**,
- *(optional)* one check star to monitor zero-point stability.

Any standard tools are acceptable:
- AstroImageJ
- Maxim DL
- Siril / CCDciel
- Python + photutils

---

## 5️⃣ Required precision

Do not aim for extreme precision.

✔ **0.01–0.03 mag is sufficient**  
✔ Repeatability matters more than absolute accuracy  
✔ Stability matters more than perfect numbers

---

## 6️⃣ Data format

Please use the provided data template:

👉 **[Download observations_template.csv →](/docs/experiments/observations_template.csv)**

Required CSV columns:

```text
time_utc, mag_diff, mag_err, filter, instrument
```

### Column description:

- time_utc — observation time in UTC (ISO 8601)
- mag_diff — differential magnitude (target − comparison stars)
- mag_err — estimated uncertainty (if available)
- filter — photometric filter (V or r′)
- instrument — brief setup description (telescope + camera)

### Example:

```text
2026-02-14T22:18:00, -0.134, 0.012, V, 200mm+ASI533
```

Optional:

- airmass,
- stacking details,
- brief description of data reduction.

---

## 7️⃣ Data submission

Choose a convenient option:

- 📂 **GitHub** — pull request or issue
- 📧 **Email** to the project coordinator

Strict formatting is not critical — assistance will be provided if needed.

---

## 8️⃣ Why this matters

Your observations help to:

- identify real systematic effects,
- test stability and reproducibility of observational data,
- support open and reproducible cosmological methodology.

This is a **real scientific contribution**, accessible to non-professional observers.

---

## 📬 Contact

**Project coordinator:**
Dmitry Vasilevich Klimov
Independent researcher

📧 d.klimov.psi@gmail.com  
[🌐 https://psi-continuum.org](https://psi-continuum.org)

