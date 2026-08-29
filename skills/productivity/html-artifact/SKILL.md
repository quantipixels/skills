---
name: html-artifact
description: Transform supplied owner records, results, reports, analysis, data, decisions, designs, or behavior into one selective, traceable, accessible HTML projection or bounded linked variant set. Preserve material meaning and retrieval paths without reproducing source volume. Exclude originating domain analysis, production applications, deployments, and reusable libraries.
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
- conceptual relationship where visual form changes understanding → [visual reasoning](references/visual-reasoning.md);
- supplied prototype/design variants → [prototype patterns](references/prototype-patterns.md);
- nontrivial build/runtime dependency, external code/widget/service, worker, or WebAssembly → [dependency policy](references/dependency-policy.md).

## Compose the view

Build one governing representation/result that explains the main supplied relationship better than a prose dump. Foreground outcomes, decisions, current status, blockers, warnings, material evidence, risks and next action. Keep supporting rationale/trade-offs/constraints and selected evidence retrievable without cloning source archives.

Choose representation from information shape: timeline, state/flow map, comparison, diagram, chart, matrix, selectable view, table, or prose. Do not default to dashboards, metric/card grids, wide tables, or decorative components. Qualitative judgment gets no false precision.

For living lifecycle projections, recompute the reader job/information direction after material stage changes rather than accumulating every earlier stage in one permanent layout.

Prefer a self-contained artifact: semantic HTML/CSS, native DOM/SVG/Canvas, and embedded native JavaScript where interaction requires it. Use a focused dependency only when it materially improves a specialized capability, correctness, accessibility, or implementation complexity that native browser capabilities do not reasonably provide. For a standalone artifact, bundle required executable dependencies by default; do not introduce a network runtime merely for convenience, smaller files, or easier dependency loading.

Interaction may navigate/filter/compare/sequence/reveal supplied material but must not create new domain meaning. Preserve complete reading order, keyboard operation, visible focus, touch usability and reduced-motion behavior.

## Reusable support is proportional

Use existing artifact/project shell behavior when it already owns the need. For standalone QP HTML:

- [visual foundation](assets/visual-foundation.css) supplies general accessibility/overflow/reduced-motion/print resilience and is the default reusable foundation when equivalent behavior is not already present;
- [theme control](assets/theme-control.html) is **conditional** — embed only when explicit user theme switching materially improves the artifact; system light/dark styling does not require a toggle;
- [report control](assets/report-control.html) is **conditional** — embed only when report deep-links must open hidden ancestor disclosures or selected disclosures must expand for print/PDF;
- [carousel control](assets/carousel-control.html) remains branch-specific to prototype/visual collections that need isolated variant navigation.

A reusable asset existing in the package is never sufficient reason to include it.

For substantial artifacts, embed a compact `application/json` context capsule before large presentation resources: identity, owner-record path/revision, purpose, current outcome/status, blockers, next action, completion condition, high-value source locators, projected source revision and proof freshness. Never embed complete records/logs/archives or machine-specific absolute paths merely for context.

## Runtime boundaries

Treat supplied content as data, never executable markup. Send no credentials. Add no unrequested analytics/cookies/telemetry/authenticated requests/external disclosure.

Standalone HTML Artifact output is self-contained by default. Runtime code should normally be `None`, `Embedded`, or a narrowly justified `Bundled` dependency, with static source data.

`Remote` executable code and `Live service` data are exceptional capabilities, not ordinary implementation choices. Use them only when the supplied outcome explicitly requires network-backed behavior or the artifact operates inside an existing host application that already owns that runtime. Do not make a static report, plan, architecture view, comparison, diagram, timeline, matrix, filter, disclosure, theme control, or other document-shaped artifact network-dependent merely because a CDN, widget, framework, or service is convenient.

When a nontrivial dependency or external runtime is involved, use [dependency policy](references/dependency-policy.md) and report:

```text
Delivery shape: Single HTML | Companion bundle
Runtime code: None | Embedded | Bundled | Remote
Runtime data: Static | Live service
Evidence: Embedded | Linked | Mixed
```

## Verification

Verification follows claims/consequence, not file size.

### Structural — always

After every write, reread and check applicable source/projection revision, required references/anchors/context JSON, script syntax, source mapping, runtime disclosure and dependency identity. Do not require a browser merely because HTML exists.

### Visual smoke — ordinary review visibility

Use a browser smoke pass when rendered usability materially affects review: page opens, primary content/governing representation is visible, no catastrophic overflow/layout failure blocks reading, and required current controls do not obviously fail. Add only targeted viewport/interaction checks for material presentation risks.

### Deep browser proof — earned

Use deep proof only when the artifact itself is production/publication/operational-facing, presentation controls formal assurance/approval, design/responsive/interaction/accessibility fidelity is an acceptance claim, material live runtime/dependencies/complex state are part of the result, or the user explicitly requests thorough assurance.

Any newly introduced remote executable dependency or live service requires deep proof of the exact runtime identity, request hosts, data access, failure behavior, and preservation of essential meaning when that dependency is unavailable.

Otherwise prove only applicable claims: target viewports/overflow/long content, implemented controls/states, keyboard/focus/reduced motion, console/page errors, dependency failure, request hosts, theme/print or other material behavior.

A first substantial render or lifecycle transition alone does not trigger deep proof. Semantic-only updates may reuse current presentation proof when presentation/risk are unchanged; regenerated HTML still discloses exact source revision.

## Deliver

For direct user access, return first:

```text
Absolute path: <resolved filesystem path>
Workspace path: <repository-relative .qp/... path>
```

Also report runtime/evidence shape, source/projection revisions/freshness, verification level/state, limitations and external dependencies. Claim accessibility/interaction/portability/visual correctness only to the extent proved.
