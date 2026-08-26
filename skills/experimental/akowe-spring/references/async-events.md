# Async work, scheduling, events, and context

**Priority:** CRITICAL  
**Rules:** 5

Own executors, proxy boundaries, context propagation, schedules, and delivery guarantees.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="async-named-bounded-executor"></a>
## `async-named-bounded-executor` — Give asynchronous work an explicit executor contract

> Configure a named executor or Boot task-execution properties with known concurrency, queueing, rejection, shutdown, and observability.

### Why it matters

The default or an unbounded executor can exhaust memory/resources and mix unrelated workloads.

### Avoid

Do not annotate arbitrary methods with `@Async` without knowing which executor and capacity serve them.

### Prefer

Select the executor by name where several workloads exist and expose saturation/rejection metrics.

### Nuance

Virtual threads remove thread scarcity, not downstream capacity limits; still bound connections and remote concurrency.

### Example

**Avoid**

```java
@Async
public void rebuildIndex() { /* ... */ }
```

**Prefer**

```java
@Async("indexExecutor")
public CompletableFuture<Void> rebuildIndex() {
    // ...
    return CompletableFuture.completedFuture(null);
}
```

### Sources

- **Spring task execution and scheduling:** <https://docs.spring.io/spring-framework/reference/integration/scheduling.html>
- **Spring Boot task execution:** <https://docs.spring.io/spring-boot/reference/features/task-execution-and-scheduling.html>

<a id="async-proxy-and-return-contract"></a>
## `async-proxy-and-return-contract` — Make `@Async` proxy and failure semantics visible

> `@Async` applies through proxy calls and asynchronous exceptions must have an observable owner.

### Why it matters

Self-invocation runs synchronously; `void` failures can be lost except to an uncaught-exception handler.

### Avoid

Do not use private/self-invoked async methods or fire-and-forget important work.

### Prefer

Return `CompletableFuture`/a suitable handle for caller-owned work, or configure a durable job/event owner for detached work.

### Nuance

A transactional method and async method on the same object often express a missing handoff boundary.

### Sources

- **Spring `@Async`:** <https://docs.spring.io/spring-framework/reference/integration/scheduling.html>

<a id="async-propagate-context-deliberately"></a>
## `async-propagate-context-deliberately` — Propagate only required request context

> Security, tracing, logging, locale, and transaction state use different mechanisms and do not automatically follow every task boundary.

### Why it matters

Assuming ThreadLocal inheritance causes missing identity/trace data or accidental leakage between tasks.

### Avoid

Do not copy every ThreadLocal blindly or pass an `Authentication` object as a trusted authorization decision after delay.

### Prefer

Use supported security/context executors, `TaskDecorator`, Micrometer context propagation, or explicit immutable context values.

### Nuance

Transactions should generally end before asynchronous handoff; start a new transaction in the worker when needed.

### Sources

- **Spring Security concurrency support:** <https://docs.spring.io/spring-security/reference/features/integrations/concurrency.html>
- **Spring Boot task execution:** <https://docs.spring.io/spring-boot/reference/features/task-execution-and-scheduling.html>

<a id="sched-idempotent-and-coordinated"></a>
## `sched-idempotent-and-coordinated` — Design scheduled work for overlap, restart, and multiple instances

> A scheduled method may run concurrently, retry after partial failure, or execute on every application replica.

### Why it matters

Single-node development hides duplicate processing and overlapping schedules.

### Avoid

Do not assume `@Scheduled` provides distributed locking or exactly-once execution.

### Prefer

Make work idempotent, define timezone/misfire/overlap policy, coordinate through the database/queue/lock where necessary, and record run state.

### Nuance

For large or durable workflows, use a scheduler/batch platform rather than an in-process annotation.

### Sources

- **Spring scheduling:** <https://docs.spring.io/spring-framework/reference/integration/scheduling.html>

<a id="event-delivery-contract"></a>
## `event-delivery-contract` — Choose in-process, transactional, or durable events by guarantee

> Ordinary application events are synchronous by default and not durable; transactional listeners bind to transaction phases.

### Why it matters

Treating either as a broker can lose work on rollback, crash, listener failure, or restart.

### Avoid

Do not publish a required integration effect as an untracked in-memory event.

### Prefer

Use ordinary events for in-process decoupling, `@TransactionalEventListener` when phase matters, and an outbox/broker for durable cross-boundary delivery.

### Nuance

Async listeners additionally need executor, context, ordering, and failure ownership.

### Sources

- **Spring application events:** <https://docs.spring.io/spring-framework/reference/core/beans/context-introduction.html#context-functionality-events>
- **Transactional events:** <https://docs.spring.io/spring-framework/reference/data-access/transaction/event.html>
- **Spring Modulith events:** <https://docs.spring.io/spring-modulith/reference/events.html>
