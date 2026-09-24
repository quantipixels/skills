---
name: html-artifact
description: Turn supplied plans, evidence, comparisons and explanations into clear, expressive, accessible HTML people can inspect and use. Support useful interaction and requested live updates. Exclude originating domain conclusions, decision prototypes, production UI and deployment.
---

# HTML Artifact

Build the browser document that helps the reader understand, compare or act on the supplied material. Preserve meaning and evidence while choosing the presentation freely.

## Shape the document

Read the current source and identify the reader's task, useful result, required coverage and material limits. Organize around that task rather than reproducing source headings. Use `fihanmi` when composition is unsettled and `oro` for substantial prose work; write incidental headings and faithful short summaries directly.

Lead with the outcome and consequential qualifications. Keep blockers, uncertainty and opposing evidence visible where they affect judgment; a bare source link cannot replace critical meaning. Link detailed evidence without copying raw archives. Preserve source identities and revisions, mark stale or incompatible inputs, and distinguish observations, proposals, verdicts, confidence and readiness. Do not invent conclusions, scores or relationships.

Choose forms by the relationship: aligned tables or specimens for comparison, diagrams for connected structure, plots for quantities, and prose or lists when sufficient. Preserve units, scales, transformations and labels. Do not imply causality from sequence or measured magnitude from decorative size. Generate diagrams for the actual material; no fixed recipe, layout or chart quota is required.

For a maintained document, keep its identity and useful anchors, reconcile summary and detail, and foreground material changes. Update an Atọ́nà HTML plan in place without an equivalent Markdown copy. Use an optional [manifest](references/manifest.md) when machine-readable identity and source revisions aid retrieval.

## Build only useful mechanics

Start from [base.html](assets/base.html), adapting its layout and illustrative content. Use Tailwind for styling and state variants, native HTML for built-in behavior, the existing jQuery runtime for needed DOM work, and plain JavaScript for calculations. Reuse project branding or the supplied QP mark. For host, offline or additional dependency choices, read [dependency policy](references/dependency-policy.md).

Reuse a shipped control when its contract fits; each asset's comment defines its inputs and fallback:

- [view control](assets/view-control.html): details, aligned comparisons or finite steps;
- [collection filter](assets/collection-filter-control.html): category/text filtering with count, reset and empty state;
- [carousel](assets/carousel-control.html): sequential visual collections;
- [report control](assets/report-control.html): reveal fragment targets and expand required print content;
- [Mermaid renderer](assets/renderer-control.html): conditional diagram rendering with source and explanation fallback.

For Mermaid, use a labelled figure containing `pre.mermaid`, `div[data-diagram-output]`, `p[data-diagram-status]` and a readable explanation. Render while visible, retain strict security and avoid coupling controls to generated SVG internals. Use locally rendered SVG for portable diagrams. Check current syntax when unfamiliar rather than retaining a recipe catalogue.

Prefer native elements or compatible host components for other controls. Add a focused library only when it earns its dependency; resolve its current API and licence at use time. Keep one behavior owner per control.

## Keep interaction trustworthy

Interaction must help the reader compare, inspect, follow, filter or explore a supplied model. Keep comparisons understandable without memorising hidden alternatives. Model controls need labelled inputs, units, baseline/reset and a known result; calculated illustrations are distinct from observations.

Keep reader state ephemeral: no browser storage, cookies, saved URL selections, files or service writes by default. Ordinary clicked anchors remain navigation. Feedback, approval, exports and persistence require an explicit request; persistence also needs a named lifetime, destination and reset/removal behavior. A reader action never silently changes an accepted decision.

Treat supplied content as data and escape it for the HTML, JSON or SVG context. Private code-review documents must not load remote executable code. Send no credentials, analytics or unrequested data. Keep local assets embedded or in the declared companion bundle.

Preserve semantic reading order, keyboard/focus, touch operation, contrast, non-colour cues, reduced motion and print meaning. Essential information must survive script failure; show controls only when ready. Filtering needs count/reset/no-match, and must not leave focus in hidden content. Use labelled overflow regions for wide tables and code.

Read [code-change review](references/code-change-review.md) for exact patch views, or [living and live views](references/living-and-live.md) when updates arrive while the document is open.

## Verify and deliver

Run `python3 <skill-directory>/scripts/verify_artifact.py <artifact.html>`. Fix definite defects and inspect warnings; this checks structure, not source truth, visual quality, security or accessibility certification.

Check source identity, critical coverage, provenance, navigation and fallback. Render a static page when readability is uncertain. Exercise introduced interactions, keyboard/focus, reset, no-match, known model results and relevant print/reload behavior. Check a layout breakpoint when its behavior matters. A renderer stub does not prove real-library rendering. Reuse valid proof and report unavailable browser checks honestly.

Write to the requested destination, otherwise `.qp/artifacts/<stable-subject>/index.html`. Return the real locator and decisive verification, noting unresolved limits. Disclose whether delivery is one HTML file or a companion bundle, runtime code is embedded/bundled/remote, data is static/live and evidence is embedded/linked. Keep dependency details in a quiet technical disclosure.

Open only when requested or needed for render proof; reuse an existing preview. Finish when the reader can understand, inspect and use the requested result.
