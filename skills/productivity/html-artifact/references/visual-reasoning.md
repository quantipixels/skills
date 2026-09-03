# Visual reasoning

Use when a material relationship can be understood, compared, or challenged more accurately through a shaped representation than through prose alone.

Coverage comes first. “Smallest sufficient view” means the least representational machinery that preserves all meaning the reader must see; it never means omitting human-critical facts merely to make the page smaller.

Choose representation per relationship/reader question, not per Markdown section. Keep one coherent page grammar across different representations.

## Low-cost structural grammar

Prefer the form that exposes the governing shape with the least machinery:

```text
logic / algorithm         → pseudocode
runtime / order           → call tree
UI/composition            → component tree
ownership / repository    → shallow file/responsibility tree
before / after            → shape-aware explanatory diff
new whole shape           → complete code/config/block
traceability              → directed chain / requirement map
state / lifecycle         → state sketch/diagram
comparison                → aligned comparison
quantitative relationship → chart/plot
large connected structure → graph/network view
```

Use prose when prose is already clearer. Use a table when the relationship is aligned lookup/comparison rather than topology or flow.

## Shape-aware change

When change is the governing relationship, match the diff grammar to the thing that changed:

```text
literal source change      → exact source diff
runtime interaction        → call-tree diff
responsibility/ownership   → ownership-tree diff
architecture/boundary      → module/boundary diff
UI composition             → component-tree diff
state behavior             → state-flow diff
repository shape           → file-tree diff
```

An explanatory shape diff is not source evidence. Preserve its epistemic status and the exact evidence it was derived from.

## Epistemic status

For non-literal visuals make the status clear where ambiguity could increase apparent authority:

- `Observed` — directly established by supplied evidence.
- `Inferred` — derived from evidence; inference remains distinguishable from observation.
- `Proposed` — candidate future shape owned by the applicable decision/design result.
- `Illustrative` — teaching simplification, not a literal implementation claim.

## Before / after structure

Use when ownership, flow, state, dependency, or concentration changes materially. Keep scale/grammar comparable and mark what changed versus remained.

Good:

```text
Before
UI → coordinator → service → provider adapter → provider

After
UI → provider client
      └─ owns retries, auth, error translation, lifecycle
```

Bad: unrelated screenshots/diagrams at different scales with no changed/unchanged relation.

## Call-graph collapse

Use when repeated forwarding/indirection is the issue. Show the actual call sequence, forwarding-only nodes, then the shorter surviving ownership path.

## Responsibility map

Use when policy, lifecycle, state, authority, or data ownership is the question. Group responsibilities under actual owners and expose duplicated/ownerless behavior rather than color-coding modules decoratively.

## State or lifecycle transition

Use source-backed states, transition labels, blockers, stale paths, and recovery. Do not invent intermediate states to make the diagram look complete.

## Evidence and assurance trace

Use when the relationship is claim → evidence → disposition, or when the reader must see acceptance → contract → implementation → proof. Broken/stale/conditional links are part of the meaning.

Good:

```text
Requirement R3
  ↓
Implementation I4
  ↓
Test T8 + runtime evidence E2
  ↓
Satisfied
```

Bad: evidence counts or health percentages that hide which claim each source supports.

## Bidirectional traceability

When initiative/review evidence requires it, also reason backward from material implementation/proof:

- requirement orphan — accepted obligation lacks adequate implementation/proof;
- implementation orphan — material mechanism lacks accepted contract/decision basis;
- proof orphan — evidence no longer establishes a current material claim.

Do not infer orphan status from a diagram alone; consume the owning semantic result/evidence.

## Candidate comparison

Keep candidates on the same visual grammar, scale, criteria, and labeling. A comparison rubric is useful only when multiple viable candidates remain and several independent criteria can change the result; hard gates are not scored or averaged away.

## Mass / concentration and cross-section

Use visual weight only from supplied evidence when the reader must see where complexity/state/dependencies concentrate. Use a cross-section when several concerns cross one boundary—identity, data, trust, lifecycle, failure, migration, or proof.

## Renderer selection

Once the representation is chosen, read [representation capabilities](representation-capabilities.md) when a mature grammar/renderer could materially improve it. Renderer choice is not representation choice, and delivery/runtime policy must not force a weaker representation merely because native HTML is available.

## Choose prose when prose is better

Do not create a visual when:

- no meaningful relationship is supplied;
- the visual only restates a short list;
- exact wording is the evidence;
- source evidence cannot support the implied state/causal/scale/ownership relation; or
- the diagram would require invented structure.

## Verification cue

The representation must encode a material supplied relationship and preserve provenance. Structural proof checks the modeled relationship and source mapping; render/runtime proof is proportional to browser-dependent claims introduced by the chosen renderer or interaction.
