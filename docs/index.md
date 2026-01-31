---
layout: default
title: Documentation
---

# Documentation

<div id="versions">Loading versions…</div>

<script>
(async () => {
  const box = document.getElementById("versions");

  try {
    // ВАЖНО: абсолютный путь, а не ./versions.json
    const res = await fetch("/docs/versions.json", { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);

    const data = await res.json();

    // 1) Авто-переход на latest (если хочешь)
    if (data.latest) {
      const latest = data.versions?.find(v => v.id === data.latest) || data.versions?.[0];
      if (latest?.url) {
        // Можно закомментировать редирект, если хочешь показывать список
        window.location.replace(latest.url);
        return;
      }
    }

    // 2) Если не редиректим — показываем список
    const items = (data.versions || [])
      .map(v => `<li><a href="${v.url}">${v.label}</a> <small>(${v.status})</small></li>`)
      .join("");

    box.innerHTML = `<ul>${items}</ul>`;
  } catch (e) {
    box.innerHTML = "Failed to load /docs/versions.json: " + e;
  }
})();
</script>
