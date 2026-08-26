# Pattern provenance

This file records the corpora used to build the shipped references. It is maintainer context, not a runtime mining procedure.

## Community skill corpora inspected

### Rust

- [`actionbook/rust-skills` `m15-anti-pattern`](https://github.com/actionbook/rust-skills/blob/main/skills/m15-anti-pattern/SKILL.md)
- [`actionbook/rust-skills` ownership, resource, mutability, async, error, and unsafe modules](https://github.com/actionbook/rust-skills)
- [`leonardomso/rust-skills`](https://github.com/leonardomso/rust-skills), especially its ownership, error, unsafe, async, numeric, API, and anti-pattern rule taxonomy
- [`wshobson/agents` `rust-async-patterns`](https://github.com/wshobson/agents/blob/main/plugins/systems-programming/skills/rust-async-patterns/SKILL.md)

### Python

- [`wshobson/agents` `python-anti-patterns`](https://github.com/wshobson/agents/blob/main/plugins/python-development/skills/python-anti-patterns/SKILL.md)
- The same repository's Python error-handling, resource-management, type-safety, resilience, testing, and asyncio skills

### Java/JVM

- [JVM Skills](https://jvmskills.com/) and [`jvm-skills/jvm-skills`](https://github.com/jvm-skills/jvm-skills) catalogue entries for Hibernate/JPA validation, JPA patterns, jOOQ, Spring, Gradle, testing, and migration
- [`adityamparikh/hibernate-jpa-validator-skill`](https://github.com/adityamparikh/hibernate-jpa-validator-skill)
- [`piomin/claude-ai-spring-boot`](https://github.com/piomin/claude-ai-spring-boot)
- The JVM Skills jOOQ knowledge-base process was studied for source freshness and supersession, not copied as Èèwọ̀'s runtime model

### Broad discovery

- [skills.sh](https://skills.sh/) listings for anti-pattern, error-handling, async, resilience, language, and static-analysis skills

## Primary validation sources

- Rust Reference, standard library, Rust API Guidelines, Rustonomicon, Clippy, and Tokio documentation
- Java SE/JDK documentation plus official Spring, Reactor, Hibernate, Jakarta Persistence, jOOQ, and Gradle documentation
- Python documentation and PEPs
- Official Elixir code/process anti-pattern guides and Task/GenServer documentation

## Deliberately rejected blanket prescriptions

The following candidate forms were not imported as universal guards:

- fixed function-length or argument-count thresholds;
- “never clone”, “never unwrap”, or “always use iterators” without an applicable failure mechanism;
- mandatory Clean Architecture, repository/service/DTO layers, DDD, MVC, or microservices;
- blanket field-injection, inheritance, mocking, or coverage rules;
- performance substitutions without a measured or structurally credible cost;
- rules already fully owned by a formatter unless the semantic failure extends beyond formatting.

The shipped references retain only patterns that can state a trigger, failure mechanism, consequence, safe path, and exception boundary.
