# WebFlux and reactive pipelines

**Priority:** HIGH  
**Rules:** 5

Use reactive Spring only where non-blocking, streaming, or backpressure semantics survive end to end.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="reactive-end-to-end-choice"></a>
## `reactive-end-to-end-choice` — Choose WebFlux for an end-to-end reactive need

> Use WebFlux when the application serves high-concurrency non-blocking I/O, streaming, or reactive data sources and the team owns Reactor semantics.

### Why it matters

Adding WebFlux to a blocking JDBC/service stack can add complexity while still consuming blocking resources.

### Avoid

Do not choose WebFlux because fluent pipelines look modern or mix MVC and WebFlux defaults without knowing Boot's application-type selection.

### Prefer

Trace database, clients, file I/O, security, and serialization; choose MVC with virtual threads when blocking APIs are the natural stack.

### Nuance

Hybrid boundaries can be valid, but isolate and schedule blocking work explicitly.

### Sources

- **Spring WebFlux overview:** <https://docs.spring.io/spring-framework/reference/web/webflux.html>
- **Spring Boot web application type:** <https://docs.spring.io/spring-boot/reference/web/spring-boot-applications.html>

<a id="reactive-no-blocking-event-loop"></a>
## `reactive-no-blocking-event-loop` — Keep blocking work off reactive event-loop threads

> Blocking JDBC, file, crypto, legacy HTTP, and `.block()` calls stall the small event-loop pool.

### Why it matters

One slow call can reduce throughput for many concurrent requests.

### Avoid

Do not call blocking repositories or `RestClient` directly inside `map`/`flatMap` on the event loop.

### Prefer

Use reactive drivers/clients, or isolate a bounded blocking adapter on an appropriate scheduler and retain cancellation/resource limits.

### Nuance

`boundedElastic` is a containment boundary, not proof that the whole application is reactive.

### Sources

- **Spring WebFlux concurrency model:** <https://docs.spring.io/spring-framework/reference/web/webflux/new-framework.html#webflux-concurrency-model>
- **Reactor schedulers:** <https://projectreactor.io/docs/core/release/reference/>

<a id="reactive-return-dont-subscribe"></a>
## `reactive-return-dont-subscribe` — Return the pipeline to the framework

> Controller/service code should compose and return `Mono`/`Flux` so the framework owns subscription, cancellation, context, and error delivery.

### Why it matters

Manual `subscribe()` detaches work from the request and usually drops errors or lifecycle ownership.

### Avoid

Do not call `subscribe()` inside a reactive controller to trigger side effects.

### Prefer

Compose side effects with `flatMap`, `then`, or transactional/durable boundaries and return the result.

### Nuance

Application startup, message adapters, and dedicated lifecycle components may be legitimate subscription owners.

### Example

**Avoid**

```java
@PostMapping
void create(@RequestBody CreateOrder request) {
    service.create(request).subscribe();
}
```

**Prefer**

```java
@PostMapping
Mono<OrderResponse> create(@RequestBody CreateOrder request) {
    return service.create(request);
}
```

### Sources

- **Spring WebFlux controllers:** <https://docs.spring.io/spring-framework/reference/web/webflux/controller.html>
- **Reactor subscription:** <https://projectreactor.io/docs/core/release/reference/>

<a id="reactive-context-not-threadlocal"></a>
## `reactive-context-not-threadlocal` — Use Reactor Context for subscriber-scoped data

> Reactive execution can switch threads; ordinary ThreadLocal state is not a stable request context.

### Why it matters

Authentication, tracing, locale, or tenant data can disappear or leak when read from thread affinity.

### Avoid

Do not capture mutable request objects or assume MDC automatically follows every operator.

### Prefer

Use Spring Security reactive context, Reactor Context, Micrometer context propagation, or explicit arguments.

### Nuance

Keep authorization decisions close to current authenticated context rather than caching them in long-lived publishers.

### Sources

- **Spring Security reactive context:** <https://docs.spring.io/spring-security/reference/reactive/authorization/index.html>
- **Reactor context:** <https://projectreactor.io/docs/core/release/reference/>

<a id="reactive-bound-concurrency-and-buffers"></a>
## `reactive-bound-concurrency-and-buffers` — Bound reactive fan-out, prefetch, and buffering

> Reactive Streams backpressure does not automatically bound every `flatMap`, cache, retry, or collection operator.

### Why it matters

An unbounded publisher or high-concurrency fan-out can exhaust memory and downstream connections.

### Avoid

Do not use unlimited `flatMap`, `.collectList()` on unknown streams, or infinite retry without cancellation/deadline.

### Prefer

Set concurrency/prefetch limits, stream incrementally, classify retries, and test cancellation and slow consumers.

### Nuance

Ordering operators such as `concatMap` trade concurrency for determinism; choose from the contract.

### Sources

- **Spring WebFlux:** <https://docs.spring.io/spring-framework/reference/web/webflux.html>
- **Reactor backpressure:** <https://projectreactor.io/docs/core/release/reference/>
