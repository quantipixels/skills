# Visual reasoning

Use this only when a substantial conceptual relationship can be understood or compared more accurately through a visual representation than through prose alone.

This is calibration, not a template library. Choose the representation from the supplied relationship and reader job. Do not force a diagram merely because the subject is technical.

## Before / after structure

Use when the reader must understand how ownership, flow, state, or dependency shape changes.

Good:

```text
Before
UI → coordinator → service → provider adapter → provider

After
UI → provider client
      └─ owns retries, auth, error translation, lifecycle
```

The visual shows what disappeared and what the surviving owner now owns.

Bad: two screenshots or diagrams at different scales with no marked changed/unchanged elements.

Avoid when the change is only wording or a tiny local edit better represented by a diff.

## Call-graph collapse

Use when repeated forwarding layers or indirection are the material issue.

Good: show the actual call sequence, label forwarding-only nodes, then show the shorter sequence with the remaining responsibility owner.

Bad: a generic box diagram that does not reveal which calls or responsibilities were removed.

## Responsibility map

Use when the question is where policy, lifecycle, state, authority, or data ownership belongs.

Good: group responsibilities under current owners and highlight duplicated or ownerless behavior.

Bad: color every package/module differently without showing responsibility.

## State or lifecycle transition

Use when the source establishes states, allowed transitions, blockers, recovery, or stale paths.

Good: show only source-backed states and transition labels; emphasize the current state or invalid transition that matters.

Bad: invent intermediate states to make the diagram look complete.

## Evidence trace

Use for assurance, review, or decision artifacts where the governing relationship is claim → evidence → disposition.

Good:

```text
Requirement R3
  ↓
Test T8 + runtime evidence E2
  ↓
Satisfied
```

Bad: a decorative evidence count that hides which claim each source supports.

## Candidate comparison

Use when alternatives must remain comparable.

Keep the same visual grammar, scale, criteria, and labeling across candidates. Show changed and unchanged structure when material.

Good: two architecture alternatives use the same boundary map and annotate trade-offs beside the affected seam.

Bad: one candidate gets a detailed architecture diagram while another is summarized in prose.

## Mass / concentration diagram

Use when the point is where complexity, state, dependencies, or behavior are concentrated rather than exact sequence.

Good: visually weight modules by supplied responsibility/complexity evidence to reveal a deep owner versus scattered thin wrappers.

Bad: size boxes by arbitrary line count while presenting the result as architectural importance.

## Cross-section

Use when several concerns cross the same boundary: identity, data, trust, lifecycle, failure, migration, or proof.

Good: a boundary cross-section shows what crosses, who owns translation, and which failures stay on each side.

Bad: a conventional architecture overview that hides the boundary-specific question.

## Choose prose when prose is better

Do not create a visual when:

- no meaningful relationship is supplied;
- the visual only restates a short list;
- exact wording is the evidence;
- the source cannot support causal, state, scale, or ownership claims; or
- the diagram would require invented structure.

A strong paragraph or compact table is preferable to decorative visualization.

## Mermaid diagrams

Mermaid is a supported optional renderer when its diagram grammar fits the supplied relationship. Preserve the Mermaid source and provide equivalent accessible text or native structure. For a standalone artifact, bundle the admitted runtime under the [external dependency policy](dependency-policy.md); do not depend on a CDN. Make Mermaid colors respond to the artifact's light and dark theme tokens, and keep the accessible fallback usable if rendering fails.

## Verification cue

The representation must encode a material supplied relationship. For ordinary review artifacts, verify it with HTML Artifact's structural checks and visual smoke when rendered usability matters. Deep browser proof is required only when the visual/interaction itself is an acceptance claim or the artifact's consequence otherwise requires it.
