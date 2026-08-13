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
 Reconcile durable knowledge
              │
              ▼
            Close
```

When an answer, fact, or confirmed decision changes, reopen every affected decision and phase; mark its proof and candidate evidence stale; and record the affected code, tests, schema, configuration, naming, and documentation. Rerun affected readiness and closure checks before restoring state.

## 1. Establish the plan and evidence

Use `html-artifact` to create or update `.qp/plans/<topic>.html`. Keep this file as the primary working plan and reuse its path when another skill contributes.

Record the request, scope, constraints, non-goals, plan status, and implementation state. Track implementation as `Not Required`, `Not Started`, `Started`, or `Complete`. Use the plan statuses and handoffs in Section 4.

Inspect the evidence needed to prove the current system: relevant parts of root `.learnings`, the complete root `.nongoals` when present, overview, architecture and ADR documents, code, tests, history, integrations, recovery paths, and branch state. When the requested direction conflicts with `.nongoals`, require an Amọ̀ṣẹ́ result that records an authorized one-time exception or boundary update before planning past the conflict.

When a substantial independent evidence result, specialist gate, or failure-focused readiness challenge would materially help, Atona may request it from a host-provided subagent. Give it the live-plan identity, bounded scope, current evidence, known gaps, and required result. Atona retains plan state, evidence freshness, readiness judgment, implementation state, and closure.

For a new plan or reopened material architecture decision, use `arojinle`. Give it the live plan path, exact decision scope, settled prerequisites, known dependent branches, current evidence, and evidence gaps. Arojinle owns the complete decision frontier and confirmation.

Reuse a confirmed Arojinle result only while its identity remains current: plan and topic, scope and tree revisions, decision identifiers, evidence or candidate identity, confirmation date, and unresolved branches. Its coverage must contain no open, silently waiting, blocking-deferred, or stale branch. Otherwise, keep the plan in `Draft`. Plan edits alone do not satisfy readiness.

Require a current Amọ̀ṣẹ́ project-knowledge packet when project-specific terms, relationships, invariants, scenarios, contexts, boundaries, prior learnings, or ADR state materially affect the architecture. Treat the packet as evidence, not architecture authority. Use `arojinle` for a material decision it exposes.

When bounded structural, call-flow, data-flow, or impact evidence would close a plan gap, request an exact-current Irinṣẹ result. Treat tool output as investigation evidence and retain architecture judgment in Atona.

Classify each durable conclusion as repository architecture, an architecture decision, project knowledge, ordinary documentation, a local convention, or plan-only information. Record any required Amọ̀ṣẹ́ update with the live-plan identity, confirmed authority, affected model or durable record, and exact candidate. Keep ordinary documentation with the outcome skill changing or verifying the behavior.

Retain every exact-current Arojinle handoff packet associated with the current plan and collect all of them into one Amọ̀ṣẹ́ reconciliation without pre-qualifying or excluding them. Supply the Amọ̀ṣẹ́-owned batch envelope with the live-plan path and revision, ordered member identifiers and packet revisions, current confirmation state, and exact evidence and implementation candidate identities. Any envelope change makes the prior result stale. Amọ̀ṣẹ́ owns ingestion, unchanged echo, aggregate model reconciliation, per-member ADR classification, and durable-record lifecycle. Atona retains plan judgment, readiness, and closure and verifies one exact-current result rather than duplicating the process.

Keep the plan in `Draft` while a material project-knowledge conflict is unresolved or a required Amọ̀ṣẹ́ result is missing, blocked, or stale.

Record evidence or a gap for every decision-shaping claim. Confirm or defer every architecture-changing uncertainty.

## 2. Decide the architecture and verify readiness

Provide a compact architecture recommendation with the problem, constraints, evidence, options, trade-offs, recommendation, phases, and proof plan.

Use these safeguards:

- Keep behavior local unless shared ownership, lifecycle, coordination, restoration, policy, or communication requires a wider owner.
- Move stable identity and durable state across boundaries. Keep runtime handles, callbacks, scopes, and framework objects with their runtime owner.
- Prefer typed state, explicit contracts, and one active owner over parallel flags and implicit coupling.
- Treat queueing, persistence, priority, global arbitration, and universal registries as separate design decisions.
- Decide ownership and visibility at the smallest meaningful capability.
- Cover each material state, ownership, lifecycle, and boundary decision with normal behavior proof and one relevant edge or failure scenario.

For each proposed module or seam, name its callers, required caller knowledge, hidden complexity or policy, and behavior proof. Reject it when deletion exposes only pass-through calls without exposing complexity. Keep a shallow seam only for a proven integration, ownership, lifecycle, policy, or testing need.

Before setting the plan to `Planned`, and after final Arojinle confirmation, run one readiness gate:

1. Re-read the plan as its implementer. Check intent and acceptance; scope and non-goals; design and ownership; behavior and risk; failure, remediation, and recovery; compatibility and migration; delivery, proof, and manual review; test replacement; rollback; documentation and operations; final acceptance; and relevant domain concerns.
2. Treat the Arojinle result as input, not proof. Verify its closure against the exact plan: decisions are realized or marked not applicable with a reason; plan clauses trace to a decision or current fact; overlaps have precedence; delivery states and authorities are ordered; and acceptance detects the top failures.
3. Treat coverage as an index. Resolve plan-local gaps without repeating the interview. Assume the outcome failed, trace the top mechanisms and interactions, and record each retained mechanism, correction or proof, gap, residual risk, and plan identity.
4. Apply corrections. Arojinle owns each new material user decision. Record readiness as `Confirmed` with evidence, `Deferred` with an owner and trigger, or `Open` with the required decision or proof.

Set the plan to `Planned` only when the recommendation covers all in-scope ownership and behavior and the implementer needs no invented material requirement. Otherwise, keep it in `Draft`. This includes an open, pending, stale, contradictory, or missing gate; a waiting prerequisite; a blocking deferral; missing evidence or decision; or invalid Arojinle identity, coverage, or closure. A non-blocking deferral needs an owner and trigger and must not force material invention. Approval covers only listed decisions.

When the plan has multiple review candidates, candidate dependencies, multiple implementers, or a multi-session handoff, or when the user requests local tickets, use `seda-ticket` before setting the plan to `Planned`. Give it the exact source semantic plan revision and input whole-artifact digest; owner-supplied stable graph ID, node-ID prefix, phase and candidate definition keys, and exact unique HTML anchors; settled phases, candidates, candidate-edge expansion, acceptance, proof, rollback, scope, and owners; and explicit predecessor mappings or pure-removal declarations for every identity change. Require one active local ticket per review candidate, a phase parent for every multi-candidate phase, explicit candidate dependency direction, and a verified result against the exact plan. Seda Ticket returns checked derived-graph contents for `<div id="local-ticket-graph">`; `html-artifact` owns the digest-checked physical update and receipt without advancing the semantic source revision; Seda Ticket verifies the returned exact artifact. Keep the plan in `Draft` when the graph is missing, incomplete, stale, cyclic, or mismatched. Atona retains readiness and plan state; the ticket graph is a derived coordination view.

## 3. Track authorized delivery

Keep the request, decisions, evidence, risks, phases, candidate, proof gaps, documentation destinations, and lifecycle states current in the plan. Remove stale guidance and redundant snapshots.

Require explicit implementation authority. Immediately before the first edit, set implementation to `Started` and record the date, candidate branch and commit or tree state, phase, and authority. Investigation, clarification, and plan edits do not start implementation.

Translate each delivery phase into one or more stable, self-contained review candidates. Give each candidate its scope, dependencies, acceptance behavior, proof, and rollback boundary. Do not make every TDD slice or local commit an Alaga invocation, and do not force a whole phase into one candidate when it contains independent reviewable changes. Keep phase-level integration and acceptance proof in the plan.

Use `audit-refactor-behavior` before a stateful refactor that can change transitions, ordering, locking, retries, idempotency, ownership, or cross-entry behavior. Use `alaga` for each full feature candidate or `tdd` for bounded test-first implementation.

For work owned by another skill, record its owner, scope, evidence, blocked outcome, and required result. Keep test, review, build, commit, and publication procedures with their owners.

Treat internal Alaga tasks, TDD slices, tests, and commits as delivery detail, not Atona tickets. Record them only when the plan promotes the work to a blocker, handoff boundary, material plan change, or independent review candidate. Accept optional exact-current Git evidence returned by a delivery owner without prescribing or performing Git operations.

Verify each specialist result against the current plan identity and candidate before recording state or evidence. Reject a mismatch as stale and rerun affected readiness or closure checks. Set implementation to `Complete` only after `qp-code-review` returns `RECOMMEND_ACCEPT` for every final in-scope review candidate and phase-level integration proof has no blocking evidence gap. Reuse a verified current result. Skip this gate when implementation is `Not Required`.

## 4. Reconcile and close

Before `Closed`, verify no blocking decision remains; delivery and review match the candidate; validation and proof gaps are recorded; deferrals have an owner or trigger; follow-ups are classified as blocking or non-blocking; freezes and `leave unchanged` decisions hold; and no unresolved item, stale name, replaced or deprecated primitive, outdated guidance, or test without replacement remains.

For each `.learnings`, `.nongoals`, or ADR destination, verify one exact-current Amọ̀ṣẹ́ result rather than repeating its discovery. For ordinary documentation, require the owning delivery skill to record `updated now`, `already reconciled` with evidence, or `not applicable`. Do not leave obsolete guidance current.

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
