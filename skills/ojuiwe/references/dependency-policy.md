# Dependency and delivery policy

The default is zero runtime dependencies. Embed a small QP stylesheet, plain JavaScript controls, inline SVG and any images in one HTML file. No CDN, webfont, build step or DOM library is needed. The bundled Markdown converter uses Python's standard library only.

## When a dependency earns its place

A selected dependency supplies a capability that is unreasonable to implement in plain CSS/JS for this page. Name that capability, the exact pinned version, its licence and browser/file compatibility, its exposure to page data, and the useful result that remains offline. Load it only on the page that uses it. A familiar library or the presence of a chart is not enough.

| Capability | Default | Explicit opt-in |
| --- | --- | --- |
| Style and controls | Inline QP CSS and plain JS assets | Use an existing trusted host without duplicate ownership |
| Small bars, lines, sparklines, timelines | Inline SVG; chart numbers also in text/table | Chart.js for large or heavily interactive data |
| HTML diagram | Inline SVG | Mermaid for a large diagram needing automatic layout |

Pinned optional builds: Chart.js `4.5.1` at `https://cdn.jsdelivr.net/npm/chart.js@4.5.1/dist/chart.umd.min.js`; Mermaid `12.1.0` at `https://cdn.jsdelivr.net/npm/mermaid@12.1.0/dist/mermaid.min.js`. These pins retain reproducible integration identity; they are not a claim that a runtime has been tested on the current page. Basecoat and jQuery are removed.

## Delivery boundary

- Default pages, generated documents and kept/shared files use `data-artifact-delivery="portable"`. Inline everything; ordinary hyperlinks to sources are fine. No active resource may depend on the network or another local file.
- An explicitly selected disposable connected preview uses `connected`. Disclose remote code and retain meaningful source/data if it fails. External executable code can inspect the whole page, so a private review page loads none.
- A committed page contains no remote runtime. Inline any justified library's pinned bytes if still needed; render Mermaid once to SVG, inline the SVG and remove its runtime. Commit Markdown as the authored document; HTML is generated on demand and committed only when sharing the file requires it.
- A trusted application may supply a `host` delivery. Reuse its capabilities without introducing a second framework.

The default chart control never fetches Chart.js. The Mermaid asset loads only for `connected` delivery and figures marked `data-mermaid-opt-in="true"`. `md_to_html.py --mermaid` is an explicit disposable-preview choice; without it, the fence is escaped diagram source with a rendering-off note.

## Renderer conditions

A Chart.js opt-in keeps the numbers and units in nearby text/table, gives the chart a fixed pixel height, and resolves QP CSS colours into colours the library accepts. A Mermaid opt-in uses strict mode, rejects embedded configuration and retains source and an explanation on failure. Render visible diagrams before hiding their panel. For saved diagrams, include a textual relationship summary as well as the static SVG.

Use a classic pinned script and draw after its load completes. Log `ready` after the real render, inspect browser errors and prove the actual renderer; a stub does not establish rendering. Preserve filters, aggregation, units, time zones and other transformations. Revisit them when the source changes.

Report runtime code (none, embedded or remote), runtime data (static or live), and evidence (embedded or linked) separately. A dependency does not justify analytics, persistence or a data service. Failure preserves the report's meaning and marks a live service stale/unavailable instead of empty success.
