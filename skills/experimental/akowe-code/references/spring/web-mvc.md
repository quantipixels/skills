# Spring MVC and HTTP API boundaries

**Priority:** CRITICAL  
**Rules:** 5

Keep HTTP semantics, transport models, versioning, and resource limits explicit.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="web-transport-dtos"></a>
## `web-transport-dtos` — Use transport-specific request and response models

> Bind and serialize DTOs whose fields, validation, and compatibility belong to the HTTP contract.

### Why it matters

Entities and internal domain objects carry persistence/lifecycle semantics that should not leak into the wire format.

### Avoid

Do not accept or return JPA entities directly or rely on Jackson to define the API accidentally.

### Prefer

Map at the controller/application boundary, expose stable fields, and model versioned request/response evolution deliberately.

### Nuance

A simple immutable domain value can serve as a DTO when its public contract is intentionally identical.

### Example

**Avoid**

```java
@GetMapping("/{id}")
OrderEntity order(@PathVariable UUID id) {
    return repository.findById(id).orElseThrow();
}
```

**Prefer**

```java
@GetMapping("/{id}")
OrderResponse order(@PathVariable UUID id) {
    return service.find(id).map(OrderResponse::from).orElseThrow();
}
```

### Sources

- **Spring MVC annotated controllers:** <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller.html>
- **Spring Data projections:** <https://docs.spring.io/spring-data/jpa/reference/repositories/projections.html>

<a id="web-explicit-http-semantics"></a>
## `web-explicit-http-semantics` — Make method, status, headers, and idempotency visible

> Choose HTTP methods and response status codes from the operation's contract, including `Location`, caching, conditional, and content headers.

### Why it matters

Returning every result as `200` or letting defaults decide obscures creation, absence, conflict, validation, and asynchronous behavior.

### Avoid

Do not use POST for every command, return `null` for 404, or encode failures only inside a success body.

### Prefer

Use typed return values/`ResponseEntity` where needed, stable error responses, and tests that assert status and headers.

### Nuance

Avoid wrapping every response in `ResponseEntity` when the annotation/default contract is already exact.

### Sources

- **Spring MVC return values:** <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-methods/return-types.html>
- **Spring MVC request mapping:** <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-requestmapping.html>

<a id="web-narrow-request-mappings"></a>
## `web-narrow-request-mappings` — Keep mappings specific and non-overlapping

> Use a coherent type-level base path and method-level mappings with explicit methods, consumes, produces, parameters, and versions where relevant.

### Why it matters

Broad catch-all routes and ambiguous conditions produce order-sensitive or startup-time mapping failures.

### Avoid

Do not use class-level wildcard mappings or duplicate controllers that differ only by hidden conditions.

### Prefer

Let the framework's mapping model select by documented conditions and cover negative/ambiguous cases in tests.

### Nuance

Functional endpoints are a valid alternative; keep one clear routing model within a bounded area.

### Sources

- **Spring MVC request mapping:** <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-requestmapping.html>

<a id="web-versioning-one-strategy"></a>
## `web-versioning-one-strategy` — Use one explicit API versioning strategy

> On Spring Framework 7, configure the built-in version resolver/parser and declare method versions rather than parsing headers or paths in controllers.

### Why it matters

Ad hoc version checks duplicate negotiation, make fallback rules inconsistent, and hide deprecation behavior.

### Avoid

Do not mix path, header, query, and media-type versioning without a documented compatibility reason.

### Prefer

Select one resolver, define supported/deprecated versions, and test missing, invalid, old, and future version behavior.

### Nuance

Framework 6 applications need an application-owned strategy; do not copy Framework 7 annotations into them.

### Sources

- **Spring MVC API versioning:** <https://docs.spring.io/spring-framework/reference/web/webmvc-versioning.html>

<a id="web-bound-streams-and-uploads"></a>
## `web-bound-streams-and-uploads` — Bound request bodies, uploads, and streaming work

> Set size/time/concurrency limits and retain ownership of resources used by asynchronous or streaming responses.

### Why it matters

A controller can otherwise tie up connections, memory, temporary files, or task executors for unbounded client-controlled input.

### Avoid

Do not call `readAllBytes`, collect unlimited multipart content, or start unowned work from a request thread.

### Prefer

Stream incrementally, enforce server/application limits, close resources, and define disconnect/cancellation behavior.

### Nuance

Streaming may require MVC async support or WebFlux; choose based on end-to-end behavior, not API style.

### Sources

- **Spring MVC asynchronous requests:** <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-async.html>
- **Spring Boot multipart properties:** <https://docs.spring.io/spring-boot/appendix/application-properties/index.html#application-properties.web.spring.servlet.multipart.max-file-size>
