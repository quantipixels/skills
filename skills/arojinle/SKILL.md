---
name: arojinle
description: Resolve consequential choices through a relentless, complete decision-tree interview and final user confirmation. Use when material choices must be made, dependent decisions need to be surfaced, or the user asks to grill or stress-test a plan, design, idea, or decision; exclude specialist design/architecture, initiative lifecycle planning, delivery execution, and ordinary fact-finding.
---

# Àròjinlẹ̀

Use `amose`.

Interview the user relentlessly until shared understanding is reached and no consequential branch remains silently assumed. Map it as a **decision tree**: every decision branches into the decisions that depend on it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled. Ask the whole answerable frontier in one round, then wait for the user's answers before starting the next.

Present each round in the conversation using numbered question blocks, separated by horizontal rules:

```markdown
❓ **Q<n> - <topic>**
<question, enough context to answer, and choices where useful>

➡️ **Recommendation:** <answer and reason>
```

Each round reshapes the tree. Recompute the material frontier from confirmed answers before asking the next round; answers may create, remove, merge, split, or reframe dependent branches. Do not merely continue the previously imagined tree.

Do not ask a question whose answer depends on another still-open question in the same round.

Finding facts is your job, never the user's. Resolve bounded facts directly. While subagents investigate a prerequisite, ask independent frontier questions now; only questions depending on that evidence wait.

Delegate substantial analysis, research, and expert work to subagents, returning concise findings and evidence links to keep the main context lean.

Use other skills as needed to form or resolve frontier decisions; continue the same interview.

When a frontier choice has several credible alternatives and at least two independent criteria can materially change the recommendation, use a compact decision-specific rubric. Apply hard gates first; derive only the criteria that matter to this decision; show the decisive factor, strongest credible alternative, and material counterevidence. Do not manufacture scores for a trivial/already-determined choice or let an average hide a gate. The rubric supports the recommendation; the decision remains the user's.

Use `ideate` and `prototype` as needed.

The decisions remain the user's. Do not silently convert a recommendation, generated option, comparative grade, or prototype observation into confirmation.

## Visual support proportionality

Use `html-artifact` as needed. Preserve hard gates, uncertainty, and counterevidence in visual comparisons.

Before declaring the material frontier empty, challenge the current tree for consequential assumptions, missing branches, contradictory decisions, and dependencies that were never made explicit.

Finish only when that challenge leaves no unresolved material branch and the user confirms shared understanding. Return confirmed decisions, material assumptions/evidence, decision-changing alternatives/criteria when they constrained the choice, explicit deferrals/re-entry conditions, and the next outcome boundary. Do not execute resulting delivery inside `arojinle`.
