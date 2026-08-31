---
name: html-artifact
description: Turn supplied material into a selective, traceable, accessible HTML visualization. Preserve its meaning, authority, and retrieval paths without reproducing source volume. Exclude originating analysis, production applications, deployments, and reusable libraries.
---

# HTML Artifact

Turn supplied material into a purpose-shaped visual view. Own semantic compression, information architecture, representation, HTML implementation, accessibility, source mapping, dependency choice, and projection verification without changing source-owner meaning/authority.

## Projection contract

Use an owner-supplied projection path when present; otherwise use the requested path or resolve a standalone `.qp/artifacts/<subject>/index.html` through `akosile`.

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

## Compose the view

Build one governing representation/result that explains the main supplied relationship better than a prose dump. Foreground outcomes, decisions, current status, blockers, warnings, material evidence, risks and next action. Keep supporting rationale/trade-offs/constraints and selected evidence retrievable without cloning source archives.

Choose representation from information shape: timeline, state/flow map, comparison, diagram, chart, matrix, selectable view, table, or prose. Do not default to dashboards, metric/card grids, wide tables, or decorative components. Qualitative judgment gets no false precision.

For living lifecycle projections, recompute the reader job/information direction after material stage changes rather than accumulating every earlier stage in one permanent layout.

Prefer a self-contained artifact: semantic HTML/CSS, native DOM/SVG/Canvas, and embedded native JavaScript where interaction requires it. Use a focused dependency only when it materially improves a specialized capability, correctness, accessibility, or implementation complexity that native browser capabilities do not reasonably provide. For a standalone artifact, bundle required executable dependencies by default; do not introduce a network runtime merely for convenience, smaller files, or easier dependency loading.

Interaction may navigate/filter/compare/sequence/reveal supplied material but must not create new domain meaning. Preserve complete reading order, keyboard operation, visible focus, touch usability and reduced-motion behavior.

## Standalone support

Use an existing artifact/project shell when it already owns the need. For standalone QP HTML, use `assets/visual-foundation.css` and `assets/theme-control.html` unless the host already supplies equivalent behavior. Add `back-to-top-control.html`, `report-control.html`, `collection-filter-control.html`, or `carousel-control.html` only when that asset's own trigger applies; read only the selected asset before embedding it. Asset existence is never another inclusion reason.

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

Verification follows claims/consequence, not file size.

- **Structural — always:** reread after every write; check applicable source/projection revision, required anchors/context, script syntax, source mapping, runtime disclosure, and dependency identity. HTML existence alone does not require a browser.
- **Visual smoke — when rendered usability materially affects review:** prove the page opens, the governing representation is visible, no catastrophic layout/overflow blocks reading, and required controls do not obviously fail. Add only targeted viewport/interaction checks for material risks.
- **Deep browser proof — earned:** use when the artifact is production/publication/operational-facing; presentation controls formal assurance; design/responsive/interaction/accessibility fidelity is an acceptance claim; material live runtime/dependencies/complex state are part of the result; or the user explicitly requests thorough assurance. A new remote executable dependency/live service also earns deep proof of exact runtime identity, request hosts, data access, failure behavior, and essential-meaning fallback.

A first substantial render/lifecycle transition alone does not trigger deep proof. Semantic-only updates may reuse current presentation proof when presentation/risk are unchanged; regenerated HTML still discloses the exact source revision.

## Deliver

For direct user access, return first:

```text
Absolute path: <resolved filesystem path>
Workspace path: <repository-relative .qp/... path>
```

Also report runtime/evidence shape, source/projection revisions/freshness, verification level/state, limitations and external dependencies. Claim accessibility/interaction/portability/visual correctness only to the extent proved.
