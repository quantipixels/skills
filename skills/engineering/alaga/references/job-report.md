# Job report

Load this contract at job acceptance and after decomposition or a material shift. Decide whether the job needs one explicit human-facing report beyond the ordinary final delivery result.

## Reuse an active `atona` plan

When an active `atona` plan governs the job, return the exact-current job result to `atona` and do not create a parallel user-facing report. Keep job-local execution mechanics and detailed evidence with Alága or their native owners.

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

Use `html-artifact` only when a substantial visual view materially improves comparison, navigation, review, or handoff, or when the user explicitly requests that representation. `html-artifact` owns only the projection/representation mechanics; Alága remains the semantic owner.

When a durable file/record is actually required, preserve the caller/repository's existing destination and persistence owner rather than inventing a new Alága storage convention.
