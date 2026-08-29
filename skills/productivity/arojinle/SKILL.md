---
name: arojinle
description: Resolve material product, plan, or design choices through a relentless, complete decision-tree interview and final user confirmation. Use when consequential choices must be made. Exclude technical architecture, initiative lifecycle planning, implementation, and ordinary fact-finding.
---

# Àròjinlẹ̀

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask now without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Use this compact question shape:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

💡 <only context/example that changes understanding>
➡️ <recommended answer and why>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

💡 <only context/example that changes understanding>
➡️ <recommended answer and why>
```

Do not ask a question whose answer depends on another still-open question in the same round.

Use `amose` before the first round when existing project/domain knowledge can materially constrain the tree.

Finding facts is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The decisions are the user's: put each to them and wait.

The decisions remain the user's. Do not silently convert a recommendation into confirmation.

## Visual support proportionality

Conversation is the primary view for a small/single-round decision set. Use `html-artifact` to visualise the tree/frontier/confirmed decisions when the decision surface is substantial, multi-round, durable across sessions/owners, or materially easier to understand as a visual relationship. Do not create/maintain an HTML projection merely because a decision interview exists.

Use `amose` after confirmation when decisions materially change durable project knowledge.

Finish when the material frontier is empty and the user confirms shared understanding. Return confirmed decisions, material assumptions/evidence, any explicit deferrals/re-entry condition, and the next owner/action. Do not implement the result inside Àròjinlẹ̀.
