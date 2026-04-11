---
layout: default
title: KTRO — Klimov Tarpen Robotic Observatory
permalink: /docs/experiments/ktro/
---

<div class="project-hero project-hero--center">
  <img 
    src="https://psi-continuum.org/docs/experiments/ktro/pic/ktro-logo.jpg" 
    alt="KTRO — Klimov Tarpen Robotic Observatory Logo" 
    class="project-hero__logo"
  >
  <p class="project-caption">
    Klimov Tarpen Robotic Observatory
  </p>
</div>

# KTRO — Klimov Tarpen Robotic Observatory

<p class="project-muted u-mb-2">
  “Tarpen” refers to the historical name associated with the Tushino area.
</p>

<div class="project-hero project-hero--split">

  <div class="project-hero__text">
    <div class="project-lead">
      A small-scale robotic observatory designed to study measurement stability,
      reproducibility, and instrument response in real observational conditions.
    </div>

    <p class="project-muted">
      KTRO (Klimov Tarpen Robotic Observatory) is a semi-automated observational
      facility developed within the Psi–Continuum Experimental Program.
    </p>

    <p class="project-muted">
      Its purpose is not large-scale survey astronomy or object discovery,
      but controlled, repeatable measurements.
    </p>
  </div>

  <div class="project-hero__image">
    <img src="/docs/experiments/ktro/pic/ktro_setup.png" alt="KTRO system configuration">
  </div>

</div>

<p>
  KTRO is designed as a controlled photometric stability platform,
  focused on long-term reproducibility, instrumental consistency,
  and methodological robustness.
</p>

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

<div class="project-panel">
  <div class="project-lead">
    KTRO is not built to discover new objects — it is built to understand how measurements behave.
  </div>

  <div class="project-grid project-grid--2">

    <div class="project-card">
      <div class="project-card__title">Measurement stability</div>
      <div class="project-card__text">
        Modern astrophysics relies on high-precision datasets, yet
        the stability of measurement systems themselves is rarely
        tested under controlled, repeatable conditions.
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Reproducibility</div>
      <div class="project-card__text">
        KTRO provides a platform where the same observations can be
        repeated over months and seasons, allowing direct evaluation
        of reproducibility and systematic drift.
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Instrument response</div>
      <div class="project-card__text">
        By operating a fixed, version-controlled pipeline, KTRO
        isolates how instruments and processing chains respond
        over time under identical conditions.
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Methodological discipline</div>
      <div class="project-card__text">
        The project emphasizes controlled procedures over data volume,
        focusing on how reliable conclusions emerge from stable
        measurement systems.
      </div>
    </div>

  </div>

  <div class="project-panel__footer">
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
- MaxVision EXOS-2 (equatorial mount)✔  
- OnStep V4 Pro controller✔  

### Optical System
- Sky-Watcher BKP 150/750 (Newtonian, f/5)✔  

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

<div class="project-panel project-panel--accent">

  <div class="project-note project-note--info">
    KTRO is being assembled as a compact robotic observatory for
    reproducible photometric monitoring. The readiness level below
    is estimated directly from the number of completed core hardware modules.
  </div>

  <div class="project-progress">
    <div class="project-progress__title">Overall hardware readiness</div>
    <div class="project-progress__subtitle">
      2 of 9 key system modules are already deployed.
      The remaining modules are currently in progress.
    </div>
    <div class="project-progress__bar">
      <div class="project-progress__fill" style="width:22%;"></div>
    </div>
    <div class="project-progress__meta">22% complete — based on completed hardware cards</div>
    <div class="project-muted u-mt-1">
      Estimated full operational readiness after hardware completion: ~85–90%
    </div>
  </div>

  <div class="project-grid project-grid--auto">

    <div class="project-card">
      <div class="project-badge project-badge--done">Completed</div>
      <div class="project-card__title">Sky-Watcher Explorer 150P</div>
      <div class="project-card__text">
        Primary optical tube already deployed as the telescope base
        of the KTRO system.
      </div>
      <div class="project-card__actions">
        <span class="project-btn project-btn--done">Completed</span>
      </div>
    </div>

    <div class="project-card">
      <div class="project-badge project-badge--done">Completed</div>
      <div class="project-card__title">MaxVision EXOS-2 + OnStep V4 Pro</div>
      <div class="project-card__text">
        Equatorial mount and controller platform already operational
        as the mechanical base of the observatory.
      </div>
      <div class="project-card__actions">
        <span class="project-btn project-btn--done">Completed</span>
      </div>
    </div>

    <div class="project-card">
      <div class="project-badge project-badge--progress">In progress</div>
      <div class="project-card__title">ZWO ASI533MM Pro</div>
      <div class="project-card__text">
        Primary monochrome scientific camera for differential photometry,
        repeatable measurements, and long-term stability analysis.
      </div>
      <div class="project-card__actions">
        <a class="project-btn project-btn--primary" href="https://aliexpress.ru/item/1005009843622926.html?shpMethod=CAINIAO_STANDARD&sku_id=12000050338468416&spm=a2g2w.productlist.search_results.0.66832e19IwRkyH" target="_blank" rel="noopener">Support component</a>
      </div>
    </div>

    <div class="project-card">
      <div class="project-badge project-badge--progress">In progress</div>
      <div class="project-card__title">ZWO EFW 2" Filter Wheel</div>
      <div class="project-card__text">
        Automated filter switching for controlled multi-band observations
        and a reproducible observing workflow.
      </div>
      <div class="project-card__actions">
        <a class="project-btn project-btn--primary" href="https://aliexpress.ru/item/1005009186375730.html?sku_id=12000048232579543" target="_blank" rel="noopener">Support component</a>
      </div>
    </div>

    <div class="project-card">
      <div class="project-badge project-badge--progress">In progress</div>
      <div class="project-card__title">Baader UBVRI Bessel Filter Set (V2)</div>
      <div class="project-card__text">
        Standard photometric filter set required for scientifically
        consistent and comparable measurements.
      </div>
      <div class="project-card__actions">
        <a class="project-btn project-btn--primary" href="https://www.optics-pro.com/pass-filters/baader-filters-ubvri-bessel-v-2-/p,73913" target="_blank" rel="noopener">Support component</a>
      </div>
    </div>

    <div class="project-card">
      <div class="project-badge project-badge--progress">In progress</div>
      <div class="project-card__title">Baader MPCC Mark III</div>
      <div class="project-card__text">
        Coma correction module for improved field uniformity and
        more stable photometric quality across the frame.
      </div>
      <div class="project-card__actions">
        <a class="project-btn project-btn--primary" href="https://www.optics-pro.com/flatteners-correctors-reducers/baader-mpcc-mark-iii-multi-purpose-newton-coma-correktor/p,33547" target="_blank" rel="noopener">Support component</a>
      </div>
    </div>

    <div class="project-card">
      <div class="project-badge project-badge--progress">In progress</div>
      <div class="project-card__title">ZWO EAFN Auto Focuser</div>
      <div class="project-card__text">
        Temperature-aware autofocus module for focus stability
        during repeatable long-duration observing sessions.
      </div>
      <div class="project-card__actions">
        <a class="project-btn project-btn--primary" href="https://aliexpress.ru/item/1005006127499191.html?sku_id=12000035878933081" target="_blank" rel="noopener">Support component</a>
      </div>
    </div>

    <div class="project-card">
      <div class="project-badge project-badge--progress">In progress</div>
      <div class="project-card__title">Mini PC (Intel N100 class)</div>
      <div class="project-card__text">
        Dedicated observatory-side computer for INDI, KStars,
        remote control, and automation pipeline operation.
      </div>
      <div class="project-card__actions">
        <a class="project-btn project-btn--primary" href="https://aliexpress.ru/item/1005008523207827.html?spm=a2g2w.favourites.0.0.8cb14aa66AnqpW&sku_id=12000045551014784" target="_blank" rel="noopener">Support component</a>
      </div>
    </div>

    <div class="project-card">
      <div class="project-badge project-badge--progress">In progress</div>
      <div class="project-card__title">Lunatico AAG CloudWatcher</div>
      <div class="project-card__text">
        Autonomous cloud and sky condition monitoring system
        required for safe unattended robotic operation.
      </div>
      <div class="project-card__actions">
        <a class="project-btn project-btn--primary" href="https://shop.lunaticoastro.com/product/aag-cloudwatcher-cloud-detector/" target="_blank" rel="noopener">Support component</a>
      </div>
    </div>

  </div>

  <div class="project-summary">
    <div class="project-summary__item">
      <div class="project-summary__label">Completed</div>
      <div class="project-summary__text">2 modules: telescope and mount/controller platform.</div>
    </div>
    <div class="project-summary__item">
      <div class="project-summary__label">In progress</div>
      <div class="project-summary__text">7 modules remain to complete the operational hardware chain.</div>
    </div>
    <div class="project-summary__item">
      <div class="project-summary__label">Current readiness</div>
      <div class="project-summary__text">22% of key hardware modules completed.</div>
    </div>
  </div>

  <div class="project-support-box">
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

## What support enables

<div class="project-panel">
  <div class="project-lead">
    Completing the KTRO hardware chain enables a transition
    from experimental setup to a stable observational system.
  </div>

  <div class="project-grid project-grid--auto">

    <div class="project-card">
      <div class="project-card__title">True photometric measurements</div>
      <div class="project-card__text">
        A cooled monochrome camera with calibrated filters enables
        scientifically consistent differential photometry,
        instead of qualitative observations.
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Reproducible observing sessions</div>
      <div class="project-card__text">
        Automated filter switching, autofocus, and stable control
        allow identical observing conditions to be repeated
        across nights and seasons.
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Fully automated operation</div>
      <div class="project-card__text">
        Integration of Mini PC, OnStep control, and environmental
        monitoring enables unattended robotic observing cycles
        with remote supervision.
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Environmental awareness</div>
      <div class="project-card__text">
        CloudWatcher provides real-time sky condition assessment,
        allowing safe operation and consistent data quality control.
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Stable data pipeline</div>
      <div class="project-card__text">
        A complete acquisition → calibration → reduction chain
        ensures traceable and reproducible data products.
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Public observational dataset</div>
      <div class="project-card__text">
        The completed system enables structured long-term datasets
        that can be published and used for independent analysis.
      </div>
    </div>

  </div>

  <div class="project-panel__footer">
    Support does not only add hardware — it transforms KTRO into
    a controlled observational system capable of producing
    scientifically meaningful and reproducible data.
  </div>
</div>

---

## System Architecture

<div class="project-panel">
  <div class="project-lead">
    KTRO is designed as a complete observational chain:
    from optical acquisition and instrument control
    to calibrated data reduction and public publication.
  </div>

  <div class="project-grid project-grid--auto">

    <div class="project-card">
      <div class="project-card__title">Optical system</div>
      <div class="project-card__text">
        Sky-Watcher 150/750 telescope → Baader MPCC Mark III →
        ASI533MM Pro camera → 2" filter wheel → autofocus module
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Mount and control</div>
      <div class="project-card__text">
        MaxVision EXOS-2 mount → OnStep V4 Pro controller →
        pointing, tracking, and repeatable motion control
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Observatory-side computing</div>
      <div class="project-card__text">
        Mini PC → INDI / KStars / automation scripts →
        session control, device coordination, and monitoring
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Environment and connectivity</div>
      <div class="project-card__text">
        Lunatico AAG CloudWatcher → sky-state monitoring →
        4G communication link for remote supervision and control
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Pipeline</div>
      <div class="project-card__text">
        Acquisition → calibration frames → reduction pipeline →
        quality checks → reproducible processed outputs
      </div>
    </div>

    <div class="project-card">
      <div class="project-card__title">Data publication</div>
      <div class="project-card__text">
        Final data products → documentation → GitHub repository →
        public archival availability where feasible
      </div>
    </div>

  </div>

  <div class="project-flow">
    <div class="project-flow__title">System flow</div>
    <div class="project-flow__line">
      <span class="project-node project-node--hardware">Telescope + Camera Chain</span>
      <span class="project-arrow">→</span>
      <span class="project-node project-node--hardware">Mount + OnStep</span>
      <span class="project-arrow">→</span>
      <span class="project-node project-node--software">Mini PC</span>
      <span class="project-arrow">→</span>
      <span class="project-node project-node--software">CloudWatcher + 4G Link</span>
      <span class="project-arrow">→</span>
      <span class="project-node project-node--software">Reduction Pipeline</span>
      <span class="project-arrow">→</span>
      <span class="project-node project-node--data">GitHub / Public Data</span>
    </div>

    <div class="project-arch-note">
      The architecture is intentionally compact: each subsystem serves
      reproducibility, remote operability, and traceable data flow.
    </div>
  </div>
</div>

---

<h2>Observational site</h2>

<div class="project-panel">

  <div class="project-lead">
    Rural site selected for controlled, repeatable observational conditions.
  </div>

  <div class="project-map">
    <iframe
      src="https://maps.google.com/maps?q=54.9955,22.1865&z=11&output=embed"
      width="100%"
      height="360"
      style="border:0;"
      loading="lazy">
    </iframe>
  </div>

  <div class="project-grid project-grid--2" style="margin-top: 16px;">
    
    <div class="project-card">
      <strong>Sky quality</strong>
      <p>Bortle class 4–5 (estimated)</p>
    </div>

    <div class="project-card">
      <strong>Conditions</strong>
      <p>Low light pollution, stable horizon, suitable for long-term monitoring.</p>
    </div>

  </div>

  <p class="project-note">
    Approximate location shown.
  </p>

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

