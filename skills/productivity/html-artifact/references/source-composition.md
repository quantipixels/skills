# Source composition

Read this for a substantial, evidence-heavy, living, reused, or owner-record input. Preserve authority and retrievability while deliberately denormalizing the meaning a human needs to judge the current outcome.

## Treat HTML as a read model

An artifact is a purpose-shaped read model over supplied sources, not their archive or semantic source of truth. Canonical records/results remain normalized with their owners; HTML may intentionally repeat concise decision-relevant meaning when colocation materially improves human understanding.

`html-artifact` may group, deduplicate, order, summarize, aggregate, select representative evidence, assign placement, and choose representation. It may not create a domain conclusion, causal claim, decision, priority, owner, status, readiness, confidence, or recommendation absent from the source owner/caller.

## Pin the conversion contract

Establish:

```text
Primary reader / stakeholder
Current concern and judgment/action
Governing question
Artifact thesis
Evidence cutoff and authority
Projection/evidence cut across composed sources
Human-visibility obligations supplied by the caller
Dominant supplied relationships
First-viewport obligation
Snapshot or living view
Lifecycle stage, when supplied
```

The thesis is one source-supported sentence: this artifact helps `<reader>` `<act/judge>` by showing `<result or relationship>`. Every foreground element must advance that reader job.

When owner records/results exist, read them before raw evidence. Pin owner, type, title, revision/status, updated time, candidate when supplied, linked records/evidence, and any projection brief. If sources were produced against incompatible controlling revisions, do not silently call the composition current: identify the stale/partial dependency or obtain a coherent cut first.

For a lifecycle record, a status/gate transition may change reader concern, first viewport, density, representation, and foreground material. Preserve source identity and useful anchors, but recompute the visual argument rather than accumulating earlier stages.

## Classify source units

Identify meaningful units such as facts, findings, decisions, status, blockers, actions, constraints, risks, assumptions, events, evidence, examples, logs, and superseded conclusions. Group equivalent statements and retain the strongest current formulation plus source identity.

For substantial work decide independently:

### Coverage

- `Complete` — required meaning and proof/retrieval path are preserved.
- `Partial` — required source, condition, or detail is unavailable/stale.
- `Input gap` — sources cannot support a required claim or representation.
- `Excluded` — scope or authority excludes the unit; retain the reason when material.

### Placement

- `Foreground` — needed for current judgment/action or to understand a limiting claim.
- `Supporting` — needed for rationale, trade-offs, confidence/counterevidence, or context.
- `Evidence` — needed to verify a material claim rather than first-pass comprehension.
- `Source-only` — safely retrievable detail whose omission cannot change the current judgment.
- `Archive` — raw/exhaustive evidence outside the working view.
- `Superseded` — retained through history/source linkage, not current.

### Fidelity

- `Exact` — identifiers, quantities, statuses, accepted wording, code/schema/conditions must remain precise.
- `Meaning-preserving` — summarize without changing implication, uncertainty, exceptions, or scope.
- `Aggregate` — combine repeated instances while preserving denominator/grouping rule/exceptions.
- `Representative` — show selected examples, selection basis, and complete inventory locator.
- `Pointer` — retain identity, role, freshness, and retrieval path with bounded summary.
- `Omit` — duplicate, irrelevant, invalid, or out-of-scope material.

## Human-critical closure

A unit is human-critical when omission could materially change the reader's judgment of outcome/scope, current gate, consequential decision, contract sufficiency, architecture/design condition, delivery state, proof strength, risk/recovery, freshness, or next action.

A human-critical unit cannot be satisfied only by `Source-only`, `Archive`, or a bare `Pointer`. Show its decision-relevant meaning in `Foreground` or `Supporting` placement and attach the canonical provenance. The complete packet may remain linked.

Caller-supplied visibility obligations override generic compression. Do not interpret “avoid duplication” as “hide critical meaning.” Conversely, human-critical closure does not authorize copying entire linked Markdown files; retain only the meaning required for the reader's current judgment.

## Keep evaluation semantics honest

Preserve semantic distinctions supplied by owners:

- **verdict** — what evidence establishes;
- **confidence** — strength/limits of that evidence or judgment;
- **grade/score** — comparative performance against an explicit rubric;
- **gate** — mandatory condition that cannot be averaged away;
- **readiness** — whether progression is currently justified;
- **evidence gap** — missing proof capable of changing the result;
- **epistemic status** — observed, inferred, proposed, or illustrative.

Do not derive one from another or turn them into a generic health score. When a hard gate or weakest material claim controls progression, foreground it instead of averaging it with supported claims.

## Build the human working view

Use progressive disclosure:

```text
Visible now
→ everything required to judge current state/gate/outcome

One action away
→ supporting rationale, important alternatives, counterevidence, detailed proof

Canonical source
→ exhaustive logs, complete packets, historical/archive evidence
```

Blocking, conditional, stale, or unproved information that can change the current judgment must not be hidden inside disclosure controls.

Choose representation per material relationship, not source section. One section can need several representations; several records/sections can collapse into one traceability, comparison, timeline, or assurance view when that improves comprehension without changing meaning.

For substantial artifacts embed a compact `application/json` context capsule before large presentation resources. Include identity, owner source revisions, purpose, current status/outcome, blockers/next action, high-value source locators, projection cut, and proof freshness. Exclude complete records, inventories, logs, archives, credentials, secret-bearing URLs, unnecessary personal data, and machine-local absolute paths.

## Living projections: delta first

After the first complete projection, prominently show material delta from the prior useful view: changed decisions, reopened/stale claims, new candidate/evidence, closed proof, new blockers, and changed next action. Reuse unchanged supporting material at lower visual weight rather than making the reader rediscover change by rereading the whole page.

The owner updates semantic truth first. Regenerate after material semantic revisions when the projection is maintained. An older projection may remain available as visibly stale evidence; it is not a current handoff.

## Projection coverage proof

For caller-supplied or derived human-critical obligations, keep an internal coverage map:

```text
obligation identity
source owner/revision/candidate
meaning that must remain visible
why omission could change judgment
visible placement / representation
provenance locator
coverage: present | partial | stale | missing
```

Before delivery require every material obligation to be `present`, or expose the `partial/stale/missing` state as an input/projection gap. Do not add a runtime/schema merely for this map; deterministic machinery must earn itself from recurring failures.

## Keep living projections honest

Run structural checks after every projection write. Apply the parent verification boundary: static information projections normally stop at structural proof plus at most one bounded render smoke when readability is materially uncertain; interactive projections prove only the material interaction claims they introduce.

Before delivery test:

- **critical closure:** no human-critical obligation is pointer-only or silently omitted;
- **coherence:** composed sources form a declared current cut, or stale/partial dependencies are visible;
- **agent entry:** current state, weakest limiting claim, and next action are available without reading full HTML when applicable;
- **retrieval:** requested detail is obtainable through a canonical source path;
- **faithfulness:** material claims trace to current source meaning and epistemic status;
- **counterevidence:** material conditions/limits are not hidden by presentation;
- **context hygiene:** raw archives are absent unless required;
- **deletion:** each foreground element earns its place;
- **stage/viewpoint fit:** opening, representation, tone, and action layer serve the current reader concern; and
- **verification fit:** reported proof matches the accepted browser claims rather than artifact size or formality.
