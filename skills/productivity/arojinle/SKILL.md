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

Finding facts is your job, never the user's. Delegate bounded independent/noisy lookup when doing it inline would materially pollute the decision context; return only the compact fact/evidence needed, let only dependent questions wait, and continue asking the rest of the frontier.

The decisions remain the user's. Do not silently convert a recommendation into confirmation.

## Visual support proportionality

Conversation is the primary view for a small/single-round decision set. Use `html-artifact` to visualise the tree/frontier/confirmed decisions when the decision surface is substantial, multi-round, durable across sessions/owners, or materially easier to understand as a visual relationship. Do not create/maintain an HTML projection merely because a decision interview exists.

Use `amose` after confirmation when decisions materially change durable project knowledge.

Finish when the material frontier is empty and the user confirms shared understanding. Return confirmed decisions, material assumptions/evidence, any explicit deferrals/re-entry condition, and the next owner/action. Do not implement the result inside Àròjinlẹ̀.
