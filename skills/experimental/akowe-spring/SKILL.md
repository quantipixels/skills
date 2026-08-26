---
name: akowe-spring
description: Encode expert Spring Framework 6.1–7.0 and Spring Boot 3.3–4.1 practice for implementation, review, refactoring, and API design. Use when Spring code needs version-aware guidance on dependency injection, configuration, auto-configuration, MVC/WebFlux, validation, HTTP clients, transactions, Spring Data JPA/Hibernate, Security, async/events, testing, observability, lifecycle, or AOT/native images. Preserve repository and platform contracts; exclude Spring Cloud, Batch, Integration, messaging-product specifics, implementation ownership, architecture selection, and final review verdicts.
disable-model-invocation: true
license: MIT
metadata:
  version: "1.0.0"
  rules: 90
  categories: 18
  researched: "2026-08-26"
  spring:
    boot-guidance: "3.3-4.1"
    current-stable: "4.1.1"
    current-preview: "4.2.0-M1"
    framework-guidance: "6.1-7.0"
    current-framework: "7.0.9"
  java:
    minimum: "17"
    current-compatible: "26"
---

# Akọ̀wé Spring

Encode what expert Spring looks like: explicit container ownership, typed configuration, controlled proxy semantics, stable HTTP and persistence boundaries, version-aware customization, bounded concurrency, production-grade observability, and proof at the smallest useful Spring context.

This is an experimental, lightweight knowledge skill. It must be selected explicitly. It does not prescribe one architecture, package layout, database, client library, cloud platform, or testing stack. It supplies focused Spring Framework and Spring Boot judgment to the owner already implementing or reviewing the candidate.

## Detect the Spring generation first

1. Read the Boot parent/plugin/BOM, Spring Framework generation, Java toolchain, Jakarta/Servlet baseline, starters, managed dependencies, servlet versus reactive application type, database/security modules, deployment runtime, and preview flags.
2. Treat the project baseline as authoritative. At the 2026-08-26 research cutoff, Spring Boot 4.1.1 is the latest stable documentation line, Boot 4.2.0-M1 is preview, and Boot 4.1.1 requires Java 17–26 and Spring Framework 7.0.9 or newer.
3. Guidance for Boot 3.x exists for established applications; it is not a support promise. Spring Boot 3.5.16 was the final OSS release of the 3.5 generation.
4. Do not introduce Boot 4/Jakarta EE 11/Jackson 3/JUnit 6/Framework 7 APIs into Boot 3, or preserve removed/deprecated Boot 3 conventions in Boot 4.
5. Revalidate current release, security, support, and migration facts after the research date.

## Load only what the candidate needs

`SKILL.md` is the navigation layer. Each runtime reference contains exactly five cohesive rules. Open only categories controlling the touched code, then use only matching rule headings.

- New or upgraded application: start with [Spring and Spring Boot baseline](references/baseline.md), then load the changed framework surfaces.
- Bean/configuration work: use bean, configuration, auto-configuration, and structure categories.
- MVC/WebFlux API work: load the matching web model plus validation/errors and security when applicable.
- Persistence work: load transactions, Spring Data, and JPA/Hibernate together when their boundaries interact.
- Async, scheduled, event, or remote work: load async/events, HTTP clients, transactions, observability, and lifecycle as required.
- Review: rule names are hypotheses. Trace the actual code path to a caller-visible, data, security, resource, or operational consequence before reporting a defect.
- Composition: when `akowe-java` is installed, use it for Java/JDK language concerns. A Spring rule may specialize a Java default because of container, proxy, transaction, reactive, or lifecycle semantics, but must not silently weaken Java correctness or safety.

Category priorities mean:

- `CRITICAL` — correctness, compatibility, security, data integrity, lifecycle, or public-contract guidance; satisfy it or prove a concrete exception.
- `HIGH` — strong Spring default whose deviation needs candidate-specific benefit and proof.
- `MEDIUM` — contextual expert guidance; optimize for clarity, project fit, and operational value rather than mechanical compliance.

## Category index

| Category | Priority | Rule IDs |
| --- | --- | --- |
| [Spring and Spring Boot baseline](references/baseline.md) | CRITICAL | `base-detect-stack`, `base-use-managed-versions`, `base-stable-over-preview`, `base-respect-jakarta-generation`, `base-supported-release-line` |
| [Application structure and module boundaries](references/structure.md) | HIGH | `struct-root-application-package`, `struct-package-by-capability`, `struct-container-only-where-needed`, `struct-explicit-public-boundary`, `struct-modulith-proves-boundaries` |
| [Beans, dependency injection, and scopes](references/beans-di.md) | CRITICAL | `bean-constructor-required-dependencies`, `bean-container-owns-managed-instances`, `bean-singleton-thread-safe`, `bean-scope-crossing-explicit`, `bean-break-cycles-not-hide` |
| [Configuration, profiles, and secrets](references/configuration.md) | CRITICAL | `config-properties-for-groups`, `config-validate-at-startup`, `config-understand-precedence`, `config-profiles-select-environments`, `config-secrets-stay-external` |
| [Auto-configuration and starter design](references/auto-configuration.md) | HIGH | `auto-prefer-starters-managed`, `auto-back-off-user-control`, `auto-register-explicitly`, `auto-customize-before-replace`, `auto-use-condition-report` |
| [Spring MVC and HTTP API boundaries](references/web-mvc.md) | CRITICAL | `web-transport-dtos`, `web-explicit-http-semantics`, `web-narrow-request-mappings`, `web-versioning-one-strategy`, `web-bound-streams-and-uploads` |
| [Validation and error responses](references/validation-errors.md) | CRITICAL | `val-validate-external-boundaries`, `val-domain-invariants-owned`, `err-use-problem-detail-contract`, `err-specific-advice`, `err-log-and-return-separately` |
| [HTTP clients and resilience](references/rest-clients.md) | CRITICAL | `client-use-boot-builders`, `client-match-blocking-model`, `client-set-all-timeouts`, `client-map-remote-failures`, `client-retry-idempotent-owned` |
| [Transactions and proxy semantics](references/transactions.md) | CRITICAL | `tx-application-boundary`, `tx-proxy-invocation-visible`, `tx-rollback-contract-explicit`, `tx-remote-effects-outside`, `tx-readonly-is-a-hint` |
| [Spring Data repositories and queries](references/spring-data.md) | HIGH | `data-repository-owned-contract`, `data-query-shape-explicit`, `data-bound-result-size`, `data-projection-for-read-model`, `data-locking-and-versioning` |
| [JPA and Hibernate persistence](references/jpa-hibernate.md) | CRITICAL | `jpa-stable-entity-equality`, `jpa-explicit-fetch-plan`, `jpa-detect-n-plus-one`, `jpa-keep-persistence-context-bounded`, `jpa-cascade-owned-lifecycle` |
| [Spring Security boundaries](references/security.md) | CRITICAL | `sec-explicit-filter-chain`, `sec-method-authorization`, `sec-csrf-matches-auth-model`, `sec-cors-central-and-specific`, `sec-credential-storage-and-redaction` |
| [Async work, scheduling, events, and context](references/async-events.md) | CRITICAL | `async-named-bounded-executor`, `async-proxy-and-return-contract`, `async-propagate-context-deliberately`, `sched-idempotent-and-coordinated`, `event-delivery-contract` |
| [WebFlux and reactive pipelines](references/reactive.md) | HIGH | `reactive-end-to-end-choice`, `reactive-no-blocking-event-loop`, `reactive-return-dont-subscribe`, `reactive-context-not-threadlocal`, `reactive-bound-concurrency-and-buffers` |
| [Spring testing and context proof](references/testing.md) | HIGH | `test-smallest-context`, `test-slices-stay-slices`, `test-version-aware-mocking`, `test-preserve-context-cache`, `test-real-infrastructure-when-semantics-matter` |
| [Actuator, observability, and health](references/observability.md) | HIGH | `obs-minimize-actuator-exposure`, `obs-health-means-service-capability`, `obs-use-observation-api`, `obs-low-cardinality-dimensions`, `obs-log-exception-once` |
| [Startup, migrations, shutdown, and deployment](references/lifecycle.md) | CRITICAL | `life-startup-work-bounded`, `life-migrations-single-owner`, `life-readiness-after-required-init`, `life-graceful-shutdown-owned`, `life-no-lazy-init-to-hide-errors` |
| [AOT processing and native images](references/aot-native.md) | MEDIUM | `aot-stabilize-jvm-behavior-first`, `aot-register-narrow-runtime-hints`, `aot-avoid-unbounded-runtime-discovery`, `aot-separate-buildtime-runtime-config`, `aot-run-native-specific-proof` |

## Working contract

For each applicable rule:

```text
candidate construct
→ detected Boot/Framework/Java/platform baseline
→ Spring container, proxy, HTTP, data, security, or lifecycle mechanism
→ smallest fitting framework design
→ focused compiler, context, test, static-analysis, or runtime proof
```

Prefer Boot-managed builders, starters, configuration, and observation hooks before replacing infrastructure. Preserve explicit project decisions when they are compatible with framework correctness; challenge them only with a concrete failure mechanism or compatibility fact. Do not rewrite working code merely to display a newer annotation or fashionable architecture.

When this skill supports another owner:

- `alaga` owns implementation, integration, test execution, and handoff.
- `atunwo` owns code-review discovery, finding validation, and verdict.
- `pare` owns maintainability-only simplification.
- `solution-architect` owns architecture and distributed-system boundaries.
- `irinse` owns setup and operation of Spring tools, static analysis, profilers, JFR, test infrastructure, or migration tooling.
- `ko-skill` owns changes to this published skill.
- Spring Cloud, Batch, Integration, Kafka/Rabbit/Pulsar, GraphQL, and other portfolio projects require their own current documentation and may specialize this core guidance.

Return the rules applied, detected versions, material exceptions, proof performed, and coverage limits. State when a conclusion depends on database, messaging, cloud, native, deployment, or distributed-system semantics outside this skill.

## Maintenance

The rules are an original synthesis of Spring Boot, Spring Framework, Spring Data, Hibernate, Spring Security, Spring Modulith, Project Reactor, Jakarta, and selected community skill corpora. Read [authoring and maintenance](references/authoring.md) before changing the catalogue and [source map](references/source-map.md) when auditing provenance or freshness.
