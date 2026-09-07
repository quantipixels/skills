# Browser visual reasoning

Use when an HTML Artifact needs shaped visual reasoning beyond ordinary prose/table composition.

Use `fihanmi` as the canonical low-cost visual-understanding grammar for pseudocode, call/component/responsibility trees, shape-aware explanatory diffs, whole-shape admission, small Mermaid views, and the base epistemic rules for non-literal visuals. Apply that capability as supporting representation behavior when useful; do not create a visible ownership handoff merely because HTML Artifact uses the same grammar.

HTML Artifact adds only the browser-projection concerns below.

## Coverage and composition

Coverage comes before representation minimization. “Smallest sufficient view” means the least representational machinery that preserves all human-critical meaning the reader must see.

Choose representation per material relationship or reader question, not per Markdown/source section. Several source sections may collapse into one useful visual relationship; one source section may require several representations. Preserve one coherent page grammar across them.

## Evidence and assurance trace

Use when the browser view must expose claim → evidence → disposition, acceptance → contract → implementation → proof, or another traceability relationship whose broken/stale/conditional links are themselves material.

Example:

```text
Requirement R3
  ↓
Implementation I4
  ↓
Test T8 + runtime evidence E2
  ↓
Satisfied
```

Do not replace traceability with evidence counts, health percentages, or aggregate status when the reader needs to know which claim each source supports.

### Bidirectional traceability

When initiative/review evidence requires it, also reason backward from material implementation/proof and surface owner-established gaps equivalent to:

- requirement orphan — accepted obligation lacks adequate implementation/proof;
- implementation orphan — material mechanism lacks accepted contract/decision basis;
- proof orphan — evidence no longer establishes a current material claim.

Do not infer semantic orphan status from page topology alone; consume the owning evidence/result.

## Quantitative and dense relationships

Use a chart/plot when the governing relationship is quantitative and a visual pattern matters more than exact lookup. Use a graph/network view when connected structure is too dense for a small tree or Mermaid diagram. Use a table when aligned lookup/comparison remains clearer.

For large or interactive structures, preserve a complete accessible reading alternative or equivalent semantic fallback. Interaction may reveal, filter, navigate, compare, select, or sequence supplied meaning but must not create new domain meaning.

## Candidate comparison in the browser

Keep candidates on the same visual grammar, scale, criteria, and labeling. Comparative scoring/rubrics remain valid only when multiple viable candidates and multiple decision-changing criteria survive hard gates. Do not turn qualitative verdict/confidence/readiness into one browser score merely because a dashboard affords it.

## Mass, concentration, and cross-section

Use visual weight only from supplied evidence when the reader must see where complexity, state, dependencies, or proof burden concentrate. Use a cross-section when several concerns cross one boundary—identity, data, trust, lifecycle, failure, migration, recovery, or proof.

## Renderer selection

Once the representation is chosen, read [representation capabilities](representation-capabilities.md) when a mature grammar/renderer could materially improve fidelity, clarity, interaction, correctness, accessibility, or implementation reliability. Renderer choice is not representation choice, and delivery/runtime policy must not force a weaker form merely because native HTML is available.

Keep named renderer anchors open-ended. If none fits the information shape, discover a current mature capability rather than degrading the representation to stay inside a cached set.

## Browser-specific epistemic and provenance rules

Carry forward `fihanmi`'s distinction between `Observed | Inferred | Proposed | Illustrative`, and between literal source evidence and explanatory shape. HTML additionally preserves source identity, evidence cut, freshness, and retrieval/provenance in the page when material.

A visually polished or interactive projection never increases semantic authority. Stale, partial, conditional, inferred, or proposed content remains visibly so.

## Verification cue

Structural proof checks the modeled relationship, required human-critical coverage, source mapping, and semantic fallback. Render/runtime proof is proportional to browser-dependent claims introduced by the chosen renderer, interaction, layout, or accessibility behavior.

Do not add browser machinery merely because a representation could be interactive. Use the lightest delivery mode that preserves the selected representation and reader job.
