---
name: html-artifact
description: Turn supplied material into a selective, traceable, accessible static or interactive browser information projection. Preserve source meaning, authority, evidence state, and retrieval paths; exclude originating analysis, slide decks, decision prototypes, production/application UI, deployments, and reusable libraries.
---

# HTML Artifact

Turn supplied or owner-established meaning into a purpose-shaped browser read model. Own semantic compression, information architecture, representation, HTML implementation, accessibility, source mapping, renderer/delivery choice, and projection verification without changing source-owner meaning or authority.

## Projection contract

Use an owner-supplied projection path when present; otherwise use the requested path or the active host's normal artifact/output surface. When the selected destination is a repository-scoped QP workspace, resolve a standalone `.qp/artifacts/<subject>/index.html` through `akosile`. Do not require a repository merely to produce an HTML artifact.

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

## Own information projection, not every HTML result

Classify the accepted result before implementation:

- **Static information projection** — supplied meaning is read, inspected, compared, or retrieved in the browser.
- **Interactive information projection** — interaction only reveals, navigates, compares, filters, sequences, selects, or inspects supplied meaning.
- **Not HTML Artifact** — a slide deck remains `slides`; a truth-bearing experiential decision instrument remains `prototype`; product/application UI remains its delivery/UI owner. File format does not transfer semantic ownership.

Interactivity alone does not create another owner, and HTML delivery alone does not make another owner's result an HTML Artifact result.

## Compose for human judgment

Establish required coverage before minimizing representation. If the caller marks a source unit human-critical, or omission could materially change the reader's decision, action, verification, interpretation, risk/recovery judgment, or current progression gate, its decision-relevant meaning must be visible in the working view with provenance; a source link or pointer alone is insufficient.

Choose representation per material relationship or reader question, not per source heading. Several source sections may collapse into one useful traceability/comparison view; one source section may require several representations when it contains different relationships.

Keep semantic types distinct. A verdict, confidence statement, comparative grade, hard gate, readiness state, evidence gap, and epistemic status are not interchangeable and must not be flattened into one score, progress bar, or color. Qualitative judgment gets no false precision.

For living projections, after the first complete view, foreground material semantic delta: what changed, reopened, became stale, closed, or now limits progression. Recompute the reader job/information direction after material stage changes rather than accumulating every earlier stage at equal weight.

## Choose representation before renderer or delivery

First identify the relationship and strongest faithful representation. Then choose a mature renderer/capability and the lightest sound delivery mode. Do not ask whether native HTML can technically draw the relationship before deciding what form would help the reader understand it best.

Use [visual reasoning](references/visual-reasoning.md) for representation shape and [representation capabilities](references/representation-capabilities.md) when a specialized grammar/renderer can materially improve information fidelity, perceptual clarity, interaction/navigation, correctness, accessibility, or implementation reliability. Named capability anchors are useful starting points, never an allowlist; when none fits, discover a current mature capability rather than degrading the representation to stay inside a cached set.

Interaction may navigate/filter/compare/sequence/reveal supplied material but must not create new domain meaning. Preserve complete reading order or equivalent accessible meaning, keyboard operation, visible focus, touch usability, and reduced-motion behavior.

## Standalone support

Use an existing artifact/project shell when it already owns the need. For standalone QP HTML, use the [visual foundation](assets/visual-foundation.css) and [theme control](assets/theme-control.html) unless the host already supplies equivalent behavior. Add the [back-to-top control](assets/back-to-top-control.html), [report control](assets/report-control.html), [collection filter control](assets/collection-filter-control.html), or [carousel control](assets/carousel-control.html) only when that asset's own trigger applies.

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

Structural proof is the baseline after every projection write: reread and check source/projection identities, required human-critical coverage, anchors/context, renderer/dependency identity, source mapping, runtime disclosure, and semantic fallback.

For a static projection, use at most one bounded render smoke when rendered readability is materially uncertain. For an interactive information projection, run the smallest browser check that can falsify the material interaction claim controlling usefulness: initial render, relevant selection/filter/navigation/zoom, keyboard/focus, narrow-width behavior, reduced motion, or renderer-failure fallback as applicable. Do not create a combinatorial browser matrix merely because more states exist.

A substantial/public/long-lived document does not by itself earn deeper browser proof. A specialized renderer does not by itself earn deep proof either; test only the browser-dependent claims it introduces. After a proved defect, rerun only invalidated proof.

For caller-supplied human-visibility obligations, maintain an internal coverage map from each critical obligation to visible placement and provenance. A deterministic verifier may be introduced only if recurring dogfood evidence shows agent/native checks cannot reliably enforce that mechanical seam.

## Deliver

Return the exact direct-access locator supported by the active host: a file path, artifact attachment/URL, or equivalent. When the artifact lives in a repository-scoped QP workspace, also return its repository-relative `.qp/...` workspace path.

Opening is host UX, not artifact semantics. Open only when the user asks or render proof requires it; reuse an existing preview/page/session when available. After rewrites, refresh/navigate that surface rather than invoking an opener repeatedly. If the only available opener would create another tab/window and opening is not required for proof, return the locator instead.

Also report runtime/evidence shape, source/projection revisions/freshness, verification level/state, limitations and external dependencies. Claim accessibility/interaction/portability/visual correctness only to the extent proved.
