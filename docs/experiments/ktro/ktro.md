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

## Project Progress

<style>
.ktro-progress-wrap {
  margin: 2rem 0 2.2rem;
}

.ktro-progress-card,
.ktro-funding-card {
  margin-top: 1.2rem;
  padding: 1.2rem 1.3rem;
  border-radius: 16px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.10);
}

.ktro-progress-title,
.ktro-funding-title {
  margin: 0 0 0.6rem;
  font-size: 1.05rem;
  font-weight: 700;
}

.ktro-progress-text,
.ktro-funding-text {
  margin: 0 0 1rem;
  line-height: 1.6;
  color: #d6d6d6;
}

.ktro-progress-bar {
  width: 100%;
  height: 16px;
  background: rgba(255,255,255,0.08);
  border-radius: 999px;
  overflow: hidden;
  margin: 0.7rem 0 0.4rem;
}

.ktro-progress-fill {
  height: 100%;
  width: 42%;
  background: linear-gradient(90deg, #5aa9ff, #8ed0ff);
  border-radius: 999px;
}

.ktro-progress-label {
  font-size: 0.95rem;
  font-weight: 600;
  color: #9fd0ff;
}

.ktro-stage-grid,
.ktro-funding-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 14px;
  margin-top: 1rem;
}

.ktro-stage-item,
.ktro-funding-item {
  padding: 0.9rem 1rem;
  border-radius: 12px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
}

.ktro-stage-item strong,
.ktro-funding-item strong {
  display: block;
  margin-bottom: 0.35rem;
}

.ktro-stage-item span,
.ktro-funding-item span {
  color: #d6d6d6;
  line-height: 1.5;
}

.ktro-funding-meter {
  display: flex;
  width: 100%;
  height: 16px;
  border-radius: 999px;
  overflow: hidden;
  background: rgba(255,255,255,0.08);
  margin: 0.8rem 0 0.5rem;
}

.ktro-funded {
  width: 34%;
  background: linear-gradient(90deg, #63d08a, #7ee2a1);
}

.ktro-needed {
  width: 66%;
  background: rgba(255,255,255,0.12);
}

.ktro-funding-legend {
  display: flex;
  gap: 18px;
  flex-wrap: wrap;
  font-size: 0.94rem;
  color: #d6d6d6;
}

.ktro-dot {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-right: 0.45rem;
}

.ktro-dot-funded {
  background: #63d08a;
}

.ktro-dot-needed {
  background: rgba(255,255,255,0.35);
}
</style>

<div class="ktro-progress-wrap">

  <div class="ktro-progress-card">
    <div class="ktro-progress-title">Overall project readiness</div>
    <p class="ktro-progress-text">
      KTRO has completed the initial mechanical platform and entered the
      semi-automation stage. The remaining work is concentrated in the
      imaging, focusing, filtering, and observatory-side control chain.
    </p>

    <div class="ktro-progress-bar">
      <div class="ktro-progress-fill"></div>
    </div>
    <div class="ktro-progress-label">42% complete</div>

    <div class="ktro-stage-grid">
      <div class="ktro-stage-item">
        <strong>Mechanical base</strong>
        <span>Operational: mount, optical tube, and controller platform are in place.</span>
      </div>
      <div class="ktro-stage-item">
        <strong>Imaging chain</strong>
        <span>Partially incomplete: camera, filter wheel, and standard photometric filters still required.</span>
      </div>
      <div class="ktro-stage-item">
        <strong>Automation</strong>
        <span>In progress: repeatable control and observatory-side automation are under development.</span>
      </div>
      <div class="ktro-stage-item">
        <strong>Monitoring mode</strong>
        <span>Planned: long-term stable observing campaigns begin after hardware chain completion.</span>
      </div>
    </div>
  </div>

  <div class="ktro-funding-card">
    <div class="ktro-funding-title">Funding status</div>
    <p class="ktro-funding-text">
      KTRO is an independently developed research infrastructure project.
      The observatory base is already established, while the remaining
      scientific hardware chain is still needed to reach full operational capability.
    </p>

    <div class="ktro-funding-meter">
      <div class="ktro-funded"></div>
      <div class="ktro-needed"></div>
    </div>

    <div class="ktro-funding-legend">
      <span><span class="ktro-dot ktro-dot-funded"></span>Funded / already deployed — 34%</span>
      <span><span class="ktro-dot ktro-dot-needed"></span>Needed for completion — 66%</span>
    </div>

    <div class="ktro-funding-grid">
      <div class="ktro-funding-item">
        <strong>Already deployed</strong>
        <span>Sky-Watcher Explorer 150P, MaxVision EXOS-2, OnStep V4 Pro.</span>
      </div>
      <div class="ktro-funding-item">
        <strong>Needed next</strong>
        <span>ASI533MM Pro, EFW 2", UBVRI filters, EAFN, MPCC Mark III, Mini PC.</span>
      </div>
      <div class="ktro-funding-item">
        <strong>Planned later</strong>
        <span>Environmental monitoring modules and enclosure-related extensions.</span>
      </div>
    </div>
  </div>

</div>

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
