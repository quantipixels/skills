# Semantic contracts, not page designs

Choose only the matching job. Combine obligations when the source genuinely combines jobs; do not assemble every section below. Existing owner authority and source fidelity govern all five contracts.

| Job / trigger | Required meaning and relationship | Useful starting form | Prove the reader can… |
| --- | --- | --- | --- |
| Plan / status: decide what happens next | Outcome, current state, next action, blockers, owned decisions and proof freshness. Planned, built, tested and live remain distinct. | Outcome-led document, dependency flow, a compact change lens for supplied revisions. | Identify the next action and its actual prerequisite without reading an archive. |
| Comparison: choose between supplied alternatives | Same criteria, units and evidence cut; differences, constraints, counterevidence and supported recommendation. | Aligned matrix or paired specimens; optional same-frame switching with stable labels. | Compare a material difference without memorising a hidden alternative. |
| Evidence / assurance: inspect a conclusion | Claim → evidence → disposition; uncertainty and missing or stale support adjacent to affected claims. | Trace table or connected evidence view with optional detail selection. | Trace a conclusion to its exact evidence and see what is not proved. |
| Mechanism / explanation: understand how or why | Actors or states, inputs, transitions, branches and outcomes supported by the source. Simulation is labelled separately. | Sequence, state or flow diagram; optional guided walkthrough retaining an overview. | Follow the consequential branch, not just read a list of boxes. |
| Timeline / change: understand progression | Ordered events, time basis, material changes and provenance. Time order alone is not causation. | Timeline or before/after with explicit dates and revision identity. | Locate the turning point, its consequence and any causal uncertainty. |

## Fixed contract / free canvas

The meaning above is fixed only when applicable. No mandatory hero, card count, section order, font, palette, radius, chart quota or animation follows from it. Typography, spacing, illustration, density and spatial composition can carry the argument. A compact paragraph can fulfil a compact job.

For an extracted template record: trigger, reader job, required slots/relationships, optional parts, fallback, proof and degrees of freedom. Omit empty optional slots. Do not turn this into metadata required on every generated page.

Examples:

- Good comparison: aligned security, recovery and cost differences, with limitations beside them. An editorial split, a table or an overlay may all work.
- Bad comparison: three independently styled sales cards hiding different caveats behind hover.
- Good mechanism: labelled retry edge returns to the operation whose idempotency matters.
- Bad mechanism: five rounded boxes titled Step 1–5 with the real branching buried in prose.

## Starter specimen: evidence trace

Use this semantic shape when it helps. Restyle, condense or use a diagram without losing its links. IDs and statements below are illustrative, not project facts.

```html
<table>
  <caption>Evidence for the retry guarantee</caption>
  <thead><tr><th scope="col">Claim</th><th scope="col">Evidence</th><th scope="col">Disposition</th></tr></thead>
  <tbody><tr><th scope="row">One durable result per key</th><td><a href="#retry-proof">Controlled duplicate request</a></td><td>Proved for this candidate</td></tr></tbody>
</table>
```

This is a content contract, not permission to claim the illustrative result occurred.
