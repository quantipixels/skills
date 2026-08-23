# Suggested direction and handoff

End each user-visible handoff with **What next**: recommendation, first step, owner or skill, and required authority. Align the plan status and derived delivery summary with remaining work.

When a material choice remains, give numbered options and mark the recommendation. Do not start the next action without its required authority.

## Status-specific handoff

| Plan status | Use when | **What next** |
| --- | --- | --- |
| `Draft` | A decision, evidence item, or readiness gate is open. | Name the next decision or evidence action. |
| `Planned` | Planning is complete without material invention. | Say, “Planning is complete. Here is a suggested direction for the build.” Give or refresh the concise direction when its trigger applies. Otherwise state only the current authority and recommended starting point. Add phases or proof gates only when they materially affect the recommendation or starting point. |
| `In Progress` | Authorized delivery work is active. | Name the next incomplete phase or gap. |
| `Closed` | No plan work remains, including a resolved amendment. | Name the next workstream or say that planning is complete. |
| `Backlog` | The plan is inventory that does not require closure. | Name its owner and reactivation trigger. |

## Build guidance

When the plan first becomes `Planned` and delivery is required, state delivery authority as `Confirmed` or `Required`. If authority is required, name the exact authority without starting delivery.

Add or refresh **Suggested direction** when the plan becomes `Planned`, delivery authority changes, the direction changes materially, or the user asks for build guidance. On other `Planned` handoffs, state only current authority and the recommended starting point.

Give `alarina` the exact plan identity, settled outcomes, required proof, constraints, and known gaps. Require an exact-current primary skill, applicable mode, necessary supporting skills, and any unavailable owner. Present that result with each owner's plan-specific purpose; do not repeat `alarina`'s inventory, selection, ordering, gap, or starting-owner procedure. The route is advice, not delivery authority. Keep models, subagents, tools, phases, and generic actions out.

End with `alarina`'s recommended starting owner and its first plan-specific action. If delivery authority is required, end with that authority action instead.

Use this compact shape and omit the skill-gap line when no required owner is unavailable:

```text
Delivery authority: Confirmed | Required

Suggested direction
1. <skill> — <outcome or proof it would own and why this plan needs it>.
2. <skill> — <outcome or proof it would own and why this plan needs it>.

Required skill gap: <skill> — <required outcome or proof>.

Recommended starting point: <skill and first plan-specific action | prerequisite action>.
```
