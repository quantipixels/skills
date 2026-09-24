# Optional CDN links for standalone HTML

Copy only the entry an artifact uses into its HTML; remove unused entries before delivery. These are ready-to-use static-site URLs, not default dependencies. The versions below were current on 2026-09-24. Recheck a version when updating an integration, and keep the delivered URL exact rather than using `@latest`. The base already links jQuery 4.0.0.

## Alpine — 3.17.4

Use for several linked transient values when native controls and the shipped assets are insufficient. `defer` lets Alpine initialize after the document has been parsed.

```html
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.17.4/dist/cdn.min.js"></script>
```

## Observable Plot — 0.6.17

Use inside the module that builds an actual chart. The CDN ESM endpoint may load transitive modules; the exact Plot version does not pin every transitive URL.

```html
<script type="module">
  import * as Plot from "https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6.17/+esm";
  // Render a chart from supplied data and insert it into the document.
</script>
```

## D3 — 7.9.0

Use for a supplied data relationship needing bespoke marks, layout or interaction beyond Plot. The CDN ESM endpoint may load transitive modules; the exact D3 version does not pin every transitive URL.

```html
<script type="module">
  import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7.9.0/+esm";
  // Build the view from supplied data and insert it into the document.
</script>
```

## Mermaid — 12.0.0

For actual diagrams, copy [renderer-control.html](../assets/renderer-control.html). It already contains the conditional CDN import and the source/explanation fallback. Do not add a second Mermaid tag.

Tailwind is already loaded by [base.html](../assets/base.html) in connected mode. Tailwind Plus Elements requires a separate commercial licence; Headless UI belongs to an existing React/Vue host. Neither is a default standalone asset.
