---
name: arojinle
description: Resolve a material plan or design through a relentless, complete decision-tree interview, durable domain reconciliation, a visual HTML record, and final user confirmation.
---

# Arojinle

Interview the user relentlessly until you reach a shared understanding. Map this as a design tree: every decision branches into the decisions that hang off it.

Work the tree in rounds. The frontier is every decision whose prerequisites are already settled: the questions you can ask now without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Each question should be formatted like so:

```
❓ **Q1** - **<question title>**: <question and choices, as needed>

💡 <brief context or example, only when it makes the decision clearer>

➡️ <your recommended answer>
```

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a later round, not this one.

Finding facts is your job, never the user's. When a frontier question needs a fact from the environment, use a bounded lookup first. Delegate when active rules permit and a fresh independent lookup materially protects the interview context or improves the evidence. Do not ask the user for facts you can find. Do not block on a running lookup: hold only its downstream questions and ask the rest of the frontier. The decisions are the user's: put each to them and wait.

Use with `amose` and `html-artifact`.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
