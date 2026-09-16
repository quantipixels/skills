# C06 — explicitly named Data change plan

**Observation:** executed outcome  
**Instruction source:** supplied candidate  
**Workspace:** a disposable copy of `evals/engineering/fixtures/migration/`

Use the supplied Alárinà candidate and installed-skill definitions available in this run.

Use Alárinà's **Data change** playbook to make a migration plan for this populated legacy database. Planning only: inspect the supplied schema, code, representative data, and tests; state the required mapping invariant, intermediate-state and retry checks, evidence needed before delivery, rollout stop conditions, and recovery obligations. Do not edit the implementation, run a live rollout, publish, or merge.

After the first plan is delivered, the evaluator supplies this follow-up: “Keep the accepted mapping and planning-only scope. Update the plan to make an observed unsupported schema version an explicit rollout stop condition, and show the changed next action and required evidence.” Apply that update to the delivered plan.
