---
layout: default
title: KTRO — Klimov Tarpen Robotic Observatory
permalink: /docs/experiments/ktro/
---

<div style="text-align: center; margin: 2rem 0 3rem;">
  <img 
    src="https://psi-continuum.org/docs/experiments/ktro/pic/ktro-logo.jpg" 
    alt="KTRO — Klimov Tarpen Robotic Observatory Logo" 
    style="max-width: 100%; height: auto; width: 320px;"
  >
  <p style="margin: 0; color: #ccc; font-size: 1.2rem;">
    Klimov Tarpen Robotic Observatory
  </p>
</div>

# KTRO — Klimov Tarpen Robotic Observatory

KTRO (Klimov Tarpen Robotic Observatory) is a small-scale,
semi-automated observational facility developed within the
Psi–Continuum Experimental Program.

Its purpose is not survey-scale astronomy or object discovery.  
KTRO is designed as a controlled photometric stability platform,
focused on long-term reproducibility, instrumental consistency,
and methodological robustness.

---

## Project Overview

KTRO is being developed as a compact robotic observatory for
controlled, repeatable astronomical measurements.

The project is oriented toward:

- differential photometry  
- long-term instrumental stability  
- reproducible observing routines  
- cross-night consistency testing  
- pipeline-level methodological validation  

Rather than maximizing volume, KTRO is built to maximize
control, traceability, and repeatability.

---

## Scientific Function within the Psi–Continuum Program

The Psi–Continuum framework operates at two scales:

- large-scale cosmological background diagnostics  
- small-scale controlled observational stability tests  

KTRO serves as a macroscopic experimental testbed for
measurement-system behavior.

While cosmological analyses rely on public datasets
(SN Ia, BAO, H(z)), KTRO allows controlled repetition
of measurements under known instrumental conditions.

The objective is methodological:

- evaluate differential photometric stability  
- quantify long-term instrumental drift  
- test cross-epoch reproducibility  
- characterize noise structure under repeated measurements  
- validate pipeline-level robustness  

The guiding principle is consistent across scales:

> Measurement systems must demonstrate stability, response coherence,
> and controlled deviations.

---

## Observational Scope

Primary targets:

- RR Lyrae stars  
- Classical Cepheids  
- stable reference stars for baseline control  

Observational protocol emphasizes:

- differential photometry  
- standard calibration frames (bias, dark, flat)  
- fixed and version-controlled reduction pipeline  
- archivable and reproducible output formats  
- cross-night consistency monitoring  

The objective is reproducibility rather than discovery.

---

## Instrumentation

### Mount
- MaxVision EXOS-2 (equatorial mount)  
- OnStep V4 Pro controller  

### Optical System
- Sky-Watcher BKP 150/750 (Newtonian, f/5)  
- Baader MPCC Mark III coma corrector  

### Camera
- ZWO ASI533MM Pro (monochrome CMOS)  

### Filters
- UBVRI Bessel set (V2)  

### Focusing
- ZWO EAF (with temperature sensor)  

The system is designed for mechanical stability,
repeatable pointing, and progressive automation.

---

## Calibration Strategy

KTRO employs a standardized calibration procedure:

- bias and dark frame libraries under temperature control  
- nightly flat-field acquisition  
- fixed reduction workflow  
- version-controlled processing scripts  

All reduction steps are documented and reproducible.

---

## Development Phases

**Phase 1 — Mechanical validation (completed)**  
Mount assembly, polar alignment testing, tracking validation.

**Phase 2 — Semi-automation (ongoing)**  
Repeatable pointing routines, motor control refinement,
pipeline integration.

**Phase 3 — Long-term monitoring mode (planned)**  
Multi-month monitoring programs, cross-season stability checks,
public data documentation where feasible.

---

## Current Project Status

KTRO is currently in **Phase 2 (semi-automation development)**.

At this stage, the project has already achieved:

- assembled and operational core mount/optical platform  
- initial tracking and alignment validation  
- defined reduction workflow  
- instrumentation baseline for photometric work  

The next milestone is transition from a semi-manual setup
to a stable repeatable monitoring system suitable for
long-term observational campaigns.

This transition depends not only on software and methodology,
but also on completing the hardware chain required for
fully reliable operation.

---

## Hardware Completion — Support This Project

<style>
.ktro-support-wrap {
  margin: 2.5rem 0;
}

.ktro-support-note {
  margin: 0 0 1.4rem;
  padding: 1rem 1.2rem;
  border-left: 4px solid #5aa9ff;
  background: rgba(90, 169, 255, 0.08);
  border-radius: 10px;
}

.ktro-support-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 18px;
  margin: 1.5rem 0 2rem;
}

.ktro-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.10);
  border-radius: 16px;
  padding: 18px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

.ktro-card h3 {
  margin-top: 0;
  margin-bottom: 0.7rem;
  font-size: 1.08rem;
}

.ktro-badge {
  display: inline-block;
  font-size: 0.76rem;
  font-weight: 600;
  padding: 0.28rem 0.55rem;
  border-radius: 999px;
  margin-bottom: 0.9rem;
  background: rgba(90, 169, 255, 0.12);
  color: #9fd0ff;
}

.ktro-card p {
  margin: 0 0 1rem;
  color: #d6d6d6;
  line-height: 1.55;
  font-size: 0.96rem;
}

.ktro-card .ktro-btn {
  display: inline-block;
  padding: 0.72rem 1rem;
  border-radius: 10px;
  background: #5aa9ff;
  color: #0e1726;
  text-decoration: none;
  font-weight: 700;
}

.ktro-card .ktro-btn.secondary {
  background: rgba(255,255,255,0.08);
  color: #f2f2f2;
  border: 1px solid rgba(255,255,255,0.12);
}

.ktro-support-box {
  margin-top: 2rem;
  padding: 1.2rem 1.3rem;
  border-radius: 16px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.10);
}

.ktro-list {
  margin: 0.8rem 0 0;
  padding-left: 1.2rem;
}
</style>

<div class="ktro-support-wrap">

  <div class="ktro-support-note">
    KTRO is at a transition point from a semi-manual system
    to a fully reproducible robotic observatory.
    Completion of the hardware chain defines this transition.
  </div>

  <div class="ktro-support-grid">

    <div class="ktro-card">
      <div class="ktro-badge">Required</div>
      <h3>ZWO ASI533MM Pro</h3>
      <p>Primary monochrome camera for scientific photometry.</p>
      <a class="ktro-btn" href="https://aliexpress.ru/item/1005009843622926.html" target="_blank">Support</a>
    </div>

    <div class="ktro-card">
      <div class="ktro-badge">Required</div>
      <h3>ZWO EFW 2" Filter Wheel</h3>
      <p>Automated multi-band observation capability.</p>
      <a class="ktro-btn" href="https://aliexpress.ru/item/1005009186375730.html" target="_blank">Support</a>
    </div>

    <div class="ktro-card">
      <div class="ktro-badge">Required</div>
      <h3>UBVRI Bessel Filters</h3>
      <p>Standard photometric system.</p>
      <a class="ktro-btn" href="https://www.optics-pro.com/pass-filters/baader-filters-ubvri-bessel-v-2-/p,73913" target="_blank">Support</a>
    </div>

    <div class="ktro-card">
      <div class="ktro-badge">Required</div>
      <h3>MPCC Mark III</h3>
      <p>Field correction for photometric consistency.</p>
      <a class="ktro-btn" href="https://www.optics-pro.com/flatteners-correctors-reducers/baader-mpcc-mark-iii-multi-purpose-newton-coma-correktor/p,33547" target="_blank">Support</a>
    </div>

    <div class="ktro-card">
      <div class="ktro-badge">Required</div>
      <h3>ZWO EAFN</h3>
      <p>Temperature-compensated autofocus.</p>
      <a class="ktro-btn" href="https://aliexpress.ru/item/1005006127499191.html" target="_blank">Support</a>
    </div>

    <div class="ktro-card">
      <div class="ktro-badge">Required</div>
      <h3>Mini PC</h3>
      <p>Control system for automation.</p>
      <a class="ktro-btn" href="https://aliexpress.ru/item/1005008523207827.html" target="_blank">Support</a>
    </div>

  </div>

  <div class="ktro-support-box">
    <strong>Recipient:</strong> Dmitry V. Klimov<br>
    <strong>Region:</strong> Kaliningrad Region, Russia<br>
    <strong>Shipping details:</strong> provided upon request<br>
    <strong>Contact:</strong> d.klimov.psi@gmail.com
  </div>

</div>

---

## Reproducibility Policy

All observational procedures are:

- documented  
- version-controlled  
- pipeline-reproducible  
- archivable  

---

## Status Summary

**Current status:** Phase 2 — semi-automation  
**Next step:** full robotic monitoring  
**Priority:** hardware completion for stability  

Structured long-term monitoring campaigns are planned.
