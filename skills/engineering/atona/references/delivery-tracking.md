# Delivery tracking

Use this contract when the plan has material delivery coordination: multiple work units or candidates, owners, dependencies, a multi-session handoff, or delivery authority.

## Decompose delivery when needed

Use `seda-ticket` when the settled plan benefits from consumable semantic delivery tickets with explicit dependencies, acceptance, and a startable frontier. Give it the scope, constraints, dependencies, acceptance, proof/evidence obligations, rollback/recovery boundaries, and exact `seda-spec` identity when one governs the work. Consume its current ticket set and derived startable frontier; do not reproduce its decomposition, dependency, startability, or terminal-disposition rules here.

When another delivery owner already has a stronger native work-unit/dependency model, consume that result instead of forcing parallel ticket semantics. Tickets are optional decomposition, not Atọ́nà's universal delivery representation.

Keep the plan in `Draft` while required decomposition is missing, ambiguous, incomplete, or cyclic. A work unit's state/startability never sets plan status, phase state, delivery authority, or Atọ́nà's delivery summary.

Semantic delivery units do not determine operational topology. Choose candidate, commit, branch, session, PR/MR, document, review package, handoff, deployment unit, or other execution containers independently for their own review, rollback/recovery, ownership, release, integration, or evidence value. When Git/provider delivery applies, default one integration branch and review unit when several tickets form one coherent integrated change; split only when the resulting units are independently useful and safely reviewable/mergeable. Never create one operational container per ticket merely because the ticket boundary exists.

## Track authorized delivery

Keep phases, dependencies, owner results, proof gaps, blockers, documentation/representation destinations, and the derived delivery summary current.

Before material delivery begins, establish a lightweight cumulative **delivery-shape envelope** from current evidence: expected delivery owners/workstreams or affected systems/surfaces, proof/evidence owners, new dependencies or public/external contracts, and handoff/review topology. Treat it as an expectation, not a numeric quota or frozen file/inventory list. Record explicit unchanged areas and any material replan triggers when they help discriminate drift.

Require delivery authority before execution starts. Set the plan to `In Progress` when authorized delivery begins; investigation, clarification, and plan edits do not start delivery.

Give each delivery owner the exact plan outcome, settled scope, dependencies, acceptance, proof/evidence obligation, rollback/recovery boundary, and governing specification identity when present. Use `alaga` when the supplied work is a software/build job that must deliver one or more candidates through implementation, proof, and required review. Otherwise consume the current delivery owner's exact-current native result rather than translating it into Alága semantics.

Execution/review progress comes from the active owner results, not from ticket/work-unit progress states. When exact-current owner evidence proves a ticket's acceptance, the caller may reconcile that ticket to `Done`; cancellation still requires its own authority. A delivery blocker remains with the active owner and affects Atọ́nà's delivery summary without creating a parallel lifecycle.

For another delivery owner, record only what the plan needs to integrate its result: owner, scope, result/candidate identity, freshness, blockers, plan effect, and next action.

## Reconcile results

Verify every supporting result against the current plan and relevant identity before using it. A mismatch makes only dependent plan conclusions stale; reopen affected phases, proof, readiness, or summaries as needed.

When an amendment changes an accepted or completed contract, record one clause-scoped amendment map before resuming dependent delivery or claiming closure:

- governing amendment authority and revision;
- each earlier owner result plus the affected decision, requirement, or clause locators;
- superseded or stale clauses and unaffected retained clauses;
- result/candidate and proof freshness effects; and
- required native-owner refresh and re-entry proof when the plan still needs an exact-current result.

Do not rewrite terminal work units or owner results to make the amended contract look original. A result that remains useful only for unaffected clauses must be described as scope-limited rather than wholly current.

After each materially shape-changing slice or before a material publication/review/handoff boundary, reconcile cumulative actual shape against the delivery-shape envelope. Counts may be useful telemetry in domains where they carry information, but counts are never the acceptance target. Material drift includes unexpected workstream/system/surface spread, repeated new proof owners, new dependencies/contracts, or handoff/review topology that has multiplied beyond its independent value.

When drift is material, stop automatic accretion and determine the owning correction: reopen Atọ́nà when accepted outcome/scope changed; use the current specialist when domain/technical boundaries changed; use `solution-architect` when software/system architecture changed; or use `pare` when software implementation/test/support structure has accumulated without clear value. Do not force a non-software drift problem through a software owner.

Derive `Complete` only when every in-scope delivery obligation has current accepting proof and plan-level integration has no blocking gap. Derive `Not required` only when the accepted plan contains no delivery work.

When software delivery uses PR/MR stewardship, treat `wo-pr`'s `PROVIDER_READY` as provider evidence only. Integrated handoff readiness still requires the relevant delivery owner's accepting result plus the current provider receipt; either becoming stale or failing invalidates only the dependent integrated conclusion.
