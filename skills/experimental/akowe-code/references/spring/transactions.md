# Transactions and proxy semantics

**Priority:** CRITICAL  
**Rules:** 5

Align transaction boundaries with use cases, proxy behavior, rollback policy, and external side effects.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="tx-application-boundary"></a>
## `tx-application-boundary` — Place transactions around application use cases

> Start the transaction at the service/application operation that owns the atomic database change.

### Why it matters

Controller- or repository-fragmented transactions expose partially loaded state and make one use case span several independent commits.

### Avoid

Do not annotate controllers broadly or rely on every repository method to form the intended atomic unit.

### Prefer

Keep transport outside the transaction, invoke repositories inside one use-case boundary, and return detached results.

### Nuance

Read-only query services may use narrower boundaries; preserve lazy-loading and consistency requirements deliberately.

### Sources

- **Spring declarative transactions:** <https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html>
- **Spring Data JPA transactions:** <https://docs.spring.io/spring-data/jpa/reference/jpa/transactions.html>

<a id="tx-proxy-invocation-visible"></a>
## `tx-proxy-invocation-visible` — Remember that proxy advice needs a proxy call

> Ensure `@Transactional`, `@Async`, method security, caching, and resilience annotations are invoked through the configured proxy mechanism.

### Why it matters

Self-invocation bypasses proxy advice, so an annotated internal call can execute without the expected transaction or interceptor.

### Avoid

Do not fix this with arbitrary self-injection or assume private methods are intercepted.

### Prefer

Move the advised operation to an owned collaborator, call through an external bean boundary, or use AspectJ only when that trade-off is explicit.

### Nuance

Inspect the actual proxy mode and method visibility for the detected Spring version.

### Example

**Avoid**

```java
@Service
class BillingService {
    public void bill() { this.persist(); }

    @Transactional
    public void persist() { /* ... */ }
}
```

**Prefer**

```java
@Service
class BillingService {
    private final BillingWriter writer;

    void bill() { writer.persist(); }
}

@Service
class BillingWriter {
    @Transactional
    public void persist() { /* ... */ }
}
```

### Sources

- **Spring AOP proxying and self invocation:** <https://docs.spring.io/spring-framework/reference/core/aop/proxying.html>
- **Spring declarative transactions:** <https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html>

<a id="tx-rollback-contract-explicit"></a>
## `tx-rollback-contract-explicit` — Make rollback semantics match the failure contract

> Know which exceptions mark rollback and declare `rollbackFor`/`noRollbackFor` only when the application contract requires different behavior.

### Why it matters

A checked exception can commit by default while a caught runtime exception can prevent rollback if it never escapes.

### Avoid

Do not catch and swallow a transactional failure or assume every thrown exception rolls back.

### Prefer

Let owned failures propagate, mark rollback programmatically only at a deliberate boundary, and test committed/rolled-back outcomes.

### Nuance

Do not use exception-type rules as business workflow branching when explicit results/states are clearer.

### Sources

- **Spring transaction rollback:** <https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/rolling-back.html>

<a id="tx-remote-effects-outside"></a>
## `tx-remote-effects-outside` — Keep slow or irreversible remote effects outside the database transaction

> Avoid holding locks and connections while calling HTTP, email, brokers, or other systems that cannot participate atomically.

### Why it matters

A remote timeout extends the transaction; a later DB rollback cannot undo an already-sent effect.

### Avoid

Do not solve cross-system atomicity by keeping one local transaction open longer.

### Prefer

Commit durable intent first, then deliver through an outbox/event worker, or use a compensating workflow with explicit idempotency.

### Nuance

A short read-only lookup inside a transaction may be acceptable, but prove latency and consistency consequences.

### Sources

- **Spring transaction strategies:** <https://docs.spring.io/spring-framework/reference/data-access/transaction/strategies.html>
- **Spring Modulith event publication:** <https://docs.spring.io/spring-modulith/reference/events.html#event-publication-registry>

<a id="tx-readonly-is-a-hint"></a>
## `tx-readonly-is-a-hint` — Treat read-only as an optimization declaration, not an authorization control

> `readOnly=true` can influence flush/driver behavior but does not prove that no write is possible on every database and stack.

### Why it matters

Relying on it for safety leaves mutation paths dependent on provider behavior.

### Avoid

Do not use a read-only transaction as the only guard against writes or as a substitute for permissions.

### Prefer

Enforce authorization and command/query separation explicitly; use read-only to communicate intent and optimize where supported.

### Nuance

Verify actual provider/database behavior before relying on read-only for routing replicas or consistency.

### Sources

- **Spring Data JPA transactionality:** <https://docs.spring.io/spring-data/jpa/reference/jpa/transactions.html>
- **Spring declarative transactions:** <https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html>
