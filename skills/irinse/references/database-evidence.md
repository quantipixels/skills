# Database and ORM evidence

Use for a material database fixture, transaction or query-observation tool gap. Reuse an applicable installed project verification specialist's application environment and journey commands; otherwise use the project's existing harness. Irinse owns the selected companion tool's readiness, while Alaga integrates changed-contract proof. Do not add a parallel startup workflow.

## A representative fixture

Discover the supported engine/version, driver/ORM, migration mechanism and build. Reuse existing disposable infrastructure. Testcontainers can provision a real engine when available, but a running process or open port is only basic readiness. Wait for the service capability the tests need, use assigned connection details, apply production migrations and isolate fixture data. Check from an empty database or an identified upgrade snapshot according to the proof question; neither substitutes for the other. Do not point migrations at an unverified shared or live target.

When generated schema bindings are used, validate them against the migrated schema and the selected runtime/generator compatibility. Keep actual engine differences visible; H2, SQLite or an in-memory ORM provider may not reproduce another engine's SQL, locking, constraints or transaction semantics.

For jOOQ programmatic transactions, use the callback-derived configuration (`trx.dsl()`). When assessing existing outer-context use, inspect the configured TransactionProvider: some integrations supply ambient transactions, so syntax alone does not prove a leak. Verify rollback and nested/savepoint behavior with the actual provider and engine. Use `alaga` for a stateful proof experiment when the behavior remains unproved.

## Observe the query that runs

For an ORM performance question, collect the generated SQL, statements/roundtrips, returned cardinality/order and relevant plan or latency at representative data scale. Query source alone does not show database work. Look for repeated per-row queries, row multiplication, buffering or changed pagination semantics; evaluate them against the actual provider, schema and plan.

Use alaga for an unexplained slowdown or selected fix, and adanwo for a comparative experiment. Reuse their baseline and bounds. A smaller query count is not a win if results change or latency/resource use worsens. Avoid universal index or query-plan claims. `EXPLAIN ANALYZE` and equivalent commands may execute the statement; preserve the environment's mutation authority and data protections.

Sources: [Testcontainers readiness](https://java.testcontainers.org/features/startup_and_waits/), [jOOQ/Flyway fixture](https://testcontainers.com/guides/working-with-jooq-flyway-using-testcontainers/), [EF Core test strategy](https://learn.microsoft.com/en-us/ef/core/testing/choosing-a-testing-strategy), [EF Core efficient querying](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying), [jOOQ transactions](https://www.jooq.org/doc/latest/manual/sql-execution/transaction-management/). Read current selected-tool documentation for execution syntax; no installation, schema change or benchmark is automatic.
