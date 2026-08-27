# Actuator, observability, and health

**Priority:** HIGH  
**Rules:** 5

Expose operational evidence with controlled endpoint access, low-cardinality dimensions, and meaningful health semantics.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="obs-minimize-actuator-exposure"></a>
## `obs-minimize-actuator-exposure` — Expose only required actuator endpoints

> Keep management endpoints on an owned network/port and authorize them separately from application traffic.

### Why it matters

Environment, configuration, heap, mappings, conditions, and shutdown endpoints can reveal secrets or change availability.

### Avoid

Do not expose `*` publicly or assume obscurity of the `/actuator` path is security.

### Prefer

Select endpoints explicitly, sanitize values, configure management networking, and test authorization.

### Nuance

Kubernetes probes may need unauthenticated local access; isolate that path from administrative endpoints.

### Sources

- **Spring Boot actuator endpoints:** <https://docs.spring.io/spring-boot/reference/actuator/endpoints.html>

<a id="obs-health-means-service-capability"></a>
## `obs-health-means-service-capability` — Model liveness and readiness separately

> Liveness asks whether the process should restart; readiness asks whether it should receive traffic.

### Why it matters

Putting every external dependency in liveness can create restart storms; declaring ready before required initialization routes failures to users.

### Avoid

Do not fail liveness because a remote dependency is down or expose one aggregate health result for every consumer.

### Prefer

Use health groups and probes aligned with deployment behavior; include only dependencies that control the relevant capability.

### Nuance

A database may be required for readiness but not liveness; a cached/read-only mode may define a separate readiness group.

### Sources

- **Spring Boot health information:** <https://docs.spring.io/spring-boot/reference/actuator/endpoints.html#actuator.endpoints.health>
- **Spring Boot Kubernetes probes:** <https://docs.spring.io/spring-boot/reference/actuator/endpoints.html#actuator.endpoints.kubernetes-probes>

<a id="obs-use-observation-api"></a>
## `obs-use-observation-api` — Instrument owned operations through Observation

> Use Micrometer Observation and Boot auto-instrumentation for correlated metrics and traces before adding custom timers/spans independently.

### Why it matters

Parallel metrics and tracing code can double-instrument, lose context, or produce inconsistent names/tags.

### Avoid

Do not create ad hoc timers around already instrumented HTTP, repository, or client operations without checking current observations.

### Prefer

Create an observation for a business/remote boundary the framework does not already own, add low-cardinality keys, and preserve error/stop semantics.

### Nuance

A log statement is not a metric or trace; use each signal for its own diagnostic question.

### Example

**Avoid**

```java
long started = System.nanoTime();
try {
    return gateway.charge(command);
} finally {
    meterRegistry.timer("charge").record(
        System.nanoTime() - started,
        TimeUnit.NANOSECONDS);
}
```

**Prefer**

```java
return Observation.createNotStarted("payment.charge", registry)
    .lowCardinalityKeyValue("provider", providerName)
    .observe(() -> gateway.charge(command));
```

### Sources

- **Spring Boot observability:** <https://docs.spring.io/spring-boot/reference/actuator/observability.html>
- **Spring Framework observability:** <https://docs.spring.io/spring-framework/reference/integration/observability.html>

<a id="obs-low-cardinality-dimensions"></a>
## `obs-low-cardinality-dimensions` — Keep metric and tracing dimensions bounded

> Use stable categories such as operation, outcome, route, provider, or error class; keep user/order/URL IDs in logs or high-cardinality trace fields only when the backend supports them.

### Why it matters

Unbounded tag values create excessive time series, memory, storage, and query cost.

### Avoid

Do not tag metrics with raw paths, exception messages, email addresses, tenant IDs, or request identifiers.

### Prefer

Normalize routes, cap exception categories, document tags, and test the emitted names/dimensions.

### Nuance

Tracing tolerates more cardinality than metrics, but sensitive data and backend limits still apply.

### Sources

- **Spring Boot observability low/high cardinality:** <https://docs.spring.io/spring-boot/reference/actuator/observability.html>
- **Micrometer concepts:** <https://docs.micrometer.io/micrometer/reference/observation.html>

<a id="obs-log-exception-once"></a>
## `obs-log-exception-once` — Assign exception logging to one boundary

> Preserve causal chains below the boundary and log once where the failure becomes operationally owned.

### Why it matters

Logging and rethrowing through controller, service, repository, and client layers multiplies noise and alert counts.

### Avoid

Do not log expected 4xx/domain failures as repeated stack traces or log secrets/request bodies for context.

### Prefer

Return or propagate typed errors, attach correlation context, log unexpected failures once, and measure expected failures separately.

### Nuance

Infrastructure libraries should generally not log application decisions; return enough context to their caller.

### Sources

- **Spring Boot logging:** <https://docs.spring.io/spring-boot/reference/features/logging.html>
- **Spring MVC error responses:** <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-rest-exceptions.html#error-responses>
