# Plan premortem

Run before declaring an initiative ready for execution, including before the managed lifecycle enters `Planned`. Reuse a completed premortem only while its plan, assumptions, dependencies, and evidence remain applicable. This is a challenge to the proposed plan, not a postmortem of events that happened.

## Assume the outcome failed

Pin the current plan or revision and its accepted outcome. Imagine that delivery finished but the outcome failed, or that executing the plan caused an unacceptable consequence. Work backward to credible causes instead of defending the proposed approach. Treat these explanations as hypotheses, not observed incidents or measured probabilities.

Look where this plan is vulnerable: a critical assumption is false, the sequence creates an unsafe intermediate state, a dependency or permission is unavailable, ownership breaks at a handoff, verification can pass the wrong result, or recovery cannot undo an effect. Include adoption, operational capacity, cost, and timing when they control the outcome. Do not fill a risk taxonomy or invent a quota of failures.

Use an independent perspective when a consequential or contested assumption warrants it and the host supports one. Generate failure explanations before showing proposed mitigations. A solo challenge remains useful, but do not describe it as independent review.

## Change the plan where the challenge matters

For each material scenario, establish the causal path, the assumption or dependency it exposes, and the earliest observable warning. Seek counterevidence and existing safeguards before adding work.

Choose the smallest adequate response: remove the exposure, revise the approach or sequence, resolve an uncertainty, add a necessary proof or recovery step, or retain a justified residual risk. Give a material mitigation an owner and a checkable completion condition; give a retained operational risk an observable re-entry or stop trigger where applicable.

Update the owning plan and affected requirements, dependencies, acceptance, or proof obligations. Use `arojinle` for material user choices and the relevant specialist for missing evidence. Do not silently enlarge scope, change accepted requirements, or acquire execution authority through a mitigation.

For example, a rename-and-backfill plan can fail while old application instances still write the old field. A credible response might change the rollout sequence and specify compatibility evidence before removing the old representation. It is not enough to append “migration risk: medium”; nor should the planner prescribe an extra compatibility layer when an existing rollout constraint already eliminates the failure.

## Readiness and freshness

The plan is not ready while a material readiness threat remains unresolved, the analysis is missing or materially stale, or a required decision or evidence source is unavailable. In the managed lifecycle, keep an unready plan `Draft`; a complete task list is not a substitute for this gate.

Readiness does not require a risk-free plan. A residual risk may remain only within accepted constraints and the responsible decision-maker's authority, with its reason and any necessary owner, detection, and recovery condition visible. Do not relabel an unmet requirement, forbidden effect, or missing mandatory proof as accepted risk.

Record the premortem's plan boundary, material findings and dispositions, resulting plan changes, and readiness conclusion in the plan or conversation. A supported “no material change” conclusion is valid; an empty heading or an unchecked box is not a premortem. Do not create a separate risk ledger or report by default. Premortem reasoning is not runtime proof.

After a material plan, scope, assumption, dependency, or evidence change, revisit the affected failure analysis before restoring readiness. Preserve unaffected analysis and authorized independent work. A mitigation that changes the plan must itself be checked for newly introduced failure paths; do not reuse a conclusion that predates it.
