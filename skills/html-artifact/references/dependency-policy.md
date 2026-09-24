# Dependency and delivery policy

Use when a renderer, build tool or runtime dependency is selected. Representation comes first: choose the capability that makes the relationship faithful, readable and reliable. Delivery cost must not silently force a weaker representation.

## Select the delivery

Tailwind is the styling foundation; the base and shipped controls use jQuery for DOM work that needs JavaScript. Default standalone documents link pinned jQuery and load pinned Tailwind from CDN; Mermaid remains conditional. These established integrations need no fresh library-selection exercise on each invocation. Reuse existing compatible host runtimes instead of loading a second copy.

| Delivery | Path | Boundary |
| --- | --- | --- |
| Standalone document (default) | Base links pinned jQuery and loads pinned Tailwind; selected diagrams load pinned Mermaid. | Disclose dependencies and retain meaningful failure content. |
| Explicit no-runtime-network constraint | Remove CDN tags; embed jQuery and compiled Tailwind CSS; render SVG locally or bundle the needed runtime. | Include asset classes and Tailwind directive blocks in compilation. No uploading private data to a conversion service. |
| Existing trusted host | Use its styling and appropriate interaction components. | Avoid duplicate runtimes and competing ownership of the same DOM. |

The base uses `connected`; `portable` and `host` select the two alternatives. Confidential source/code-review restrictions still govern remote execution. External code can inspect the document; a CDN does not remove that trust boundary. Tailwind's browser compiler is a document/prototyping convenience, not a substitute for a deployed application's production build.

Mermaid 12 requires ES2024-capable browsers, including Safari 17.4+, and Node 22.12+ for package tooling. Its ELK default changes layout from Mermaid 11. Use the supported top-level layout setting when choosing a different layout; do not rely on removed defaultRenderer settings. Static SVG avoids a viewer-side Mermaid compatibility requirement. Version pins do not prove rendering works.

## When embedded CSS is required

Use the project's supported compiler where present. For an authorised new tool installation follow the official CLI path; do not install globally or invent a build framework for one document. A v4 input imports tailwindcss and declares the actual artifact source; run the selected CLI once, then embed emitted CSS in an ordinary style element. Preserve licence notices, remove browser-runtime loading and test the final file offline. Uncompiled type=text/tailwindcss directives are not browser CSS.

Primary references: [CLI](https://tailwindcss.com/docs/installation/tailwind-cli), [Play CDN](https://tailwindcss.com/docs/installation/play-cdn), [themes](https://tailwindcss.com/docs/theme), [Mermaid 12 release](https://github.com/mermaid-js/mermaid/releases/tag/mermaid%4012.0.0). Match APIs and browser targets to the selected release. Pins live at integrations, not in an ecosystem catalogue.

## Admission and fallback

Establish exact/reproducible identity, capability gain, compatible file/HTTP environment, licence, cost, accessible meaning, data exposure and failure behaviour. Remote executable code can inspect the document; CDN popularity does not remove this trust boundary. No credentials, telemetry, unrequested data transmission or persistence. Pinning one ESM entry does not integrity-pin all transitive modules; use a locally bundled output when that stronger guarantee matters.

Use the selected delivery consistently. A no-network requirement changes dependency packaging, not the representation or utility vocabulary. A live service still requires a live-data request and a producer; document controls do not justify one.

Enhancement failure preserves base meaning. Core renderer failure retains conclusions, source, units and a readable alternative. Service failure is unavailable/stale, not empty success. Do not rebuild an entire renderer as its fallback.

## Transformations and disclosure

Preserve aggregation, binning, filters, time zones, normalisation and meaningful layout configuration. A changed transformation invalidates dependent faithfulness proof.

Report delivery shape (Single HTML or Companion bundle), runtime code (None, Embedded, Bundled or Remote), runtime data (Static or Live service) and evidence (Embedded, Linked or Mixed) independently, plus identities and proof limits.

Reconsider complexity when capabilities overlap, several renderers accumulate, remote code can inspect non-public content, or service/worker infrastructure appears solely to host a document. One focused reusable dependency can be simpler than repeated bespoke implementation.
