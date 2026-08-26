# Source map

Research date: **2026-08-26**

This skill is an original synthesis. Each rule carries direct sources. This map records the principal authority families, discovery corpora, and curation boundaries.

## Current platform facts at the cutoff

- Spring Boot documentation identifies **4.1.1** as the latest stable line and **4.2.0-M1** as preview.
- Spring Boot 4.1.1 requires at least Java 17, supports Java through 26, and requires Spring Framework 7.0.9 or newer.
- Spring Framework documentation lists stable 7.0.9 and 6.2.19 lines.
- Spring Boot 3.5.16 was announced as the final OSS release of the 3.5 generation.
- Spring Boot 4 uses Spring Framework 7, Jakarta EE 11, Servlet 6.1, modularized Boot artifacts/starters, and Boot 4 migration rules.
- Current facts must be rechecked after the research date.

## Primary Spring sources

- [Spring Boot reference](https://docs.spring.io/spring-boot/)
- [Spring Boot system requirements](https://docs.spring.io/spring-boot/system-requirements.html)
- [Spring Boot 4 migration guide](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide)
- [Spring Framework reference](https://docs.spring.io/spring-framework/reference/)
- [Spring Framework 7 resilience](https://docs.spring.io/spring-framework/reference/core/resilience.html)
- [Spring Data JPA reference](https://docs.spring.io/spring-data/jpa/reference/)
- [Spring Security reference](https://docs.spring.io/spring-security/reference/)
- [Spring Modulith reference](https://docs.spring.io/spring-modulith/reference/)
- [Project Reactor reference](https://projectreactor.io/docs/core/release/reference/)
- [Hibernate ORM user guide](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html)
- [Jakarta Persistence specification](https://jakarta.ee/specifications/persistence/3.2/jakarta-persistence-spec-3.2)

Rules link the exact section governing dependency injection, configuration, web contracts, transactions, repositories, persistence, security, scheduling, reactive behavior, testing, observability, lifecycle, and AOT.

## Community discovery corpora

These sources helped identify recurring agent errors, version boundaries, useful taxonomies, and counterexamples. They do not override primary Spring documentation.

- [JVM Skills](https://jvmskills.com/) and [jvm-skills/jvm-skills](https://github.com/jvm-skills/jvm-skills)
- [Aditya Parikh's version-aware Spring Boot skill](https://github.com/adityamparikh/spring-boot-skill)
- [SivaLabs agent skills](https://github.com/sivaprasadreddy/sivalabs-agent-skills), especially its Spring Boot and testing material
- [Piotr Minkowski's Spring Boot skill corpus](https://github.com/piomin/claude-ai-spring-boot)
- [Hibernate/JPA validator skill](https://github.com/adityamparikh/hibernate-jpa-validator-skill)
- [Spring Boot 4 migration skill listing](https://github.com/jvm-skills/jvm-skills/blob/main/skills/framework/spring-boot-4-migration.yaml)
- [Project Reactor skill listing](https://github.com/jvm-skills/jvm-skills/blob/main/skills/framework/project-reactor.yaml)
- [skills.sh](https://skills.sh/)

## Material conflicts rejected as universal Spring rules

Community sources and common team conventions disagree on:

- package-by-feature, global layers, hexagonal architecture, and mandatory Spring Modulith;
- mandatory constructor injection versus framework/legacy construction constraints;
- mandatory MVC, WebFlux, virtual threads, or reactive clients;
- `@SpringBootTest` everywhere versus almost no Spring tests;
- mocking frameworks and fixed test counts;
- always exposing entities, always wrapping DTOs, or always using repositories directly;
- globally disabling CSRF, enabling CORS wildcards, or using URL authorization alone;
- retries around every remote call;
- always enabling lazy initialization, open-session-in-view, or automatic DDL;
- one logging, tracing, database, migration, or deployment technology.

Akọ̀wé Spring retains the durable mechanism and leaves architecture, product, infrastructure, and project decisions to their actual owners.

## Curation path

```text
community candidate or recurring agent behavior
→ controlling Spring/Jakarta/Hibernate/Reactor source
→ Boot/Framework generation check
→ MVC/reactive/data/security/deployment boundary check
→ strongest legitimate counterexample
→ original scoped rule
```

No substantial source prose or code examples are copied. URLs remain under their respective owners and licenses.
