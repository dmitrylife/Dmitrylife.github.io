---
layout: default
title: Documentation
---

# Documentation

<p>Select a documentation version:</p>

<div id="versions">
  Loading versions…
</div>

<script>
(async () => {
  const box = document.getElementById("versions");

  try {
    const res = await fetch("/docs/versions.json", { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);

    const data = await res.json();

    const latestId = data.latest;

    const list = (data.versions || []).map(v => {
      const isLatest = v.id === latestId;
      const badge = isLatest
        ? `<strong style="color:#159957;">LATEST</strong>`
        : `<span style="opacity:0.6">${v.status}</span>`;

      return `
        <li style="margin:0.5em 0">
          <a href="${v.url}">${v.label}</a>
          &nbsp; ${badge}
        </li>
      `;
    }).join("");

    box.innerHTML = `<ul style="list-style: none; padding-left: 0">${list}</ul>`;
  } catch (e) {
    box.innerHTML = "Failed to load versions.json: " + e;
  }
})();
</script>
