# Delivery tracking

Use this contract when the plan has material delivery coordination: tickets, multiple candidates or owners, dependencies, a multi-session handoff, or delivery authority.

## Decompose delivery when needed

Use `seda-ticket` when the settled plan needs consumable delivery tickets. Give it the scope, constraints, dependencies, acceptance, proof, and rollback boundaries. Consume its current ticket set and startable frontier; do not reproduce its lifecycle or transition rules here.

Keep the plan in `Draft` while required decomposition is missing, ambiguous, incomplete, or cyclic. Ticket state never sets plan status, phase state, delivery authority, or Atọ́nà's delivery summary.

## Track authorized delivery

Keep phases, dependencies, owner results, proof gaps, blockers, documentation destinations, and the derived delivery summary current.

Require delivery authority before implementation starts. Set the plan to `In Progress` when authorized delivery begins; investigation, clarification, and plan edits do not start delivery.

Give each delivery owner the exact plan outcome, settled scope, dependencies, acceptance, proof, and rollback boundary. Use `alaga` when a supplied build job must deliver one or more candidates through implementation, proof, and required review. Consume the delivery owner's exact-current native result rather than copying its execution, test, snapshot, review, or recovery mechanics.

For another delivery owner, record only what the plan needs to integrate its result: owner, scope, candidate/result identity, freshness, blockers, plan effect, and next action.

## Reconcile results

Verify every supporting result against the current plan and candidate before using it. A mismatch makes only dependent plan conclusions stale; reopen affected phases, proof, readiness, or summaries as needed.

Derive `Complete` only when every in-scope delivery obligation has current accepting proof and plan-level integration has no blocking gap. Derive `Not required` only when the accepted plan contains no delivery work.
