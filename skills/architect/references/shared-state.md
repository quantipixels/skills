# Shared-state design

Use when correctness depends on overlapping transactions or multiple writers to shared mutable state. State the invariant in domain terms, name its authoritative owner, enumerate every writer—including jobs, migrations, administrative paths and retries—and construct the smallest counterexample interleaving that could violate it. Traffic volume alone does not establish or dismiss a race.

Separate atomicity from isolation. Atomicity makes one transaction's local changes commit or roll back together; isolation governs what concurrent work can observe and which interleavings may commit. Determine whether the invariant is row-local, depends on a predicate or range, or spans multiple rows. Then choose the smallest enforcement mechanism that protects that exact invariant across every writer: a database constraint when it can express the rule, a conditional mutation or version check when one authoritative record decides the transition, or provider-supported locking or isolation when the relevant predicate or multi-row relationship requires it. This is not a fixed hierarchy, and stronger isolation is not a universal default. Verify the actual database, driver and framework semantics.

When a serialization failure requires retry, rerun the whole decision in a fresh transaction from fresh authoritative reads; do not replay an inner write derived from stale state. Bound retry behavior according to the accepted contract. Treat ordinary remote side effects as outside the local transaction's rollback boundary; when coordination is required, design explicit durable intent, idempotency or compensation.

Architect returns the invariant, writer set, enforcement boundary and failure semantics. Alága owns executable proof, including controlled interleavings and durable-state checks in its stateful-proof method.

Sources: PostgreSQL [transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) and [serialization failure handling](https://www.postgresql.org/docs/current/mvcc-serialization-failure-handling.html).
