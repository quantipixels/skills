---
name: atona
description: Maintain one exact-current initiative plan from unclear intent through delivery and closure. Use when a feature, migration, or material workstream needs exploration, shaping, lifecycle-plan readiness, coordinated handoffs, proof, and final reconciliation. Exclude technical architecture design or review, complete decision interviews, implementation, and generic routing.
---

# Atọ́nà

Turn unclear intent into one live initiative plan and keep that plan current through delivery and closure. Own lifecycle-plan sufficiency, not every specialist judgment. Keep technical architecture with `solution-architect`, material decision closure with `arojinle`, implementation with delivery owners, and route selection with `alarina`.

When an answer, fact, or confirmed decision changes, reopen every affected decision and phase; mark its proof and candidate evidence stale; and record the affected code, tests, schema, configuration, naming, and documentation. Rerun affected readiness and closure checks before restoring state.

## 1. Establish the plan and evidence

Use `html-artifact` to create or update `.qp/plans/<topic>.html`. Invoking `atona` authorizes only this task-local HTML plan and, if its owner becomes unavailable, non-user-facing recovery checkpoints under `.qp/plans/.receipts/<plan-stem>/`, unless the user says `propose`, `read-only`, or `do not edit`. Source, ADR, ticket provider, publication, and other durable writes keep their own authority gates.

Keep the HTML file as the one human-facing plan. Lead with a review sheet, current status, decisions, blockers, and the next action. Keep evidence and detailed contributions behind stable links and progressive disclosure. Do not create a Markdown twin.

If `html-artifact` is unavailable or the plan cannot be created, updated, reread, or verified safely, keep the plan in `Draft`, report the required-skill or artifact gap, and do not claim `Planned` or `Closed`.

Record the request, desired outcome, scope, constraints, non-goals, plan status, decision and receipt ledger, delivery summary, evidence cutoff, and next action.

Track one plan status:

| Status | Enter when | Leave when |
| --- | --- | --- |
| `Draft` | planning begins, a material decision or readiness gap opens, or a closed plan is amended | all readiness gates pass (`Planned`), or active scope is deferred as inventory (`Backlog`) |
| `Planned` | the readiness gate passes and delivery has not started | authorized delivery work begins (`In Progress`), a material gap opens (`Draft`), or no delivery is required and closure passes (`Closed`) |
| `In Progress` | authorized delivery work is active | a material planning gap opens (`Draft`), or delivery and closure pass (`Closed`) |
| `Backlog` | the plan is retained as inactive inventory with an owner and reactivation trigger | active work resumes (`Draft`) |
| `Closed` | every in-scope planning, delivery, and reconciliation obligation is complete | a material amendment opens (`Draft`) |

The status is `atona`'s judgment. A ticket, job, review, provider, or delivery-summary value does not set it.

Derive one delivery summary from exact-current owner receipts:

- `Not required` — the accepted plan needs no delivery work.
- `Not started` — delivery is required, but no authorized owner has started an exact candidate.
- `Active` — at least one authorized delivery candidate is active and none blocks the complete plan.
- `Blocked` — a current blocker prevents all safe progress needed for the plan.
- `Complete` — every in-scope candidate and phase has current accepting proof.
- `Stale` — changed evidence or identity invalidates a result used by the summary.

The delivery summary is a plan view, not another state machine. Recompute it from receipts after every relevant candidate, result, blocker, dependency, or evidence change.

Inspect the evidence needed to prove the current system: relevant parts of root `.learnings`, the complete root `.nongoals` when present, overview, architecture and ADR documents, code, tests, history, integrations, recovery paths, and branch state. When the requested direction conflicts with `.nongoals`, require an `amose` result that records an authorized one-time exception or boundary update before planning past the conflict.

When a substantial independent evidence result, specialist gate, or failure-focused readiness challenge would materially help, `atona` may request it from a host-provided subagent. Give it the live-plan identity, bounded scope, current evidence, known gaps, and required result. `atona` retains plan state, evidence freshness, readiness judgment, delivery-summary derivation, and closure.

Use `arojinle` for a new or reopened material user decision.

Reuse a confirmed `arojinle` result only while its identity remains current: plan and topic, scope and tree revisions, decision identifiers, evidence or candidate identity, confirmation date, and unresolved branches. Its coverage must contain no open, silently waiting, blocking-deferred, or stale branch. Otherwise, keep the plan in `Draft`. Plan edits alone do not satisfy readiness.

Use `amose` when project knowledge materially affects the initiative. Treat its exact-current result as evidence, not decision authority; use `arojinle` for a material decision it exposes.

When bounded structural, call-flow, data-flow, or impact evidence would close a plan gap, request an exact-current `irinse` result. Treat tool output as investigation evidence.

Classify each durable conclusion as an architecture decision, project knowledge, ordinary documentation, local convention, or plan-only information. Keep ordinary documentation with the outcome owner. Reconcile all exact-current `arojinle` results for the plan once through `amose`; any change to the plan, result set, evidence, or delivery candidate makes that reconciliation stale. `atona` retains readiness and closure judgment.

Keep the plan in `Draft` while a material project-knowledge conflict is unresolved or a required `amose` result is missing, blocked, or stale.

Record evidence or a gap for every decision-shaping claim. Confirm or defer every plan-changing uncertainty. Every deferral records an owner and re-entry trigger. A durable deferral also records its reason, next evidence, relative priority, review or close date, and default disposition if that date passes. Reconcile the required record immediately when its basis changes. A blocking deferral keeps the plan in `Draft`; a non-blocking deferral must not force material invention.

## 2. Explore, shape, and verify readiness

Pin the desired outcome, affected people and capabilities, scope, constraints, assumptions, non-goals, evidence, risks, and open decisions. Identify which specialist results the plan needs. Do not invoke a specialist when current evidence already closes its boundary.

Use `solution-architect` when technical design or architecture review is material. Give it the plan identity, exact candidate, outcomes, constraints, accepted decisions, evidence, required scenarios, and required result. Record its packet identity, result, recommendation, risks, proof, evidence freshness, and affected phases. Do not copy or recreate its design method.

Use `iwadi` for decision-changing primary-source research that needs a durable report. Use `amose` for exact-current domain knowledge and durable decision records. Treat each specialist result as evidence within its native authority.

`atona` alone changes shared plan meaning, status, readiness, staleness, integration, delivery summary, and closure. Supporting skills do not mutate the plan. Each returns one exact-current receipt with:

- the plan identity and revision, owner, receipt identity, and receipt revision;
- the exact decision, packet, candidate, ticket set, report, or provider target;
- the owner's native result and the result's effect on the plan;
- the evidence identity, cutoff, gaps, and `CURRENT` or `STALE` freshness;
- blockers and affected decisions, phases, proof, or summaries; and
- the next owner, required authority, and checkable completion condition.

Keep raw research, ADRs, domain records, ticket-provider state, review evidence, operational checkpoints, and job-local mechanics with their native owners. Link them from the receipt instead of copying them into the plan. A supporting skill may use a non-user-facing recovery checkpoint under `.qp/plans/.receipts/<plan-stem>/` only when the active plan owner is unavailable; validate and reconcile or reject it when ownership resumes. When a receipt becomes stale, reopen only the plan content that depends on it and reject downstream completion claims until refreshed.

Before setting the plan to `Planned`, and after final `arojinle` confirmation, run one readiness gate:

1. Re-read the plan as its implementer. Check intent and acceptance; scope and non-goals; required specialist results; ownership and precedence; behavior and risk; failure and recovery; compatibility and migration; delivery, proof, rollback, documentation, operations, and final acceptance.
2. Treat specialist results as inputs, not plan proof. Verify each result against the exact plan and candidate. When technical architecture is material, require an exact-current `solution-architect: IMPLEMENTATION_READY` result. Verify that confirmed decisions are realized or marked not applicable, overlaps have precedence, delivery authorities are ordered, and acceptance detects the top failures.
3. Treat coverage as an index. Resolve plan-local gaps without repeating the interview. Assume the outcome failed, trace the top mechanisms and interactions, and record each retained mechanism, correction or proof, gap, residual risk, and plan identity.
4. Apply corrections. `arojinle` owns each new material user decision. Record readiness as `Confirmed` with evidence, `Deferred` with its required record, or `Open` with the required decision or proof.

Set the plan to `Planned` only when the composed plan covers all in-scope ownership and behavior and the implementer needs no invented material requirement. Otherwise, keep it in `Draft`. This includes an open, pending, stale, contradictory, or missing gate; a waiting prerequisite; a blocking deferral; missing evidence or decision; or an invalid required specialist result. Approval covers only listed decisions.

## 3. Track authorized delivery

When the user requests tickets, the plan has multiple delivery candidates, dependencies, implementers, or a multi-session handoff, or delivery authority is granted, read [delivery-tracking.md](references/delivery-tracking.md). It owns ticket integration, delivery-owner handoffs, receipt reconciliation, and exact-current completion proof. `atona` retains plan identity, readiness, integration, delivery-summary derivation, and closure.

## 4. Reconcile and close

Before `Closed`, verify no blocking decision remains; delivery and review match the candidate; validation and proof gaps are recorded; deferrals carry their required records; follow-ups are classified as blocking or non-blocking; freezes and `leave unchanged` decisions hold; and no unresolved item, stale name, replaced or deprecated primitive, outdated guidance, or test without replacement remains.

For each affected `.learnings`, `.nongoals`, or ADR destination, verify one exact-current `amose` result rather than repeating its discovery. For ordinary documentation, require the owning delivery skill to record `updated now`, `already reconciled` with evidence, or `not applicable`. Do not leave obsolete guidance current.

Before every user-visible handoff, align the plan status and derived delivery summary with remaining work, then apply [suggested-direction.md](references/suggested-direction.md). Do not start its next action without the required authority.
