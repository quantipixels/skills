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

If `html-artifact` is unavailable or the plan cannot be created, updated, reread, or verified safely, keep the plan in `Draft`, report the required-skill or artifact gap, and do not claim `Planned` or `Closed`.

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
- Prefer deep modules at clean seams: minimize what callers must know while hiding meaningful behavior, policy, or integration complexity. Depth means interface leverage, not implementation size. Treat invariants, ordering, errors, configuration, and performance constraints as part of the interface.
- Cover each material state, ownership, lifecycle, and boundary decision with normal behavior proof and one relevant edge or failure scenario.

For each proposed module or seam, name its callers, the complete interface knowledge they require, the complexity or policy hidden inside, and the behavior proof exercised through that interface.

Apply the deletion test: a useful module causes its hidden complexity to reappear across callers when removed. Reject a pass-through module whose deletion removes only forwarding calls. Keep a shallow module only for a proven integration, ownership, lifecycle, policy, or testing reason.

Do not introduce a speculative seam only for possible future variation. One implementation needs an independent ownership, integration, lifecycle, policy, or testing reason; actual variation makes the seam stronger evidence.

Before setting the plan to `Planned`, and after final Arojinle confirmation, run one readiness gate:

1. Re-read the plan as its implementer. Check intent and acceptance; scope and non-goals; design and ownership; behavior and risk; failure, remediation, and recovery; compatibility and migration; delivery, proof, and manual review; test replacement; rollback; documentation and operations; final acceptance; and relevant domain concerns.
2. Treat the Arojinle result as input, not proof. Verify its closure against the exact plan: decisions are realized or marked not applicable with a reason; plan clauses trace to a decision or current fact; overlaps have precedence; delivery states and authorities are ordered; and acceptance detects the top failures.
3. Treat coverage as an index. Resolve plan-local gaps without repeating the interview. Assume the outcome failed, trace the top mechanisms and interactions, and record each retained mechanism, correction or proof, gap, residual risk, and plan identity.
4. Apply corrections. Arojinle owns each new material user decision. Record readiness as `Confirmed` with evidence, `Deferred` with an owner and trigger, or `Open` with the required decision or proof.

Set the plan to `Planned` only when the recommendation covers all in-scope ownership and behavior and the implementer needs no invented material requirement. Otherwise, keep it in `Draft`. This includes an open, pending, stale, contradictory, or missing gate; a waiting prerequisite; a blocking deferral; missing evidence or decision; or invalid Arojinle identity, coverage, or closure. A non-blocking deferral needs an owner and trigger and must not force material invention. Approval covers only listed decisions.

## 3. Track authorized delivery

When the user requests tickets, the plan has multiple review candidates, dependencies, implementers, or a multi-session handoff, or implementation authority is granted, read [delivery-tracking.md](references/delivery-tracking.md). It owns ticket reconciliation, implementation start, review-candidate shaping, delivery-owner handoffs, and exact-current completion proof. Atona retains plan identity, readiness, integration, and closure.

## 4. Reconcile and close

Before `Closed`, verify no blocking decision remains; delivery and review match the candidate; validation and proof gaps are recorded; deferrals have an owner or trigger; follow-ups are classified as blocking or non-blocking; freezes and `leave unchanged` decisions hold; and no unresolved item, stale name, replaced or deprecated primitive, outdated guidance, or test without replacement remains.

For each `.learnings`, `.nongoals`, or ADR destination, verify one exact-current Amọ̀ṣẹ́ result rather than repeating its discovery. For ordinary documentation, require the owning delivery skill to record `updated now`, `already reconciled` with evidence, or `not applicable`. Do not leave obsolete guidance current.

Align plan and implementation states with remaining work. Before every user-visible handoff, read [suggested-direction.md](references/suggested-direction.md). It owns status-specific **What next**, implementation-authority presentation, required skill gaps, and the conditional **Suggested direction**. Do not start the next action without its required authority.
