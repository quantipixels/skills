# Behavior contract

Turn supplied intent into a compact, implementation-independent specification that a fresh delivery or review owner can use as an oracle. Own normative behavior, scope, examples, acceptance, proof traceability and readiness; exclude initiative lifecycle, architecture, decomposition, execution and publication.

Pin the authoritative inputs and identities, actors, current gap, desired observable outcome, material freshness/compatibility boundary, confirmed authority, inferences and unresolved questions. Use settled context directly. Inspect code, tests, schemas, history or other project evidence only where they clarify established behavior, vocabulary or proof seams. Current implementation is evidence of existing behavior, not authority for desired behavior.

Persist at an established specification destination, otherwise `.qp/atona/contracts/`; existing `.qp/seda-spec/` records remain valid migration inputs. A transient record is not automatically durable authority. Preserve a normative contract or required change history at its established destination and mark supersession rather than silently deleting it.

Specify only material:

- problem, actors, outcome, scope and non-goals;
- triggers, preconditions, observable results and externally meaningful state transitions;
- applicable normal, failure, misuse, recovery, compatibility and changeover scenarios;
- invariants, boundaries and concrete examples needed to remove ambiguity;
- acceptance plus the highest stable evidence seam for each material behavior; and
- source identities, assumptions, unresolved questions and evidence limits.

Give material behaviors stable short identities when downstream traceability needs them. Label whether examples are normative. Walk a concrete actor through ambiguous flows, including retry and recovery effects, but do not invent a requirement or prescribe modules, algorithms, schemas, ticket boundaries, tests or delivery order unless externally observable constraints require them.

Separate confirmed behavior from inference; use `amose`, `iwadi`, `arojinle` or `architect` only for the missing result they own. Return:

- `SPEC_READY` when every in-scope material behavior is observable, consistent, traceable to current authority and mapped to a credible evidence seam; or
- `SPEC_NOT_READY` with each blocking ambiguity, conflict, missing authority or evidence gap and its owner.

Tests may prove the specification but do not define desired behavior automatically. Readiness grants no design, delivery, publication or unrelated persistence authority. Return the specification, result, exact source identities, destination/state, limits and next owner; include a stable identity, revision or digest when downstream work depends on it.
