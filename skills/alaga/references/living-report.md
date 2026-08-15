# Living report

Load this contract when an Alaga job qualifies for an independent report.

## Select and create the report

Keep one report for the complete supplied job. Delivery units, candidates, and specialist results are sections or exact links within it.

Create the report when any of these triggers holds:

- multiple delivery units or review candidates;
- multiple specialist owners whose independent delivery results need job-level integration;
- Atona or Seda Ticket coordination;
- session or owner handoff;
- partial-blocker continuation;
- external, destructive, or irreversible writes;
- data, schema, or state migration;
- a security, authentication, privacy, financial, compatibility, rollback, or recovery boundary;
- an early bounded review for material risk; or
- an explicit user or repository requirement.

Routine proof and required review of one candidate do not by themselves count as coordinated specialist delivery. Skip the report only when every safe-harbor condition holds: one unit, one candidate, one session, no handoff, no coordinated delivery-result integration, no listed risk or authority boundary, no blocker or continuation state, and no explicit requirement. Do not use subjective complexity or agent-selected decomposition to escape a trigger.

Alaga supplies the exact report purpose, content, state, and evidence to `html-artifact`. HTML Artifact owns requested, existing, or default path selection; creation or update; composition; accessibility; resource policy; verification; portability; lifecycle return; and full absolute path handoff. Alaga must not implement a storage subsystem or fallback writer.

When Atona coordinates the job, its live plan pins the report path, owner, status, content identity or revision, and last verified time. The plan summarizes only integration effects and does not copy report state.

## Maintain exact-current job state

Keep a concise header and work map with:

- requested outcome, scope, exclusions, authority, and horizon;
- delivery units, owners, dependencies, acceptance, and proof;
- candidates, current states, blockers, and next action; and
- exact-current specialist result identities and their dependency effect.

Alaga owns job-state decisions. When the report exists, it is the authoritative durable record of Alaga's job envelope and current job state. HTML Artifact owns the report's representation and file lifecycle. Each specialist retains its native state and lifecycle.

Update the report for a material scope, decision, dependency, candidate, proof, blocker, authority, context, or next-action change. Mark affected claims stale or superseded, preserve concise lineage and reason, and recompute blockers, proof gaps, and next action. Do not overwrite material history silently.

Retain enough evidence to audit and review the job: authority, material changes and reasons, exact artifacts and candidates, proof and review results, transition receipts, blockers and resume triggers, documentation disposition, handoffs, residual limitations, and verified times.

Update only for material changes. Summarize by outcome and evidence. Link native artifacts and detailed logs, collapse superseded detail into concise lineage, and omit step-by-step operations unless they explain a failure or authority-sensitive action. Do not turn the report into a transcript, chronological activity feed, or command log.
