# Spring Framework and Spring Boot guidance index

Research baseline: Spring Framework 6.1–7.0 and Spring Boot 3.3–4.1 guidance preserved from the former `akowe-spring` experiment. The public Spring skill is retired; this index routes Akọ̀wé Code into detailed category references without loading the full catalogue.

Establish the exact Boot/Framework/Java/Kotlin/Jakarta generation, application type, starters/modules, managed dependency graph, and deployment constraints before applying version-sensitive guidance. Then open only categories controlling the touched code.

Priority meanings:

- `CRITICAL` — correctness, compatibility, security, data integrity, lifecycle, or public-contract guidance; satisfy it or prove a concrete exception.
- `HIGH` — strong Spring default whose deviation needs candidate-specific benefit and proof.
- `MEDIUM` — contextual expert guidance; optimize for clarity, project fit, and operational value.

| Candidate mechanism | Priority | Detailed reference |
| --- | --- | --- |
| Boot/Framework/Java/Jakarta generation, managed versions, preview/support line | CRITICAL | [Spring and Spring Boot baseline](../spring/baseline.md) |
| Application/package/module boundaries, container surface, Modulith | HIGH | [Application structure and module boundaries](../spring/structure.md) |
| Required collaborators, container-owned instances, scopes, singleton state, cycles | CRITICAL | [Beans, dependency injection, and scopes](../spring/beans-di.md) |
| ConfigurationProperties, precedence, profiles, startup validation, secrets | CRITICAL | [Configuration, profiles, and secrets](../spring/configuration.md) |
| Starters, back-off, auto-configuration metadata, customization hooks | HIGH | [Auto-configuration and starter design](../spring/auto-configuration.md) |
| MVC transport DTOs, mappings, HTTP semantics/versioning, uploads/streams | CRITICAL | [Spring MVC and HTTP API boundaries](../spring/web-mvc.md) |
| External validation, domain invariants, ProblemDetail/error advice, logging | CRITICAL | [Validation and error responses](../spring/validation-errors.md) |
| RestClient/WebClient, blocking model, timeouts, remote failure/retry semantics | CRITICAL | [HTTP clients and resilience](../spring/rest-clients.md) |
| Transaction boundaries, proxy invocation, rollback, remote effects, readOnly | CRITICAL | [Transactions and proxy semantics](../spring/transactions.md) |
| Repository contracts, query shape, bounded results, projections, locking/versioning | HIGH | [Spring Data repositories and queries](../spring/spring-data.md) |
| Entity identity/equality, fetch plans, N+1, persistence context, cascades | CRITICAL | [JPA and Hibernate persistence](../spring/jpa-hibernate.md) |
| Filter chain, method authorization, CSRF/CORS, credential handling | CRITICAL | [Spring Security boundaries](../spring/security.md) |
| Async executors, scheduling, events, context propagation, durability | CRITICAL | [Async work, scheduling, events, and context](../spring/async-events.md) |
| WebFlux, event-loop blocking, subscribe ownership, Reactor context, backpressure | HIGH | [WebFlux and reactive pipelines](../spring/reactive.md) |
| Test slices/context size, mocking generation, cache reuse, real infrastructure | HIGH | [Spring testing and context proof](../spring/testing.md) |
| Actuator exposure, health semantics, Observation/Micrometer, dimensions/logging | HIGH | [Actuator, observability, and health](../spring/observability.md) |
| Startup work, migrations, readiness, graceful shutdown, lazy initialization | CRITICAL | [Startup, migrations, shutdown, and deployment](../spring/lifecycle.md) |
| AOT/runtime hints, reflection/discovery, build-time/runtime config, native proof | MEDIUM | [AOT processing and native images](../spring/aot-native.md) |

For Kotlin × Spring candidates, also load [Kotlin guidance](kotlin.md) when Kotlin language/coroutine/nullability semantics are material. Spring rules may specialize Kotlin/Java defaults because of container, proxy, transaction, reactive, serialization, or lifecycle behavior, but must not silently weaken the underlying language/runtime contract.

Use rule headings as hypotheses, not a lint set. Apply only a rule whose trigger exists in the exact candidate and trace it to a caller-visible, data, security, resource, compatibility, or operational consequence.

Primary source families and freshness boundaries are recorded in [the Akọ̀wé Code source map](../source-map.md).
