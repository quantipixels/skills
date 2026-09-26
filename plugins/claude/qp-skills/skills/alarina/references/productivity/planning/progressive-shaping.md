# Progressive shaping

Use when the desired outcome is recognizable but the route is unclear, or a material initiative cannot yet be planned responsibly as a whole. Session size alone does not decide whether shaping is needed.

The purpose is to expose the route progressively without inventing future requirements. This is a shaping method inside Atọ́nà, not another lifecycle, owner, or ticket system. When the managed initiative lifecycle applies, it does not replace the Decision Frontier Gate.

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

Resolve enough breadth to know what can be worked now. Keep a simple account of what is known, unresolved, ready to build, and blocked. Do not force the entire initiative into a complete future task tree.

A slice may proceed under existing authority when its acceptance and dependencies are settled and unresolved later choices cannot invalidate it. Keep dependent work blocked. Slice readiness does not establish whole-initiative readiness; in the managed lifecycle, it does not satisfy the `Planned` gate for the whole initiative.

## Make the next learning step actionable

In the existing plan, give each consequential open question a descriptive name, the decision it affects, its actual prerequisites, the evidence or human response needed, and its next owner. Keep this compact; create separate records only when their detail or independent work needs them. Link by meaningful names and retain the deciding evidence at its existing source. Resume from the current overview and open relevant detail on demand.

Choose from questions whose prerequisites are satisfied. Prefer a bounded step that could eliminate a major uncertainty, distinguish credible directions or unlock several dependent questions, relative to its cost and reversibility. Do not default to the easiest implementation task or invent numerical information-gain scores. State what different results would change before starting.

- Missing facts → investigate directly or use [iwadi](../../../commands/iwadi.md) when substantial research is needed.
- Preferences that experience could reveal → use [adanwo](../../../commands/adanwo.md), with the user supplying the reactions.
- Consequential choices → ask the answerable question or use [arojinle](../../../commands/arojinle.md) for dependent decisions.
- Access, a sample or another practical prerequisite → name the smallest enabling action and its authority. Do authorized work directly; give the human precise steps only for what requires them. Completion provides evidence or access, not a product decision.

Record the answer, its basis and which questions it unlocks, changes or rules out. A rejected or cancelled question does not automatically satisfy its dependants. Avoid a second tracker or runtime status system; when an authorized tracker already owns the work, reuse its identities and dependency links. Concurrent work needs explicit ownership before mutation, without a session quota or mandatory worker.

If every visible question is blocked, work on the controlling prerequisite. If none can yet be stated, use contrasting concrete examples or a cheap prototype to make the uncertainty expressible. If the destination itself is unclear, return to purpose and beneficiary. Never substitute the agent's preference for missing human input.

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

Keep this in-scope unknown territory separate from explicit non-goals. Learning can make an unknown question actionable; it cannot silently restore excluded work. Record a changed scope decision before reopening an exclusion. A decision question is resolved by an answer and its evidence, while a delivery slice is complete only with its accepted outcome and proof; closing one does not close the other.

## Keep user-decision authority separate

When the managed initiative lifecycle applies, the Decision Frontier Gate remains only the state of consequential user decisions:

```text
EMPTY | OPEN | BLOCKED
```

Do not add `FOG` or another exploration state to that gate.

A shaping frontier describes what planning territory is currently actionable. In the managed lifecycle, the Decision Frontier describes whether material user authority is currently required. One may change without the other. Outside that lifecycle, preserve the distinction without introducing its formal gate or states.

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

Stop progressive shaping when the initiative can satisfy Atọ́nà's normal readiness work without inventing material requirements. When the managed initiative lifecycle applies, do not set `Planned` while material not-yet-specifiable territory remains that implementation could encounter inside the accepted scope. Outside that lifecycle, this is the bound for completing whole-initiative shaping, not a prerequisite for building an independently ready slice.

A deferred item may remain only when it is genuinely non-blocking and already has Atọ́nà's normal re-entry contract.

Good: a future optional reporting enhancement is excluded or explicitly deferred with a trigger.

Bad: mark a core migration failure path as 'later' because the plan has not yet discovered the real question.
