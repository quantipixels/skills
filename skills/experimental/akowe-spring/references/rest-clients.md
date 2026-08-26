# HTTP clients and resilience

**Priority:** CRITICAL  
**Rules:** 5

Make client construction, blocking model, timeouts, failure mapping, retries, and instrumentation one owned contract.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="client-use-boot-builders"></a>
## `client-use-boot-builders` — Build clients from Boot-configured builders

> Inject `RestClient.Builder` or `WebClient.Builder` so message conversion, SSL, observation, and project customizers remain attached.

### Why it matters

Ad hoc static clients diverge in timeouts, codecs, authentication, metrics, and connection management.

### Avoid

Do not instantiate a new raw client in every service or mutate a shared builder after publication.

### Prefer

Create one immutable client per remote contract/host from the injected prototype builder and centralize its defaults.

### Nuance

HTTP service interfaces can reduce call-site ceremony, but the underlying client still owns transport policy.

### Example

**Avoid**

```java
this.client = RestClient.create("https://inventory.example");
```

**Prefer**

```java
this.client = builder
    .baseUrl("https://inventory.example")
    .build();
```

### Sources

- **Spring Boot calling REST services:** <https://docs.spring.io/spring-boot/reference/io/rest-client.html>
- **Spring REST clients:** <https://docs.spring.io/spring-framework/reference/integration/rest-clients.html>

<a id="client-match-blocking-model"></a>
## `client-match-blocking-model` — Match the client to the application's execution model

> Use `RestClient` for imperative applications and `WebClient` for genuinely reactive/non-blocking or streaming paths.

### Why it matters

Using WebClient and immediately blocking adds Reactor complexity without non-blocking benefit; using blocking clients on an event loop stalls all work.

### Avoid

Do not select a client because it is newer or fluent.

### Prefer

Trace the end-to-end call path and choose the model that preserves its scheduling, cancellation, and backpressure contract.

### Nuance

An imperative application may use WebClient for a specific streaming integration, but isolate the reactive boundary.

### Sources

- **Spring Boot calling REST services:** <https://docs.spring.io/spring-boot/reference/io/rest-client.html>
- **Spring REST clients:** <https://docs.spring.io/spring-framework/reference/integration/rest-clients.html>

<a id="client-set-all-timeouts"></a>
## `client-set-all-timeouts` — Configure connect, acquisition, response/read, and overall deadlines

> Remote calls need finite limits aligned with the caller's latency budget and connection pool capacity.

### Why it matters

A missing timeout can consume threads, virtual threads, event-loop slots, or pooled connections indefinitely.

### Avoid

Do not rely on library defaults or configure only connect timeout.

### Prefer

Set transport-specific timeouts, bound response bodies, propagate cancellation, and expose timeout classification in metrics.

### Nuance

Long-lived streaming calls need different policies; make them separate clients or operations.

### Sources

- **Spring Boot HTTP client configuration:** <https://docs.spring.io/spring-boot/reference/io/rest-client.html>
- **Spring REST client request factories:** <https://docs.spring.io/spring-framework/reference/integration/rest-clients.html>

<a id="client-map-remote-failures"></a>
## `client-map-remote-failures` — Translate remote responses at the client boundary

> Map status, headers, and error bodies into typed remote-contract failures before they enter application logic.

### Why it matters

Generic `RestClientException`, null bodies, or ad hoc status checks at each caller lose retryability and compatibility information.

### Avoid

Do not suppress all 4xx/5xx responses or return an empty object on parse/error failure.

### Prefer

Define default status handlers or exchange logic, preserve safe diagnostics, and distinguish caller errors, remote rejection, transient failure, and protocol defects.

### Nuance

Some APIs legitimately use 404 as absence; encode that in the client contract rather than globally suppressing 404.

### Sources

- **Spring REST client error handling:** <https://docs.spring.io/spring-framework/reference/integration/rest-clients.html>

<a id="client-retry-idempotent-owned"></a>
## `client-retry-idempotent-owned` — Retry only an idempotent, classified, bounded operation

> Put retry in one layer with finite attempts/deadline, backoff/jitter, cancellation, and observability.

### Why it matters

Nested or indiscriminate retries duplicate side effects and amplify dependency outages.

### Avoid

Do not apply `@Retryable` to every client method or retry authentication, validation, and permanent 4xx failures.

### Prefer

Classify transient exceptions/statuses, establish idempotency/deduplication for writes, and ensure the caller budget covers all attempts.

### Nuance

Spring Framework 7 resilience annotations require explicit enablement; older stacks may use Spring Retry or a client library. Do not mix owners.

### Sources

- **Spring Framework resilience:** <https://docs.spring.io/spring-framework/reference/core/resilience.html>
- **Spring Boot 4 migration guide:** <https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide>
