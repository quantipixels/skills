---
name: arojinle
description: Resolve a material product, plan, or design through a relentless, complete decision-tree interview and final user confirmation. Use when consequential choices must be made. Exclude technical architecture design or review, initiative lifecycle planning, implementation, and ordinary fact-finding.
---

# Àròjinlẹ̀

Interview the user relentlessly until you reach a shared understanding. Map this as a design tree: every decision branches into the decisions that hang off it.

Work the tree in rounds. The frontier is every decision whose prerequisites are already settled: the questions you can ask now without guessing at answers you have not heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Each question should be formatted like so:

```text
❓ **Q1** - **<question title>**: <question and choices, as needed>

💡 <brief context or example, only when it makes the decision clearer>

➡️ <your recommended answer>
```

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a later round, not this one.

Use `amose` before the first round when existing project knowledge can materially constrain the decision tree. Finding facts is your job, never the user's. When a frontier question needs a fact from the environment, use a bounded lookup first. Delegate when active rules permit and a fresh independent lookup materially protects the interview context or improves the evidence. Do not ask the user for facts you can find. Do not block on a running lookup: hold only its downstream questions and ask the rest of the frontier. The decisions are the user's: put each to them and wait.

Use `html-artifact` to visualise the decision tree, current frontier, and confirmed decisions as the primary human view. Use `amose` after confirmation when confirmed decisions change durable project knowledge.

The session is done when the frontier is empty: every material branch of the design tree has been visited and nothing consequential is left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
