# Behavior contract

Read [planning inputs](../references/productivity/planning/planning-inputs.md). Return the standalone behavior contract. Do not start an initiative, ticket decomposition or require a living HTML plan.

Turn supplied intent into one compact behavior specification that a fresh human or agent can use as an independent delivery and review oracle. Own normative behavior, scope, examples, acceptance, proof traceability, and specification readiness.

Delegate independent contract extraction or edge-case investigation to subagents when useful. Integrate their findings and source evidence into one consistent specification.

Keep initiative lifecycle, consequential user-choice closure, specialist design, delivery decomposition, execution/proof, durable project knowledge, persistence mechanics, and external publication outside the specification result.

## Establish the contract boundary

Pin:

- the supplied conversation, issue, plan, policy, procedure, existing specification, or other inputs and their identities when available;
- intended actors and use;
- current behavior/rule or gap and desired observable outcome;
- freshness, version, compatibility, or changeover boundaries when material; and
- confirmed authority, inferences, and unresolved material questions.

Use settled context directly. Do not replay discovery or start an interview merely because the source is conversational. Inspect the current work context only enough to use established vocabulary, behavior, governing decisions, interfaces, and proof/evidence seams accurately. In repository work this may include code, tests, ADRs, schemas, configuration, and history; none is required merely because behavior-contract mode is active.

Current implementation or operating practice is evidence of existing behavior, not automatic authority for desired behavior. Do not turn implementation detail into a requirement unless the supplied or confirmed contract requires it.

## Place and retire the specification

Use the existing or selected specification destination; otherwise follow [records](../references/productivity/records.md) when the contract must be saved for downstream work. Existing `.qp/seda-spec/` records remain valid inputs.

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

When a flow is ambiguous, walk one concrete actor from its actual entry point through material branches to success, rejection, cancellation or recovery. Compare each step with the specified behavior and shared handling already provided by the project. For example, a timed-out request may leave a completed remote effect: what can the caller safely retry, and what result should it observe? Name that specific unresolved decision and its consequence; do not add generic edge-case questions or turn a plausible default into an accepted requirement.

A specification defines what must be true. It does not choose modules, teams, dependencies, algorithms, schemas, deployment topology, ticket boundaries, proof mechanics, or delivery order unless one of those is itself a confirmed externally observable constraint.

## Resolve material gaps

Separate confirmed behavior from inference. Route domain identity, lifecycle, policy or rule-applicability gaps to [amose](amose.md); substantive external facts to [iwadi](iwadi.md); unsettled desire, success, trade-offs or latent choices to [arojinle](arojinle.md); and structure or technical-fitness gaps to [architect-design](architect-design.md). Reuse current accepted results and return newly exposed controlling gaps to the same caller rather than starting a competing initiative.

Do not fill a gap with a plausible requirement. If a material behavior cannot be specified without invention, keep the gap visible and return `SPEC_NOT_READY`.

## Judge readiness

Return one result:

- `SPEC_READY` — every in-scope material behavior is observable, internally consistent, traceable to current authority, and mapped to a credible proof/evidence seam; no unresolved material decision or evidence gap remains.
- `SPEC_NOT_READY` — name each blocking ambiguity, conflict, missing authority, or evidence gap and the owner/evidence needed to resolve it.

Tests are one possible evidence type against the specification, not a universal source from which desired expectations are reverse-engineered. A ready specification grants no specialist-design, delivery, publication, or unrelated persistence authority. Write only to a destination covered by the request/caller authority.

Return the specification, result, exact source identities, destination/persistence shape, current or superseded state, unresolved limits, and the next owner when one is required. When downstream work depends on it, also return its stable identity, revision, or content digest.
