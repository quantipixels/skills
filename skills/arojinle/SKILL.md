---
name: arojinle
description: Resolve consequential choices through a relentless, complete decision-tree interview and final user confirmation. Use when the user wants to work through dependent choices together or be grilled until decisions are settled. Explicit invocation selects the interview. Use ro-wo for a bounded critique or stress-test; exclude specialist design/architecture, initiative lifecycle planning, delivery execution, and ordinary fact-finding.
---

# Àròjinlẹ̀

Use `amose` when unresolved project-specific meaning—terms, identities, boundaries, relationships, ownership, or invariants—can materially change the decision tree.

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

Use `atona` in exploration mode and `prototype` as needed.

The decisions remain the user's. Do not silently convert a recommendation, generated option, comparative grade, or prototype observation into confirmation.

## Make shared understanding visible

When the interview establishes or changes a plan or proposed direction, use `html-artifact` for a living decision view as soon as meaningful direction can be shown; do not wait for the interview to finish or invent content before it exists. Within an initiative, contribute to its existing view through the caller, preserving document identity. For a standalone direction, maintain one view and pass it to the next owner. Keep questions in the conversation and the evolving direction in the document. Other bounded decisions may use visual support when it helps.

Make the problem, intended outcome, recommended direction and rationale understandable without prior project or chat context. Show confirmed decisions, open choices and their dependencies, material alternatives, hard gates, uncertainty, and consequences. After a round materially changes the direction or decision tree, update the source decisions and view before the next dependent decision. Scale the required view to the direction's complexity.

Before final confirmation of a plan or direction, present the current consolidated view so the user can assess what they are agreeing to and what remains deferred. A series of answers or an empty frontier alone does not establish shared understanding. If the required view cannot be delivered, report the gap; continue independent fact-finding without claiming that deliverable is complete.

Before declaring the material frontier empty, challenge the current tree for consequential assumptions, missing branches, contradictory decisions, and dependencies that were never made explicit.

Finish only when that challenge leaves no unresolved material branch, any required view is current, and the user confirms shared understanding. Return confirmed decisions, material assumptions/evidence, decision-changing alternatives/criteria when they constrained the choice, explicit deferrals/re-entry conditions, and the next outcome boundary. Include the view's locator when present and hand its source identity to the delivery/planning owner for continued updates; do not execute resulting delivery inside `arojinle`.
