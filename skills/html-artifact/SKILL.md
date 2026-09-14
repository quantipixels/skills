---
name: html-artifact
description: Turn supplied material into a selective, traceable, accessible static or interactive browser information projection. Preserve source meaning, authority, evidence state, and retrieval paths; exclude originating analysis, slide decks, decision prototypes, production/application UI, deployments, and reusable libraries.
---

# HTML Artifact

Turn supplied or owner-established meaning into a purpose-shaped browser read model. Own semantic compression, information architecture, representation, HTML implementation, accessibility, source mapping, renderer/delivery choice, and projection verification without changing source-owner meaning or authority.

## Projection contract

**Output:** requested/host destination; otherwise `.qp/artifacts/<stable-subject>/index.html`. Use temp for disposable intermediates.

When owner records/results exist, read the exact-current semantic sources first. Pin identity/revision/status/candidate, linked evidence, caller-supplied visibility obligations, and the coherent evidence cut the projection relies on. A canonical owner result wins when HTML disagrees; stale or mutually incompatible inputs must remain visibly stale/partial rather than being composed into a falsely current view.

For substantial/evidence-heavy/living/reused/owner-record input, read [source composition](references/source-composition.md). Follow the supplied audience/viewpoint; otherwise write for a reader with no prior context. Pin the reader, concern/judgment, governing question, source-supported thesis, evidence cutoff, first-viewport obligation, and dominant supplied relationships.

Request only missing structure that can change truth/usefulness. Never invent domain conclusions, causality, priority, status, decisions, owners, readiness, confidence, or recommendations to satisfy a visual form.

Load branch guidance only when applicable:

- report/evidence/living/candidate comparison → [report patterns](references/report-patterns.md);
- diff, commit/branch change, or pinned pull-request or merge-request evidence → [code-change review](references/code-change-review.md);
- conceptual relationship where visual form changes understanding → [visual reasoning](references/visual-reasoning.md);
- a mature renderer/tool could materially improve the chosen representation → [representation capabilities](references/representation-capabilities.md);
- interactive relationship map, coordinated perspectives, or guided sequence → [interactive projections](references/interactive-projections.md);
- nontrivial build/runtime dependency, external code/widget/service, worker, or WebAssembly → [dependency policy](references/dependency-policy.md).

## Compose for human judgment

Establish required coverage before minimizing representation. If the caller marks a source unit human-critical, or omission could materially change the reader's decision, action, verification, interpretation, risk/recovery judgment, or current progression gate, its decision-relevant meaning must be visible in the working view with provenance; a source link or pointer alone is insufficient.

For plans and decision views, show the problem, direction, rationale, settled/open choices, progress, and next action without assuming prior project or chat context. Use `oro` in its human-facing branch for reader calibration; return missing source meaning to its owner.

Choose representation per material relationship or reader question, not per source heading. Several source sections may collapse into one useful traceability/comparison view; one source section may require several representations when it contains different relationships.

Use `oro`'s visual-explanation branch for clearer representations within relevant sections. Apply its guidance beside the supported text/evidence; this is not a new artifact request.

Keep semantic types distinct. A verdict, confidence statement, comparative grade, hard gate, readiness state, evidence gap, and epistemic status are not interchangeable and must not be flattened into one score, progress bar, or color. Qualitative judgment gets no false precision.

Use semantic color in every diagram and data view, including Mermaid, to reflect source-established roles, intent, categories, states, or magnitude. Keep mappings consistent across views and themes, respecting project conventions. Choose categorical, sequential, or diverging palettes to suit the data. Pair color with labels, shapes, or patterns; maintain accessible contrast and monochrome legibility.

For living projections, preserve document identity and useful anchors. Foreground material change and its consequences while retaining enough context for a new reader. Recompute the reader job after stage changes; [source composition](references/source-composition.md) governs source freshness and updates.

## Choose representation before renderer or delivery

Choose the faithful representation before the renderer, then use the lightest sound delivery mode.

The linked capabilities are starting points, not an allowlist. Discover a mature alternative when the supplied anchors cannot represent the meaning well.

Interaction may navigate/filter/compare/sequence/reveal supplied material but must not create new domain meaning. Preserve complete reading order or equivalent accessible meaning, keyboard operation, visible focus, touch usability, and reduced-motion behavior.

## Standalone support

Start standalone artifacts from the [base template](assets/base.html). Preserve its embedded branding and accessible controls, including the always-visible, bottom-right back-to-top button. Set the title, language and control labels; build the representation inside `main`. Use an existing host shell or supplied branding when present.

Add the [report control](assets/report-control.html), [collection filter control](assets/collection-filter-control.html), or [carousel control](assets/carousel-control.html) only when that asset's own trigger applies; read only the selected asset before embedding it.

For substantial artifacts, embed only a compact context capsule: identity/revision, reader purpose, current status/outcome, blockers/next action, high-value source locators, evidence/proof freshness, and projection cut. Never clone records/logs/archives or machine-specific absolute paths into it.

## Runtime boundaries

Treat supplied content as data, never executable markup. Send no credentials. Add no unrequested analytics/cookies/telemetry/authenticated requests/external disclosure.

Representation choice and delivery choice are separate. A selected renderer may be staticized at build time, bundled as a focused runtime, reused from an existing trusted host runtime, or exceptionally loaded remotely when the requested outcome genuinely requires that behavior and the trust/data/failure boundary is explicit. Use [dependency policy](references/dependency-policy.md) for any nontrivial dependency/runtime.

Report independently:

```text
Delivery shape: Single HTML | Companion bundle
Runtime code: None | Embedded | Bundled | Remote
Runtime data: Static | Live service
Evidence: Embedded | Linked | Mixed
```

## Verification

Before delivery, check the current source/projection identity, human-critical coverage, opening/status, navigation, provenance, renderer/dependency identity, semantic color and non-color cues, contrast, runtime disclosure, and fallback. After changes, rerun only invalidated checks; reuse proof that remains current.

Check that the view alone explains the supplied direction and current state to its intended reader. Repair opaque explanations; distinguish this assessment from observed reader comprehension or agreement.

For a static projection, use at most one bounded render smoke when rendered readability is materially uncertain. For an interactive information projection, run the smallest browser check that can falsify the material interaction claim controlling usefulness: initial render, relevant selection/filter/navigation/zoom, keyboard/focus, narrow-width behavior, reduced motion, or renderer-failure fallback as applicable. Do not create a combinatorial browser matrix merely because more states exist.

Document size, lifespan or renderer choice alone does not justify deeper browser testing.

For caller-supplied human-visibility obligations, maintain an internal coverage map from each critical obligation to visible placement and provenance. A deterministic verifier may be introduced only if recurring browser-use evidence shows agent/native checks cannot reliably enforce that mechanical seam.

## Deliver

Return the verified artifact locator.

Open only when requested or needed for render proof; reuse and refresh the existing preview instead of opening repeated tabs.

Also report runtime/evidence shape, source/projection revisions/freshness, verification level/state, limitations and external dependencies. Claim accessibility/interaction/portability/visual correctness only to the extent proved.
