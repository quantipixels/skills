# Delivery tracking

Use this contract when the plan has material delivery coordination: multiple work units or candidates, owners, dependencies, or a multi-session handoff.

## Decompose delivery when needed

Use [delivery decomposition](decomposition.md) with the settled plan and governing behavior contract.

When another delivery owner already has a stronger native work-unit/dependency model, consume that result instead of forcing parallel ticket semantics. Tickets are optional decomposition, not Atọ́nà's universal delivery representation.

Treat affected delivery as unready while required decomposition is missing, ambiguous, incomplete, or cyclic. In the managed lifecycle, keep the plan in `Draft`. A work unit's state/startability never sets plan status, phase state, delivery authority, or Atọ́nà's delivery summary.

Semantic delivery units do not determine operational topology. Choose candidate, commit, branch, session, PR/MR, document, review package, handoff, deployment unit, or other execution containers independently for their own review, rollback/recovery, ownership, release, integration, or evidence value. When Git/provider delivery applies, default one integration branch and review unit when several tickets form one coherent integrated change; split only when the resulting units are independently useful and safely reviewable/mergeable. Never create one operational container per ticket merely because the ticket boundary exists.

## Track authorized delivery

Keep phases, dependencies, owner results, proof gaps, blockers, documentation/representation destinations, and the derived delivery summary current.

Before material delivery begins, establish a lightweight cumulative **delivery-shape envelope** from current evidence: expected delivery owners/workstreams or affected systems/surfaces, proof/evidence owners, new dependencies or public/external contracts, and handoff/review topology. Treat it as an expectation, not a numeric quota or frozen file/inventory list. Record explicit unchanged areas and any material replan triggers when they help discriminate drift.

Use existing delivery authority; obtain it only when missing. In the managed lifecycle, set the plan to `In Progress` when authorized delivery begins; investigation, clarification, and plan edits do not start delivery.

Use `alaga` as the builder under the main skill’s delivery seam. Track its candidate, acceptance evidence, blockers, and scope effects; keep implementation, test execution, and coding corrections with Alága.

Execution/review progress comes from the active owner results, not from ticket/work-unit progress states. When exact-current owner evidence proves a ticket's acceptance, the caller may reconcile that ticket to `Done`; cancellation still requires its own authority. A delivery blocker remains with the active owner and affects Atọ́nà's delivery summary without creating a parallel lifecycle.

For another delivery owner, record only what the plan needs to integrate its result: owner, scope, result/candidate identity, freshness, blockers, plan effect, and next action.

## Reconcile results

Verify every supporting result against the current plan and relevant identity before using it. A mismatch makes only dependent plan conclusions stale; reopen affected phases, proof, readiness, or summaries as needed.

When an amendment changes an accepted or completed contract, reconcile it before resuming dependent delivery or claiming closure. For a simple localized change with one clear dependency effect, a concise amendment note is sufficient: governing authority and revision, changed clause locator, affected result/proof, what becomes stale or remains current, and any required owner refresh or re-entry proof.

Use a full clause-scoped amendment map when effects span multiple results or clauses, retained coverage is partial, or the reconciliation is otherwise complex:

- governing amendment authority and revision;
- each earlier owner result plus the affected decision, requirement, or clause locators;
- superseded or stale clauses and unaffected retained clauses;
- result/candidate and proof freshness effects; and
- required native-owner refresh and re-entry proof when the plan still needs an exact-current result.

Do not rewrite terminal work units or owner results to make the amended contract look original. A result that remains useful only for unaffected clauses must be described as scope-limited rather than wholly current.

After each materially shape-changing slice or before a material publication/review/handoff boundary, reconcile cumulative actual shape against the delivery-shape envelope. Counts may be useful telemetry in domains where they carry information, but counts are never the acceptance target. Material drift includes unexpected workstream/system/surface spread, repeated new proof owners, new dependencies/contracts, or handoff/review topology that has multiplied beyond its independent value.

When drift is material, replan from the changed scope and constraints. Use `architect` for structural decisions or `atunwo` for a code assessment with a simplification focus. Supply the bounded candidate/system, intended delivery shape, observed drift, and current evidence; review depth belongs to `atunwo` unless explicitly set. Consume its findings, proof gaps, and retained contracts when replanning; recommendations alone do not authorize implementation or prove delivery complete.

Derive `Complete` only when every in-scope delivery obligation has current accepting proof and plan-level integration has no blocking gap. Derive `Not required` only when the accepted plan contains no delivery work.

When software delivery uses PR/MR stewardship, treat `seda-pr`'s `PROVIDER_READY` as provider evidence only. Integrated handoff readiness still requires the relevant delivery owner's accepting result plus the current provider receipt; either becoming stale or failing invalidates only the dependent integrated conclusion.
