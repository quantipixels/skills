# Delivery tracking

Use this contract when the user requests tickets, the plan has multiple delivery candidates, dependencies, implementers, or a multi-session handoff, or delivery authority is granted.

## Reconcile tickets

Use `seda-ticket` before setting a plan with material delivery coordination to `Planned`. Give it the settled scope, constraints, candidates, dependencies, acceptance, proof, and rollback boundaries. Verify that confirmed tickets cover the plan. Keep the plan in `Draft` while the breakdown is missing, ambiguous, incomplete, or cyclic.

Record the ticket-set identity, current native states, dependency frontier, blockers, evidence, and plan effect. Keep provider-native fields and transition mechanics outside the plan. Before recording a transition receipt, refresh the ticket identity, dependency states, evidence, authority, and exact-current `seda-ticket` lifecycle. Reject a transition that this evidence does not permit. Cancellation requires separate explicit authority.

Ticket state never sets plan status, phase state, delivery authority, or the derived delivery summary. `atona` retains plan identity, grouping, readiness, integration, and closure.

## Track authorized delivery

Keep the request, decisions, evidence, risks, phases, receipt ledger, proof gaps, documentation destinations, and delivery summary current. Remove stale guidance and redundant snapshots.

Require explicit delivery authority. Immediately before the first source or external edit, record the authority, date, delivery owner, exact branch and commit or tree candidate, and affected phase. Set the plan to `In Progress` when authorized delivery starts. Investigation, clarification, and plan edits do not start delivery.

Give each delivery owner the exact plan identity, settled scope, dependencies, acceptance behavior, proof, and rollback boundary. The delivery owner shapes and reviews its candidates. `atona` groups their plan effects and retains phase-level integration and acceptance.

Use `alaga` when one supplied build job must deliver a candidate or candidate set through proof and the review required by its type. When an active Atọ́nà plan governs the job, require an exact-current contribution receipt instead of a parallel user-facing job report. Keep test-first slices, tests, commits, snapshots, review mechanics, and job recovery inside the delivery owner.

For work owned by another skill, record its owner, scope, exact candidate, native result, evidence, blocker, plan effect, and required next action. Do not copy the owner's procedure or state machine.

Verify every receipt against the current plan revision and candidate before using it. Reject a mismatch as stale. Reopen affected readiness, phases, proof, and summaries. Derive `Complete` only after every in-scope candidate has its required exact-current accepting result and phase-level integration proof has no blocking gap. Derive `Not required` only when the accepted plan contains no delivery work.
