# Spring Framework and Spring Boot

Distilled from the former `akowe-spring` experiment. Detect the exact Boot/Framework/Java/Kotlin/Jakarta generation and managed dependency graph before applying version-sensitive guidance.

- Let Boot manage its coordinated dependency graph; prefer a supported maintenance line and deliberate overrides with compatibility evidence.
- Keep container ownership explicit. Use constructor dependencies for required collaborators and do not manually instantiate beans that depend on proxy, scope, configuration, interception, or lifecycle semantics.
- Treat singleton beans as shared concurrent objects; keep request/task state in arguments or owned scopes, not mutable singleton fields.
- Use typed `@ConfigurationProperties` for owned configuration groups, validate required configuration at startup, understand property precedence, and keep secrets external/sanitized.
- Auto-configuration/starter code must back off to application control and register through the generation's supported metadata. Customize Boot-provided builders/hooks before replacing whole infrastructure.
- Keep HTTP transport contracts separate from entities/internal models. Make method/status/header/version/error semantics explicit and bound uploads/streams.
- Use `ProblemDetail`/equivalent stable error contracts and map exceptions at the narrowest useful boundary; do not leak raw exception/SQL/stack detail.
- Match `RestClient`/imperative versus `WebClient`/reactive use to the end-to-end execution model. Reuse Boot-configured builders, set finite timeouts, classify remote failures, and retry only bounded idempotent operations.
- Put database transactions around application use cases. Proxy-based advice requires a real proxy invocation path; self-invocation can bypass `@Transactional`, `@Async`, method security, caching, or resilience advice.
- Keep slow/irreversible remote effects outside local DB transactions unless an explicit coordination mechanism owns consistency. Treat `readOnly=true` as intent/optimization, not authorization.
- Bound Spring Data result size, use explicit query/fetch/projection shapes, and prove lock/version/idempotency semantics where concurrency matters.
- For JPA/Hibernate, keep entity equality stable, define use-case fetch plans, detect N+1 behavior, bound persistence-context lifetime, and cascade only true owned lifecycles.
- Define explicit `SecurityFilterChain` rules, protect sensitive use cases at the service boundary when adapter-independent, align CSRF with browser credential semantics, centralize precise CORS, and never log credentials/tokens.
- Own async executors/schedulers and context propagation; virtual threads/coroutines do not remove datasource, HTTP pool, broker, or downstream limits. Application events are not durable messaging by default.
- Use WebFlux only when reactive semantics survive end-to-end; do not block event-loop threads or call `subscribe()` in controllers to detach work.
- Use the smallest Spring test context that proves the seam. Preserve context-cache reuse and use real compatible infrastructure when database/provider semantics matter.
- Expose only required actuator endpoints; distinguish liveness/readiness; use Observation/Micrometer with bounded dimensions; log unexpected failures once at the owning boundary.
- Give database migration one production owner; gate readiness on required initialization and own graceful shutdown/background work.

## Kotlin × Spring

- Detect Spring's supported Kotlin baseline and required `kotlin-reflect`; use the Kotlin/Jackson module when Jackson serializes Kotlin classes.
- Kotlin classes/functions are final by default; use the supported Kotlin Spring/all-open plugin or deliberate openness for proxy-required beans rather than manual scatter.
- Prefer primary-constructor injection and immutable configuration properties.
- Be deliberate with suspend functions, Reactor/coroutine context, transaction/security proxy paths, cancellation, and blocking JPA/HTTP work.
- Avoid ordinary Kotlin data classes as mutable JPA entities unless equality/hash/lifecycle semantics are explicitly designed; use the Kotlin JPA/no-arg support required by the stack.
- Use validation use-site targets correctly and test absent-vs-explicit-null/default-parameter serialization semantics.

Primary sources:

- Spring Boot reference: <https://docs.spring.io/spring-boot/>
- Spring Framework reference: <https://docs.spring.io/spring-framework/reference/>
- Spring Kotlin support: <https://docs.spring.io/spring-framework/reference/languages/kotlin.html>
- Spring Data JPA: <https://docs.spring.io/spring-data/jpa/reference/>
- Spring Security: <https://docs.spring.io/spring-security/reference/>
- Hibernate ORM guide: <https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html>
