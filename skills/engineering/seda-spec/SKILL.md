---
name: seda-spec
description: Create or refine one confirmed, implementation-independent behavior specification from supplied intent and evidence. Use when material behavior needs a normative contract for planning, architecture, ticket decomposition, implementation, or review; exclude initiative lifecycle, decision interviews, technical design, ticketing, implementation, persistence, and publication.
---

# Ṣẹ̀dá Spec

Turn supplied intent into one compact behavior specification that a fresh human or agent can use as an independent implementation and review oracle. Own normative behavior, scope, examples, acceptance, proof traceability, and specification readiness.

Do not absorb adjacent outcomes:

- `atona` owns initiative lifecycle;
- `arojinle` owns unresolved consequential user choices;
- `solution-architect` owns technical design;
- `seda-ticket` owns delivery decomposition;
- `alaga` owns implementation and proof;
- `amose` owns durable project/domain truth; and
- the caller's authorized owner owns storage and publication.

## Establish the contract boundary

Pin:

- the supplied conversation, issue, plan, existing specification, or other inputs and their identities when available;
- intended actors and use;
- current behavior or gap and desired observable outcome;
- freshness, version, and compatibility boundaries; and
- confirmed authority, inferences, and unresolved material questions.

Use settled context directly. Do not replay discovery or start an interview merely because the source is conversational. Inspect the repository only enough to use current vocabulary, behavior, ADRs, interfaces, and proof seams accurately.

Current code is evidence of existing behavior, not automatic authority for desired behavior. Do not turn implementation details into requirements unless the supplied or confirmed contract requires them.

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

Tests are evidence against the specification, not the source from which desired expectations are reverse-engineered. A ready specification does not grant architecture, implementation, persistence, provider, or publication authority.

Return the specification, result, exact source identities, unresolved limits, and the next owner when one is required. When downstream work will depend on the specification, also return its stable identity, revision, or content digest. The caller decides whether to keep the specification inline, persist it, or link it from an initiative plan.
