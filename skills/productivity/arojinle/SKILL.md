---
name: arojinle
description: Resolve a material plan or design through a relentless, complete decision-tree interview, durable domain reconciliation, a visual HTML record, and final user confirmation.
---

# Àròjinlẹ̀

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

Before the first round, give `amose` the project identity and the relevant terms, rules, knowledge, and decision records. Consume its exact-current domain model and conflicts as interview inputs. `amose` does not answer open questions or make the user's decisions. Keep its work read-only before confirmation. Refresh this evidence when a settled answer changes a domain term, invariant, boundary, or prior decision.

After the first settled round, give `html-artifact` the exact-current tree, confirmed and deferred answers, open frontier, evidence, and intended audience. Creating or updating this task's visual record is the only implied write. It does not authorize source or durable domain writes. Keep one artifact identity through later rounds and treat its result as representation evidence only. Refresh it after each material change without letting it add or reinterpret a decision.

When the frontier is empty, present the complete decision set, remaining evidence gaps, and current artifact for user confirmation. Do not persist a decision or declare shared understanding before that confirmation. After confirmation, use `amose` to reconcile only the confirmed domain terms, rules, and decisions into destinations authorized by the user or repository. Consume its readback, then give `html-artifact` the confirmed decisions and durable record identities for the final visual record.

If either specialist is unavailable, preserve the exact-current tree and report the missing result. Continue only branches that do not depend on that result. Do not claim durable reconciliation or a complete visual record unless the user explicitly accepts the reduced outcome.
