---
name: seda-spec
description: Create or refine one confirmed, implementation-independent behavior specification from supplied intent and evidence. Use when material behavior or operating rules need a normative contract for planning, design, delivery, or review; exclude initiative lifecycle, decision interviews, specialist design, delivery decomposition, execution, and provider publication.
---

# Ṣẹ̀dá Spec

Turn supplied intent into one compact behavior specification that a fresh human or agent can use as an independent delivery and review oracle. Own normative behavior, scope, examples, acceptance, proof traceability, and specification readiness.

Keep initiative lifecycle, consequential user-choice closure, specialist design, delivery decomposition, execution/proof, durable project knowledge, persistence mechanics, and external publication outside the specification result.

## Establish the contract boundary

Pin:

- the supplied conversation, issue, plan, policy, procedure, existing specification, or other inputs and their identities when available;
- intended actors and use;
- current behavior/rule or gap and desired observable outcome;
- freshness, version, compatibility, or changeover boundaries when material; and
- confirmed authority, inferences, and unresolved material questions.

Use settled context directly. Do not replay discovery or start an interview merely because the source is conversational. Inspect the current work context only enough to use established vocabulary, behavior, governing decisions, interfaces, and proof/evidence seams accurately. In repository work this may include code, tests, ADRs, schemas, configuration, and history; none is required merely because Ṣẹ̀dá Spec is active.

Current implementation or operating practice is evidence of existing behavior, not automatic authority for desired behavior. Do not turn implementation detail into a requirement unless the supplied or confirmed contract requires it.

## Place and retire the specification

Use the existing or user-selected specification destination when one exists. Otherwise choose the smallest placement that preserves the specification for its real consumers:

- keep it inline for one immediate bounded use and return a stable content digest/identity when needed downstream;
- use the active host/project's normal durable document or knowledge surface when the specification must survive the current context;
- when the selected destination is a repository-scoped QP workspace, resolve a working record through `akosile` with `owner: seda-spec`, `record_type: behavior-spec`, and a stable behavior identity; or
- use an external/provider destination only when explicitly selected and an authorized publication owner performs the write.

A working or transient record is not automatically durable authority. While planning, delivery, or review depends on the specification, retain its exact identity and current content. When the specification itself must remain normative after delivery, preserve it in its established durable destination; for change-specific specifications, preserve required history and mark supersession rather than silently deleting the contract.

## Specify observable behavior

Write only the material contract:

- problem/gap, actors, outcome, scope, and non-goals;
- triggers and preconditions;
- observable results and externally meaningful state transitions;
- applicable normal, failure, misuse, recovery, compatibility, and changeover scenarios;
- invariants and boundary conditions;
- concrete examples where rules remain ambiguous without them;
- acceptance conditions and the highest stable proof/evidence seam for each material behavior; and
- unresolved questions, assumptions, evidence limits, and source identities.

Give each material behavior a stable short identity when downstream delivery, proof, review, or later revisions need traceability. Keep examples normative only when the specification labels them as such. Do not require user-story phrasing, exhaustive scenario taxonomies, or implementation structure when a shorter observable contract is unambiguous.

A specification defines what must be true. It does not choose modules, teams, dependencies, algorithms, schemas, deployment topology, ticket boundaries, proof mechanics, or delivery order unless one of those is itself a confirmed externally observable constraint.

## Resolve material gaps

Separate confirmed behavior from inference. Resolve discoverable facts directly or through `iwadi` when substantial reusable research is needed. Use `arojinle` for unresolved consequential user decisions. Use the current specialist when specification readiness depends on an independently useful design result; software/system technical architecture belongs to `solution-architect`.

Do not fill a gap with a plausible requirement. If a material behavior cannot be specified without invention, keep the gap visible and return `SPEC_NOT_READY`.

## Judge readiness

Return one result:

- `SPEC_READY` — every in-scope material behavior is observable, internally consistent, traceable to current authority, and mapped to a credible proof/evidence seam; no unresolved material decision or evidence gap remains.
- `SPEC_NOT_READY` — name each blocking ambiguity, conflict, missing authority, or evidence gap and the owner/evidence needed to resolve it.

Tests are one possible evidence type against a specification, not a universal source from which desired expectations are reverse-engineered. A ready specification grants no specialist-design, delivery, publication, or unrelated persistence authority. Write only to a destination covered by the request/caller authority.

Return the specification, result, exact source identities, destination/persistence shape, current or superseded state, unresolved limits, and the next owner when one is required. When downstream work depends on it, also return its stable identity, revision, or content digest.
