# Design convergence

Load this branch when the current product evidence leaves a material design choice open, when several materially different compositions remain credible, or when an implemented UI needs design review against an accepted direction. The goal is to expose enough design space to make a strong choice, then converge on the real rendered result without turning every task into a variant exercise or review ceremony.

## Decide whether exploration is earned

Exploration is useful when different choices could materially change the user job, information hierarchy, interaction model, density, navigation, state treatment, responsive behavior, brand expression, or implementation burden.

Before generating candidates, freeze every current product/brand constraint that the request does not explicitly reopen. Treat approved identity, positioning, user/audience, primary action, accessibility commitments, platform boundaries, and other controlling project evidence as candidate invariants rather than dimensions to vary for novelty. A candidate that violates a frozen constraint is invalid, not an alternative. Explore only the unresolved mechanism or composition that remains after those constraints are applied.

Do not generate alternatives merely because design work exists. Skip exploration when current product/brand evidence already determines the direction, the request is a narrow correction, or the only remaining variation is cosmetic.

When exploration is warranted, identify the unresolved design question first. Examples include:

- whether a workflow should be progressive or single-surface;
- whether dense data should use a table-first or card-first composition;
- whether navigation should prioritize persistent context or maximum content area;
- whether a primary task should use inline editing or a focused editor; or
- how a mobile transformation should preserve the desktop hierarchy.

## Explore mechanisms, not skins

Produce only materially different viable directions. A candidate earns distinction through composition, hierarchy, interaction, state behavior, navigation, density, or another decision-bearing mechanism—not a different palette, typeface, radius, shadow, or ornamental treatment applied to the same structure.

For each candidate, keep enough detail to compare the governing mechanism:

```text
Candidate intent
Primary hierarchy / information architecture
Interaction and state model
Responsive behavior
Accessibility implications
Brand/product fit
Implementation constraints or risk
Evidence that supports or weakens it
```

Do not assign arbitrary numeric scores. Compare only criteria that actually govern the product decision.

## Select one coherent direction

Evaluate candidates against the actual user job, product/brand evidence, content/data shape, platform conventions, accessibility needs, supported states, and implementation constraints.

Select one direction when the evidence is sufficient. Preserve rejected alternatives only when the rejection teaches an implementation boundary, prevents a likely regression, or explains a consequential trade-off. Do not keep a permanent gallery of losing ideas.

When no candidate can be selected because a consequential product/design choice requires user authority, return the material decision to the caller for `arojinle`; do not silently convert Amọ̀ye judgment into product authority.

## Review the real render

After implementation, pin the accepted direction and the exact rendered candidate/evidence. Review observed UI behavior, not source-code intent or an imagined render.

Use the available project/host rendering surface that can establish the relevant claim: current screenshots, local/preview browser, device/simulator capture, or another exact-current rendered artifact. If the necessary surface/state cannot be observed, report the evidence gap rather than inferring visual fidelity from code.

Review only the surfaces/states that materially support the accepted direction and current change. Trace findings to concrete evidence such as:

- hierarchy or grouping no longer expressing the accepted priority;
- interaction/state behavior diverging from the chosen model;
- responsive transformation losing important context or controls;
- accessibility behavior undermining the intended interaction;
- typography/color/motion weakening semantic roles or brand constraints; or
- component realization introducing visual noise, density drift, or inconsistent affordances that materially change the result.

Distinguish a material deficiency from subjective polish preference. Do not keep iterating merely because another aesthetically plausible variant could exist.

## Converge through owner boundaries

Amọ̀ye returns design findings only. `asa-oju-ibanisoro` or the applicable implementation owner applies accepted corrections, runs its native proof, and rerenders the affected surfaces/states.

Request another Amọ̀ye review pass only when the correction can materially change the design verdict or the previous evidence gap has been cleared. Stop when no material design deficiency remains against the accepted direction and controlling product evidence.

This loop does not create a new lifecycle owner:

```text
accepted direction
  → implementation owner
  → exact rendered result
  → Amọ̀ye review
  → accepted correction when needed
  → implementation owner
  → rerender / native proof
  → stop when material deficiencies are resolved
```

## Compound only durable project truth

After selection or convergence, ask whether the work established non-obvious reusable project-specific design knowledge that future work should begin with: a stable hierarchy rule, interaction constraint, brand/product composition principle, accessibility boundary, or other confirmed project truth.

When it did, use `amose` to reconcile the appropriate durable destination. Do not persist generic UX principles, one-off visual fixes, rejected taste, or transient implementation details as project knowledge.
