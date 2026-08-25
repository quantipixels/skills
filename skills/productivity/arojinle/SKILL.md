---
name: arojinle
description: Resolve one material product, plan, or design decision through a complete decision-tree interview, durable domain reconciliation, a visual HTML record, and final user confirmation. Use when the user must choose among consequential alternatives. Exclude technical architecture design or review, initiative lifecycle planning, implementation, and ordinary fact-finding.
---

# Àròjinlẹ̀

Interview the user relentlessly until you reach a shared understanding. Map this as a design tree: every decision branches into the decisions that hang off it.

Work the tree in rounds. The frontier is every decision whose prerequisites are already settled. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Format each question as:

```text
❓ Q1 — <question title>: <question and choices>
💡 <brief context only when useful>
➡️ <recommended answer>
```

Each answer reshapes the tree. Recompute the frontier after every round; a question depending on another open question belongs to a later round.

Finding facts is your job, never the user's. Use bounded lookup for environment facts. Delegate only when active rules permit and independent evidence materially helps. Hold only downstream questions while evidence is pending. Decisions remain the user's.

Before the first round, determine whether an active Atọ́nà plan governs the decision. If it does, pin the plan record reference/revision, topic, scope, evidence identity, and requested plan effect. Treat that as the caller envelope. Do not mutate the plan or create another user-facing plan/report.

Before the first round, give `amose` the project identity and relevant terms, rules, knowledge, and decision records. Consume its exact-current domain model/conflicts as interview inputs. `amose` does not answer open questions or make the user's decisions. Refresh this evidence when a settled answer changes a domain term, invariant, boundary, or prior decision.

After each settled round under an active Atọ́nà plan, return one exact-current receipt to the plan owner with plan/receipt revisions, decision/tree identities, confirmed/deferred answers, open frontier/coverage, evidence identity/freshness, plan effect, blockers, and next action. The plan owner renders the decision view.

Without an active Atọ́nà plan, give `html-artifact` the exact-current tree, confirmed/deferred answers, open frontier, evidence, and intended audience after the first settled round. Creating/updating this task's visual record is the only implied write. It does not authorize source or durable domain writes. Keep one artifact identity through later rounds and do not let representation add or reinterpret a decision.

When the frontier is empty, present the complete decision set, remaining evidence gaps, and current active-plan link or standalone artifact for user confirmation. Do not persist a decision or declare shared understanding before confirmation. After confirmation, use `amose` to reconcile only confirmed domain terms/rules/decisions into authorized destinations and consume its readback. Then return a final receipt with confirmation identity and durable-record links to the active Atọ́nà owner, or give `html-artifact` the confirmed decisions and durable-record identities for the standalone view.

If a required specialist is unavailable, preserve the exact-current tree and report the missing result. Continue only branches that do not depend on it.

If work under an active Atọ́nà plan must pause before integration, keep a non-user-facing checkpoint receipt in the active plan bundle's `receipts/` directory with the pinned caller envelope, complete tree, freshness, and resume condition. On resume, Atọ́nà validates the checkpoint against the current plan revision and reconciles or rejects it.
