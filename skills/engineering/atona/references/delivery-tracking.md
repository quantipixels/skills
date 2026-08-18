# Delivery tracking

Use this contract when the user requests tickets, the plan has multiple review candidates, dependencies, implementers, or a multi-session handoff, or implementation authority is granted.

## Reconcile tickets

Use `seda-ticket` before setting a plan with material delivery coordination to `Planned`. Give it the settled scope, constraints, candidates, dependencies, acceptance, proof, and rollback boundaries. Verify that confirmed tickets cover the plan, persist them in the live plan, and keep the plan in `Draft` while the breakdown is missing, ambiguous, incomplete, or cyclic. `atona` retains plan identity, readiness, grouping, persistence, and state.

Persist each ticket's current lifecycle fields and reconcile valid transition results for plan awareness. Delegate ticket-state updates only for exact tickets and permitted transitions. Cancellation requires separate explicit authority. Without delegated write authority, require the delivery owner to return the requested transition and evidence for `atona` to apply.

Before persisting a transition, refresh ticket identity, current state, dependency states, evidence, authority, and the exact-current `seda-ticket` lifecycle supplied with the confirmed ticket set. Reject a transition that this evidence does not permit. Persist only the lifecycle fields and evidence that its resulting state requires; do not restate or independently evolve their derivation. Ticket state never sets plan or phase state, implementation authority, or implementation completion; `atona`'s readiness, integration, proof, and review gates remain authoritative.

## Track authorized implementation

Keep the request, decisions, evidence, risks, phases, candidate, proof gaps, documentation destinations, and lifecycle states current in the plan. Remove stale guidance and redundant snapshots.

Require explicit implementation authority. Immediately before the first edit, set implementation to `Started` and record the date, candidate branch and commit or tree state, phase, and authority. Investigation, clarification, and plan edits do not start implementation.

Translate each delivery phase into one or more stable, self-contained review candidates. Give each candidate its scope, dependencies, acceptance behavior, proof, and rollback boundary. Do not make every TDD slice or local commit an `alaga` invocation, and do not force a whole phase into one candidate when it contains independent reviewable changes. Keep phase-level integration and acceptance proof in the plan.

Use `audit-refactor-behavior` before a stateful refactor that can change transitions, ordering, locking, retries, idempotency, ownership, or cross-entry behavior. Use `alaga` for bounded test-first implementation and when one supplied build job must compose and deliver the planned candidate or candidate set through proof and the review required for each candidate type. When `alaga` is already an active ancestor for the same job, return the implementation request to it instead of invoking it again.

For work owned by another skill, record its owner, scope, evidence, blocked outcome, and required result. Keep test, review, build, commit, and publication procedures with their owners.

Treat internal `alaga` tasks, test-first slices, tests, and commits as delivery detail, not `atona` tickets. Record them only when the plan promotes the work to a blocker, handoff seam, material plan change, or independent review candidate. Accept optional exact-current Git evidence returned by a delivery owner without prescribing or performing Git operations.

Verify each specialist result against current plan identity and candidate before recording state or evidence. Reject a mismatch as stale and rerun affected readiness or closure checks. Set implementation to `Complete` only after every final in-scope candidate has the exact-current accepting or closed review result required by its type and contract, and phase-level integration proof has no blocking evidence gap. For a code candidate, this includes `qp-code-review: RECOMMEND_ACCEPT`. Reuse a verified current result. Skip this gate when implementation is `Not Required`.
