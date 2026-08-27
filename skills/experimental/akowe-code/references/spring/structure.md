# Application structure and module boundaries

**Priority:** HIGH  
**Rules:** 5

Make component scanning, ownership, and feature boundaries visible without imposing one enterprise architecture.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="struct-root-application-package"></a>
## `struct-root-application-package` — Place the application class in a meaningful root package

> Keep the `@SpringBootApplication` class above the packages it should scan and avoid the default package.

### Why it matters

Boot uses the application package as an implicit search and entity/repository boundary. A misplaced root silently expands or shrinks discovery.

### Avoid

Do not put the main class in the default package or a low-level feature package and compensate with broad manual scans.

### Prefer

Use a root package owned by the application and add explicit scan configuration only when the boundary genuinely crosses packages.

### Nuance

Multi-module builds may intentionally separate configuration; make every extra scan/import boundary explicit and tested.

### Example

**Avoid**

```java
package com.example.orders.web;

@SpringBootApplication
class Application {}
```

**Prefer**

```java
package com.example.orders;

@SpringBootApplication
class Application {}
```

### Sources

- **Spring Boot structuring code:** <https://docs.spring.io/spring-boot/reference/using/structuring-your-code.html>

<a id="struct-package-by-capability"></a>
## `struct-package-by-capability` — Organize code around owned capabilities

> Prefer cohesive capability or application-module packages when global controller/service/repository layers scatter one change across the tree.

### Why it matters

Feature ownership and allowed dependencies become easier to inspect when a capability's API and internals are colocated.

### Avoid

Do not mechanically reorganize a small or established codebase, and do not treat package-by-feature as proof of good boundaries.

### Prefer

Choose packages that reflect business or integration ownership, expose a small API, and keep internal collaborators package-private where practical.

### Nuance

A layered boundary can still be correct when the layer itself owns policy or infrastructure; optimize for dependency direction, not labels.

### Sources

- **Spring Boot structuring code:** <https://docs.spring.io/spring-boot/reference/using/structuring-your-code.html>
- **Spring Modulith fundamentals:** <https://docs.spring.io/spring-modulith/reference/fundamentals.html>

<a id="struct-container-only-where-needed"></a>
## `struct-container-only-where-needed` — Do not make every object a Spring bean

> Register objects that need container lifecycle, configuration, interception, or integration; keep pure domain/value logic ordinary Java.

### Why it matters

Unnecessary bean registration hides construction, increases context coupling, and makes focused tests depend on Spring.

### Avoid

Do not annotate data carriers, deterministic calculators, or short-lived values solely for convenient injection.

### Prefer

Construct pure collaborators directly and inject them into boundary/application beans. Use `@Bean` when third-party or configured construction belongs to the container.

### Nuance

A class can remain framework-neutral while its factory is Spring-managed.

### Sources

- **Spring bean overview:** <https://docs.spring.io/spring-framework/reference/core/beans/basics.html>
- **Spring dependency injection:** <https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html>

<a id="struct-explicit-public-boundary"></a>
## `struct-explicit-public-boundary` — Expose only the intended module API

> Keep implementation types internal and make cross-package/module access pass through deliberate contracts.

### Why it matters

Wide visibility lets other features depend on concrete persistence, web, or configuration details and makes later refactoring unsafe.

### Avoid

Do not make every component public or publish internal events/entities as a convenience.

### Prefer

Use package visibility, public facade/contracts, and named interfaces or module verification when the system is large enough to benefit.

### Nuance

Java module exports, Spring Modulith APIs, and package visibility are complementary tools; use the least mechanism that proves the boundary.

### Sources

- **Spring Modulith verification:** <https://docs.spring.io/spring-modulith/reference/verification.html>
- **Spring Boot structuring code:** <https://docs.spring.io/spring-boot/reference/using/structuring-your-code.html>

<a id="struct-modulith-proves-boundaries"></a>
## `struct-modulith-proves-boundaries` — Use Spring Modulith to verify an existing modular intent

> Adopt Spring Modulith when module dependency verification, module tests, events, or observability materially improve a modular monolith.

### Why it matters

The library can detect cycles and illegal access, but cannot invent meaningful modules from arbitrary packages.

### Avoid

Do not add Modulith annotations as decoration or use application events to hide synchronous coupling.

### Prefer

Define modules from real capabilities, verify them, and use events only when the temporal/ownership contract is explicit.

### Nuance

Small applications may need only packages and tests; introduce Modulith when the verification value exceeds its conceptual cost.

### Sources

- **Spring Modulith verification:** <https://docs.spring.io/spring-modulith/reference/verification.html>
- **Spring Modulith events:** <https://docs.spring.io/spring-modulith/reference/events.html>
