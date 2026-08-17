# Suggested direction and handoff

End each user-visible handoff with **What next**: recommendation, first step, owner or skill, and required authority. Align plan and implementation states with remaining work.

When a material choice remains, give numbered options and mark the recommendation. Do not start the next action without its required authority.

## Status-specific handoff

| Plan status | Use when | **What next** |
| --- | --- | --- |
| `Draft` | A decision, evidence item, or readiness gate is open. | Name the next decision or evidence action. |
| `Planned` | Planning is complete without material invention. | Say, “Planning is complete. Here is a suggested direction for the build.” Give or refresh the concise direction when its trigger applies. Otherwise state only the current authority and recommended starting point. Add phases or proof gates only when they materially affect the recommendation or starting point. |
| `In Progress` | Implementation, documentation, or proof is active. | Name the next incomplete phase or gap. |
| `Closed` | No plan work remains, including a resolved amendment. | Name the next workstream or say that planning is complete. |
| `Backlog` | The plan is inventory that does not require closure. | Name its owner and reactivation trigger. |

## Build guidance

When the plan first becomes `Planned` and implementation is required, state implementation authority as `Confirmed` or `Required`. If authority is required, name the exact authority without starting implementation.

Add or refresh **Suggested direction** when the plan becomes `Planned`, implementation authority changes, the direction changes materially, or the user asks for implementation guidance. On other `Planned` handoffs, state only current authority and the recommended starting point.

Check the active skill inventory. List only available skills that fit the plan, in a useful likely order. For each, name the plan-specific outcome or proof it owns and why the plan needs it. Mark a gate required only when the confirmed plan or owning skill requires it. The list is advice, not implementation authority or a fixed route. Keep models, subagents, tools, phases, and generic actions out; add requested routing separately.

When a required owner is unavailable, add `Required skill gap: <skill> — <required outcome or proof>.` outside **Suggested direction**. Recommend making the owner available before implementation. Do not hide the gap, substitute another owner, or recommend starting past it.

End with the recommended starting skill and its first plan-specific action. If a required owner is unavailable, end with the action that resolves the gap. If implementation authority is required, end with that authority action instead.

Use this compact shape and omit the skill-gap line when no required owner is unavailable:

```text
Implementation authority: Confirmed | Required

Suggested direction
1. <skill> — <outcome or proof it would own and why this plan needs it>.
2. <skill> — <outcome or proof it would own and why this plan needs it>.

Required skill gap: <skill> — <required outcome or proof>.

Recommended starting point: <skill and first plan-specific action | prerequisite action>.
```
