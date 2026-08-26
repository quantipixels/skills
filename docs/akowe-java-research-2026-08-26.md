# Research: Akọ̀wé Java

**Date:** 2026-08-26  
**Repository candidate:** `quantipixels/skills`, branch `feature/akowe-java`  
**Question:** How should a portable skill encode what expert modern Java looks like while remaining baseline-aware, framework-neutral, auditable, and economical in agent context?

## Executive result

**Premise verdict: SUPPORTED, with a control boundary.**

A broad Java knowledge skill is useful because Java expertise is not one pattern or one current syntax feature. It combines language contracts, API design, value semantics, nullability, generics, equality, exceptions, collections, streams, the Java Memory Model, virtual threads, resources, security, diagnostics, build compatibility, and disciplined proof.

The skill becomes harmful when “expert Java” is implemented as one giant prompt, one author's taste, or a framework architecture manual. The selected design therefore follows the strongest architectural idea in `leonardomso/rust-skills`: a concise navigation layer, stable independently addressable rules, progressive disclosure, explicit source attribution, and independent use during implementation or review.

The result is `akowe-java`: **105 original Java rules across 21 category references**, covering Java 17–26 and optimized for Java 25 LTS plus Java 26 GA. The project baseline always controls. Preview/incubator features remain opt-in.

## Current Java baseline

At the research date:

- Oracle's support roadmap identifies Java 25 as an LTS release: <https://www.oracle.com/java/technologies/java-se-support-roadmap.html>.
- Java SE 26 API and specification sets are published: <https://docs.oracle.com/en/java/javase/26/docs/api/> and <https://docs.oracle.com/en/java/javase/26/docs/specs/>.
- The Java SE 26 specification still identifies primitive types in patterns/`instanceof`/`switch` as preview, confirming that “current JDK” does not mean “all available features are permanent”.
- Java 25 remains the appropriate current LTS optimization point while Java 26 supplies the current feature-release API surface.

The skill deliberately does not make Java 25 or 26 the repository baseline. It teaches the agent to read compiler toolchains, `--release`, CI/runtime images, library consumer constraints, and preview flags before selecting syntax or APIs.

## Benchmark: `leonardomso/rust-skills`

The benchmark repository describes its purpose as encoding what expert Rust looks like rather than leaving the agent at average language behavior. Its useful structural properties are:

- one portable skill rather than dozens of overlapping micro-skills;
- a lightweight `SKILL.md` index;
- small independently selectable rule units;
- stable category prefixes and IDs;
- progressive disclosure;
- bad/good reasoning plus sources;
- current-version metadata;
- original synthesis rather than copying source documentation.

Source: <https://github.com/leonardomso/rust-skills>.

What was copied: **the architectural ideas only**.

What was not copied:

- Rust-specific taxonomy, prose, examples, priorities, or rule content;
- the assumption that every optimization/pattern is universal;
- a fixed design-pattern curriculum;
- framework-specific architecture;
- any substantial copyrighted expression.

## Java corpus reviewed

### Primary sources

The rule set follows facts back to:

- Java Language/JVM/JDK specifications and tool docs;
- Java SE 25 and 26 APIs;
- OpenJDK JEPs;
- `dev.java`;
- Oracle secure coding guidance;
- official JUnit, JSpecify, Error Prone/NullAway, JMH, Maven, and SLF4J documentation where applicable.

Each rule file links the exact source pages controlling its claims.

### Java skill corpora

The research also inspected:

- JVM Skills language listings: <https://jvmskills.com/> and <https://github.com/jvm-skills/jvm-skills>;
- Stephan Janssen's Java best-practices skill: <https://github.com/stephanj/claude-code-collections/tree/master/skills/java-best-practices>;
- Adam Bien's Java 25 conventions: <https://github.com/AdamBien/airails/tree/main/java/java-conventions>;
- François Martin's Java Optional and Java Streams skills:
  - <https://github.com/martinfrancois/java-optionals-skill>
  - <https://github.com/martinfrancois/java-streams-skill>
- the broader Skills index: <https://skills.sh/>.

These sources were treated as discovery and counterexample evidence, not authority.

### Material conflicts

The corpora disagree on several points. Examples include:

- streams as a universal preference versus imperative code for stateful/checked-I/O flow;
- package-private fields/methods for test access versus least visibility and behavioral testing;
- field injection versus explicit construction;
- unchecked exceptions as a universal preference versus API-specific recoverability contracts;
- fixed limits on tests/classes versus risk-based proof and cohesion;
- one logging/assertion framework versus repository composition.

`akowe-java` resolves these conflicts by retaining the durable semantic principle and leaving framework/project choice to its actual owner. It does not encode an author's personal house style as Java expertise.

## Design alternatives

The Experimental `ideate` lens produced four materially different shapes:

| Candidate | Mechanism | Result |
| --- | --- | --- |
| A — monolithic guide | Put all advice and examples in one `SKILL.md` | Rejected: selection is easy but every invocation pays the complete context cost and rules become difficult to audit. |
| B — many Java micro-skills | Separate Optional, streams, concurrency, records, exceptions, and other skills | Rejected: routing overlap and installation burden fragment one language-level outcome. |
| C — one skill, bounded category references | `SKILL.md` plus 21 references with five anchored rules each | **Selected:** preserves progressive disclosure while keeping the QP package simple; a category load is capped at five cohesive rules. |
| D — one skill, one rule per file | `SKILL.md` index plus 105 rule files | Strongest isolation and closest physical layout to the benchmark, but rejected for this version because five-rule category bundles already bound context and avoid disproportionate file churn. |

## Prototype result

The Experimental `prototype` lens tested representative entries in three different domains:

1. `null-no-optional-get` — ordinary API/readability rule;
2. `vthread-dont-pool` — modern concurrency rule with operational consequences;
3. `num-bigdecimal-equality` — semantic correctness rule with a material exception.

The bounded category-reference prototype consistently supported each rule as:

```text
summary
why it matters
avoid
prefer
nuance
primary/supporting sources
```

This was sufficient to distinguish a principle from a rigid ban. No executable prototype was needed because the unsettled dimension was information architecture/readability, not runtime behavior.

## Selected capability boundary

`akowe-java` owns expert Java language/JDK guidance for writing, reviewing, and refactoring code.

It does not own:

- production implementation or test execution (`alaga`);
- review finding validation or verdict (`atunwo`);
- maintainability-only simplification (`pare`);
- architecture (`solution-architect`);
- Spring/Jakarta/Hibernate/jOOQ/Gradle policy;
- tool installation/operation (`irinse`);
- skill authoring lifecycle (`ko-skill`);
- Java teaching curricula.

It is classified as **lightweight**, despite its breadth. The owned result is a relevant subset of rules and judgment, not an ordered lifecycle or state machine.

## Taxonomy

| Category | Priority | Rules |
| --- | --- | ---: |
| Version and platform baseline | CRITICAL | 5 |
| Naming, visibility, and communication | MEDIUM | 5 |
| Types and generics | CRITICAL | 5 |
| Value semantics and immutability | CRITICAL | 5 |
| Records, sealed types, and pattern matching | HIGH | 5 |
| API design | CRITICAL | 5 |
| Nullability and Optional | CRITICAL | 5 |
| Equality, hashing, and ordering | CRITICAL | 5 |
| Exceptions and failure contracts | CRITICAL | 5 |
| Collections | HIGH | 5 |
| Streams, collectors, and pipelines | HIGH | 5 |
| Concurrency and the Java Memory Model | CRITICAL | 5 |
| Virtual threads and task concurrency | HIGH | 5 |
| Resources, files, HTTP, and I/O | CRITICAL | 5 |
| Numeric and time correctness | CRITICAL | 5 |
| Performance and allocation | HIGH | 5 |
| Security-sensitive coding | CRITICAL | 5 |
| Testing and proof | HIGH | 5 |
| Logging, metrics, and diagnostics | MEDIUM | 5 |
| Modules, dependencies, and packaging | MEDIUM | 5 |
| Reflection, serialization, and native interop | MEDIUM | 5 |

**Total: 105 rules.**

## Rule acceptance standard

A rule entered the skill only when it was:

1. broadly useful across modern Java;
2. materially non-obvious or recurrent in coding-agent output;
3. tied to a language/JDK contract or durable engineering mechanism;
4. scoped by baseline and exceptions;
5. not merely formatter trivia;
6. original prose with source attribution; and
7. independently loadable.

Rules that merely said “use pattern X,” “always write functional code,” or “keep methods below N lines” were rejected.

## QP skill usage

| Skill | Use in this work | Outcome |
| --- | --- | --- |
| `alarina` | route selection | `ko-skill` primary, with research/review/delivery support |
| `ro-wo` | tested whether a broad expert-language skill is useful or just another prescriptive manual | `SUPPORTED` only with progressive disclosure and strong boundaries |
| `iwadi` | current Java release, LTS, API, JEP, tooling, and corpus research | primary-source-backed rule data and this report |
| `ideate` (Experimental) | compared monolith, micro-skills, category references, and rule-per-file designs | selected one skill plus bounded five-rule category references |
| `prototype` (Experimental) | tested representative rules inside a five-rule reference bundle | retained the six-part rule contract and bounded bundle size |
| `ko-skill` | skill classification, authoring, package integration, and validation contract | lightweight Engineering skill |
| `solution-architect` | ownership and progressive-disclosure architecture check | language/JDK owner kept separate from framework, implementation, and verdict owners |
| `alaga` | integrated source, metadata, docs, and verification as one build job | one candidate branch |
| `pare` | planned simplification pass | remove redundant prose/mechanism before acceptance |
| `atunwo` | planned final broad candidate review | defects, maintainability evidence, and candidate identity |
| `technical-writing` | structure human-facing skill/research prose | layered navigation and direct rule language |
| `yo-slop` | final prose pruning after semantics | preserve IDs, sources, and guardrails |
| `seda-pr` | publication after exact-candidate validation | PR only after checks |
| `wo-pr` | CI and review readiness | post-PR stewardship |
| `ayewo-igba-ise` | post-delivery retrospective | determine justified QP skill improvements |
| `atona` | not persisted; initiative state was simple enough for the active branch/task envelope | no parallel plan artifact |
| `arojinle` | not invoked; the user had already selected the desired outcome and benchmark | no unresolved decision interview |
| `root-cause`, `dogfood`, `pepeye` | not applicable to a non-runtime skill authoring candidate | deliberately not simulated |

“Use all skills accordingly” was treated as **use every relevant owner and explicitly justify exclusions**, not as forcing inapplicable workflows.

## Verification plan

Before publication:

- validate the skill package and all local links;
- verify rule and category counts;
- parse plugin metadata;
- inspect the complete branch diff;
- sample rules across all categories against their primary sources;
- run prose and duplication checks;
- run `pare` and broad `atunwo` review;
- confirm the branch remains based on the requested latest `ori` starting point;
- open the PR through `seda-pr`;
- inspect CI/readiness through `wo-pr`.

## Residual limits

- Framework and persistence expertise remains outside this first release.
- Java evolves every six months; the version metadata and preview boundaries require periodic maintenance.
- The rule corpus is broad but not exhaustive. Absence of a matching rule is not proof that a Java candidate is correct.
- Some sources describe tools or conventions rather than Java SE itself; these are labeled supporting sources and never override the project.
