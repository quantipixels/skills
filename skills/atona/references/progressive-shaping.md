# Progressive shaping

Use this branch only when a material `Draft` initiative is too large or uncertain for its whole planning surface to be stated responsibly at once.

The purpose is to expose the route progressively without inventing future requirements. This is a shaping method inside Atọ́nà, not another lifecycle, owner, ticket system, or replacement for the Decision Frontier Gate.

## Name the destination first

State the destination at the lowest useful resolution:

```text
What must be true when this initiative succeeds?
```

The destination may still be revised by confirmed evidence or user decisions. It is not an excuse to guess architecture, implementation, migration, or policy details.

Good: `Customers can migrate from provider A to provider B without losing active subscriptions or requiring manual support repair.`

Bad: `Build tables X/Y, queue Z, four migration jobs, and a retry dashboard` before the relevant design and evidence exist.

## Explore breadth before depth

Before drilling into one attractive branch, surface the currently visible planning territory:

- facts or evidence that can change the plan;
- currently formable technical-design questions;
- currently formable material user decisions;
- reversible plan-local choices;
- known dependencies and blocked branches; and
- in-scope territory whose actual question cannot yet be stated without guessing.

Resolve enough breadth to know what can be worked now. Do not force the entire initiative into a complete future task tree.

## Distinguish blocked from not yet specifiable

A **blocked question** is already precise, but a prerequisite fact, decision, or specialist result is missing.

```text
Question: Which compatibility mode should migration use?
Blocked by: provider contract/version support evidence.
```

**Not yet specifiable** territory is different: earlier results determine what the future question itself will be.

```text
Territory: billing migration implications after the storage ownership model is selected.
Why not specifiable yet: the storage decision determines which billing identities and reconciliation paths exist.
```

Good: preserve that territory as a short exact-current reminder and return to it after the prerequisite result.

Bad: invent several billing decisions now merely so the plan appears complete.

Do not use not-yet-specifiable territory for vague work that can already be made precise. If the question can be stated responsibly now, classify it through Atọ́nà's normal uncertainty owners even when it remains blocked.

## Keep the Decision Frontier separate

The Decision Frontier Gate remains only the state of consequential user decisions:

```text
EMPTY | OPEN | BLOCKED
```

Do not add `FOG` or another exploration state to that gate.

A shaping frontier describes what planning territory is currently actionable. The Decision Frontier describes whether material user authority is currently required. One may change without the other.

Good: a later integration area is not yet specifiable while the current Decision Frontier is `EMPTY`.

Bad: mark the Decision Frontier `OPEN` because some future technical question has not become formable.

## Re-chart after material results

After a result materially changes what can be known:

1. update the exact-current plan meaning;
2. retire assumptions made obsolete by the result;
3. identify newly formable facts, technical-design questions, material user decisions, or plan-local choices;
4. move no-longer-uncertain territory out of the shaping remainder;
5. stale only dependent proof or conclusions; and
6. continue from the newly visible edge.

Do not retain historical copies of every prior map. The plan remains exact-current and links detailed evidence to its owner.

## Know when this branch is no longer needed

Stop progressive shaping when the initiative can satisfy Atọ́nà's normal readiness work without inventing material requirements. Before `Planned`, no material not-yet-specifiable territory may remain if implementation could encounter it inside the accepted scope.

A deferred item may remain only when it is genuinely non-blocking and already has Atọ́nà's normal re-entry contract.

Good: a future optional reporting enhancement is excluded or explicitly deferred with a trigger.

Bad: mark a core migration failure path as 'later' because the plan has not yet discovered the real question.
