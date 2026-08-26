# Research: Akọ̀wé Spring

**Date:** 2026-08-26  
**Repository candidate:** `quantipixels/skills`, branch `feature/akowe-spring`  
**Starting point:** current `ori` at `9785058f6c236391f2f37ae0e2e81b35bec30915`  
**Question:** How should a portable skill encode what expert Spring Framework and Spring Boot look like without becoming a framework architecture template, migration workflow, or indiscriminate best-practices checklist?

## Executive result

**Premise verdict: SUPPORTED, with a composition boundary.**

Spring expertise is not reducible to Java syntax or one application architecture. It depends on container ownership, bean scopes, proxy interception, externalized configuration, auto-configuration, HTTP semantics, validation and error contracts, transaction behavior, repository/query shape, persistence-context lifetime, Security filter/method boundaries, async and reactive context, test context selection, actuator exposure, health semantics, graceful shutdown, and AOT/native constraints.

The useful result is a **separate Spring framework knowledge skill**, not an expansion of `akowe-java` and not a production workflow. The selected design is:

```text
akowe-java (when installed)
    Java/JDK contracts
        +
akowe-spring
    Spring Framework / Spring Boot specialization
        ↓
alaga or atunwo owns the actual implementation/review outcome
```

The skill contains **90 original rules across 18 bounded category references**. Each reference contains five rules so the agent loads only the Spring mechanisms controlling the candidate.

## Current Spring baseline

At the research cutoff:

- Spring Boot documentation lists `4.1.1` as the latest stable line and `4.2.0-M1` as preview: <https://docs.spring.io/spring-boot/>.
- Spring Boot 4.1.1 requires Java 17, supports Java through 26, and requires Spring Framework 7.0.9 or newer: <https://docs.spring.io/spring-boot/system-requirements.html>.
- Spring Framework documentation lists stable `7.0.9` and `6.2.19` lines: <https://docs.spring.io/spring-framework/reference/>.
- Spring Boot 3.5.16 was the last OSS release of the 3.5 generation: <https://spring.io/blog/2026/06/25/spring-boot-3-5-16-available-now/>.
- Spring Boot 4 is based on Spring Framework 7, Jakarta EE 11, and Servlet 6.1, and introduced significant module/starter/package, Jackson, testing, and dependency changes: <https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide>.

The skill covers Boot 3.3–4.1 for established codebases, but this is **compatibility guidance, not a support promise**. The project build, managed dependencies, runtime, Jakarta generation, application type, and organizational support policy remain authoritative.

## Why this is not part of `akowe-java`

A language skill can say:

```text
preserve interruption
bound external work
make lifetimes explicit
keep contracts typed
```

Spring must specialize those principles:

```text
configure and own the executor selected by @Async
do not assume virtual threads remove datasource/HTTP limits
do not manually instantiate an intercepted or scoped bean
keep transaction/security/cache/resilience annotations on a real proxy path
```

These are independent Spring mechanisms. Loading them for every Java task would waste context and could incorrectly impose container semantics on plain Java.

The Spring skill therefore composes with `akowe-java` when available, but remains independently useful because PR #34 is not yet merged into `ori`. It never requires a missing installed skill to operate.

## Corpus reviewed

### Primary sources

The rule set was grounded in current:

- Spring Boot reference, system requirements, application properties, migration guide, testing, actuator, observability, graceful-shutdown, and native-image documentation;
- Spring Framework core container, AOP/proxy, web MVC, WebFlux, validation, transaction, REST client, resilience, scheduling, test-context, and AOT documentation;
- Spring Data Commons and Spring Data JPA repository, query, projection, transaction, entity-graph, and locking documentation;
- Spring Security servlet/reactive authorization, method security, CSRF, CORS, password storage, and concurrency documentation;
- Spring Modulith fundamentals, verification, and event publication documentation;
- Project Reactor reference documentation;
- Hibernate ORM user guide;
- Jakarta Persistence specification.

Every runtime rule carries exact source links.

### Community discovery corpora

The research inspected:

- JVM Skills and the `jvm-skills/jvm-skills` catalogue;
- Aditya Parikh's version-aware `spring-boot` skill;
- SivaLabs' Spring Boot and test reference corpus;
- Piotr Minkowski's Spring Boot corpus;
- Hibernate/JPA validation skills;
- Spring Boot 4 migration and Project Reactor skill listings;
- `skills.sh`.

These were treated as **candidate and counterexample evidence**, not authority. Embedded commands, tool permissions, architecture mandates, build workflows, and fixed technology choices were not followed.

### Material conflicts

The sources and community practices disagree on:

- package-by-feature versus global technical layers;
- mandatory Spring Modulith, hexagonal architecture, or microservices;
- field versus constructor injection;
- MVC versus WebFlux versus virtual-thread MVC;
- DTOs everywhere versus direct model exposure;
- open-session-in-view and eager fetching;
- all integration tests versus almost no context tests;
- `@SpringBootTest` as the default;
- retries and circuit breakers around every call;
- disabling CSRF/CORS/security defaults;
- one migration, logging, tracing, or cloud stack;
- fixed test counts, class lengths, coverage gates, and JavaDoc requirements.

Akọ̀wé Spring retains the controlling Spring mechanism and the strongest safe default, while preserving legitimate project-specific alternatives.

## Design alternatives

The Experimental `ideate` lens generated and challenged four shapes:

| Candidate | Mechanism | Result |
| --- | --- | --- |
| A — extend `akowe-java` | Add Spring categories to the Java language catalogue | Rejected: Spring container/proxy/data/security semantics would load for non-Spring Java and blur ownership. |
| B — one `akowe-spring` skill | One Spring owner with bounded category references | **Selected:** one reusable framework judgment capability with progressive disclosure. |
| C — many micro-skills | Separate Boot, MVC, Data, JPA, Security, WebFlux, testing, and observability skills | Rejected for the first release: routing overlap and installation burden fragment one framework-level outcome. |
| D — architecture template | One Spring Boot scaffolding workflow with package layout, build stack, database, security, Docker, and test policy | Rejected: it would encode one author's application architecture rather than expert Spring semantics. |

Spring Cloud, Batch, Integration, messaging products, GraphQL, and portfolio-specific projects remain outside this first skill. They can become independent skills when their trigger and result are independently useful.

## Prototype result

The Experimental `prototype` lens tested the five-rule category representation against three Spring-specific questions:

1. `tx-proxy-invocation-visible` — self-invocation bypassing proxy advice;
2. `client-use-boot-builders` — preserving Boot HTTP customization and instrumentation;
3. `jpa-explicit-fetch-plan` — query-specific fetch shape instead of eager mappings/open-session behavior.

For each, the following representation was enough to distinguish a framework mechanism from a rigid rule:

```text
stable id
summary
why it matters
avoid
prefer
nuance
official sources
illustrative example where it materially clarifies the boundary
```

No executable product prototype was required because the unsettled dimension was retrieval and explanation quality. The relevant runtime semantics were checked against official documentation and representative code shapes.

## Selected capability boundary

`akowe-spring` owns expert Spring Framework and Spring Boot guidance for implementation, review, refactoring, and API design.

It does not own:

- production implementation, builds, migrations, or test execution (`alaga`);
- code-review discovery, finding validation, or verdict (`atunwo`);
- maintainability-only simplification (`pare`);
- architecture or distributed-system design (`solution-architect`);
- Java/JDK language guidance (`akowe-java` when installed);
- tool selection/operation (`irinse`);
- Spring Cloud, Batch, Integration, Kafka/Rabbit/Pulsar, GraphQL, or other portfolio-specific frameworks;
- framework version migration as a durable multi-stage workflow;
- Spring teaching curricula.

It is **lightweight**, despite its breadth. The result is a selected subset of knowledge and judgment, not a lifecycle state machine.

## Taxonomy

| Category | Priority | Rules |
| --- | --- | ---: |
| Spring and Spring Boot baseline | CRITICAL | 5 |
| Application structure and module boundaries | HIGH | 5 |
| Beans, dependency injection, and scopes | CRITICAL | 5 |
| Configuration, profiles, and secrets | CRITICAL | 5 |
| Auto-configuration and starter design | HIGH | 5 |
| Spring MVC and HTTP API boundaries | CRITICAL | 5 |
| Validation and error responses | CRITICAL | 5 |
| HTTP clients and resilience | CRITICAL | 5 |
| Transactions and proxy semantics | CRITICAL | 5 |
| Spring Data repositories and queries | HIGH | 5 |
| JPA and Hibernate persistence | CRITICAL | 5 |
| Spring Security boundaries | CRITICAL | 5 |
| Async work, scheduling, events, and context | CRITICAL | 5 |
| WebFlux and reactive pipelines | HIGH | 5 |
| Spring testing and context proof | HIGH | 5 |
| Actuator, observability, and health | HIGH | 5 |
| Startup, migrations, shutdown, and deployment | CRITICAL | 5 |
| AOT processing and native images | MEDIUM | 5 |

**Total: 90 rules.**

## Rule acceptance standard

A rule entered the catalogue only when it was:

1. broadly useful across a meaningful range of Spring applications;
2. materially non-obvious, recurrent in coding-agent output, or tied to a Spring failure mechanism;
3. scoped by Boot/Framework generation and application style;
4. explicit about legitimate exceptions and project specialization;
5. not merely formatter, IDE, or deterministic-linter trivia;
6. independent from one fixed architecture or vendor stack;
7. original prose with source attribution; and
8. retrievable by one stable ID.

Rules such as “always use package-by-feature,” “always use WebFlux,” “all services need interfaces,” “always disable CSRF for APIs,” “always use `@SpringBootTest`,” or “every remote call needs retry” were rejected.

## QP skill usage

| Skill | Use in this work | Outcome |
| --- | --- | --- |
| `alarina` | route selection | `ko-skill` primary with research, architecture, delivery, review, and publication support |
| `ro-wo` | tested whether Spring should extend Java or become a separate capability | `SUPPORTED` as one separate framework owner |
| `iwadi` | current Boot/Framework versions, support, migration, and primary-source research | baseline and 90 sourced rules |
| `ideate` (Experimental) | compared Java extension, one Spring skill, micro-skills, and architecture template | selected one bounded Spring catalogue |
| `prototype` (Experimental) | tested transaction, HTTP-client, and JPA rule representation | retained bounded five-rule references |
| `ko-skill` | ownership, lightweight classification, progressive disclosure, integration, and validation | `akowe-spring` Engineering skill |
| `solution-architect` | checked language/framework/architecture and Spring-project boundaries | no architecture mandate in the skill |
| `alaga` | integrated skill, references, metadata, research, package surfaces, and proof | one exact branch candidate |
| `pare` | challenged category overlap, repeated rationale, and unnecessary micro-skill/file expansion | 18 cohesive categories retained |
| `atunwo` | final broad candidate review | defects corrected before PR |
| `technical-writing` | structured selector, navigation, rules, and research | layered runtime/maintainer content |
| `yo-slop` | pruned repeated prose after semantics stabilized | IDs, exceptions, sources, and boundaries preserved |
| `seda-pr` | exact branch publication | PR after final candidate validation |
| `wo-pr` | CI, mergeability, and review readiness | post-PR verification |
| `ayewo-igba-ise` | retrospective on skill use | compare findings against existing knowledge-catalogue learning before proposing more meta-work |
| `atona` | not persisted; the branch/research envelope was sufficient and no multi-session initiative state was needed | no duplicate plan record |
| `arojinle` | not invoked; the user selected the outcome and companion boundary | no unresolved decision interview |
| `root-cause`, `dogfood`, `pepeye` | not applicable: no reproducible runtime defect, browser journey, or provider-neutral playbook lifecycle | deliberately not simulated |

“Use all skills accordingly” was applied as **use every relevant owner and explicitly reject inapplicable machinery**, not invoke every installed skill regardless of fit.

## Verification plan

Before publication:

- validate frontmatter, agent metadata, manifest, router, README, and changeset;
- verify 18 categories, 90 unique IDs, and five rules per runtime category;
- verify index-to-reference and rule-anchor completeness;
- verify all Markdown fences and local links;
- sample every category against its primary sources;
- challenge Boot 3/4, MVC/WebFlux, transaction, JPA, Security, testing, operations, and AOT boundaries;
- check examples for proxy, lifecycle, resource, and security correctness;
- run a simplification pass and broad review;
- confirm the branch remains based on the requested latest `ori`;
- open the PR through `seda-pr`;
- inspect CI/readiness through `wo-pr`.

## Retrospective expectation

The existing `ko-skill` knowledge-catalogue follow-up in PR #35 already addresses the main reusable authoring lessons: one-owner classification, primary/community evidence boundaries, version/freshness policy, stable rule IDs, progressive disclosure, counterexamples, maintainer-only source maps, and catalogue proof.

This Spring work may justify one small addition to that existing follow-up: a **layered composition contract** for language and framework catalogues. It does not currently justify a new meta-skill or another catalogue validator.

## Residual limits

- Spring Cloud, Batch, Integration, messaging, GraphQL, and platform-specific deployment guidance are excluded.
- The catalogue covers core Spring Data JPA/Hibernate semantics but is not an exhaustive Hibernate optimizer.
- Spring evolves quickly; current release, support, security, and migration claims require periodic maintenance.
- The catalogue is broad but incomplete. Absence of a matching rule is not proof that a candidate is correct.
