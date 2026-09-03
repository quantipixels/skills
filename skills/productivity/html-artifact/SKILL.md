---
name: html-artifact
description: Turn supplied material into a selective, traceable, accessible HTML visualization. Preserve its meaning, authority, and retrieval paths without reproducing source volume. Exclude originating analysis, production applications, deployments, and reusable libraries.
---

# HTML Artifact

Turn supplied material into a purpose-shaped visual view. Own semantic compression, information architecture, representation, HTML implementation, accessibility, source mapping, dependency choice, and projection verification without changing source-owner meaning/authority.

## Projection contract

Use an owner-supplied projection path when present; otherwise use the requested path or the active host's normal artifact/output surface. When the selected destination is a repository-scoped QP workspace, resolve a standalone `.qp/artifacts/<subject>/index.html` through `akosile`. Do not require a repository merely to produce an HTML artifact.

When an owner record exists, read it first and pin identity/revision/status/candidate, `Resume`, linked evidence, and projection brief. Record wins when HTML disagrees.

For substantial/evidence-heavy/living/reused/owner-record input, read [source composition](references/source-composition.md). Follow the supplied audience; otherwise write for a reader with no prior context. Pin one reader outcome, governing question, source-supported thesis, evidence cutoff, dominant supplied relationship, and first-viewport obligation.

Request only missing structure that can change truth/usefulness. Never invent domain conclusions, causality, priority, status, decisions, owners, or recommendations to satisfy a visual form.

Load branch guidance only when applicable:

- report/evidence/living/candidate comparison → [report patterns](references/report-patterns.md);
- diff, commit/branch change, or pinned pull-request or merge-request evidence → [code-change review](references/code-change-review.md);
- interactive relationship map, multiple coordinated views, or guided walkthrough → [interactive projections](references/interactive-projections.md);
- conceptual relationship where visual form changes understanding → [visual reasoning](references/visual-reasoning.md);
- supplied prototype/design variants → [prototype patterns](references/prototype-patterns.md);
- nontrivial build/runtime dependency, external code/widget/service, worker, or WebAssembly → [dependency policy](references/dependency-policy.md).

## Classify representation vs experience

Classify the artifact job before choosing proof.

- **Document-shaped projection** — the browser presents supplied information. This includes reports, plans, decision trees/frontiers, research/resources, specifications, tickets/work breakdowns, architecture packets/diagrams, code-change/review/maintainability/triage/premise views, postmortems, status/progress views, timelines, matrices/comparisons, and evidence reports. Themes, disclosures, filters, sorting, charts, anchors, and simple navigation remain document affordances when they only navigate/reveal/compare supplied information; they do not promote the artifact into a UI acceptance surface.
- **Interface-shaped artifact** — the rendered UI/interaction itself is part of the requested result or decision, such as a UI prototype, product/application interface, interaction/design candidate, responsive workflow, or component/state demonstration. The caller's accepted result must actually depend on rendered experience; interactivity alone is insufficient.

When a document-shaped artifact's accepted result genuinely changes so rendered experience itself is being designed or evaluated, reclassify from the current request/owner contract rather than from HTML features. For literal UI/design/application work, keep the appropriate `prototype`/Design/UI owner primary and use HTML Artifact only for the representation work it owns.

## Compose the view

Build one governing representation/result that explains the main supplied relationship better than a prose dump. Foreground outcomes, decisions, current status, blockers, warnings, material evidence, risks and next action. Keep supporting rationale/trade-offs/constraints and selected evidence retrievable without cloning source archives.

Choose representation from information shape: timeline, state/flow map, comparison, diagram, chart, matrix, selectable view, table, or prose. Do not default to dashboards, metric/card grids, wide tables, or decorative components. Qualitative judgment gets no false precision.

For living lifecycle projections, recompute the reader job/information direction after material stage changes rather than accumulating every earlier stage in one permanent layout.

Prefer a self-contained artifact: semantic HTML/CSS, native DOM/SVG/Canvas, and embedded native JavaScript where interaction requires it. Use a focused dependency only when it materially improves a specialized capability, correctness, accessibility, or implementation complexity that native browser capabilities do not reasonably provide. For a standalone artifact, bundle required executable dependencies by default; do not introduce a network runtime merely for convenience, smaller files, or easier dependency loading.

Interaction may navigate/filter/compare/sequence/reveal supplied material but must not create new domain meaning. Preserve complete reading order, keyboard operation, visible focus, touch usability and reduced-motion behavior.

## Standalone support

Use an existing artifact/project shell when it already owns the need. For standalone QP HTML, use the [visual foundation](assets/visual-foundation.css) and [theme control](assets/theme-control.html) unless the host already supplies equivalent behavior. Add the [back-to-top control](assets/back-to-top-control.html), [report control](assets/report-control.html), [collection filter control](assets/collection-filter-control.html), or [carousel control](assets/carousel-control.html) only when that asset's own trigger applies; read only the selected asset before embedding it. Asset existence is never another inclusion reason.

For icon-only controls, hide the icon from assistive technology and provide the asset's visually-hidden accessible label. For substantial artifacts, embed only a compact context capsule (identity/revision, purpose/status, blockers/next action, high-value source locators, proof freshness); never clone records/logs/archives or machine-specific absolute paths into it.

## Runtime boundaries

Treat supplied content as data, never executable markup. Send no credentials. Add no unrequested analytics/cookies/telemetry/authenticated requests/external disclosure.

Standalone output is self-contained by default. Runtime code should normally be `None`, `Embedded`, or a narrowly justified `Bundled` dependency, with static source data. `Remote` executable code and `Live service` data are exceptional: use them only when the supplied outcome explicitly needs network-backed behavior or an existing host application already owns that runtime.

When a nontrivial dependency/external runtime is involved, use [dependency policy](references/dependency-policy.md) and report:

```text
Delivery shape: Single HTML | Companion bundle
Runtime code: None | Embedded | Bundled | Remote
Runtime data: Static | Live service
Evidence: Embedded | Linked | Mixed
```

## Verification

Verification follows the artifact job and accepted claims, not importance, size, longevity, publication status, or HTML feature count.

### Document-shaped projection — structural ceiling

Structural proof is the normal completion boundary. After every write, reread and check applicable source/projection revision, required content/anchors/context, script syntax, source mapping, runtime disclosure, and dependency identity.

Use at most one bounded render smoke only when rendered readability is materially uncertain: open the artifact, confirm the governing content is visible and no catastrophic layout/overflow failure prevents reading, then stop. Do not run a render merely because HTML exists.

Do not escalate a document-shaped projection to targeted or deep browser proof merely because it is substantial, public, polished, interactive, long-lived, operationally relevant, or contains ordinary document controls. Semantic-only updates may reuse current presentation proof while presentation behavior is unchanged.

### Interface-shaped artifact — risk-driven browser proof

When rendered experience itself is part of acceptance, start with the smallest render/interaction check that can falsify the accepted UI claim. Escalate to targeted browser proof only for specific material risks structural proof cannot establish, such as materially different responsive layouts, state transitions, keyboard/focus behavior, interaction semantics, or runtime behavior.

### Deep browser proof — exceptional

Use deep browser proof only for interface-shaped artifacts whose material browser-dependent acceptance claims remain uncertain after narrower checks, or when the user explicitly requests thorough browser assurance.

Before starting, pin the exact browser-dependent claims and the smallest representative states, viewports, and interactions capable of falsifying them. Do not create a combinatorial browser matrix or exploratory regression sweep merely because more combinations exist.

A new remote executable dependency or live service earns targeted runtime proof of exact runtime identity, request hosts, data access, failure behavior, and preservation of essential meaning. It does not by itself promote a document-shaped projection to deep browser proof.

After a proved defect, rerun only proof invalidated by the correction. Unrelated observations do not automatically expand proof scope. Stop when every declared material browser-dependent claim is `proved`, an explicit evidence gap, or `not applicable`.

## Deliver

Return the exact direct-access locator supported by the active host: a file path, artifact attachment/URL, or equivalent. When the artifact lives in a repository-scoped QP workspace, also return its repository-relative `.qp/...` workspace path. Do not invent an absolute filesystem path or `.qp` locator when the host/destination does not have one.

Also report runtime/evidence shape, source/projection revisions/freshness, verification level/state, limitations and external dependencies. Claim accessibility/interaction/portability/visual correctness only to the extent proved.
