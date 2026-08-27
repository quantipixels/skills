# Startup, migrations, shutdown, and deployment

**Priority:** CRITICAL  
**Rules:** 5

Make startup completion, database migration, readiness, shutdown, and background-work ownership explicit.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="life-startup-work-bounded"></a>
## `life-startup-work-bounded` — Keep startup work finite and failure-explicit

> `ApplicationRunner`, `CommandLineRunner`, initialization callbacks, and bean creation delay readiness and can fail the whole application.

### Why it matters

Unbounded remote calls or data repair during startup cause restart loops and unpredictable deploy time.

### Avoid

Do not run long migrations, full data imports, or detached background jobs from a startup callback.

### Prefer

Limit startup work to required validation/bootstrap, apply deadlines, and move durable work to an owned job system.

### Nuance

A failed required invariant should stop startup; optional warm-up can degrade gracefully and report status.

### Sources

- **Spring Boot startup runners:** <https://docs.spring.io/spring-boot/reference/features/spring-application.html#features.spring-application.command-line-runner>
- **Spring bean lifecycle:** <https://docs.spring.io/spring-framework/reference/core/beans/factory-nature.html>

<a id="life-migrations-single-owner"></a>
## `life-migrations-single-owner` — Give schema evolution one production owner

> Use Flyway or Liquibase with versioned, reviewable migrations and disable competing implicit schema creation in production.

### Why it matters

Hibernate DDL, `schema.sql`, Flyway, and manual deployment scripts can race or disagree.

### Avoid

Do not use `ddl-auto=update` as the production migration strategy or edit an already-applied migration.

### Prefer

Choose one migration tool, order data/schema changes for rolling compatibility, and verify on the production database engine.

### Nuance

Boot 4 modular starters may require explicit Flyway/Liquibase starters; follow the detected generation.

### Example

**Avoid**

```yaml
spring:
  jpa:
    hibernate:
      ddl-auto: update
  sql:
    init:
      mode: always
```

**Prefer**

```yaml
spring:
  jpa:
    hibernate:
      ddl-auto: validate
# Flyway or Liquibase owns versioned production migrations.
```

### Sources

- **Spring Boot database initialization:** <https://docs.spring.io/spring-boot/how-to/data-initialization.html>
- **Spring Boot 4 migration guide:** <https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide>

<a id="life-readiness-after-required-init"></a>
## `life-readiness-after-required-init` — Publish readiness only after required state is usable

> The instance should not receive traffic before essential migrations, caches, registrations, or local state are ready.

### Why it matters

A process can be alive while every request fails during initialization.

### Avoid

Do not mark ready from process start or put long optional dependency checks into liveness.

### Prefer

Use readiness state/health groups and lifecycle ordering; make required initialization synchronous or explicitly gate traffic.

### Nuance

For rolling deploys, new and old versions must tolerate the shared database/message schema during the overlap.

### Sources

- **Spring Boot availability states:** <https://docs.spring.io/spring-boot/reference/features/spring-application.html#features.spring-application.application-availability>
- **Kubernetes probes:** <https://docs.spring.io/spring-boot/reference/actuator/endpoints.html#actuator.endpoints.kubernetes-probes>

<a id="life-graceful-shutdown-owned"></a>
## `life-graceful-shutdown-owned` — Drain requests and background work during shutdown

> Graceful shutdown stops accepting new work while allowing active requests and lifecycle components a bounded completion window.

### Why it matters

Abrupt termination loses in-flight work; infinite waits block deployment and autoscaling.

### Avoid

Do not spawn executors/threads that the context cannot close or ignore interruption/cancellation.

### Prefer

Use Boot graceful shutdown, lifecycle phases, managed executors, bounded timeouts, and durable checkpoints for unfinished work.

### Nuance

Container termination grace must exceed the application shutdown window and load-balancer drain time.

### Sources

- **Spring Boot graceful shutdown:** <https://docs.spring.io/spring-boot/reference/web/graceful-shutdown.html>
- **Spring bean lifecycle:** <https://docs.spring.io/spring-framework/reference/core/beans/factory-nature.html>

<a id="life-no-lazy-init-to-hide-errors"></a>
## `life-no-lazy-init-to-hide-errors` — Do not use lazy initialization to conceal broken wiring

> Eager singleton creation exposes missing beans, invalid configuration, and cycles at startup.

### Why it matters

Global lazy initialization moves failures to the first live request and can create unpredictable cold paths.

### Avoid

Do not enable `spring.main.lazy-initialization=true` merely to make startup pass.

### Prefer

Fix the dependency/configuration error; use targeted lazy/provider semantics only for expensive optional components with tested fallback.

### Nuance

Startup-time optimization should be profiled and balanced against operational failure visibility.

### Sources

- **Spring Boot lazy initialization:** <https://docs.spring.io/spring-boot/reference/features/spring-application.html#features.spring-application.lazy-initialization>
- **Spring dependency initialization:** <https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html>
