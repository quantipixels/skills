# Job record

Load this contract at job acceptance and after decomposition or a material shift. Choose one human-facing record for the job.

## Contribute to an active Atọ́nà plan

When an active Atọ́nà plan governs the job, do not create a parallel user-facing job report. Return one exact-current contribution receipt to the active plan owner. The receipt includes:

- the plan path and revision, job identity, receipt identity, and receipt revision;
- the exact job and candidate identities, delivered units, and native job result;
- acceptance, proof, required review receipts, blockers, and residual limits;
- the evidence cutoff and `CURRENT` or `STALE` freshness;
- the effect on plan phases, risks, proof, delivery summary, and closure; and
- the next owner, required authority, and checkable completion condition.

Keep job-local execution mechanics, test slices, logs, snapshots, and recovery checkpoints outside the plan. Link independently durable evidence instead of copying it. Return a revised receipt after a material job or candidate change. `atona` alone changes shared plan meaning and status.

## Require a standalone report

Without an active Atọ́nà plan, keep one report for the complete supplied job when any condition below holds.

- multiple delivery units or review candidates;
- multiple specialist results need job-level integration;
- `seda-ticket` coordinates work that is not already governed by an Atọ́nà plan;
- a blocker or continuation state exists, or a session or owner handoff is required;
- an external, destructive, or irreversible write is in scope;
- data, schema, or state migration is in scope;
- a security, authentication, privacy, financial, compatibility, rollback, or recovery boundary is material;
- an early bounded review addresses material risk; or
- the user or repository requires the report.

Routine proof and required review of one candidate do not alone require a report. Do not use subjective complexity or agent-selected decomposition to bypass a trigger.

## Supply exact standalone job state

`alaga` supplies `html-artifact` with the purpose, audience, and exact-current:

- requested outcome, scope, exclusions, authority, and horizon;
- delivery units, owners, dependencies, acceptance, and proof;
- candidates, states, blockers, and next action;
- specialist result identities and their dependency effects; and
- material changes, receipts, handoffs, residual limits, and verified times.

`alaga` owns job-state decisions. The report becomes the job envelope. Each specialist retains its native state. After a material change, supply the revised state, affected prior claim, reason, and recomputed blockers or proof gaps to `html-artifact`.
