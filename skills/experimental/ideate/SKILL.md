---
name: ideate
description: Generate, challenge, and reduce several materially different evidence-grounded possibilities before one is selected for decision or planning. Use when the user needs credible directions, improvements, or opportunities rather than refinement of one existing proposal.
disable-model-invocation: true
---

# Ideate

Expand one grounded opportunity into a diverse candidate set, critique every candidate, and explain only the survivors. Do not choose for the user, turn an idea into requirements, or skip directly to implementation.

## 1. Ground the opportunity

Pin the problem or opportunity, intended beneficiaries, current project or product reality, constraints, known non-goals, evidence boundary, time horizon, and what would make an idea useful. Read only the project surfaces needed to avoid detached suggestions.

Use `iwadi` when current external primary-source evidence can materially change the candidate set. Use `irinse` only when a bounded tool-derived view can expose a relevant structure or pattern. Load either dependency at the evidence branch that requires it, not during selection.

## 2. Generate before judging

Generate the complete initial set before critiquing any candidate so early preferences do not collapse the search. Cover materially different mechanisms, not cosmetic variants. Include at least one conservative extension, one structural alternative, and one surprising but plausible direction when the evidence supports them.

Give every candidate a stable short ID and state:

- the mechanism, not merely the feature label;
- who benefits and how;
- the project evidence or constraint it uses;
- the main cost, dependency, and failure mode; and
- what would have to be true for it to be worthwhile.

Do not invent unsupported product requirements or hide assumptions inside a polished pitch.

## 3. Critique every candidate

Assess each candidate against value, distinctiveness, fit, feasibility, reversibility, operational burden, trust or data boundaries, and the strongest credible alternative. Reject duplicates, weak variants, off-strategy ideas, and candidates whose expected value does not justify their cost. State one concise rejection reason for every removed candidate.

Rank only the survivors. Explain why each survived, the evidence it still needs, and the decision it would create. Novelty is not a benefit by itself.

## 4. Hand off without absorbing the next outcome

Return the opportunity, evidence boundary, complete candidate inventory, rejected candidates with reasons, ranked survivors, unresolved assumptions, and one next-step menu.

Use `ro-wo` when the user wants one survivor tested as a proposition, `arojinle` when consequential alternatives must be chosen through a complete decision interview, and `atona` when a selected direction must become an initiative plan. Invoke the next owner only after the user selects or explicitly requests that outcome.

## 5. Persist only when candidate identity matters

Return inline by default. When downstream work needs stable candidate IDs or the user requests an archive, resolve one record through `akosile`:

```text
owner: ideate
record_type: ideation
subject: <stable opportunity identity>
```

Keep the candidate inventory, critique, survivors, evidence, and next step in `record.md`. A substantial comparison may receive an HTML projection, but rejected volume should remain linked or supporting rather than polluting an active plan. Under Atọ́nà, return a compact receipt; the plan decides which selected or decision-relevant content enters its continuous view.
