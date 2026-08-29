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
- external code/widgets/services → [dependency policy](references/dependency-policy.md).

## Compose the view

Build one governing representation/result that explains the main supplied relationship better than a prose dump. Foreground outcomes, decisions, current status, blockers, warnings, material evidence, risks and next action. Keep supporting rationale/trade-offs/constraints and selected evidence retrievable without cloning source archives.

Choose representation from information shape: timeline, state/flow map, comparison, diagram, chart, matrix, selectable view, table, or prose. Do not default to dashboards, metric/card grids, wide tables, or decorative components. Qualitative judgment gets no false precision.

For living lifecycle projections, recompute the reader job/information direction after material stage changes rather than accumulating every earlier stage in one permanent layout.

Use semantic HTML/CSS/native DOM/SVG/Canvas or one focused dependency according to the actual capability. Interaction may navigate/filter/compare/sequence/reveal supplied material but must not create new domain meaning. Preserve complete reading order, keyboard operation, visible focus, touch usability and reduced-motion behavior.

## Reusable support is proportional

Use existing artifact/project shell behavior when it already owns the need. For standalone QP HTML:

- [visual foundation](assets/visual-foundation.css) supplies general accessibility/overflow/reduced-motion/print resilience, including semantic-table containment with a tunable narrow-container rule, and is the default reusable foundation when equivalent behavior is not already present;
- [theme control](assets/theme-control.html) is **default** — embed it unless the existing artifact/project shell supplies an equivalent explicit user control; system light/dark styling alone does not replace the toggle;
- [back-to-top control](assets/back-to-top-control.html) is **required after its trigger** — embed it when page length or navigation makes returning to the opening context require substantial reverse scrolling; omit it for a short single-view artifact;
- [report control](assets/report-control.html) is **conditional** — embed only when report deep-links must open hidden ancestor disclosures or selected disclosures must expand for print/PDF;
- [collection filter](assets/collection-filter-control.html) is **conditional** — embed only for a supplied single-select categorical view; keep category meaning/predicates source-owned and keep every item visible without JavaScript and in print;
- [carousel control](assets/carousel-control.html) remains branch-specific to prototype/visual collections that need isolated variant navigation.

Follow each asset's stated default or trigger. Its existence is not another reason to include it.

For substantial artifacts, embed a compact `application/json` context capsule before large presentation resources: identity, owner-record path/revision, purpose, current outcome/status, blockers, next action, completion condition, high-value source locators, projected source revision and proof freshness. Never embed complete records/logs/archives or machine-specific absolute paths merely for context.

## Runtime boundaries

Treat supplied content as data, never executable markup. Send no credentials. Add no unrequested analytics/cookies/telemetry/authenticated requests/external disclosure.

When external code/services are involved, use [dependency policy](references/dependency-policy.md) and report:

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

Then prove only applicable claims: target viewports/overflow/long content, implemented controls/states, keyboard/focus/reduced motion, console/page errors, dependency failure, request hosts, theme/print or other material behavior.

A first substantial render or lifecycle transition alone does not trigger deep proof. Semantic-only updates may reuse current presentation proof when presentation/risk are unchanged; regenerated HTML still discloses exact source revision.

## Deliver

For direct user access, return first:

```text
Absolute path: <resolved filesystem path>
Workspace path: <repository-relative .qp/... path>
```

Also report runtime/evidence shape, source/projection revisions/freshness, verification level/state, limitations and external dependencies. Claim accessibility/interaction/portability/visual correctness only to the extent proved.
