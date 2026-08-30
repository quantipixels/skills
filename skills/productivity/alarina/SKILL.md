---
name: alarina
description: Inventory the skills published in this repository and select the shortest useful skill or flow from the work's current state to the requested outcome. Use when the user or agent is unsure what skill to use, asks what skills are available, or needs the route between several owned outcomes; respect explicit user selection and explicit-only experiments.
---

# Alárinà

Serve as the interface to this repository's skill portfolio. A **route** is the shortest justified path through one or more skills from the work's current state to the requested outcome. Do not force work to begin at an earlier phase merely because that phase commonly precedes the current one.

The name reflects the Yorùbá **alárinà**: a trusted intermediary or go-between who knows enough about both sides to make the right introduction, carries the information needed for them to understand each other, and steps aside once the relationship can proceed directly. Apply the same discipline here: understand the request and available owners, connect only the necessary results/context, never absorb another owner's work, and stop routing once the correct ownership path is established.

Build the current inventory from repository/package skill descriptions and invocation metadata rather than maintaining a second static catalogue inside Alárinà.

## Inventory before routing

For an inventory request, list the current repository skills with:

- category;
- exact trigger;
- owned outcome; and
- Experimental/explicit-only status when applicable.

For an ordinary routing request, inspect the same inventory but surface only the relevant shortlist. Use descriptions/metadata for the first pass; read shortlisted `SKILL.md` contracts only when their ownership boundary, accepted input, handoff, or invocation policy is needed to distinguish the route.

When no repository skill materially improves the result, return `NO_ROUTE`. Do not maintain a catalogue or fallback tree for external skills, tools, plugins, or generic agent capabilities; the calling agent can continue with its ordinary capabilities and environment.

## Route from the current work state

1. Pin the requested outcome, current work state, supplied artifacts/results, active owner when known, and any explicit skill/mode choice.
2. Preserve an explicit user-selected skill when it owns the requested result and its invocation boundary is satisfied.
3. Otherwise choose the narrowest skill that can accept the **current** state and own the next required result. Do not replay exploration, planning, architecture, implementation, review, or publication already settled by exact-current evidence.
4. Follow only real owner handoffs needed to reach the requested outcome. Every added skill must contribute an independently useful result that the next owner actually needs.
5. Treat conditional support as a detour, not a mandatory phase. Keep the primary owner primary while a supporting result is obtained, then return to the owning flow.
6. Pass only the context/result needed for the next owner to begin correctly; do not make Alárinà a durable transcript, copied result store, or parallel coordinator.
7. Once the next owner and necessary handoff are established, step aside. Re-enter only when another material routing choice appears.
8. Experimental skills are explicit-only. Present the exact branch they would improve and wait for acceptance; never make a stable route depend on an unaccepted experiment.
9. Stop at the requested outcome. Do not append review, publication, documentation, retrospective, persistence, or other later work merely because it often follows.

Do not insert `handoff` merely because ownership changes. Use `handoff` only when a portable transfer to another agent/session/context is itself needed; ordinary skill-to-skill composition should consume native results directly.

Routing grants no mutation, provider, credential, publication, review-verdict, or continuing-stewardship authority.

## Route relationships

Use these relationships rather than a fixed flow catalogue:

| Relationship | Meaning |
| --- | --- |
| **Start** | owner that can accept the current state and produce the next required result |
| **Support** | independently useful result required while another owner remains primary |
| **Then** | successor owner needed for another requested outcome |
| **Detour** | conditional branch whose result may materially change the main path |
| **Stop** | requested outcome is satisfied; do not continue automatically |

A request may therefore be one skill, a short flow, or an entry into the middle of a longer possible flow.

## Resolve close boundaries by owned result

Use outcome/authority distinctions, not keywords:

- planning lifecycle vs one material user decision vs technical architecture;
- implementation/proof vs code review vs read-only simplification;
- PR publication vs PR stewardship vs review verdict;
- issue triage vs causal diagnosis vs defect implementation;
- durable project knowledge vs generic documentation/writing cleanup;
- artifact projection vs slide/presentation creation;
- broad design routing vs one directly owned design deliverable;
- tool evidence vs the engineering judgment that consumes it.

When a plan's material user-decision frontier is open, keep the plan owner primary and use the decision owner only for that frontier. When technical/reversible architecture is material, use the architecture owner rather than turning it into a user interview. Keep `.qp` mechanics with `akosile` and semantic record meaning with the originating owner.

## Design routing

Use the exact design specialist directly when one output owner is clear. Use `apere` only while it remains the published design-domain routing owner and design-specific multi-deliverable prerequisites/dependency/approval routing is itself needed. Integrated multi-artifact production belongs to `alaga`, not the router.

## Human-led review

Use `hitl-review` when the user wants a walkthrough, review-category coverage, specialist-backed evidence, and a final human decision. Direct specialist review owners remain preferable for one-shot verdicts.

## Report

For a route, return only the useful path:

```text
Start: <skill/mode> — <why this is the current entry>
Support: <skill/mode + condition, or none>
Then: <next owner + why, only when required>
Detour: <conditional or explicit-only branch, or none>
Stop: <requested outcome>
Why not: <closest materially different route, when useful>
```

For an inventory request, list the repository skills rather than forcing a route.

Ask one focused question only when its answer selects a materially different owner/mode and the answer cannot be established from current context/evidence.
