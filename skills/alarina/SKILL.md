---
name: alarina
description: Select the shortest useful route through published QP skills. Focus on one primary outcome owner and only necessary supporting skills.
---

# Alarina

Map one user prompt to one primary QP skill and any necessary supporting skills. Alarina owns route selection, not the selected specialist workflow.

## 1. Select the route

Use the task's current state and requested outcome. Respect a QP skill that the user explicitly selected. Recommend an additional QP skill only when a clear gap, conflict, or safety condition requires it.

Choose the shortest route that fully covers the requested outcome. Select one primary skill as the outcome owner. Add supporting skills only when they have a clear role. Do not prescribe a broader process when a direct skill covers the task.

Before implementation, a stateful refactor requires an `audit-refactor-behavior` result when it may change transitions, ordering, locking, retries, idempotency, financial ownership, or behavior across entry points. `tdd` or `alaga` owns later implementation only after the audit establishes the baseline and implementation guardrails.

When `atona` finds a new or reopened material architecture decision, `arojinle` owns the interview. Atona supplies the live plan and decision evidence as starting context. Reuse an earlier clarification only when its coverage, scope, decision tree, closure proof, evidence, and unresolved branches remain current. Atona remains the primary owner and verifies the confirmed Arojinle closure proof against the exact plan before readiness.

Keep runtime-behavior work separate from repository review policy, agent skills, external review automation, credential discovery, and secret-file conventions unless the request explicitly includes those surfaces. Use separate routes or candidates when it does not.

Treat an unqualified request to review code as broad. Select `qp-code-review` as the primary owner and `simplify` as its supporting maintainability specialist. Select `qp-code-review` alone only when the user explicitly limits the review to defects and excludes maintainability.

| Starting situation | Primary route |
| --- | --- |
| The user needs help selecting the shortest useful QP route | `alarina` |
| Domain language, canonical project knowledge, an ADR lifecycle action, or root `.nongoal` needs reconciliation | `alakowe` |
| An idea, plan, or decision needs complete frontier rounds and a durable record | `arojinle` |
| Production behavior must change under test-first proof | `tdd` |
| One feature needs clarification, test-backed implementation, and broad review | `alaga` |
| Changed code needs a read-only maintainability or documentation review | `simplify` |
| Bounded code or an active PR or MR needs broad or defect-only review | `qp-code-review`, with `simplify` for broad review |
| A planned or completed refactor needs a parity ledger, or a stateful refactor requires a pre-implementation behavior gate | `audit-refactor-behavior` |
| One standalone HTML artifact, such as a report, visualization, prototype, demo, or bounded interactive tool, is the requested result | `html-artifact` |
| Architecture or migration work needs one live plan from decisions through delivery, with a clear next action | `atona` |
| The current conversation needs a safe handoff for another agent | `handoff` |
| One coding-agent session needs an evidence-backed friction analysis and durable improvement assessment | `ayewo-igba-ise` |
| A question needs high-trust research from primary sources, captured in a Markdown file | `iwadi` |
| One portable agent skill needs creation or revision | `ko-skill` |
| Coding-agent communication instructions plus companion tools or supported integrations need a baseline setup | `qp-setup` |

Keep an unresolved material product or architecture decision with `arojinle` or `atona`; use `alakowe` only after authority is confirmed or when it must surface the knowledge conflict. Keep read-only maintainability and documentation review with `simplify`.

Check the active skill inventory before returning the route. When the correct owner is unavailable, name it as unavailable and do not substitute another skill.

Ask one focused question only when different answers would select materially different owners. Return no QP route when no published skill fits the requested outcome.

## 2. Report the route

If the user asks only which skill owns the prompt, report the primary skill, one concise reason, and any supporting skills.

If the selected primary skill is unavailable, report the route and missing owner.

State the route only when its choice, trade-off, or unresolved decision affects the user.
