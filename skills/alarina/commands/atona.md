# Carry an initiative to completion

Own progression through the requested outcome, from the first unresolved result to accepting evidence and the authorized handoff. Use one living plan. A supporting command's return is intermediate when the user requested completed delivery. A settled bounded coding task can go directly to [alaga-deliver](alaga-deliver.md).

## Establish the finish and current state

Recover the request, accepted decisions, active plan/candidate, current proof and stopping point. State what must be observably true at completion and which actions the session authorizes. Reuse sufficient existing work; a discovered plan or backlog item is not authority to execute it. Exploration-only, planning-only and review-only requests keep their narrower stops. For planning-only work, use [atona-plan](atona-plan.md) and return its result without starting delivery.

For resumed work, follow the entrypoint’s [resume path](../SKILL.md#resume-without-restarting) to recover the incomplete plan, last relevant session or other actual owner before choosing the next result. Reconcile historical claims with the current workspace and retain the original stopping point; a generic request to continue does not turn planning into implementation.

Distinguish verified implementation, an open PR, provider readiness, merge, deployment and live acceptance. Continue through the requested finish without asking permission again for each authorized stage. Autonomous execution does not itself authorize publication, merge, deployment, installation or destructive cleanup. Explicit-only commands retain their invocation rules.

For long-running end-to-end work, put a concrete goal in the existing plan: the intended user outcome, observable finish and scope/authority limits. Keep a current path from actual state to that goal, with the next ready result and controlling uncertainty. For example: “Goal: the accepted migration preserves existing records and passes the agreed checks; stop at a verified local candidate. Path: establish the failing case → repair → verify consumers → integrate review and documentation.” Use a short path for simple work; when later steps are uncertain, name the next evidence-producing step rather than inventing them. A goal guides execution; it does not add permission or a second tracker.

## Compose the next useful result

Use the matched playbook for progression and load only methods needed by the current state. If no playbook covers the outcome, follow Alárinà's scoped command/reference discovery and compose a sufficient path. A custom path needs no new command or script to run.

- Alternative directions → [atona-direction](atona-direction.md).
- Shape one idea → [arojinle](arojinle.md) for consequential unresolved intent, [seda-spec](seda-spec.md) for observable behavior, and direction exploration only when alternatives remain useful.
- Establish or revise the approach, sequence and proof → [atona-plan](atona-plan.md). It owns planning depth, progressive wayfinding, premortem and rollout-planning methods; consume its result in the existing plan.
- Implement a sufficiently settled outcome → [alaga-deliver](alaga-deliver.md), including its verification, local review, corrections and affected documentation.

Pass the bounded question, current evidence, authority and stopping point. Inspect the returned result before advancing. A blocker or incomplete proof is not overridden by an artifact's existence. Resolve the controlling gap, continue independent authorized work where useful, and then resume the dependent path. Do not cycle between owners over the same unanswered prerequisite.

## Continue autonomously when requested

### Entry examples

| Request | Action and stopping point |
| --- | --- |
| `alarina take this accepted change from implementation through verified delivery; work autonomously` | Continue through implementation, relevant checks, required review and documentation. Finish at the verified local candidate. |
| `alarina atona implement the accepted fix, verify it and open a PR; I’m AFK` | Continue through local readiness and authorized PR publication. Opening the PR does not authorize merge or deployment. |
| `alarina work hands-off on a plan for this migration; do not implement` | Use [atona-plan](atona-plan.md); return the plan without source edits or delivery. |
| `alarina resume the accepted initiative; implementation is complete and only verification remains` | Inspect the actual candidate and recorded proof, then complete the remaining verification without restarting settled stages. |
| `alarina finish the feature while I’m away; the retention period still needs my decision` | Resolve discoverable facts and independent work. Keep retention-dependent implementation blocked until the user supplies that policy; absence is not an answer. |

These are illustrative requests through the same entrypoint. Once loaded, `atona` is sufficient; there is no separate autonomous skill, agent profile or background-service switch.

### Interaction and continuation

An end-to-end request authorizes continued work through its stated scope; an explicit hands-off or AFK request changes interaction, not the finish or permissions. Resolve observable facts from the project or a suitable experiment. Make routine and explicitly delegated choices, recording consequential assumptions in the current plan. Ask the human only for a missing decision they still own; their absence does not confirm a preference. Block dependent work when that decision is necessary and continue independent work within scope.

Present the initial direction and material changes for visibility, without adding an approval gate unless the user requested one. After a command or worker returns, consume its evidence and continue to the next ready obligation in the active run. Do not end with an offer to perform already-authorized work.

Use the host's supported execution, waiting and resumption capabilities. Do not promise progress after the session ends unless durable background execution is actually available. For external waits, use native event delivery where supported; preserve a resumable handoff if the host cannot continue. No custom loop service is required.

When an attempt fails, use the evidence to correct the cause or change approach. Repeating an unchanged failed attempt is not progress. Respect user/host budgets and pause requests; report a genuine capability, authority or evidence blocker instead of spinning or weakening acceptance. Revert only owned unsuccessful changes when safe; a source revert does not undo external effects.

## Integrate delivery and proof

Keep the current plan aligned with material decisions, discoveries, candidate changes and evidence. [atona-plan](atona-plan.md) owns substantive replanning; routine progress updates need no new planning pass. Preserve requested work and mandatory obligations, retire invalid assumptions and reopen only dependent choices or proof. Optional recommendations do not become completion conditions.

At resumption, worker handoff and a material discovery, compare the next action with the goal and current path. Include newly discovered necessary work within scope, revise the path when evidence invalidates it, and keep interesting but unrelated improvements optional. Change the destination only when evidence or a user decision justifies it; do not substitute a convenient intermediate artifact for the accepted finish.

Delegate useful independent work through native controls, with clear scope, workspace, acceptance and authority. Before delegating or accepting a worker handoff, read [coordination](../references/productivity/coordination.md) for ownership, observed worker state and lifecycle controls. Bound assignments and completed candidates awaiting integration by the capacity to integrate and verify them. Inspect decisive evidence, not worker completion claims; the main agent owns acceptance of the combined result.

Give each dependency-ready coding slice to [alaga-deliver](alaga-deliver.md). Consume its candidate, proof, documentation result and remaining gaps. Reuse its independent review; use [atunwo](atunwo.md) for additional integrated judgment only when warranted or requested, returning accepted corrections to delivery. When multiple work units, candidates or sessions need coordination, read [delivery tracking](../references/engineering/delivery/delivery-tracking.md). When a governing workflow requires formal initiative states, read [managed initiatives](../references/productivity/planning/managed-initiative.md); size alone does not require it.

Assess the combined result against initiative acceptance, including interactions between slices and the actual user journey when relevant. Give delivery the bounded integration gap to verify and correct. Task counts, isolated checks and provider status do not establish whole-system success. Use the smallest sufficient check; broaden only for changed behavior, invalid evidence, a concrete failure or a governing requirement.

Confirm required documentation across slices is reconciled. Reuse delivery's documentation evidence; [akowe-audit](akowe-audit.md) or [akowe-sync](akowe-sync.md) handles a remaining set-wide assessment or authorized reconciliation. Keep gaps in this same plan.

Use [seda-pr](seda-pr.md) for authorized publication and [wo-pr](wo-pr.md) when the requested finish includes PR readiness or stewardship. Complete applicable local readiness before pushing. A publication-only request ends at verified publication; it does not silently become merge or release work.

## Preserve continuity and finish

For useful persistence, follow [records](../references/productivity/records.md) and update the existing plan. Preserve scope, decisions, current candidate/workspace, decisive proof, unresolved obligations and next action. Record the main-worktree path for a linked worktree when needed for resumption; omit machine-specific paths from portable/public artifacts unless requested. Keep ordinary rationale in the plan; use [durable reconciliation](../references/engineering/documentation/durable-reconciliation.md) when governing knowledge needs updating.

Before closing a linked-worktree initiative, reconcile required state with the accepting workspace and record its disposition. Preserve unresolved state; remove a worktree only with applicable user approval. Retaining it does not block completion.

Close when the requested outcome has current accepting proof, required integration and documentation are complete, and no blocking in-scope obligation remains. Keep the plan current without rebuilding unaffected reports or repeating valid checks. Return the outcome, actual delivery state, plan locator when saved, decisive evidence and material limits. If blocked, return the exact unmet requirement and next input/action. Optional cleanup, broader review and polish remain follow-up.
