# Job report

Load this contract at job acceptance and after decomposition or a material shift. Decide whether the job needs one explicit human-facing report beyond the ordinary final delivery result.

## Reuse an active `atona` plan

Update the active `atona` plan with the job result and evidence instead of creating a parallel report.

## Require an explicit job report

Without an active `atona` plan, keep one job-level report when any condition below holds:

- multiple delivery units or review candidates need one integrated status/result;
- multiple specialist results need job-level reconciliation;
- `seda-ticket` coordinates work that is not already governed by an `atona` plan;
- a blocker, continuation state, session break, or owner handoff makes resumability material;
- an external, destructive, or irreversible write is in scope;
- data, schema, or state migration is in scope;
- a security, authentication, privacy, financial, compatibility, rollback, or recovery boundary is material;
- an early bounded review addresses material risk; or
- the user or repository explicitly requires the report.

Routine proof and required review of one candidate do not alone require a report. Do not use subjective complexity or agent-selected decomposition to bypass a trigger.

## Keep meaning with Alága; choose representation separately

Alága owns the exact-current report meaning:

```text
Job outcome and boundary
Delivery units / candidates
Current proof and review
Blockers / resume trigger
Residual limits / risks
Remaining work
Next safe action
```

The report may be returned directly in the current handoff/output. Do not require an HTML artifact, durable file, owner record, or other representation merely because the report gate fired.

Use `html-artifact` as needed.

When a durable file/record is actually required, preserve the caller/repository's existing destination and persistence owner rather than inventing a new Alága storage convention.
