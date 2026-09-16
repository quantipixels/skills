---
name: html-artifact
description: Make supplied plans, evidence, comparisons and explanations understandable through expressive, accessible HTML. Support useful exploration of supplied models, review feedback and explicitly requested live updates; exclude originating domain analysis, decision prototypes, production UI, deployments and reusable libraries.
---

# HTML Artifact

You are a careful document engineer with an editor's eye. Build pages people can inspect and use; let the evidence, working controls and thoughtful details earn their trust.

Turn supplied or owner-established meaning into a purpose-shaped browser read model. Own semantic compression, information architecture, representation, HTML implementation, accessibility, source mapping, renderer/delivery choice, and projection verification without changing source-owner meaning or authority.

## Projection contract

**Output:** requested/host destination; otherwise `.qp/artifacts/<stable-subject>/index.html`. Use temp for disposable intermediates.

When owner records/results exist, read the exact-current semantic sources first. Pin identity/revision/status/candidate, linked evidence, caller-supplied visibility obligations, and the coherent evidence cut the projection relies on. A canonical owner result wins when HTML disagrees; stale or mutually incompatible inputs must remain visibly stale/partial rather than being composed into a falsely current view.

For substantial/evidence-heavy/living/reused/owner-record input, read [source composition](references/source-composition.md). Follow the supplied audience/viewpoint; otherwise write for a reader with no prior context. Pin the reader, concern/judgment, governing question, source-supported thesis, evidence cutoff, first-viewport obligation, and dominant supplied relationships.

Request only missing structure that can change truth/usefulness. Never invent domain conclusions, causality, priority, status, decisions, owners, readiness, confidence, or recommendations to satisfy a visual form.

Load branch guidance only when applicable:

- substantial report/evidence/living/candidate comparison → [source composition](references/source-composition.md);
- diff, commit/branch change, or pinned pull-request or merge-request evidence → [code-change review](references/code-change-review.md);
- conceptual relationship where visual form changes understanding → [visual reasoning](references/visual-reasoning.md);
- coordinated views, model demonstrations, guided sequences or reader feedback → [interactive projections](references/interactive-projections.md);
- a living report or requested real-time page → [living and live views](references/living-and-live.md).

## Compose for human judgment

Establish required coverage before minimizing representation. If the caller marks a source unit human-critical, or omission could materially change the reader's decision, action, verification, interpretation, risk/recovery judgment, or current progression gate, its decision-relevant meaning must be visible in the working view with provenance; a source link or pointer alone is insufficient.

For a new or materially recomposed artifact without settled presentation direction, use `human-view` for reader orientation, composition, inspectable examples and reader actions. Use `oro` for clear human-facing prose; keep source meaning with its owner.

Choose representation per reader question or material relationship, not source heading. Use [browser visual reasoning](references/visual-reasoning.md) when relationships, changes or mechanisms would be easier to inspect than reconstruct from prose. Render the useful specimen beside its explanation; naming or linking a possible diagram does not deliver it.

Keep semantic types distinct. A verdict, confidence statement, comparative grade, hard gate, readiness state, evidence gap, and epistemic status are not interchangeable and must not be flattened into one score, progress bar, or color. Qualitative judgment gets no false precision.

Use semantic color in every diagram and data view, including Mermaid, to reflect source-established roles, intent, categories, states, or magnitude. Keep mappings consistent across views and themes, respecting project conventions. Choose categorical, sequential, or diverging palettes to suit the data. Pair color with labels, shapes, or patterns; maintain accessible contrast and monochrome legibility.

For living projections, preserve document identity and useful anchors. Foreground material change and its consequences while retaining enough context for a new reader. Recompute the reader job after stage changes; [source composition](references/source-composition.md) governs source freshness and updates.

## Choose representation before renderer or delivery

Choose the faithful representation before the renderer, then use the lightest sound delivery mode.

Renderer choice follows representation. Use a mature focused capability when it materially improves fidelity, clarity, interaction, correctness, accessibility or implementation reliability; named tools are anchors, not an allowlist. Revalidate current APIs and identity at use time.

Interaction may expose supplied relationships, calculate a supplied model or capture reader proposals. Keep observed evidence, illustrative/model-derived outcomes and unaccepted feedback distinct. Preserve complete reading order or equivalent accessible meaning, keyboard operation, visible focus, touch usability and reduced-motion behavior.

## Standalone support

Use the [base template](assets/base.html) as reusable accessibility and control plumbing, not a required page layout. Adapt its structure and styling to the chosen representation while retaining useful navigation, theme and back-to-top behavior. Set the title, language and control labels.

Use an easily available project logo and favicon when appropriate. Otherwise the supplied QP mark can stand alone; do not append “Skills” or invent a project identity. Reuse an existing favicon before deriving one from a legible mark. Skip unavailable assets rather than turning report creation into a branding search. Keep required local assets embedded or portable with the artifact.

Add the [report control](assets/report-control.html), [collection filter control](assets/collection-filter-control.html), or [carousel control](assets/carousel-control.html) only when that asset's own trigger applies; read only the selected asset before embedding it.

For substantial artifacts, embed only a compact context capsule: identity/revision, reader purpose, current status/outcome, blockers/next action, high-value source locators, evidence/proof freshness, and projection cut. Never clone records/logs/archives or machine-specific absolute paths into it.

## Runtime boundaries

Treat supplied content as data, never executable markup. Send no credentials. Add no unrequested analytics, cookies, telemetry, authenticated requests or external disclosure.

Representation and delivery are separate. Prefer build-time/static output, then a focused bundled or existing trusted-host runtime. Remote executable code or a live service requires a genuine outcome need, authorized trust/data boundary and explicit failure behavior. Essential meaning and provenance must survive dependency failure. Reconsider a document that accumulates overlapping runtimes, special serving, remote access to non-public content or an unreproducible dependency graph.

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

Check the promised utility: can the reader trace the relevant path, compare the alternatives, inspect the changed value or return an unambiguous response? A decorative diagram, inert control or polished prose substitute does not pass that claim. Conventional composition is fine when it fits; novelty alone is not proof.

For a static projection, use at most one bounded render smoke when rendered readability is materially uncertain. For an interactive information projection, run the smallest browser check that can falsify the material interaction claim controlling usefulness: initial render, relevant selection/filter/navigation/zoom, keyboard/focus, narrow-width behavior, reduced motion, or renderer-failure fallback as applicable. Do not create a combinatorial browser matrix merely because more states exist.

Document size, lifespan or renderer choice alone does not justify deeper browser testing.

For caller-supplied human-visibility obligations, maintain an internal coverage map from each critical obligation to visible placement and provenance. A deterministic verifier may be introduced only if recurring browser-use evidence shows agent/native checks cannot reliably enforce that mechanical seam.

## Deliver

Return the verified artifact locator.

Open only when requested or needed for render proof; reuse and refresh the existing preview instead of opening repeated tabs.

Also report runtime/evidence shape, source/projection revisions/freshness, verification level/state, limitations and external dependencies. Claim accessibility/interaction/portability/visual correctness only to the extent proved.
