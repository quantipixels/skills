# Spring runtime mechanics

Load only when the exact candidate uses Spring Framework/Boot/Data and touches a mechanism below whose semantics can change correctness, ownership, lifecycle, compatibility, or proof. This is mechanism calibration, not a Spring architecture template or cached framework manual.

The detected Spring Boot/Framework/Data/Hibernate/Reactor/Jakarta/Java/database baseline controls version-specific details. Verify current official behavior whenever proxy mode, method visibility, defaults, annotations, provider behavior, or generation can change the answer.

## Proxy advice exists only on an intercepted call path

`@Transactional`, `@Async`, method security, caching, resilience, and other proxy-based advice do not become true merely because an annotation is present.

- Establish the actual proxy/advice mode and method boundary.
- Treat self-invocation as a likely advice bypass in proxy mode.
- Prefer a real collaborator/owned boundary when an advised operation must be independently intercepted; do not introduce arbitrary self-injection or proxy-aware code just to make an annotation fire.
- Do not rely on proxy advice during initialization before the proxy/lifecycle is actually active.

When AspectJ/weaving or another mechanism is selected, reason from that mechanism rather than applying proxy assumptions universally.

## Transactions should match the atomic use case

- Put the database transaction around the application operation that owns the atomic state change, not around transport plumbing or scattered repository calls by habit.
- Make rollback semantics match the failure contract. Caught/swallowed failures and exception-type defaults can change commit/rollback behavior.
- Do not hold a local database transaction open across slow or irreversible remote effects as a substitute for cross-system atomicity. Prefer durable intent/outbox/event delivery, idempotency, or an explicit compensating workflow when the accepted architecture requires it.
- Treat `readOnly` as intent/optimization where supported, not an authorization boundary or universal write prohibition.

A transaction annotation is not proof. Verify the effective interceptor, propagation, database/provider behavior, and committed/rolled-back outcomes when material.

## Persistence context and fetch shape are use-case decisions

- Keep entity equality/hash semantics stable across the lifecycle states the application actually uses; generated identifiers, proxies, mutable associations, and detached entities make naive generated equality risky.
- Select fetch shape per use case with an explicit query/entity graph/projection/batch strategy rather than changing association mappings globally to hide a loading failure.
- Prove representative query count/cardinality when association traversal can create N+1 or row-explosion behavior. Correctness-only tests can miss this entirely.
- Bound persistence-context lifetime during large/batch work; unmanaged growth increases dirty-checking/state retention and can surface stale in-memory state.
- Cascade only across true lifecycle ownership. `ALL`/remove cascades are not harmless convenience on shared relationships.

Open-session-in-view, eager fetching, and broad cascades are implementation choices with lifecycle and query consequences, not default fixes.

## Startup, readiness, migration, and shutdown form one lifecycle

- Startup work must be finite and failure semantics explicit. Long repair/import/background jobs need an owned durable execution path rather than an initialization callback.
- Give production schema evolution one owner. Avoid competing implicit DDL/init/migration mechanisms and preserve rolling compatibility when old/new versions overlap.
- Readiness means required local state is usable for traffic; liveness should not become a dependency-health restart trigger.
- Drain traffic and managed background work during shutdown with a bounded completion policy. Container/orchestrator grace, application shutdown, queues/executors, and durable checkpoints must agree.
- Do not use broad lazy initialization merely to postpone broken wiring until the first live request.

## Reactive behavior must be end-to-end enough to justify its cost

- Choose WebFlux/Reactor for a real non-blocking, streaming, backpressure, or reactive-data need; do not add it to a fundamentally blocking stack merely for fluent APIs.
- Keep blocking work off event-loop threads or isolate it behind a bounded, explicit blocking boundary.
- Return composed publishers to the framework when the request lifecycle owns subscription; internal `subscribe()` commonly detaches cancellation, context, and error ownership.
- Treat subscriber context as distinct from thread affinity. Authentication, tracing, locale, tenancy, or MDC-style data needs the framework/Reactor context propagation contract rather than an assumed `ThreadLocal`.
- Bound fan-out, buffering, retries, prefetch, and collection of unknown streams; Reactive Streams backpressure does not automatically bound every operator or downstream resource.

## Retrieval anchors

Use current first-party sources for the detected generation, especially Spring Framework AOP proxying and transaction references, Spring Data JPA transaction/entity-graph documentation, Spring Boot application-availability and graceful-shutdown guidance, Spring WebFlux concurrency/reactive documentation, and the matching Hibernate ORM user guide for persistence-context/fetch/equality behavior.

## What not to preserve locally

Do not cache endpoint annotations, property names, starter matrices, security DSL syntax, Boot defaults, migration-tool recipes, or framework-version feature tables here. Use the project's current generation and official sources for those details. Keep this reference only for recurring mechanism traps whose consequences remain stable across versions.
