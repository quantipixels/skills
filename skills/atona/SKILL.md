---
name: atona
description: Shape and maintain a useful initiative plan from the current goal, decisions, dependencies, and evidence. Use for material work that needs a coherent route to an outcome, including changed plans and coordinated delivery. Use formal lifecycle gates only when the initiative requires them.
---

# Atọ́nà

Keep one current plan that makes the desired outcome, remaining choices, dependencies, and next action clear.

Delegate bounded analysis, research, or specialist work to subagents when it materially helps. Keep the plan and planning judgment in the current context.

## Shape the plan

Start from supplied decisions and current evidence. Do not replay discovery or ask the user for facts you can establish. Distinguish confirmed requirements from inference, and keep the scope and non-goals explicit.

When project knowledge could change the approach, constraints, sequence, or proof, reuse applicable evidence already supplied; otherwise search the existing knowledge and research destinations by affected concepts and components. Read plausible matches, check their authority and current applicability, and carry forward only what changes this plan. Flag conflicts rather than treating historical guidance as current authority. An empty search does not itself require a new record or a repository-wide search.

Include the outcome and observable acceptance, the material decisions and assumptions, a useful delivery sequence, dependencies and risks that can change it, the current blocker, and the next action. Match detail to what a fresh contributor would otherwise have to invent. Omit empty sections and bookkeeping that has no consumer.

When execution is tied to a concrete working directory, keep that workspace with the plan: its absolute path and `branch: <branch-name> [main|worktree]`; for a linked worktree also keep the absolute main-worktree path. Update this context when execution moves.

Use `arojinle`, `amose`, `seda-spec`, `architect`, and `seda-ticket` as needed.

When the initiative cannot yet be responsibly stated at full depth, read [progressive shaping](references/progressive-shaping.md). Resolve prerequisites without inventing future requirements or blocking independent work.

## Challenge readiness

For a consequential, uncertain, difficult-to-reverse, or materially coordinated plan, run a [premortem](references/premortem.md) before presenting it as execution-ready and reconcile material findings into the plan.

When the formal managed lifecycle applies, a current premortem is always required before the initiative can enter `Planned`, regardless of whether the ordinary planning path would otherwise skip it. Keep the analysis proportional and in the existing plan or conversation, not a separate report.

## Keep it current

After a material decision, discovery, or delivery result, update the affected plan. Reopen only dependent choices and invalidate only proof that no longer applies. A partly superseded plan is not wholly current.

Use the delivery owner's actual evidence. A task count, worker completion, provider status, or aggregate score does not prove the accepted outcome. Keep missing proof, blocked dependencies, changed scope, and residual limits visible. Planning advice does not authorize implementation or publication.

When the governing workflow requires named readiness states, coordinated multi-candidate delivery, or a durable lifecycle record, use [managed initiatives](references/managed-initiative.md). That branch retains the formal planning, contract, delivery, and closure gates; an ordinary plan does not acquire them by being large or involving several skills.

## Deliver

Persistence: existing project plan; otherwise `.qp/atona/`.

Use `html-artifact` as needed, with [the initiative brief](references/human-view.md).

Before closing work performed in a linked worktree, reconcile the relevant `.qp` state into the accepting workspace so no required initiative state remains stranded in the disposable candidate, then clean reconciled/disposable `.qp` state from the completed worktree while preserving anything not safely reconciled. Record the workspace disposition. Offer to remove the completed worktree; removal requires user approval and declining it does not block closure.

Keep ordinary rationale in the plan and normal delivery history. Use [durable reconciliation](references/durable-reconciliation.md) only for a real governing-knowledge obligation. Required stale sources or missing authority remain blockers, not reasons to manufacture a reconciliation ledger.

Return the current plan, workspace when relevant, any blocking choice or evidence gap, and the first useful action. Report completion only when the accepted planning outcome and its required proof are satisfied; keep planning, implementation, integration, and release state distinct.
