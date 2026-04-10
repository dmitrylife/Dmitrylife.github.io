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
  <p style="margin: 0; color: #666; font-size: 1.1rem;">
    Klimov Tarpen Robotic Observatory
  </p>
</div>

# KTRO — Klimov Tarpen Robotic Observatory

KTRO (Klimov Tarpen Robotic Observatory) is a small-scale,
semi-automated observational facility developed within the
Psi–Continuum Experimental Program.

Its purpose is not large-scale survey astronomy or object discovery,
but controlled, repeatable measurements.  
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

## Why this matters

<style>
.ktro-why-wrap {
  margin: 2rem 0 2.5rem;
  padding: 1.4rem 1.5rem;
  border-radius: 16px;
  background: #f8fafc;
  border: 1px solid #d9e2ec;
}

.ktro-why-lead {
  font-size: 1.05rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #0f172a;
}

.ktro-why-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
  margin-top: 1rem;
}

.ktro-why-card {
  background: #ffffff;
  border: 1px solid #dbe4ee;
  border-radius: 14px;
  padding: 16px;
}

.ktro-why-card strong {
  display: block;
  margin-bottom: 0.5rem;
  color: #0f172a;
}

.ktro-why-card span {
  color: #475569;
  line-height: 1.6;
  font-size: 0.95rem;
}

.ktro-why-bottom {
  margin-top: 1.2rem;
  padding-top: 1rem;
  border-top: 1px solid #e2e8f0;
  color: #475569;
  line-height: 1.7;
}
</style>

<div class="ktro-why-wrap">

  <div class="ktro-why-lead">
    KTRO is not built to discover new objects — it is built to understand how measurements behave.
  </div>

  <div class="ktro-why-grid">

    <div class="ktro-why-card">
      <strong>Measurement stability</strong>
      <span>
        Modern astrophysics relies on high-precision datasets, yet
        the stability of measurement systems themselves is rarely
        tested under controlled, repeatable conditions.
      </span>
    </div>

    <div class="ktro-why-card">
      <strong>Reproducibility</strong>
      <span>
        KTRO provides a platform where the same observations can be
        repeated over months and seasons, allowing direct evaluation
        of reproducibility and systematic drift.
      </span>
    </div>

    <div class="ktro-why-card">
      <strong>Instrument response</strong>
      <span>
        By operating a fixed, version-controlled pipeline, KTRO
        isolates how instruments and processing chains respond
        over time under identical conditions.
      </span>
    </div>

    <div class="ktro-why-card">
      <strong>Methodological discipline</strong>
      <span>
        The project emphasizes controlled procedures over data volume,
        focusing on how reliable conclusions emerge from stable
        measurement systems.
      </span>
    </div>

  </div>

  <div class="ktro-why-bottom">
    KTRO complements large-scale cosmological datasets by providing
    a small-scale, controlled environment where measurement behavior
    can be directly examined.
    <br><br>
    The goal is not more data — but better-understood data.
  </div>

</div>

> KTRO is not about equipment.  
> It is about creating a stable observational reference system.

---

## Scientific Function within the Psi–Continuum Program

The Psi–Continuum framework operates at two scales:

- large-scale cosmological background diagnostics  
- small-scale controlled observational stability tests  

KTRO serves as a controlled experimental testbed for
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

### Planned Imaging Chain
- Baader MPCC Mark III coma corrector  
- ZWO ASI533MM Pro (monochrome CMOS)  
- ZWO EFW 2" filter wheel  
- UBVRI Bessel filter set (V2)  
- ZWO EAFN autofocus system  
- Mini PC for observatory-side control  
- Lunatico AAG CloudWatcher  

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
- baseline observatory platform established for photometric work  

The next milestone is transition from a semi-manual setup
to a stable repeatable monitoring system suitable for
long-term observational campaigns.

This transition depends not only on software and methodology,
but also on completing the hardware chain required for
fully reliable operation.

---

## KTRO Build Status

<style>
.ktro-build-wrap {
  margin: 2rem 0 2.5rem;
}

.ktro-build-note,
.ktro-summary-box,
.ktro-ship-box {
  margin: 0 0 1.4rem;
  padding: 1.15rem 1.3rem;
  border-radius: 16px;
  background: #f8fafc;
  border: 1px solid #d9e2ec;
  color: #334155;
}

.ktro-build-note {
  border-left: 4px solid #2563eb;
  background: #f3f7ff;
}

.ktro-progress-head {
  margin: 1.4rem 0 1rem;
}

.ktro-progress-title {
  font-size: 1.08rem;
  font-weight: 700;
  margin-bottom: 0.45rem;
  color: #0f172a;
}

.ktro-progress-subtitle {
  color: #475569;
  line-height: 1.6;
}

.ktro-progress-bar {
  width: 100%;
  height: 18px;
  background: #dbe7f3;
  border-radius: 999px;
  overflow: hidden;
  margin-top: 0.9rem;
  border: 1px solid #c8d7e8;
}

.ktro-progress-fill {
  width: 22%;
  height: 100%;
  background: linear-gradient(90deg, #16a34a, #22c55e);
  border-radius: 999px;
}

.ktro-progress-meta {
  margin-top: 0.5rem;
  font-size: 0.95rem;
  color: #475569;
  font-weight: 600;
}

.ktro-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(245px, 1fr));
  gap: 18px;
  margin-top: 1.5rem;
}

.ktro-card {
  background: #ffffff;
  border: 1px solid #dbe4ee;
  border-radius: 18px;
  padding: 18px;
  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
}

.ktro-status {
  display: inline-block;
  font-size: 0.76rem;
  font-weight: 700;
  padding: 0.32rem 0.62rem;
  border-radius: 999px;
  margin-bottom: 0.9rem;
}

.ktro-status.done {
  background: #dcfce7;
  color: #166534;
}

.ktro-status.progress {
  background: #dbeafe;
  color: #1d4ed8;
}

.ktro-card h3 {
  margin: 0 0 0.65rem;
  font-size: 1.08rem;
  color: #0f172a;
}

.ktro-card p {
  margin: 0 0 1rem;
  line-height: 1.6;
  color: #475569;
  min-height: 84px;
}

.ktro-card .ktro-btn {
  display: inline-block;
  padding: 0.72rem 1rem;
  border-radius: 11px;
  background: #2563eb;
  color: #ffffff;
  text-decoration: none;
  font-weight: 700;
  transition: 0.18s ease;
}

.ktro-card .ktro-btn:hover {
  background: #1d4ed8;
  transform: translateY(-1px);
}

.ktro-card .ktro-btn.done-btn {
  background: #16a34a;
  cursor: default;
  pointer-events: none;
}

.ktro-summary-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 14px;
  margin-top: 1rem;
}

.ktro-summary-item {
  padding: 0.95rem 1rem;
  background: #ffffff;
  border: 1px solid #dbe4ee;
  border-radius: 14px;
}

.ktro-summary-item strong {
  display: block;
  margin-bottom: 0.35rem;
  color: #0f172a;
}

.ktro-summary-item span {
  color: #475569;
  line-height: 1.55;
}

.ktro-ship-box a {
  color: #2563eb;
  text-decoration: none;
  font-weight: 600;
}

.ktro-ship-box a:hover {
  text-decoration: underline;
}
</style>

<div class="ktro-build-wrap">

  <div class="ktro-build-note">
    KTRO is being assembled as a compact robotic observatory for
    reproducible photometric monitoring. The readiness level below
    is estimated directly from the number of completed core hardware modules.
  </div>

  <div class="ktro-progress-head">
    <div class="ktro-progress-title">Overall hardware readiness</div>
    <div class="ktro-progress-subtitle">
      2 of 9 key system modules are already deployed.
      The remaining modules are currently in progress.
    </div>
    <div class="ktro-progress-bar">
      <div class="ktro-progress-fill"></div>
    </div>
    <div class="ktro-progress-meta">22% complete — based on completed hardware cards</div>
  </div>
  <div style="margin-top:6px; font-size:0.9rem; color:#64748b;">
    Estimated full operational readiness after hardware completion: ~85–90%
  </div>  

  <div class="ktro-card-grid">

    <div class="ktro-card">
      <div class="ktro-status done">Completed</div>
      <h3>Sky-Watcher Explorer 150P</h3>
      <p>
        Primary optical tube already deployed as the telescope base
        of the KTRO system.
      </p>
      <span class="ktro-btn done-btn">Completed</span>
    </div>

    <div class="ktro-card">
      <div class="ktro-status done">Completed</div>
      <h3>MaxVision EXOS-2 + OnStep V4 Pro</h3>
      <p>
        Equatorial mount and controller platform already operational
        as the mechanical base of the observatory.
      </p>
      <span class="ktro-btn done-btn">Completed</span>
    </div>

    <div class="ktro-card">
      <div class="ktro-status progress">In progress</div>
      <h3>ZWO ASI533MM Pro</h3>
      <p>
        Primary monochrome scientific camera for differential photometry,
        repeatable measurements, and long-term stability analysis.
      </p>
      <a class="ktro-btn" href="https://aliexpress.ru/item/1005009843622926.html?shpMethod=CAINIAO_STANDARD&sku_id=12000050338468416&spm=a2g2w.productlist.search_results.0.66832e19IwRkyH" target="_blank" rel="noopener">
        Support this component
      </a>
    </div>

    <div class="ktro-card">
      <div class="ktro-status progress">In progress</div>
      <h3>ZWO EFW 2&quot; Filter Wheel</h3>
      <p>
        Automated filter switching for controlled multi-band observations
        and a reproducible observing workflow.
      </p>
      <a class="ktro-btn" href="https://aliexpress.ru/item/1005009186375730.html?sku_id=12000048232579543" target="_blank" rel="noopener">
        Support this component
      </a>
    </div>

    <div class="ktro-card">
      <div class="ktro-status progress">In progress</div>
      <h3>Baader UBVRI Bessel Filter Set (V2)</h3>
      <p>
        Standard photometric filter set required for scientifically
        consistent and comparable measurements.
      </p>
      <a class="ktro-btn" href="https://www.optics-pro.com/pass-filters/baader-filters-ubvri-bessel-v-2-/p,73913" target="_blank" rel="noopener">
        Support this component
      </a>
    </div>

    <div class="ktro-card">
      <div class="ktro-status progress">In progress</div>
      <h3>Baader MPCC Mark III</h3>
      <p>
        Coma correction module for improved field uniformity and
        more stable photometric quality across the frame.
      </p>
      <a class="ktro-btn" href="https://www.optics-pro.com/flatteners-correctors-reducers/baader-mpcc-mark-iii-multi-purpose-newton-coma-correktor/p,33547" target="_blank" rel="noopener">
        Support this component
      </a>
    </div>

    <div class="ktro-card">
      <div class="ktro-status progress">In progress</div>
      <h3>ZWO EAFN Auto Focuser</h3>
      <p>
        Temperature-aware autofocus module for focus stability
        during repeatable long-duration observing sessions.
      </p>
      <a class="ktro-btn" href="https://aliexpress.ru/item/1005006127499191.html?sku_id=12000035878933081" target="_blank" rel="noopener">
        Support this component
      </a>
    </div>

    <div class="ktro-card">
      <div class="ktro-status progress">In progress</div>
      <h3>Mini PC (Intel N100 class)</h3>
      <p>
        Dedicated observatory-side computer for INDI, KStars,
        remote control, and automation pipeline operation.
      </p>
      <a class="ktro-btn" href="https://aliexpress.ru/item/1005008523207827.html?spm=a2g2w.favourites.0.0.8cb14aa66AnqpW&sku_id=12000045551014784" target="_blank" rel="noopener">
        Support this component
      </a>
    </div>

    <div class="ktro-card">
      <div class="ktro-status progress">In progress</div>
      <h3>Lunatico AAG CloudWatcher</h3>
      <p>
        Autonomous cloud and sky condition monitoring system 
        required for safe unattended robotic operation.
      </p>
      <a class="ktro-btn" href="https://shop.lunaticoastro.com/product/aag-cloudwatcher-cloud-detector/" target="_blank" rel="noopener">
        Support this component
      </a>
    </div>

  </div>

  <div class="ktro-summary-box">
    <div class="ktro-summary-grid">
      <div class="ktro-summary-item">
        <strong>Completed</strong>
        <span>2 modules: telescope and mount/controller platform.</span>
      </div>
      <div class="ktro-summary-item">
        <strong>In progress</strong>
        <span>7 modules remain to complete the operational hardware chain.</span>
      </div>
      <div class="ktro-summary-item">
        <strong>Current readiness</strong>
        <span>22% of key hardware modules completed.</span>
      </div>
    </div>
  </div>

  <div class="ktro-ship-box">
    <strong>Equipment support and shipment</strong><br><br>
    <strong>Recipient:</strong> Dmitry V. Klimov<br>
    <strong>Region:</strong> Kaliningrad Region, Russia<br>
    <strong>Shipping details:</strong> provided upon request<br>
    <strong>Contact:</strong> <a href="mailto:d.klimov.psi@gmail.com">d.klimov.psi@gmail.com</a><br><br>
    Please contact before purchase or shipment to confirm compatibility,
    current priority, and delivery details.
  </div>

</div>

---

## Reproducibility Policy

All data products will be made publicly available where possible.

All observational procedures are:

- documented  
- version-controlled  
- pipeline-reproducible  
- archivable  

The program is methodological and complementary to
professional observatories.

It aims to explore response diagnostics and stability structure
under controlled small-scale conditions.

---

## Status Summary

**Current status:** Phase 2 — semi-automation development  
**Hardware readiness:** 22% complete  
**Completed modules:** telescope; mount and controller  
**Priority:** camera, filters, automation, weather monitoring  

Structured long-term monitoring campaigns are planned
for the sky conditions of the Nemansky region.

