# Spring and Spring Boot baseline

**Priority:** CRITICAL  
**Rules:** 5

Detect the actual Spring generation before selecting APIs, starters, annotations, or migration advice.

Apply only the rules whose trigger exists in the candidate. Preserve the detected Spring Boot, Spring Framework, Java, Jakarta, servlet/reactive, database, security, and deployment contracts.

Examples are illustrative; preserve the repository baseline, imports, build system, framework generation, public API, and operational constraints.

<a id="base-detect-stack"></a>
## `base-detect-stack` — Detect the complete managed stack

> Read the Spring Boot, Spring Framework, Java, Jakarta/Servlet, build-plugin, and application-style baseline before changing code.

### Why it matters

Spring Boot coordinates a platform, not one library. A correct API on Boot 4.1 may be absent, renamed, or semantically different on Boot 3.x.

### Avoid

Do not infer the version from imports, memory, or a single dependency. Do not assume an MVC application merely because `spring-web` is present.

### Prefer

Read the Boot parent/plugin and dependency management, Java toolchain, starters, servlet/reactive stack, Spring Data/Security versions, preview flags, and deployment image.

### Nuance

For a library or shared starter, also inspect its consumer range; the producer's build JDK is not the consumer baseline.

### Example

**Avoid**

```xml
<parent>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-parent</artifactId>
  <version>4.1.1</version>
</parent>
<properties>
  <java.version>25</java.version>
</properties>
```

**Prefer**

```xml
# Also inspect:
# - managed Spring Framework/Data/Security versions
# - servlet vs reactive starters
# - Java toolchain / --release
# - deployment runtime and preview flags
```

### Sources

- **Spring Boot system requirements:** <https://docs.spring.io/spring-boot/system-requirements.html>
- **Spring Boot build systems:** <https://docs.spring.io/spring-boot/reference/using/build-systems.html>

<a id="base-use-managed-versions"></a>
## `base-use-managed-versions` — Let Spring Boot manage its dependency graph

> Use the Boot BOM, parent, or dependency-management plugin and avoid overriding managed Spring/third-party versions casually.

### Why it matters

Boot tests a coordinated graph. An isolated override can introduce binary incompatibility, duplicate API generations, or unsupported combinations.

### Avoid

Do not pin Framework, Security, Data, Jackson, Hibernate, or container versions independently merely to obtain one fix or feature.

### Prefer

Upgrade the Boot maintenance line first. Override a managed dependency only with compatibility evidence, a bounded reason, and proof of the resulting graph.

### Nuance

Security advisories can justify a temporary override, but record the removal trigger and verify the owning project's guidance.

### Sources

- **Spring Boot build systems:** <https://docs.spring.io/spring-boot/reference/using/build-systems.html>
- **Spring Boot dependency versions:** <https://docs.spring.io/spring-boot/appendix/dependency-versions/coordinates.html>

<a id="base-stable-over-preview"></a>
## `base-stable-over-preview` — Keep preview framework lines opt-in

> Use stable Spring Boot and Framework releases unless the repository explicitly accepts milestone, release-candidate, snapshot, preview, or incubator risk.

### Why it matters

Framework previews can change APIs, configuration properties, generated metadata, and transitive dependencies before GA.

### Avoid

Do not copy examples from 4.2 snapshots into a 4.1 application or enable a preview Java/Spring feature because it appears in current docs.

### Prefer

Pin the exact preview line, flags, reason, upgrade/removal plan, and CI/runtime compatibility when preview use is authorized.

### Nuance

At the 2026-08-26 cutoff, Boot 4.1.1 is the latest stable documentation line and 4.2.0-M1 is preview; revalidate after the cutoff.

### Sources

- **Spring Boot stable documentation:** <https://docs.spring.io/spring-boot/>
- **Spring Boot 4.2 system requirements:** <https://docs.spring.io/spring-boot/4.2/system-requirements.html>

<a id="base-respect-jakarta-generation"></a>
## `base-respect-jakarta-generation` — Do not mix Spring/Jakarta generations

> Keep Boot 3/Framework 6 and Boot 4/Framework 7 code aligned with their Jakarta EE and Servlet generations.

### Why it matters

Mixed `javax.*`/`jakarta.*`, servlet baselines, or starter generations create class-loading and signature failures that may surface only at runtime.

### Avoid

Do not solve migration errors by adding old Java EE APIs beside Jakarta APIs or by forcing an incompatible embedded container.

### Prefer

Follow the migration guide, update imports/dependencies together, and verify the deployed container baseline. Treat Boot 4 modular starters as a deliberate dependency change.

### Nuance

Third-party libraries may lag the platform; isolate or upgrade them rather than polluting the whole classpath with both generations.

### Sources

- **Spring Boot 4 migration guide:** <https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide>
- **Spring Boot system requirements:** <https://docs.spring.io/spring-boot/system-requirements.html>

<a id="base-supported-release-line"></a>
## `base-supported-release-line` — Differentiate compatibility coverage from supported deployment

> Preserve older project compatibility, but do not present an ended OSS line as the default for new production work.

### Why it matters

A project can still compile on an older Boot line after public maintenance ends, while missing security and dependency updates.

### Avoid

Do not start new work on an obsolete line merely because the skill contains compatibility guidance for it.

### Prefer

Check Spring's current support policy; use the latest stable supported maintenance release for new work and plan explicit upgrades for older applications.

### Nuance

Spring Boot 3.5.16 was announced as the last OSS release of 3.5.x; commercial support and organizational constraints are separate decisions.

### Sources

- **Spring Boot 3.5.16 end of OSS support:** <https://spring.io/blog/2026/06/25/spring-boot-3-5-16-available-now>
- **Spring Boot releases:** <https://spring.io/projects/spring-boot#support>
