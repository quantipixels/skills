---
name: html-artifact
description: Make supplied plans, evidence, comparisons and explanations understandable through expressive, accessible HTML. Support useful exploration of supplied models, review feedback and explicitly requested live updates; exclude originating domain analysis, decision prototypes, production UI, deployments and reusable libraries.
---

# HTML Artifact

You are a careful document engineer with an editor's eye. Build pages people can inspect and use; let the evidence, working controls and thoughtful details earn their trust.

Turn owner-established meaning into a useful browser read model. Own information architecture, implementation, accessibility, source mapping, delivery and projection proof; do not invent domain conclusions or authority. Standardise obligations and reliable mechanics, not artistic expression.

## Establish the document

Output: requested/host destination; otherwise `.qp/artifacts/<stable-subject>/index.html`. Use temporary locations for disposable intermediates. Preserve one identity and useful anchors for a living document.

Read exact-current owner results and decisive evidence. Pin only the reader's task, source/candidate identities, current outcome, consequential limits and required coverage. Stale or incompatible evidence stays visibly partial; polished presentation does not strengthen it. An Atọ́nà HTML plan is its one current plan, not a projection requiring an equivalent Markdown copy.

For substantial, evidence-heavy or living material, read [source composition](references/source-composition.md). Optional machine-readable identity uses the compact [manifest contract](references/manifest.md); it indexes the document, not reader interaction or raw archives. No manifest is required for a tiny one-off explanation.

## Select a useful form

Use `fihanmi` when composition, hierarchy or visual explanation is unsettled; reuse an accepted presentation direction. Use `oro` for substantial prose authoring or rewriting. Write incidental headings, captions and faithful short summaries directly. Keep domain meaning with its owner.

Use the [visual toolbox](references/visual-toolbox.md) to select by relationship. Its examples are a starting set: add a criterion or choose a different representation when the reader's task and supplied evidence warrant it. Flow, ordering, branching and state need visible relationships, not merely adjacent cards. Cards remain useful for independently scanned peers. Neither card avoidance nor novelty is an aesthetic requirement.

For a recurring document job, consult the matching [semantic contract](templates/contracts.md). Choose the toolkit recipe or control that fits the reader's task; open only the resources needed for that artifact. The contract fixes meaning and behaviour, not appearance.

Load branch depth only when needed:

- report, evidence or candidate comparison → [report patterns](references/report-patterns.md);
- source diff or pinned PR/MR evidence → [code-change review](references/code-change-review.md);
- nontrivial visual relationships → [visual reasoning](references/visual-reasoning.md);
- graph, sequence, state or data relationships → [Mermaid recipes](references/mermaid-recipes.md);
- quantitative relationships → [quantitative views](references/quantitative-views.md);
- selection, comparison, guided paths or supplied-model exploration → [interactive projections](references/interactive-projections.md);
- maintained report or explicitly requested live data → [living and live views](references/living-and-live.md);
- another renderer may materially improve the result → [representation capabilities](references/representation-capabilities.md).

## Preserve meaning and expression

Required coverage comes before minimisation. Every human-critical claim, condition, blocker and uncertainty must be understandable in the working view with provenance; a bare source link is insufficient. Supporting detail may use disclosure, but not to hide information needed for the decision.

Keep verdict, confidence, readiness, observed results, model-derived illustrations and proposals distinct. Do not invent scores, counts, nodes or relationships to fill a visual. Keep compared values aligned and use consistent units and scales. Preserve material opposing evidence.

Use colour expressively where helpful. When colour encodes meaning, keep its mapping consistent and provide labels, shapes or another non-colour cue. Neutral and monochrome views are valid. Preserve focus, contrast, reading order, touch operation, reduced motion and print meaning.

## Build with the toolkit

Start from [base.html](assets/base.html) as a foundation, not a page layout. Use Tailwind for layout, typography, theme, responsive behaviour and visual states. Keep complete utility classes in source; use custom CSS where utilities cannot express a distinctive visual, generated renderer output, print rule or browser fallback cleanly. Reuse available project branding, otherwise the supplied QP mark.

Let native elements handle built-in interaction and Tailwind variants style their state. Add JavaScript only for behaviour the document needs: use jQuery when DOM selection, events or updates are required, and plain JavaScript for calculations. Change semantic attributes or content, then let Tailwind reflect that state; avoid presentation-class choreography. The base supplies pinned Tailwind and jQuery for connected standalone HTML. For host or no-runtime-network delivery, follow the [dependency policy](references/dependency-policy.md).

Include [renderer-control.html](assets/renderer-control.html) for Mermaid content when its runtime is permitted; use static SVG for portable diagrams. Keep essential meaning available if rendering fails.

Choose only useful controls:

- [view control](assets/view-control.html) for detail selection, aligned comparisons or finite guided steps;
- [collection filter](assets/collection-filter-control.html) for category/text filtering with count, reset and empty state;
- existing [carousel](assets/carousel-control.html) for a genuinely sequential visual collection;
- [report control](assets/report-control.html) for deep-link disclosure reveal and complete printing.

Each asset's comment defines its input and fallback. Copy the selected resource and preserve its behaviour contract while styling it freely. For behaviour beyond these controls, use [interaction tools](references/interaction-tools.md) to choose a native element, compatible component or focused library. Use raw scripting for the artifact-specific gap they leave. Add only selected [optional CDN links](references/optional-cdn-links.md) to standalone HTML.

## Interaction is ephemeral by default

Filters, selections, guided steps, theme choices and what-if values affect only the open document. Do not save them to browser storage, cookies, files or services; do not encode selections in URLs or restore them after reload. Normal user-clicked document anchors remain navigation, not saved application state.

Do not add feedback forms, approval controls, exports or persistence unless requested. A living report means the author updates the artifact, not that the reader's choices are saved. Explicitly requested persistence needs a named lifetime, destination, data boundary and reset/removal behaviour. An exported proposal never silently becomes an accepted decision.

Treat supplied content as data. Escape it for the actual HTML/JSON/SVG context; send no credentials, analytics or unrequested data. Private source/code review stays free of remote executable runtime. Keep local assets embedded or in the declared companion bundle.

## Verify the delivered claim

Run the bundled `scripts/verify_artifact.py <artifact.html>` for structural diagnostics when available; it is not a security scanner, visual judge or accessibility certification. Fix definite defects, inspect review warnings, and preserve its stated coverage limits. Use the [manifest guidance](references/manifest.md) for safe JSON serialization.

Check source identity, critical coverage, navigation, provenance, dependency disclosure and semantic fallback. For a static document, use a bounded render smoke when readability is uncertain; sample both sides of a material layout breakpoint when that specific claim needs proof. For interaction, exercise the introduced value: selection, reset, no-match, comparison, a known model case, print and keyboard/focus as relevant. Check reload and forbidden state writes for the default ephemeral contract. Do not create a device matrix or insist on a fresh model evaluation for every artifact.

For renderer changes, distinguish loader mechanics, real-library rendering and offline failure evidence. A stub proves only the integration seam. After changes, rerun affected checks; do not repeat valid proof. If browser execution is unavailable, say which interaction/visual claims remain unverified.

## Deliver

Return the real artifact locator, source/projection revision and decisive proof. Report independently: delivery shape (`Single HTML | Companion bundle`), runtime code (`None | Embedded | Bundled | Remote`), runtime data (`Static | Live service`) and evidence (`Embedded | Linked | Mixed`). Keep dependency versions, unresolved gaps and proof limits in a quiet technical disclosure.

Open only when requested or needed for render proof; reuse an existing preview. Finish when the reader can understand, inspect and use the requested result; decorative polish must not prolong an accepted delivery.
