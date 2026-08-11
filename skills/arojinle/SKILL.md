---
name: arojinle
description: Resolve material decisions into one confirmed decision tree and durable HTML record. Focus on complete decision frontiers, explicit deferrals, current evidence, and final confirmation.
---

# Arojinle

Interview the user relentlessly until you reach a shared understanding. Map this as a *design tree*: every decision branches into the decisions that hang off it. Keep the tree, facts, answers, and final confirmation in the supplied HTML artifact, or use `html-artifact` to create one.

Work the tree in *rounds*. The *frontier* is every decision whose prerequisites are already settled — the questions you can ask now without guessing at answers you have not heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Each question should be formatted like so:

```
❓ **Q1** - **<question title>**: <question and choices, as needed>

💡 <brief context or example, only when it makes the decision clearer>

➡️ <your recommended answer>
```

Each round the user answers reshapes the tree — settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a later round, not this one.

Finding facts is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it — don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report — ask the rest of the frontier now. The decisions are the user's — put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.

For each confirmed material decision, include an `alakowe` handoff packet with:

- the decision identifier, packet revision, and exact confirmed decision;
- its context and constraints;
- credible alternatives and the real trade-off, or an explicit `none` when the confirmed constraints leave no credible alternative;
- known consequences;
- confirmation and decision authority;
- the exact plan, candidate, or evidence identity; and
- affected readers, surfaces, and nearest known destination.

Do not invent an alternative, pre-filter the packet, apply the ADR qualification threshold, or mutate repository destinations during the interview. Alakowe owns qualification, documentation discovery, creation, and lifecycle reconciliation after confirmation.

Increment the packet revision whenever its identifier, decision, context, alternatives, trade-off, consequences, confirmation, authority, identity, readers, surfaces, or destination changes.
