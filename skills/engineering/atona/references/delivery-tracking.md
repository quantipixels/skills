# Delivery tracking

Use this contract when the plan has material delivery coordination: tickets, multiple candidates or owners, dependencies, a multi-session handoff, or delivery authority.

## Decompose delivery when needed

Use `seda-ticket` when the settled plan needs consumable delivery tickets. Give it the scope, constraints, dependencies, acceptance, proof, rollback boundaries, and exact `seda-spec` identity when one governs the work. Consume its current ticket set and derived startable frontier; do not reproduce its decomposition, dependency, startability, or terminal-disposition rules here.

Keep the plan in `Draft` while required decomposition is missing, ambiguous, incomplete, or cyclic. Ticket state/startability never sets plan status, phase state, delivery authority, or Atọ́nà's delivery summary.

Ticket decomposition describes semantic delivery outcomes, not operational topology. Choose candidate, commit, branch, session, and PR/MR boundaries independently for their own review, rollback, ownership, release, or integration value. Default one integration branch and review unit when several tickets form one coherent integrated change; split only when the resulting units are independently useful and safely reviewable/mergeable. Never create one branch, PR/MR, commit, test file, or agent session per ticket merely because the ticket boundary exists.

## Track authorized delivery

Keep phases, dependencies, owner results, proof gaps, blockers, documentation destinations, and the derived delivery summary current.

Before material delivery begins, establish a lightweight cumulative **delivery-shape envelope** from current evidence: expected production owners/subsystems, proof/test owners, new dependencies or public contracts, and candidate/review topology. Treat it as an expectation, not a numeric quota or frozen file list. Record explicit unchanged areas and any material replan triggers when they help discriminate drift.

Require delivery authority before implementation starts. Set the plan to `In Progress` when authorized delivery begins; investigation, clarification, and plan edits do not start delivery.

Give each delivery owner the exact plan outcome, settled scope, dependencies, acceptance, proof, rollback boundary, and governing specification identity when present. Use `alaga` when a supplied build job must deliver one or more candidates through implementation, proof, and required review. Consume the delivery owner's exact-current native result rather than copying its execution, test, snapshot, review, or recovery mechanics.

Execution/review progress comes from the active owner results, not from ticket progress states. When exact-current owner evidence proves a ticket's acceptance, the caller may reconcile that ticket to `Done`; cancellation still requires its own authority. A runtime blocker remains with the active delivery/review owner and affects Atọ́nà's delivery summary without creating a parallel ticket lifecycle.

For another delivery owner, record only what the plan needs to integrate its result: owner, scope, candidate/result identity, freshness, blockers, plan effect, and next action.

## Reconcile results

Verify every supporting result against the current plan and candidate before using it. A mismatch makes only dependent plan conclusions stale; reopen affected phases, proof, readiness, or summaries as needed.

When an amendment changes an accepted or completed contract, record one clause-scoped amendment map before resuming dependent delivery or claiming closure:

- governing amendment authority and revision;
- each earlier owner result plus the affected decision, requirement, or clause locators;
- superseded or stale clauses and unaffected retained clauses;
- candidate and proof freshness effects; and
- required native-owner refresh and re-entry proof when the plan still needs an exact-current result.

Do not rewrite terminal tickets or owner results to make the amended contract look original. A result that remains useful only for unaffected clauses must be described as scope-limited rather than wholly current.

After each materially shape-changing slice or before a material publication/review boundary, reconcile cumulative actual shape against the delivery-shape envelope. File/test counts may be useful telemetry, but counts are never the acceptance target. Material drift includes unexpected subsystem spread, repeated new proof owners, new dependencies/contracts, or review topology that has multiplied beyond its independent value.

When drift is material, stop automatic accretion and determine the owning correction: reopen Atọ́nà when accepted outcome/scope changed, use `solution-architect` when technical boundaries changed, or use `pare` when implementation/test/support structure has accumulated without clear value. Surface the candidate identity, material shape change, and next reconciliation action before publishing further material expansion.

Derive `Complete` only when every in-scope delivery obligation has current accepting proof and plan-level integration has no blocking gap. Derive `Not required` only when the accepted plan contains no delivery work.

Treat `wo-pr`'s `PROVIDER_READY` as provider evidence only. Integrated handoff readiness requires both a current accepting `alaga` result and the current provider receipt; either becoming stale or failing invalidates only the dependent integrated conclusion.
