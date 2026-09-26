# Dependency and delivery policy

Read before constructing standalone HTML, and when selecting host delivery, a renderer, build tool or runtime dependency. Representation comes first: choose the capability that makes the relationship faithful, readable and reliable. Delivery cost must not silently force a weaker representation.

## Select the delivery

The standalone default is the base shell with Basecoat's precompiled standalone CSS. Apply the construction and substitution rules in [HTML Artifact](../../../commands/html-artifact.md); choose the least complex behavior within that path. Basecoat's CSS-only components need no Basecoat JavaScript. Retain jQuery only for behaviors that use it; native HTML can provide built-in behavior. Mermaid remains conditional. Reuse compatible host runtimes instead of loading a second copy.

| Delivery | Path | Boundary |
| --- | --- | --- |
| Connected standalone document | Base links pinned Basecoat CSS; retain jQuery and load pinned Mermaid only for selected behaviors. | Disclose dependencies and retain meaningful failure content. |
| Portable or no-runtime-network document | Keep the base and replace CDN tags with the pinned precompiled Basecoat standalone stylesheet and any needed jQuery file, embedded or in a declared companion bundle; render SVG locally or bundle the needed renderer. | Preserve Basecoat's licence and source identity. No uploading private data to a conversion service. |
| Existing trusted host | Use its styling and appropriate interaction components. | Avoid duplicate runtimes and competing ownership of the same DOM. |

The base declares `data-artifact-delivery="connected"` on `html`; set `portable` or `host` for those delivery paths. A replacement document uses the same attribute. Confidential source/code-review restrictions still govern remote execution. External code can inspect the document; a CDN does not remove that trust boundary. Basecoat's npm source installation uses a Tailwind build step, so this artifact path uses its standalone precompiled distribution without a Tailwind compiler or direct Tailwind dependency.

Mermaid 12 requires ES2024-capable browsers, including Safari 17.4+, and Node 22.12+ for package tooling. Its ELK default changes layout from Mermaid 11. Use the supported top-level layout setting when choosing a different layout; do not rely on removed defaultRenderer settings. Static SVG avoids a viewer-side Mermaid compatibility requirement. Version pins do not prove rendering works.

## When embedded CSS is required

For a portable single file, obtain the pinned `basecoat.cdn.min.css` distribution, embed its contents in an ordinary style element before the base's scoped CSS, and remove the CDN link. Include the distribution's licence notice. If controls need jQuery, embed its selected distribution after the styles; a static document may omit it. Test the final file offline. Do not copy source imports or introduce a Tailwind build step for this path.

Primary references: [Basecoat installation](https://basecoatui.com/installation/), [Basecoat customization](https://basecoatui.com/customization/), [Mermaid 12 release](https://github.com/mermaid-js/mermaid/releases/tag/mermaid%4012.0.0). Match APIs and browser targets to the selected release. Pins live at integrations, not in an ecosystem catalogue.

## Fonts

Apply the command's Google Fonts default and user/host exceptions. For connected delivery, use the [Google Fonts CSS API](https://developers.google.com/fonts/docs/css2), request only selected families/weights and use `display=swap` with a suitable fallback. Keep private document text out of font requests, including the `text=` parameter. Confirm the chosen family loads and supports the actual text.

For portable or no-network delivery, obtain the selected font files, embed them in the single HTML or bundle them with local `@font-face` rules, and remove Google stylesheet links and other font network references. Preserve the font licence and source identity; record the selected file/version identity when packaging it. The base's Source Sans 3 is a working specimen, not a universal font recommendation. Update its family, requested weights and delivery disclosure together when adapting it.

## Admission and fallback

Establish exact/reproducible identity, capability gain, compatible file/HTTP environment, licence, cost, accessible meaning, data exposure and failure behaviour. Remote executable code can inspect the document; CDN popularity does not remove this trust boundary. No credentials, telemetry, unrequested data transmission or persistence. Pinning one ESM entry does not integrity-pin all transitive modules; use a locally bundled output when that stronger guarantee matters.

Use the selected delivery consistently. A no-network requirement changes dependency packaging, not the representation or component semantics. A live service still requires a live-data request and a producer; document controls do not justify one.

Enhancement failure preserves base meaning. Core renderer failure retains conclusions, source, units and a readable alternative. Service failure is unavailable/stale, not empty success. Do not rebuild an entire renderer as its fallback.

## Transformations and disclosure

Preserve aggregation, binning, filters, time zones, normalisation and meaningful layout configuration. A changed transformation invalidates dependent faithfulness proof.

Report delivery shape (Single HTML or Companion bundle), runtime code (None, Embedded, Bundled or Remote), runtime data (Static or Live service) and evidence (Embedded, Linked or Mixed) independently, plus selected dependency identities and proof limits. Declare `None` when the document has no runtime code; do not infer a base dependency from the artifact type.

Reconsider complexity when capabilities overlap, several renderers accumulate, remote code can inspect non-public content, or service/worker infrastructure appears solely to host a document. One focused reusable dependency can be simpler than repeated bespoke implementation.
