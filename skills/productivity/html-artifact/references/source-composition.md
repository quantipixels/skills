# Source composition

Read this for a substantial, evidence-heavy, living, reused, or owner-record input. Preserve meaning and retrievability without reproducing source volume.

## Treat HTML as a view

An artifact is a purpose-shaped view over supplied sources, not their default archive. Preserve material meaning, exact obligations, decisions, status, exceptions, uncertainty, evidence relationships, and retrieval paths. Do not preserve source order, prose volume, table shape, or log volume merely because it was supplied.

`html-artifact` may group, deduplicate, order, summarize, aggregate, select representative evidence, assign presentation placement, and choose representation. It may not create a domain conclusion, causal claim, decision, priority, owner, status, or recommendation absent from the source owner.

## Pin the conversion contract

Establish:

```text
Primary reader and outcome
Governing question
Artifact thesis
Evidence cutoff and authority
Dominant supplied relationship
First-viewport obligation
Snapshot or living view
Lifecycle stage and reader job, when supplied
```

The thesis is one source-supported sentence: this artifact helps `<reader>` `<act>` by showing `<result or relationship>`. Every foreground section must advance it.

When an owner record exists, read it before raw evidence. Pin owner, record type, title, revision, status, updated time, candidate when supplied, `Resume`, linked records/evidence, and projection brief. If record and HTML disagree, the record wins.

For a lifecycle record, do not freeze one information direction across all stages. A status transition may change the reader's job, purpose, tone, density, layout, governing representation, and foreground material. Preserve the same record identity, projection path, source disclosure, and useful anchors, but recompute the visual argument from the owner-supplied stage brief.

When the owner requires a continuously available human view, create the first projection from the first meaningful record revision and regenerate it after every material semantic revision. A temporarily stale projection may exist after a failed render, but it is not a current accessible handoff.

## Classify source units

Identify meaningful units such as facts, findings, decisions, status, blockers, actions, constraints, risks, assumptions, events, evidence, examples, notes, logs, sources, and superseded conclusions. Group equivalent statements and retain the strongest current formulation plus source references.

For substantial work, decide three independent properties:

### Coverage

- `Complete` — required meaning and proof path are preserved.
- `Partial` — required source, condition, or detail is unavailable.
- `Input gap` — sources cannot support a required claim or representation.
- `Excluded` — scope or authority excludes the unit; retain the reason when material.

### Placement

- `Foreground` — needed for outcome comprehension or next action.
- `Supporting` — needed for rationale, trade-offs, confidence, or context.
- `Evidence` — needed to verify a material claim, not for first-pass comprehension.
- `Source-only` — covered by a reliable source and not duplicated.
- `Archive` — raw or exhaustive evidence outside the working view.
- `Superseded` — retained through history/source linkage, not current.

### Fidelity

- `Exact` — preserve identifiers, quantities, statuses, accepted wording, code, schema, or conditions precisely.
- `Meaning-preserving` — summarize without changing scope, implication, uncertainty, or exceptions.
- `Aggregate` — combine repeated instances while preserving denominator, grouping rule, and exceptions.
- `Representative` — show selected examples, state the basis, and link the complete inventory.
- `Pointer` — retain identity, role, freshness, and retrieval path with a bounded summary.
- `Omit` — remove duplicate, irrelevant, invalid, or out-of-scope material.

A unit can be `Complete`, `Source-only`, and `Pointer`. Full coverage does not require co-location. An in-page anchor or collapsed `<details>` does not reduce HTML or future-agent context.

## Decide relevance

Apply in order:

1. Would omission change the reader's decision, action, verification, monitoring, comparison, or understanding?
2. Could omission cause unsafe, invalid, irreversible, financial, or incomplete action?
3. Does it constrain interpretation?
4. Is it minimum proof for a material claim?
5. Is it current and authoritative for this candidate?
6. Does it add unique meaning?
7. Can complete detail be retrieved reliably elsewhere?

Foreground current outcome, decisions, status, blockers, warnings, next action, governing relationship, and material exceptions. Summarize key evidence. Aggregate repeated findings. Use aligned comparison for repeated candidates. Include only necessary code fragments. Keep raw logs, transcripts, exhaustive inventories, and routine history linked unless exact inline inspection is required.

## Build two useful resolutions

### Human working view

Show thesis, outcome, governing representation, material exceptions, action, and concise navigation. It must be complete for the reader's current purpose. For living lifecycle records, the working view should evolve with the reader's stage-specific job rather than accumulate every earlier stage as equal-weight content.

### Agent context capsule

For substantial artifacts, embed compact `application/json` before large presentation resources. Include identity, owner record path/revision, purpose, current status/outcome, blockers, next action, completion condition, high-value source locators, projected source revision, and proof freshness. Exclude the complete record, inventories, logs, and archives.

Link supporting records/evidence with stable relative paths or pinned provider identities. Keep credentials, secret-bearing URLs, unnecessary personal data, machine-local absolute paths, and protected locators out of shared HTML.

## Compose around one relationship

Choose one dominant supplied relationship or result and let it organize the artifact. Supporting sections explain meaning, confidence, exceptions, action, and evidence. Do not add a central visual and then repeat every source unit below it.

Use a matrix, timeline, state map, flow, comparison, architecture map, chart, or another form when it replaces repeated prose. Change form on narrow screens when containment would hide the relationship.

For each foreground section ask: if removed, would decision, action, understanding, verification, or trust materially worsen? If not, demote, link, merge, or remove it.

## Keep living projections honest

The owner updates `record.md` first. The projection records its source path and revision. Regenerate after each material semantic revision when continuous accessibility is required.

Run structural checks after every projection write. Run targeted browser checks after presentation-affecting changes. Run full checks for the first substantial render, lifecycle transitions that change information direction, and applicable formal-review, readiness, terminal, or publication gates.

Within one stage, a semantic update may reuse current browser proof when presentation structure and risk remain unchanged. The regenerated HTML still needs exact source revision/status disclosure. If regeneration fails, keep the older file visibly stale and report the accessible view as incomplete.

Before delivery test:

- **agent entry:** current state and next action are available without reading full HTML;
- **retrieval:** one requested detail is obtainable through a source link;
- **faithfulness:** material claims trace to current source meaning;
- **context hygiene:** raw archives are absent unless required;
- **deletion:** each foreground section earns its place;
- **stage fit:** the opening, representation, tone, and action layer serve the current lifecycle stage rather than an earlier one.
