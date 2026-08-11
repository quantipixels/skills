---
name: atona
description: Maintain one evidence-backed architecture or migration plan across design and delivery. Focus on complete decisions, implementation readiness, clear build handoffs, proof, and documentation consistency.
---

# Atona

Own one live architecture plan from evidence through closure. Keep implementation and review procedures with their owning skills and record their verified results.

## Functional workflow

```text
Request + repository evidence
              │
              ▼
      One shared live plan
              │
              ▼
   Evidence + clarification
              │
              ▼
  Architecture + readiness
              │
              ▼
      Authorized delivery
              │
              ▼
  Reconcile documentation
              │
              ▼
            Close
```

When an answer, fact, or confirmed decision changes, reopen every affected decision and phase; mark its proof and candidate evidence stale; and record the affected code, tests, schema, configuration, naming, and documentation. Rerun affected readiness and closure checks before restoring state.

## 1. Establish the plan and evidence

Use `html-artifact` to create or update `.qp/plans/<topic>.html`. Keep this file as the primary working plan and reuse its path when another skill contributes.

Record the request, scope, constraints, non-goals, plan status, and implementation state. Track implementation as `Not Required`, `Not Started`, `Started`, or `Complete`. Use the plan statuses and handoffs in Section 4.

Inspect the evidence needed to prove the current system: the complete root `.nongoal` when present; relevant overview, architecture, context, architecture decision record (ADR), module, and prior-plan documents; code; tests; history; integrations; recovery paths; and branch state. When the requested direction conflicts with `.nongoal`, use `alakowe` to resolve a one-time exception or an authorized boundary update before planning past the conflict.

When a substantial independent evidence result, specialist gate, or failure-focused readiness challenge would materially help, Atona may request it from a host-provided subagent. Give it the live-plan identity, bounded scope, current evidence, known gaps, and required result. Atona retains plan state, evidence freshness, readiness judgment, implementation state, and closure.

For a new plan or reopened material architecture decision, use `arojinle`. Give it the live plan path, exact decision scope, settled prerequisites, known dependent branches, current evidence, and evidence gaps. Arojinle owns the complete decision frontier and confirmation.

Reuse a confirmed Arojinle result only while its identity remains current: plan and topic, scope and tree revisions, decision identifiers, evidence or candidate identity, confirmation date, and unresolved branches. Its coverage must contain no open, silently waiting, blocking-deferred, or stale branch. Otherwise, keep the plan in `Draft`. Plan edits alone do not satisfy readiness.

Compare architecture-significant terms across user statements, repository documents, and code. When a project-specific term, relationship, or rule is ambiguous and can change scope, ownership, state, or behavior, record the competing meanings and one concrete scenario that distinguishes them. Treat code as evidence of current behavior, not automatic domain authority. Use `arojinle` for a material decision.

Classify each durable conclusion as domain or context language, repository architecture, an architecture decision, a local convention, or plan-only information. For confirmed domain language, context boundaries, ADR state, or project exclusions, record the required `alakowe` handoff with the live-plan identity, confirmed authority, competing meanings and scenario, affected surfaces, and nearest known destination. Request its result when durable reconciliation is authorized and required for readiness or closure. Alakowe owns canonical destination discovery and reconciliation; Atona retains plan evidence, readiness, and closure.

Keep the plan in `Draft` while a material project-language conflict is unresolved or an Alakowe result required for current readiness is missing, blocked, or stale.

Record evidence or a gap for every decision-shaping claim. Confirm or defer every architecture-changing uncertainty.

## 2. Decide the architecture and verify readiness

Provide a compact decision packet with the problem, constraints, evidence, options, trade-offs, recommendation, phases, and proof plan.

Use these safeguards:

- Keep behavior local unless shared ownership, lifecycle, coordination, restoration, policy, or communication requires a wider owner.
- Move stable identity and durable state across boundaries. Keep runtime handles, callbacks, scopes, and framework objects with their runtime owner.
- Prefer typed state, explicit contracts, and one active owner over parallel flags and implicit coupling.
- Treat queueing, persistence, priority, global arbitration, and universal registries as separate design decisions.
- Decide ownership and visibility at the smallest meaningful capability.
- Cover each material state, ownership, lifecycle, and boundary decision with normal behavior proof and one relevant edge or failure scenario.

For each proposed module or seam, name its callers, required caller knowledge, hidden complexity or policy, and behavior proof. Reject it when deletion exposes only pass-through calls without exposing complexity. Keep a shallow seam only for a proven integration, ownership, lifecycle, policy, or testing need.

Propose an ADR only for a real trade-off that is costly to reverse and surprising without its reason. Require approval before creation.

Before setting the plan to `Planned`, and after final Arojinle confirmation, run one readiness gate:

1. Re-read the plan as its implementer. Check intent and acceptance; scope and non-goals; design and ownership; behavior and risk; failure, remediation, and recovery; compatibility and migration; delivery, proof, and manual review; test replacement; rollback; documentation and operations; final acceptance; and relevant domain concerns.
2. Treat the Arojinle result as input, not proof. Verify its closure against the exact plan: decisions are realized or marked not applicable with a reason; plan clauses trace to a decision or current fact; overlaps have precedence; delivery states and authorities are ordered; and acceptance detects the top failures.
3. Treat coverage as an index. Resolve plan-local gaps without repeating the interview. Assume the outcome failed, trace the top mechanisms and interactions, and record each retained mechanism, correction or proof, gap, residual risk, and plan identity.
4. Apply corrections. Arojinle owns each new material user decision. Record readiness as `Confirmed` with evidence, `Deferred` with an owner and trigger, or `Open` with the required decision or proof.

Set the plan to `Planned` only when the recommendation covers all in-scope ownership and behavior and the implementer needs no invented material requirement. Otherwise, keep it in `Draft`. This includes an open, pending, stale, contradictory, or missing gate; a waiting prerequisite; a blocking deferral; missing evidence or decision; or invalid Arojinle identity, coverage, or closure. A non-blocking deferral needs an owner and trigger and must not force material invention. Approval covers only listed decisions.

## 3. Track authorized delivery

Keep the request, decisions, evidence, risks, phases, candidate, proof gaps, documentation destinations, and lifecycle states current in the plan. Remove stale guidance and redundant snapshots.

Require explicit implementation authority. Immediately before the first edit, set implementation to `Started` and record the date, candidate branch and commit or tree state, phase, and authority. Investigation, clarification, and plan edits do not start implementation.

Translate each delivery phase into one or more stable, self-contained review candidates. Give each candidate its scope, dependencies, acceptance behavior, proof, and rollback boundary. Do not make every TDD slice or local commit an Alaga invocation, and do not force a whole phase into one candidate when it contains independent reviewable changes. Keep phase-level integration and acceptance proof in the plan.

Use `audit-refactor-behavior` before a stateful refactor that can change transitions, ordering, locking, retries, idempotency, ownership, or cross-entry behavior. Use `alaga` for each full feature candidate or `tdd` for bounded test-first implementation.

For work owned by another skill, record its owner, scope, evidence, blocked outcome, and required result. Keep test, review, build, commit, and publication procedures with their owners.

Verify each specialist result against the current plan identity and candidate before recording state or evidence. Reject a mismatch as stale and rerun affected readiness or closure checks. Set implementation to `Complete` only after `qp-code-review` returns `RECOMMEND_ACCEPT` for every final in-scope review candidate and phase-level integration proof has no blocking evidence gap. Reuse a verified current result. Skip this gate when implementation is `Not Required`.

## 4. Reconcile and close

Before `Closed`, verify no blocking decision remains; delivery and review match the candidate; validation and proof gaps are recorded; deferrals have an owner or trigger; follow-ups are classified as blocking or non-blocking; freezes and `leave unchanged` decisions hold; and no unresolved item, stale name, replaced or deprecated primitive, outdated guidance, or test without replacement remains.

For each documentation destination, record `updated now`, `already reconciled` with evidence, or `not applicable`. When domain language, context boundaries, ADR state, canonical project knowledge, or `.nongoal` is affected, verify one exact-current Alakowe result rather than repeating its discovery. Do not leave obsolete guidance current.

Align plan and implementation states with remaining work. End each user-visible handoff with **What next**: recommendation, first step, owner or skill, and required authority.

When the plan first becomes `Planned` and implementation is required, state implementation authority as `Confirmed` or `Required`. If authority is required, name the exact authority without starting implementation.

Add or refresh **Suggested direction** when the plan becomes `Planned`, implementation authority changes, the suggested direction changes materially, or the user asks for implementation guidance. On other `Planned` handoffs, state only the current authority and recommended starting point.

Check the active skill inventory. Under **Suggested direction**, list only available skills that fit the current plan. Put them in a useful likely order. For each skill, name the plan-specific outcome or proof it would own and why the plan needs it. Mark an outcome or proof gate as required only when the confirmed plan or owning skill requires it. Treat the list as advice, not implementation authority or a fixed route. Keep models, subagents, tools, phases, and generic actions out of this list; add requested routing separately.

When a required gate's owning skill is unavailable, add `Required skill gap: <skill> — <required outcome or proof>.` outside **Suggested direction**. Recommend making the owner available before implementation. Do not hide the gap, substitute another owner, or recommend starting work past it.

End with the recommended starting skill and its first plan-specific action. If a required owner is unavailable, end with the action needed to resolve that gap. If implementation authority is required, end with that authority action instead.

When giving or refreshing **Suggested direction**, use this compact shape:

Omit the required skill gap line when no required owner is unavailable.

```text
Implementation authority: Confirmed | Required

Suggested direction
1. <skill> — <outcome or proof it would own and why this plan needs it>.
2. <skill> — <outcome or proof it would own and why this plan needs it>.

Required skill gap: <skill> — <required outcome or proof>.

Recommended starting point: <skill and first plan-specific action | prerequisite action>.
```

| Plan status | Use when | **What next** |
| --- | --- | --- |
| `Draft` | A decision, evidence item, or readiness gate is open. | Name the next decision or evidence action. |
| `Planned` | Planning is complete without material invention. | Say, “Planning is complete. Here is a suggested direction for the build.” Give or refresh the concise direction when its trigger applies. Otherwise state only the current authority and recommended starting point. Add phases or proof gates only when they materially affect the recommendation or starting point. |
| `In Progress` | Implementation, documentation, or proof is active. | Name the next incomplete phase or gap. |
| `Closed` | No plan work remains, including a resolved amendment. | Name the next workstream or say that planning is complete. |
| `Backlog` | The plan is inventory that does not require closure. | Name its owner and reactivation trigger. |

When a material choice remains, give numbered options and mark the recommendation. Do not start the next action without its required authority.
