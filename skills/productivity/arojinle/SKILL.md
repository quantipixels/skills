---
name: arojinle
description: Resolve one material product, plan, or design decision through a decision-tree interview, current evidence, durable reconciliation when needed, and final user confirmation. Use when the user must choose among consequential alternatives. Exclude technical architecture design or review, initiative lifecycle planning, implementation, and ordinary fact-finding.
---

# Àròjinlẹ̀

Resolve the complete **material** decision tree: every consequential branch that can change accepted outcome, scope, policy, user experience, risk, cost, compatibility, or trade-off. Do not explore every conceivable preference or reopen choices already confirmed by exact-current evidence.

## 1. Pin the decision and caller

Determine whether an active Atọ́nà plan governs the decision.

When it does, pin the plan record/revision, decision identity, scope, evidence identity, current frontier, and requested plan effect. Treat this as the caller envelope. Do not mutate the plan or create a second user-facing plan/report.

Without an active plan, pin one standalone decision identity, scope, constraints, known evidence, and confirmation boundary.

Use `amose` before the first round only when existing project terms, invariants, `.nongoals`, ADRs, prior decisions, or durable working knowledge can materially constrain the frontier. Do not invoke project-knowledge machinery for a standalone choice that current evidence already frames completely.

Finding facts is the agent's job; making consequential choices is the user's. Use bounded lookup for discoverable facts, and `iwadi` only when substantial reusable research is the needed result. Do not ask the user for a fact the environment/primary source can establish.

## 2. Work the current material frontier

The frontier is every material decision whose prerequisites are settled now. A question whose answer depends on another open choice or missing fact belongs behind that prerequisite.

Ask the whole current material frontier in one round when it remains cognitively manageable. If it is unusually large, group independent questions clearly in the same handoff rather than silently dropping branches. A typical round should be small enough to answer deliberately; do not enforce a numerical quota over material completeness.

Format each question as:

```text
❓ Q1 — <question title>: <question and bounded choices>
💡 <brief evidence/trade-off context only when useful>
➡️ <recommended answer and why>
```

Recommendations are advisory. Wait for the user's answers before settling those branches.

After every round:

1. record confirmed, deferred, and still-open answers;
2. recompute which material branches are now unlocked;
3. mark evidence/candidate-dependent conclusions stale when their prerequisites changed;
4. do not re-ask a settled decision unless new evidence materially invalidates it.

Completion means **no unresolved material branch remains**, not that every imaginable design preference has been discussed.

## 3. Integrate with Atọ́nà or keep one standalone record

### Under an active Atọ́nà plan

After each settled round, return one exact-current receipt containing:

```text
Caller plan/revision
Decision/tree identity and revision
Confirmed answers
Deferred answers and re-entry conditions
Current frontier: EMPTY | OPEN | BLOCKED
Coverage: <material branches inspected>
Evidence identity/freshness
Plan effect and affected phases
Blockers / prerequisite evidence
Next action
```

The Atọ́nà plan owner updates plan meaning and renders the user view. Àròjinlẹ̀ does not create another public plan artifact.

If work must pause before integration, keep only a non-user-facing checkpoint receipt in the active plan bundle's `receipts/` slot when authorized. On resume, Atọ́nà validates it against the current plan/candidate before use.

### Standalone decision

After the first settled round, resolve one owner record through `akosile`:

```text
owner: arojinle
record_type: decision
subject: <stable decision identity>
```

Keep the exact-current material tree, answers, frontier, evidence identity/freshness, next action, and confirmation state in `record.md`; refresh its optional `index.html` through `html-artifact` after material revisions. The record is semantic truth and the HTML must not invent/reinterpret choices.

## 4. Confirm and reconcile

When the material frontier becomes `EMPTY`, present the complete decision set, relevant evidence gaps/deferrals, and current plan/record identity for final user confirmation.

Do not declare shared understanding or persist a consequential decision into durable project knowledge before confirmation.

After confirmation, use `amose` only for destinations actually affected by confirmed terms, invariants, non-goals, ADR-worthy decisions, or authorized project-local craft knowledge. Consume its exact-current readback; do not copy its reconciliation procedure.

Under Atọ́nà, return a final receipt containing the confirmation identity and durable-record links. Standalone, update the decision record first and refresh its HTML from that exact revision.

If required evidence or a required specialist is unavailable, preserve the current tree, classify the frontier `BLOCKED`, and continue only independent branches. Never guess the user's material decision to make progress.
