# Job report

Load this contract when an `alaga` job can require an independent report.

## Require the report

Keep one report for the complete supplied job. Require it when any of these conditions holds:

- multiple delivery units or review candidates;
- multiple specialist results need job-level integration;
- `atona` or `seda-ticket` coordinates the work;
- a blocker or continuation state exists, or a session or owner handoff is required;
- an external, destructive, or irreversible write is in scope;
- data, schema, or state migration is in scope;
- a security, authentication, privacy, financial, compatibility, rollback, or recovery boundary is material;
- an early bounded review addresses material risk; or
- the user or repository requires the report.

Routine proof and required review of one candidate do not alone require a report. Do not use subjective complexity or agent-selected decomposition to bypass a trigger.

## Supply exact job state

`alaga` supplies `html-artifact` with the purpose, audience, and exact-current:

- requested outcome, scope, exclusions, authority, and horizon;
- delivery units, owners, dependencies, acceptance, and proof;
- candidates, states, blockers, and next action;
- specialist result identities and their dependency effects; and
- material changes, receipts, handoffs, residual limits, and verified times.

`alaga` owns job-state decisions. The report becomes the job envelope. Each specialist retains its native state. After a material change, supply the revised state, affected prior claim, reason, and recomputed blockers or proof gaps to `html-artifact`.

When `atona` coordinates the job, its live plan pins the report path, status, content identity or revision, and last verified time. The plan records integration effects without copying report state.
