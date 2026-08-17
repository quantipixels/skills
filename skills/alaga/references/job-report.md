# Job report

Load this contract when an Alaga job can require an independent report.

## Require the report

Keep one report for the complete supplied job. Require it when any of these conditions holds:

- multiple delivery units or review candidates;
- multiple specialist results need job-level integration;
- Atona or Seda Ticket coordinates the work;
- a session or owner handoff or partial-blocker continuation is required;
- an external, destructive, or irreversible write is in scope;
- data, schema, or state migration is in scope;
- a security, authentication, privacy, financial, compatibility, rollback, or recovery boundary is material;
- an early bounded review addresses material risk; or
- the user or repository requires the report.

Routine proof and required review of one candidate do not by themselves require a report. Skip it only when the job has one unit, one candidate, one session, no handoff, no coordinated specialist integration, no listed risk or authority boundary, no blocker or continuation state, and no explicit requirement. Do not use subjective complexity or agent-selected decomposition to bypass a trigger.

## Supply exact job state

Alaga supplies HTML Artifact with the report purpose and audience plus the exact-current:

- requested outcome, scope, exclusions, authority, and horizon;
- delivery units, owners, dependencies, acceptance, and proof;
- candidates, states, blockers, and next action;
- specialist result identities and their dependency effects; and
- material changes, reasons, receipts, handoffs, residual limits, and verified times.

Alaga owns job-state decisions. The report is the durable job envelope when it exists; each specialist retains its native state. For every material scope, decision, dependency, candidate, proof, blocker, authority, context, or next-action change, supply the revised state, affected prior claim, reason, and recomputed blockers or proof gaps to HTML Artifact. HTML Artifact owns input-gap requests, representation, accessibility, revision history, path, file lifecycle, requested non-UI verification, portability, and absolute-path return.

When Atona coordinates the job, its live plan pins the report path, status, content identity or revision, and last verified time. The plan records integration effects without copying report state.
