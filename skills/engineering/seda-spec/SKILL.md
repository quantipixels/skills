---
name: seda-spec
description: Create or refine one confirmed, implementation-independent behavior specification from supplied intent and evidence. Use when material behavior needs a normative contract for planning, architecture, ticket decomposition, implementation, or review; exclude initiative lifecycle, decision interviews, technical design, ticketing, implementation, and provider publication.
---

# Ṣẹ̀dá Spec

Turn supplied intent into one compact behavior specification that a fresh human or agent can use as an independent implementation and review oracle. Own normative behavior, scope, examples, acceptance, proof traceability, and specification readiness.

Keep initiative lifecycle, consequential user-choice closure, technical design, delivery decomposition, implementation/proof, durable project knowledge, workspace mechanics, and provider publication outside the specification result.

## Establish the contract boundary

Pin:

- the supplied conversation, issue, plan, existing specification, or other inputs and their identities when available;
- intended actors and use;
- current behavior or gap and desired observable outcome;
- freshness, version, and compatibility boundaries; and
- confirmed authority, inferences, and unresolved material questions.

Use settled context directly. Do not replay discovery or start an interview merely because the source is conversational. Inspect the repository only enough to use current vocabulary, behavior, ADRs, interfaces, and proof seams accurately.

Current code is evidence of existing behavior, not automatic authority for desired behavior. Do not turn implementation details into requirements unless the supplied or confirmed contract requires them.

## Place and retire the specification

Use the project's existing specification destination or the user's explicit destination when one exists. Otherwise choose the smallest placement that preserves the specification for its actual consumers:

- keep it inline only for one immediate bounded use, and return a content digest;
- for reusable downstream work with no durable project convention, resolve a QP working record through `akosile`:

  ```text
  owner: seda-spec
  record_type: behavior-spec
  subject: <stable behavior identity>
  ```

- use a versioned project document, when write authority exists, if the specification itself must remain normative after delivery; or
- use an issue or another durable provider record only when the user requests that destination and an authorized provider owner publishes it.

An untracked `.qp` record is working memory, not durable repository knowledge. While planning, tickets, implementation, or review depend on the specification, retain its exact identity and current content. At lifecycle closure, keep a lasting specification in its versioned or authorized durable destination. For a change-specific specification, preserve any required history, reconcile enduring knowledge into its natural project owners, and mark the specification superseded instead of silently deleting it.

## Specify observable behavior

Write only the material contract:

- problem or gap, actors, outcome, scope, and non-goals;
- triggers and preconditions;
- observable results and externally meaningful state transitions;
- applicable normal, failure, misuse, recovery, and compatibility scenarios;
- invariants and boundary conditions;
- concrete examples where rules remain ambiguous without them;
- acceptance conditions and the highest stable proof seam for each material behavior; and
- unresolved questions, assumptions, evidence limits, and source identities.

Give each material behavior a stable short identity when tickets, tests, reviews, or later revisions need traceability. Keep examples normative only when the specification labels them as such. Do not require user-story phrasing, exhaustive scenario taxonomies, or implementation structure when a shorter observable contract is unambiguous.

A specification defines what must be true. It does not choose modules, dependencies, algorithms, schemas, deployment topology, ticket boundaries, test mechanics, or delivery order unless one of those is itself a confirmed externally observable constraint.

## Resolve material gaps

Separate confirmed behavior from inference. Resolve discoverable facts directly or through `iwadi` when substantial reusable research is needed. Use `arojinle` for unresolved material user decisions and `solution-architect` when defining the behavior depends on a material technical-design result.

Do not fill a gap with a plausible requirement. If a material behavior cannot be specified without invention, keep the gap visible and return `SPEC_NOT_READY`.

## Judge readiness

Return one result:

- `SPEC_READY` — every in-scope material behavior is observable, internally consistent, traceable to current authority, and mapped to a credible proof seam; no unresolved material decision or evidence gap remains.
- `SPEC_NOT_READY` — name each blocking ambiguity, conflict, missing authority, or evidence gap and the owner or evidence needed to resolve it.

Tests are evidence against the specification, not the source from which desired expectations are reverse-engineered. A ready specification does not grant architecture, implementation, provider publication, or unrelated persistence authority. Write only to a selected destination covered by the request or caller's authority.

Return the specification, result, exact source identities, destination and persistence shape, current or superseded state, unresolved limits, and the next owner when one is required. When downstream work will depend on the specification, also return its stable identity, revision, or content digest.
