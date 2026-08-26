# Spring testing and context proof

**Priority:** HIGH  
**Rules:** 5

Load the smallest Spring context that proves the changed boundary, while preserving version-specific test APIs.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="test-smallest-context"></a>
## `test-smallest-context` — Use the smallest test boundary that can fail for the requirement

> Plain unit tests prove pure logic; slices prove one Spring adapter; full contexts prove integration and runtime wiring.

### Why it matters

Starting the whole application for every case slows feedback and makes failures hard to localize.

### Avoid

Do not use `@SpringBootTest` as the default for every service or mapper.

### Prefer

Select unit, `@WebMvcTest`, `@DataJpaTest`, `@RestClientTest`, `@JsonTest`, or full integration from the contract under test.

### Nuance

A slice can still import a small owned configuration; avoid recreating the entire application manually.

### Example

**Avoid**

```java
@SpringBootTest
class PriceCalculatorTest { /* pure arithmetic tests */ }
```

**Prefer**

```java
class PriceCalculatorTest { /* plain JUnit test */ }

@WebMvcTest(OrderController.class)
class OrderControllerTest { /* MVC contract */ }
```

### Sources

- **Spring Boot testing:** <https://docs.spring.io/spring-boot/reference/testing/index.html>
- **Spring Boot test slices:** <https://docs.spring.io/spring-boot/appendix/test-auto-configuration/slices.html>

<a id="test-slices-stay-slices"></a>
## `test-slices-stay-slices` — Keep slice tests focused on their auto-configured layer

> A slice deliberately excludes most beans to prove one adapter with controlled collaborators.

### Why it matters

Importing production configuration recursively turns the slice into an undocumented partial full context.

### Avoid

Do not fix every missing bean with broad `@Import` or component scanning.

### Prefer

Mock or import only the direct boundary collaborator, or choose `@SpringBootTest` when the real integration is the subject.

### Nuance

Know each slice's included auto-configuration for the detected Boot generation.

### Sources

- **Spring Boot test slices:** <https://docs.spring.io/spring-boot/appendix/test-auto-configuration/slices.html>

<a id="test-version-aware-mocking"></a>
## `test-version-aware-mocking` — Use the mocking annotation supported by the Spring generation

> Spring Framework `@MockitoBean`/`@MockitoSpyBean` replace Boot's deprecated and Boot 4-removed `@MockBean`/`@SpyBean` path.

### Why it matters

Copying old test annotations into Boot 4 breaks compilation or context customization.

### Avoid

Do not pin a deprecated annotation merely because existing examples use it.

### Prefer

Detect the Boot/Framework version, prefer current framework annotations on supported 3.x lines, and migrate before Boot 4.

### Nuance

A mock bean changes the context cache key; too many per-test variants can destroy cache reuse.

### Sources

- **Spring `@MockitoBean`:** <https://docs.spring.io/spring-framework/reference/testing/annotations/integration-spring/annotation-mockitobean.html>
- **Spring Boot 4 migration guide:** <https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide>

<a id="test-preserve-context-cache"></a>
## `test-preserve-context-cache` — Design tests to reuse application contexts

> The TestContext framework caches contexts by configuration, properties, profiles, dynamic values, mocks, and customizers.

### Why it matters

Unique configuration on every class causes repeated expensive startups and suite instability.

### Avoid

Do not use `@DirtiesContext`, random properties, or per-class mock combinations without evidence.

### Prefer

Share coherent base configurations, keep dynamic properties deterministic, and dirty a context only when state cannot be reset safely.

### Nuance

Parallel tests also require thread-safe fixtures and isolated external state.

### Sources

- **Spring TestContext caching:** <https://docs.spring.io/spring-framework/reference/testing/testcontext-framework/ctx-management/caching.html>

<a id="test-real-infrastructure-when-semantics-matter"></a>
## `test-real-infrastructure-when-semantics-matter` — Use real compatible infrastructure for provider-specific behavior

> Database dialects, transactions, locks, migrations, brokers, and HTTP stacks differ from in-memory substitutes.

### Why it matters

A green H2/mock test can miss production SQL, isolation, collation, or serialization behavior.

### Avoid

Do not claim PostgreSQL/MySQL/Kafka/Redis compatibility from a fake that does not implement the required semantics.

### Prefer

Use Testcontainers or an approved disposable service and Boot service connections; keep focused unit/slice tests for fast logic.

### Nuance

Container tests need deterministic images, cleanup, and bounded suite cost.

### Sources

- **Spring Boot Testcontainers:** <https://docs.spring.io/spring-boot/reference/testing/testcontainers.html>
