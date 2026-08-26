# Source map

Research date: **2026-08-26**

This skill is an original synthesis. Individual rules carry direct source links. This map records the main source families, benchmark corpora, and curation boundaries.

## Primary Java sources

- [Java SE 26 API specification](https://docs.oracle.com/en/java/javase/26/docs/api/) — current feature-release APIs at the research date.
- [Java SE 26 specifications](https://docs.oracle.com/en/java/javase/26/docs/specs/) — language, JVM, tools, serialization, JNI, and related specifications; also identifies preview features.
- [Java SE 25 API specification](https://docs.oracle.com/en/java/javase/25/docs/api/) — current LTS API baseline at the research date.
- [Java SE support roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html) — LTS designation and support horizon.
- [OpenJDK JEP index](https://openjdk.org/jeps/0) — feature rationale, status, and release history.
- [dev.java](https://dev.java/learn/) — first-party Java learning and language/JDK guidance.
- [Java secure coding guidelines](https://www.oracle.com/java/technologies/javase/seccodeguide.html) — security-sensitive API and coding guidance.

The rules also cite the exact API/package/tool/JEP pages that support their semantics.

## First-party standards and tools

- [JSpecify](https://jspecify.dev/) — nullness annotations and specification.
- [JUnit 5](https://junit.org/junit5/docs/current/user-guide/) — test contracts and parameterized testing.
- [Error Prone](https://errorprone.info/) and [NullAway](https://github.com/uber/NullAway) — compiler/static-analysis evidence.
- [OpenJDK JMH](https://github.com/openjdk/jmh) — JVM microbenchmarking.
- [SLF4J](https://www.slf4j.org/manual.html) — logging API behavior when a project uses SLF4J.
- [Maven compiler `release`](https://maven.apache.org/plugins/maven-compiler-plugin/examples/set-compiler-release.html) — build configuration evidence.

## Benchmark and discovery corpora

These sources informed taxonomy, common agent mistakes, progressive disclosure, and counterexamples. They do not override primary Java sources.

- [leonardomso/rust-skills](https://github.com/leonardomso/rust-skills) — benchmark architecture: concise skill index, stable rule IDs, one focused rule at a time, progressive disclosure, and explicit sources.
- [JVM Skills](https://jvmskills.com/) and [jvm-skills/jvm-skills](https://github.com/jvm-skills/jvm-skills) — discovery index for Java/JVM skills and supersession metadata.
- [Stephan Janssen Java best practices](https://github.com/stephanj/claude-code-collections/tree/master/skills/java-best-practices) — type-first modeling, records, sealed types, value objects, exceptions, testing, and modern Java candidates.
- [Adam Bien Java conventions](https://github.com/AdamBien/airails/tree/main/java/java-conventions) — dense modern-Java conventions and useful counterexamples to universalizing author preference.
- [Java Optional skill](https://github.com/martinfrancois/java-optionals-skill) — Optional flow, laziness, baseline compatibility, and hard-stop candidates.
- [Java Streams skill](https://github.com/martinfrancois/java-streams-skill) — stream/collector semantics, ordering, nulls, parallelism, and terminal-operation selection.
- [skills.sh](https://skills.sh/) — broad discovery of existing language and review skills.

## Curation decisions

Accepted ideas had to survive:

```text
community claim
→ primary-source check
→ safe counterexample search
→ framework/baseline boundary check
→ original rule synthesis
```

Examples deliberately rejected as universal rules include mandatory streams, package-private-by-default internals for test access, fixed limits on tests or class length, field injection as a language convention, mandatory unchecked exceptions, and mandatory use of any one logging/testing framework.

## Source distribution

The 105 rules currently include **209 labeled source references across 152 distinct URLs**. Main cited domains:

- `docs.oracle.com` — 151 rule-source references
- `openjdk.org` — 23 rule-source references
- `dev.java` — 16 rule-source references
- `github.com` — 6 rule-source references
- `www.oracle.com` — 4 rule-source references
- `junit.org` — 3 rule-source references
- `google.github.io` — 2 rule-source references
- `jspecify.dev` — 2 rule-source references
- `www.slf4j.org` — 1 rule-source reference
- `maven.apache.org` — 1 rule-source reference

Counts describe links, not authority. A rule may cite several primary pages because Java semantics often span the language, API, and tool contracts.
