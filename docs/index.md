---
layout: default
title: Documentation
---

# Documentation

<p>Select a documentation version:</p>

<div id="versions" aria-live="polite">
<ul aria-label="Documentation versions">
  <li><a href="{{ '/docs/v5/' | relative_url }}">v5 — State-Space diagnostics</a></li>
  <li><a href="{{ '/docs/v2/' | relative_url }}">v2 — archived cosmology documentation</a></li>
</ul>
</div>

<script>
(async () => {
  const box = document.getElementById("versions");

  try {
    const res = await fetch("/docs/versions.json", { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);

    const data = await res.json();

    const list = (data.versions || []).map(v => {

      let badge;

      if (v.id === "v5") {
        badge = `<strong style="color:#159957;">CONSOLIDATED</strong>`;
      } else {
        badge = `<span style="opacity:0.6">${v.status}</span>`;
      }

      return `
        <li style="margin:0.5em 0">
          <a href="${v.url}">${v.label}</a>
          &nbsp; ${badge}
        </li>
      `;
    }).join("");

    box.innerHTML = `<ul style="list-style:none; padding-left:0">${list}</ul>`;
  } catch (e) {
    // Keep the static version links if metadata cannot be loaded.
  }
})();
</script>

<div style="
  margin-top: 2em;
  padding: 1.1em 1.3em;
  border-left: 4px solid #159957;
  background: #f7f9f9;
">

<strong>v2 audit notice — September 2026</strong>

<p style="margin-bottom:0.6em;">
  The frozen v2 release remains available as an archival scientific record.
  An independent audit confirmed internal numerical reproducibility of the
  archived pipeline while identifying a model–implementation mismatch for
  non-zero response amplitude.
</p>

<p style="margin-bottom:0;">
  The original v2 software and archived scientific results remain preserved;
  documentation now includes contextual audit notices.
  <a href="https://github.com/dmitrylife/psi-continuum-v2-audit"
     target="_blank"
     rel="noopener noreferrer">
    View independent audit →
  </a>
</p>

</div>
