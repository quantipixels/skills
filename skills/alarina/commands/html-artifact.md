# HTML Artifact

Build the browser document that helps the reader understand, compare or act on the supplied material. Preserve meaning and evidence while choosing the presentation freely.

## Shape the document

Read the current source and identify the reader's task, useful result, required coverage and material limits. Organize around that task rather than reproducing source headings. For a new or materially recomposed artifact, read [fihanmi](fihanmi.md) before settling the layout; reuse its current guidance for minor updates. Use [oro-eniyan](oro-eniyan.md) for substantial prose work; write incidental headings and faithful short summaries directly.

Lead with the outcome and consequential qualifications. Keep blockers, uncertainty and opposing evidence visible where they affect judgment; a bare source link cannot replace critical meaning. Link detailed evidence without copying raw archives. Preserve source identities and revisions, mark stale or incompatible inputs, and distinguish observations, proposals, verdicts, confidence and readiness. Do not invent conclusions, scores or relationships.

Choose forms by the relationship: aligned tables or specimens for comparison, diagrams for connected structure, plots for quantities, and prose or lists when sufficient. Preserve units, scales, transformations and labels. Do not imply causality from sequence or measured magnitude from decorative size. Generate diagrams for the actual material; no fixed recipe, layout or chart quota is required.

For a maintained document, keep its identity and useful anchors, reconcile summary and detail, and foreground material changes. When Atọ́nà uses HTML for its plan, update that plan in place without an equivalent Markdown copy. Use an optional [manifest](../references/design/html/manifest.md) when machine-readable identity and source revisions aid retrieval.

## Build only useful mechanics

For standalone HTML, read [base.html](../references/design/html/assets/base.html) and the [dependency policy](../references/design/html/dependency-policy.md) before construction. Adapt the base and use Basecoat's precompiled standalone CSS by default. Layout, typography and content remain a free canvas; illustrative sections are not required. Keep native HTML for built-in behavior and plain JavaScript for calculations. Load jQuery only for retained behaviors that need it; Mermaid and other renderers remain conditional.

Standalone defaults include the inline [QP SVG mark](../references/design/html/assets/brand.svg) and footer attribution to Oluwaseyi Sobande / Quanti Pixels. Retain them unless the user explicitly directs different branding or attribution. Preserve the base's system-theme support, keyboard/focus behavior, navigation, overflow handling and print meaning unless the task calls for a specific adaptation. A static artifact can follow the system theme with CSS and omit the scripted theme toggle. A containing application's established design system takes precedence over the standalone shell.

Select suitable typography from [Google Fonts](https://fonts.google.com/) by default for standalone artifacts. Choose for the document's reading density, tone, language/glyph coverage and required weights; the base's sample family is not the answer for every use case. Use another source or system fonts when the user explicitly chooses them or opts out; a containing host keeps its established typography. Package fonts for the selected delivery through the dependency policy and keep a readable fallback.

Replace a default when explicit user direction or a concrete task/host constraint makes it unsuitable. Inspect the asset first, then state the reason and which applicable behavior the replacement preserves or intentionally changes; a short construction note is sufficient. A simple report, offline delivery or fewer browser checks alone does not justify rebuilding shared mechanics. A different path must preserve meaning, accessibility, privacy, fallback and the delivery contract. For host-contained artifacts, read the dependency policy and reuse the host's capabilities.

Declare the selected delivery on the document root as `data-artifact-delivery="portable"`, `"connected"` or `"host"`, including when replacing the base. Portable delivery embeds or bundles required assets; it does not require abandoning Basecoat or the shell.

Reuse a shipped control when its contract fits; each asset's comment defines its inputs and fallback:

- [view control](../references/design/html/assets/view-control.html): details, aligned comparisons or finite steps;
- [collection filter](../references/design/html/assets/collection-filter-control.html): category/text filtering with count, reset and empty state;
- [carousel](../references/design/html/assets/carousel-control.html): sequential visual collections;
- [report control](../references/design/html/assets/report-control.html): reveal fragment targets and expand required print content;
- [Mermaid renderer](../references/design/html/assets/renderer-control.html): conditional diagram rendering with source and explanation fallback.

For Mermaid, use a labelled figure containing `pre.mermaid`, `div[data-diagram-output]`, `p[data-diagram-status]` and a readable explanation. Render while visible, retain strict security and avoid coupling controls to generated SVG internals. Use locally rendered SVG for portable diagrams. Check current syntax when unfamiliar rather than retaining a recipe catalogue.

Prefer native elements or compatible host components for other controls. Add a focused library only when it earns its dependency; resolve its current API and licence at use time. Keep one behavior owner per control.

## Keep interaction trustworthy

Interaction must help the reader compare, inspect, follow, filter or explore a supplied model. Keep comparisons understandable without memorising hidden alternatives. Model controls need labelled inputs, units, baseline/reset and a known result; calculated illustrations are distinct from observations.

Keep reader state ephemeral: no browser storage, cookies, saved URL selections, files or service writes by default. Ordinary clicked anchors remain navigation. Feedback, approval, exports and persistence require an explicit request; persistence also needs a named lifetime, destination and reset/removal behavior. A reader action never silently changes an accepted decision.

Treat supplied content as data and escape it for the HTML, JSON or SVG context. Private code-review documents must not load remote executable code. Send no credentials, analytics or unrequested data. Keep local assets embedded or in the declared companion bundle.

Preserve semantic reading order, keyboard/focus, touch operation, contrast, non-colour cues, reduced motion and print meaning. Essential information must survive script failure; show controls only when ready. Filtering needs count/reset/no-match, and must not leave focus in hidden content. Use labelled overflow regions for wide tables and code.

Read [code-change review](../references/design/html/code-change-review.md) for exact patch views, or [living and live views](../references/design/html/living-and-live.md) when updates arrive while the document is open.

## Verify and deliver

Run `python3 <alarina-directory>/scripts/verify_artifact.py <artifact.html>`, resolving `<alarina-directory>` from the loaded Alárinà `SKILL.md`. Confirm its reported delivery profile matches the intended artifact. Fix definite defects and inspect warnings; this checks structure, not source truth, visual quality, security or accessibility certification.

Check source identity, critical coverage, provenance, navigation and fallback. Render a static page when readability is uncertain. Exercise introduced interactions, keyboard/focus, reset, no-match, known model results and relevant print/reload behavior. Check a layout breakpoint when its behavior matters. A renderer stub does not prove real-library rendering. Reuse valid proof and report unavailable browser checks honestly.

Write to the requested or established visible destination. Otherwise choose a reviewable destination through [records](../references/productivity/records.md), and return its real locator and decisive verification, noting unresolved limits. Carry any material departure from the defaults and its preserved behavior into that handoff. Disclose whether delivery is one HTML file or a companion bundle, runtime code is embedded/bundled/remote, data is static/live and evidence is embedded/linked. Keep dependency details in a quiet technical disclosure.

Open only when requested or needed for render proof; reuse an existing preview. Finish when the reader can understand, inspect and use the requested result with accepting proof for its actual delivery and interactions. A disclosed limit does not complete a missing required check or required content; resolve that gap or report the artifact as incomplete.
