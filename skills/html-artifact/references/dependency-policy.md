# Dependency and delivery policy

Use when a renderer, build tool or runtime dependency is selected. Representation comes first: choose the capability that makes the relationship faithful, readable and reliable. Delivery cost must not silently force a weaker representation.

## Authoring is not delivery

Tailwind utilities are the default ordinary composition vocabulary. The pinned browser integration is a development path, not a production deployment prescription. Mermaid is conditional. Supporting these tools does not authorise remote access to private content.

| Delivery | Suitable path | Boundary |
| --- | --- | --- |
| Connected, non-sensitive development document | Base loads Tailwind 4.3.3; optional renderer loads Mermaid 12.0.0 only for diagrams. | Disclose runtime/network dependence and preserve meaningful fallback. Not self-contained. |
| Portable, private or offline document | Compile Tailwind locally and inline CSS; render SVG locally or bundle a focused runtime. Native CSS/SVG is valid when tooling is unavailable. | No runtime network dependency. Never upload private material to a conversion service. |
| Existing trusted host | Reuse installed styling/rendering capabilities. | No duplicate framework or assumed storage permission. |

The base defaults to portable. Select connected delivery deliberately during authoring, not as an automatic fallback from a failed local build. A public-looking filename does not establish non-sensitive content. Private code review retains its stricter no-remote-executable boundary.

Mermaid 12 requires ES2024-capable browsers, including Safari 17.4+, and Node 22.12+ for package tooling. Its ELK default changes layout from Mermaid 11. Use the supported top-level layout setting when choosing a different layout; do not rely on removed defaultRenderer settings. Static SVG avoids a viewer-side Mermaid compatibility requirement. Version pins do not prove rendering works.

## Portable Tailwind path

Use the project's supported compiler where present. For an authorised new tool installation follow the official CLI path; do not install globally or invent a build framework for one document. A v4 input imports tailwindcss and declares the actual artifact source; run the selected CLI once, then embed emitted CSS in an ordinary style element. Preserve licence notices, remove browser-runtime loading and test the final file offline. Uncompiled type=text/tailwindcss directives are not browser CSS.

Primary references: [CLI](https://tailwindcss.com/docs/installation/tailwind-cli), [Play CDN](https://tailwindcss.com/docs/installation/play-cdn), [themes](https://tailwindcss.com/docs/theme), [Mermaid 12 release](https://github.com/mermaid-js/mermaid/releases/tag/mermaid%4012.0.0). Match APIs and browser targets to the selected release. Pins live at integrations, not in an ecosystem catalogue.

## Admission and fallback

Establish exact/reproducible identity, capability gain, compatible file/HTTP environment, licence, cost, accessible meaning, data exposure and failure behaviour. Remote executable code can inspect the document; CDN popularity does not remove this trust boundary. No credentials, telemetry, unrequested data transmission or persistence. Pinning one ESM entry does not integrity-pin all transitive modules; use a locally bundled output when that stronger guarantee matters.

Staticize when runtime adds no reader value. Bundle runtime for useful exploration/selection; use remote runtime only inside the declared connected profile or another explicitly authorised outcome. A live service requires a live-data request and a producer; a static file is not self-updating.

Enhancement failure preserves base meaning. Core renderer failure retains conclusions, source, units and a readable alternative. Service failure is unavailable/stale, not empty success. Do not rebuild an entire renderer as its fallback.

## Transformations and disclosure

Preserve aggregation, binning, filters, time zones, normalisation and meaningful layout configuration. A changed transformation invalidates dependent faithfulness proof.

Report delivery shape (Single HTML or Companion bundle), runtime code (None, Embedded, Bundled or Remote), runtime data (Static or Live service) and evidence (Embedded, Linked or Mixed) independently, plus identities and proof limits. Single HTML may still depend on the network.

Reconsider complexity when capabilities overlap, several renderers accumulate, remote code can inspect non-public content, or service/worker infrastructure appears solely to host a document. One focused reusable dependency can be simpler than repeated bespoke implementation.
