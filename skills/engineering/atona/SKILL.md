---
name: atona
description: Maintain one evidence-backed architecture or migration plan across design and delivery. Focus on complete decisions, implementation readiness, clear build handoffs, proof, and documentation consistency.
---

# Atọ́nà

Own one live architecture plan from evidence through closure. Keep implementation and review procedures with their owning skills and record their verified results.

When an answer, fact, or confirmed decision changes, reopen every affected decision and phase; mark its proof and candidate evidence stale; and record the affected code, tests, schema, configuration, naming, and documentation. Rerun affected readiness and closure checks before restoring state.

## 1. Establish the plan and evidence

Use `html-artifact` to create or update `.qp/plans/<topic>.html`. Keep this file as the primary working plan and reuse its path when another skill contributes.

If `html-artifact` is unavailable or the plan cannot be created, updated, reread, or verified safely, keep the plan in `Draft`, report the required-skill or artifact gap, and do not claim `Planned` or `Closed`.

Record the request, scope, constraints, non-goals, plan status, and implementation state. Track implementation as `Not Required`, `Not Started`, `Started`, or `Complete`.

Track one plan status:

| Status | Enter when | Leave when |
| --- | --- | --- |
| `Draft` | planning begins, a material decision or readiness gap opens, or a closed plan is amended | all readiness gates pass (`Planned`), or active scope is deferred as inventory (`Backlog`) |
| `Planned` | the readiness gate passes and delivery has not started | authorized delivery work begins (`In Progress`), a material gap opens (`Draft`), or no delivery is required and closure passes (`Closed`) |
| `In Progress` | authorized delivery work is active | a material planning gap opens (`Draft`), or delivery and closure pass (`Closed`) |
| `Backlog` | the plan is retained as inactive inventory with an owner and reactivation trigger | active work resumes (`Draft`) |
| `Closed` | every in-scope planning, delivery, and reconciliation obligation is complete | a material amendment opens (`Draft`) |

The status is `atona`'s judgment; ticket state and implementation state do not set it.

Inspect the evidence needed to prove the current system: relevant parts of root `.learnings`, the complete root `.nongoals` when present, overview, architecture and ADR documents, code, tests, history, integrations, recovery paths, and branch state. When the requested direction conflicts with `.nongoals`, require an `amose` result that records an authorized one-time exception or boundary update before planning past the conflict.

When a substantial independent evidence result, specialist gate, or failure-focused readiness challenge would materially help, `atona` may request it from a host-provided subagent. Give it the live-plan identity, bounded scope, current evidence, known gaps, and required result. `atona` retains plan state, evidence freshness, readiness judgment, implementation state, and closure.

Use `arojinle` for a new or reopened material architecture decision.

Reuse a confirmed `arojinle` result only while its identity remains current: plan and topic, scope and tree revisions, decision identifiers, evidence or candidate identity, confirmation date, and unresolved branches. Its coverage must contain no open, silently waiting, blocking-deferred, or stale branch. Otherwise, keep the plan in `Draft`. Plan edits alone do not satisfy readiness.

Use `amose` when project knowledge materially affects the architecture. Treat its exact-current result as evidence, not architecture authority; use `arojinle` for a material decision it exposes.

When bounded structural, call-flow, data-flow, or impact evidence would close a plan gap, request an exact-current `irinse` result. Treat tool output as investigation evidence and retain architecture judgment in `atona`.

Classify each durable conclusion as architecture, architecture decision, project knowledge, ordinary documentation, local convention, or plan-only information. Keep ordinary documentation with the outcome owner. Reconcile all exact-current `arojinle` results for the plan once through `amose`; any change to the plan, result set, evidence, or implementation candidate makes that reconciliation stale. `atona` retains readiness and closure judgment.

Keep the plan in `Draft` while a material project-knowledge conflict is unresolved or a required `amose` result is missing, blocked, or stale.

Record evidence or a gap for every decision-shaping claim. Confirm or defer every architecture-changing uncertainty. Every deferral records an owner and re-entry trigger. A durable deferral also records its reason, next evidence, relative priority, review or close date, and default disposition if that date passes. Reconcile the required record immediately when its basis changes. A blocking deferral keeps the plan in `Draft`; a non-blocking deferral must not force material invention.

## 2. Decide the architecture and verify readiness

Provide a compact architecture recommendation with the problem, constraints, evidence, options, trade-offs, recommendation, phases, and proof plan.

Use these safeguards:

- Keep behavior local unless shared ownership, lifecycle, coordination, restoration, policy, or communication requires a wider owner.
- Move stable identity and durable state across boundaries. Keep runtime handles, callbacks, scopes, and framework objects with their runtime owner.
- Prefer typed state, explicit contracts, and one active owner over parallel flags and implicit coupling.
- Treat queueing, persistence, priority, global arbitration, and universal registries as separate design decisions.
- Decide ownership and visibility at the smallest meaningful capability.
- Prefer deep modules at clean seams: minimize what callers must know while hiding meaningful behavior, policy, or integration complexity. Depth means interface leverage, not implementation size. Treat invariants, ordering, errors, configuration, and performance constraints as part of the interface.
- Cover each material state, ownership, lifecycle, and boundary decision with normal behavior proof and one relevant edge or failure scenario.

For each proposed module or seam, name its callers, the complete interface knowledge they require, the complexity or policy hidden inside, and the behavior proof exercised through that interface.

Apply the deletion test: a useful module causes its hidden complexity to reappear across callers when removed. Reject a pass-through module whose deletion removes only forwarding calls. Keep a shallow module only for a proven integration, ownership, lifecycle, policy, or testing reason.

Do not introduce a speculative seam only for possible future variation. One implementation needs an independent ownership, integration, lifecycle, policy, or testing reason; actual variation makes the seam stronger evidence.

Before setting the plan to `Planned`, and after final `arojinle` confirmation, run one readiness gate:

1. Re-read the plan as its implementer. Check intent and acceptance; scope and non-goals; design and ownership; behavior and risk; failure, remediation, and recovery; compatibility and migration; delivery, proof, and manual review; test replacement; rollback; documentation and operations; final acceptance; and relevant domain concerns.
2. Treat the `arojinle` result as input, not proof. Verify its closure against the exact plan: decisions are realized or marked not applicable with a reason; plan clauses trace to a decision or current fact; overlaps have precedence; delivery states and authorities are ordered; and acceptance detects the top failures.
3. Treat coverage as an index. Resolve plan-local gaps without repeating the interview. Assume the outcome failed, trace the top mechanisms and interactions, and record each retained mechanism, correction or proof, gap, residual risk, and plan identity.
4. Apply corrections. `arojinle` owns each new material user decision. Record readiness as `Confirmed` with evidence, `Deferred` with its required record, or `Open` with the required decision or proof.

Set the plan to `Planned` only when the recommendation covers all in-scope ownership and behavior and the implementer needs no invented material requirement. Otherwise, keep it in `Draft`. This includes an open, pending, stale, contradictory, or missing gate; a waiting prerequisite; a blocking deferral; missing evidence or decision; or invalid `arojinle` identity, coverage, or closure. Approval covers only listed decisions.

## 3. Track authorized delivery

When the user requests tickets, the plan has multiple review candidates, dependencies, implementers, or a multi-session handoff, or implementation authority is granted, read [delivery-tracking.md](references/delivery-tracking.md). It owns ticket reconciliation, implementation start, review-candidate shaping, delivery-owner handoffs, and exact-current completion proof. `atona` retains plan identity, readiness, integration, and closure.

## 4. Reconcile and close

Before `Closed`, verify no blocking decision remains; delivery and review match the candidate; validation and proof gaps are recorded; deferrals carry their required records; follow-ups are classified as blocking or non-blocking; freezes and `leave unchanged` decisions hold; and no unresolved item, stale name, replaced or deprecated primitive, outdated guidance, or test without replacement remains.

For each affected `.learnings`, `.nongoals`, or ADR destination, verify one exact-current `amose` result rather than repeating its discovery. For ordinary documentation, require the owning delivery skill to record `updated now`, `already reconciled` with evidence, or `not applicable`. Do not leave obsolete guidance current.

Before every user-visible handoff, align plan and implementation states with remaining work, then apply [suggested-direction.md](references/suggested-direction.md). Do not start its next action without the required authority.
