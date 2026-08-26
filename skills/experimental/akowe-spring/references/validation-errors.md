# Validation and error responses

**Priority:** CRITICAL  
**Rules:** 5

Separate input-shape validation, domain invariants, and stable client-facing failure contracts.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="val-validate-external-boundaries"></a>
## `val-validate-external-boundaries` — Validate data at the transport/configuration boundary

> Use Jakarta Bean Validation on request models and method parameters so malformed input is rejected before application work begins.

### Why it matters

Without boundary validation, invalid values fail deeper as persistence, null, or business errors with poorer diagnostics.

### Avoid

Do not spread repetitive manual null/range checks across controllers or trust deserialization alone.

### Prefer

Annotate DTOs, use `@Valid`/`@Validated`, and test field, cross-field, collection-element, and method validation.

### Nuance

Validation groups can model distinct operations, but excessive groups often indicate separate request types are clearer.

### Sources

- **Spring MVC validation:** <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-validation.html>
- **Spring Bean Validation integration:** <https://docs.spring.io/spring-framework/reference/core/validation/beanvalidation.html>

<a id="val-domain-invariants-owned"></a>
## `val-domain-invariants-owned` — Keep domain invariants in the domain/application owner

> Recheck rules whose truth depends on current state, authorization, uniqueness, or multiple aggregates inside the owning transaction/use case.

### Why it matters

Bean Validation proves object shape, not that a command is currently permitted or globally unique.

### Avoid

Do not treat controller annotations as the only protection for business invariants.

### Prefer

Use boundary validation for syntax/shape and explicit domain/application checks for stateful rules, with consistent error mapping.

### Nuance

The same annotation may be reused on domain values when it truly expresses an intrinsic invariant.

### Sources

- **Spring validation overview:** <https://docs.spring.io/spring-framework/reference/core/validation/validator.html>
- **Declarative transactions:** <https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html>

<a id="err-use-problem-detail-contract"></a>
## `err-use-problem-detail-contract` — Return structured, stable problem responses

> Use `ProblemDetail`/`ErrorResponse` or an equivalent documented schema with stable type/code, status, title, detail, and correlation information.

### Why it matters

Free-form strings and stack-derived bodies are hard for clients to branch on and easy to change accidentally.

### Avoid

Do not expose exception class names, SQL, stack traces, or arbitrary internal messages as the API contract.

### Prefer

Map owned failure categories to one schema, localize human detail if needed, and keep machine identifiers stable.

### Nuance

Legacy APIs may retain an existing error envelope; preserve compatibility rather than forcing RFC 9457 shape midstream.

### Example

**Avoid**

```java
@ExceptionHandler(OrderNotFound.class)
String missing(OrderNotFound ex) {
    return ex.getMessage();
}
```

**Prefer**

```java
@ExceptionHandler(OrderNotFound.class)
ProblemDetail missing(OrderNotFound ex) {
    ProblemDetail problem = ProblemDetail.forStatus(404);
    problem.setType(URI.create("https://example.test/problems/order-not-found"));
    problem.setDetail("The requested order does not exist");
    return problem;
}
```

### Sources

- **Spring MVC REST exceptions:** <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-rest-exceptions.html>
- **ProblemDetail responses:** <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-rest-exceptions.html#error-responses>

<a id="err-specific-advice"></a>
## `err-specific-advice` — Handle exceptions at the narrowest useful boundary

> Use focused `@ExceptionHandler` methods and advice scoped to the controllers/contracts they understand.

### Why it matters

One global `catch (Exception)` mapping loses distinctions, can hide defects, and often leaks inconsistent statuses.

### Avoid

Do not convert every exception to 500 or every failure to 200 with an error payload.

### Prefer

Map expected application exceptions explicitly, preserve framework defaults where correct, and let unexpected defects reach the operational error path.

### Nuance

A final defensive handler may sanitize unexpected errors, but it must preserve 5xx semantics and observability.

### Sources

- **Spring MVC exception handling:** <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-rest-exceptions.html>

<a id="err-log-and-return-separately"></a>
## `err-log-and-return-separately` — Separate client detail from operational evidence

> Return a safe problem response while recording the causal chain, correlation identifier, and relevant structured context at the owning boundary.

### Why it matters

Logging in every layer creates duplicates; returning logs or raw causes exposes implementation and secrets.

### Avoid

Do not log and rethrow at every method or include full request bodies/tokens in error logs.

### Prefer

Log once where the failure becomes owned or crosses a process boundary, and propagate typed causes below that point.

### Nuance

Expected client errors may need metrics rather than stack traces; preserve enough evidence to diagnose unexpected failures.

### Sources

- **Spring Boot logging:** <https://docs.spring.io/spring-boot/reference/features/logging.html>
- **Spring MVC error responses:** <https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-rest-exceptions.html#error-responses>
