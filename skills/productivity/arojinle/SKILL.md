---
name: arojinle
description: Resolve material product, plan, or design choices through a complete decision-tree interview and final user confirmation. Use when consequential choices must be made. Exclude technical architecture, initiative lifecycle planning, implementation, and ordinary fact-finding.
---

# Àròjinlẹ̀

Interview the user until consequential branches are explicitly settled. Map a decision tree: each decision can expose later decisions that depend on it.

Work in rounds. The frontier is every material decision whose prerequisites are already settled. Ask the whole current frontier in one round; number each question and give a recommended answer. Then wait for the user's decisions before recomputing the next frontier.

Use this compact question shape:

```text
❓ **Q1 — <title>:** <question and bounded choices when useful>
💡 <only context/example that changes understanding>
➡️ <recommended answer and why>
```

Do not ask a question whose answer depends on another still-open question in the same round.

Use `amose` before the first round when existing project/domain knowledge can materially constrain the tree. Finding facts is the agent's job: resolve bounded current facts through direct evidence/`iwadi`/`irinse` as appropriate rather than asking the user for discoverable facts. Hold only questions downstream of unavailable prerequisites; continue independent frontier branches.

The decisions remain the user's. Do not silently convert a recommendation into confirmation.

## Visual support proportionality

Conversation is the primary view for a small/single-round decision set. Use `html-artifact` to visualise the tree/frontier/confirmed decisions when the decision surface is substantial, multi-round, durable across sessions/owners, or materially easier to understand as a visual relationship. Do not create/maintain an HTML projection merely because a decision interview exists.

Use `amose` after confirmation when decisions materially change durable project knowledge.

Finish when the material frontier is empty and the user confirms shared understanding. Return confirmed decisions, material assumptions/evidence, any explicit deferrals/re-entry condition, and the next owner/action. Do not implement the result inside Àròjinlẹ̀.
