# Proving stateful behavior

Use when a changed contract depends on committed state, concurrent operations or recovery and existing proof misses a plausible failure. Select only the relevant experiment below. An applicable installed project verification specialist supplies its actual API, persistence and assembled-journey proof. Alaga integrates that evidence, or exercises the required boundary directly when no specialist applies. This method selects distinguishing evidence, not another workflow. Atunwo may consult it read-only to assess proof.

When uncertainty concerns valid command or state-machine sequences rather than a chosen concurrent interleaving, use the generated-sequence method in [property-based testing](property-based-testing.md). It establishes only the boundaries the subject actually exercises.

## Persistence and atomicity

State the durable postcondition and the transaction that should own it. Exercise the public operation against the supported storage engine when its semantics matter. Commit through the application's real boundary, then read through a fresh transaction/context so an identity map or cached object cannot impersonate persisted data. Verify identity, important values and relationships after hydration. A test's automatic rollback can hide commit-time failures or callbacks; match the claimed behavior.

For atomic multi-write behavior, introduce a controlled failure after an earlier write and before completion, then inspect the durable result from outside the failed transaction. Check the successful control as well. Confirm all writes use the intended transaction context; a transaction-shaped callback alone proves nothing. Exercise caught and propagated errors when their different rollback behavior matters. Verify nested/savepoint and isolation semantics for the actual provider.

## Concurrency, retry and cancellation

Name the forbidden outcome and the ordering that could cause it. Coordinate the relevant operations with a barrier or controllable dependency where feasible; sleeps alone do not establish the intended interleaving. Observe final state and external effects, and retain the order needed to reproduce a failure. A few schedules prove those cases, not all concurrency correctness. A model checker is justified only when a consequential state-space question remains beyond such probes.

For ambiguous completion, allow the effect to occur and then withhold or fail its acknowledgement at a controlled test boundary. Retry the same logical operation and verify its identity and allowed effect count. This differs from failing before the effect. Keep the invariant's business meaning and provider guarantees explicit; do not impose exactly-once semantics universally.

When process-loss recovery is claimed, stop an isolated worker after the effect but before its durable acknowledgement, then restart against the same durable state and external substitute. Check reconciliation, identity and permitted effect count from outside the worker. An exception that runs cleanup is not evidence of abrupt process loss; preserve the failpoint and distinguish which failure model was exercised.

For cancellation, reach the blocked or active phase before requesting cancellation, then observe worker completion, cleanup and any prohibited late effects within a justified bound. Forwarding a token or timing out the caller does not prove the worker stopped. Irreversible work may require reconciliation rather than rollback.

## Migration and recovery

For supported coexistence, use expand–migrate–contract: add the compatible form, migrate consumers, then retire the old form. Verify the real migration from representative populated and intermediate states; test restart at the relevant progress boundary and verify data invariants and completion. An empty-database or final-schema pass does not prove upgrade safety. An enforced stopped-system rollout need not use parallel forms.

Select the supported old/new combinations that could break the changed contract, including generated clients when consumed. Preserve representative persisted and wire values, enum meanings, absent-field behavior and rounding where relevant. Exercise an old writer during transition when supported, then verify the new reader and any promised rollback reader. Regenerating a client successfully proves generation, not that an existing deployed client can consume the new response.

When a transform can alter existing values, audit the mapping against authorized representative populated data, not only clean fixtures. Inspect each mapping branch with exact read-only queries or equivalent evidence: grouped legacy/new pairs, nulls, orphaned references, unmapped values and partial-completion markers as applicable. State the expected invariant and explain discrepancies. Use a stable snapshot, transaction, watermark or recorded time window when available; otherwise account explicitly for legitimate concurrent writes before comparing counts. This method does not grant access to live data or permission to mutate it.

When a schema dump or generated structure artifact changes, pin the supplied comparison base and reconcile its diff with the in-scope migrations. Explain every changed object, relationship and version marker from those migrations. Treat unexplained additions, removals or version changes as drift candidates; skip this check when no generated schema artifact changed. Regeneration or cleanup belongs to an authorized delivery, not to a read-only proof request.

Reuse existing fixtures and failpoints. Use `irinse` for non-obvious database engine, readiness or tool questions. Fault injection belongs in an authorized isolated test environment, never an inferred permission to disrupt live services. If the needed boundary cannot be exercised, report the exact unproved claim.

Sources: [jOOQ transactions](https://www.jooq.org/doc/latest/manual/sql-execution/transaction-management/), [.NET cancellation](https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads), [SQLite anomaly testing](https://www.sqlite.org/testing.html#anomaly_testing), [AWS idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
