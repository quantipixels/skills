# Mining sources

Use source mining to discover candidate failure classes, not to bulk-import somebody else's opinions.

## Evidence ladder

Prefer in this order:

1. official language/framework documentation, specifications, source, and maintained linter/compiler rules;
2. project-owner documentation and maintained first-party examples;
3. curated specialist catalogues that lead back to their source repositories;
4. community skills and review checklists;
5. local session/review evidence.

Local evidence is decisive for recurrence in the user's environment, but it does not make an external technical claim true. Validate volatile or disputed claims through `iwadi` before activation.

## Discovery catalogues

- <https://jvmskills.com/> — strong JVM discovery index, especially for focused Java/Kotlin/Spring/Gradle/database/testing skills. Treat listing trust and author metadata as discovery evidence, then inspect the source repository and primary framework documentation.
- <https://skills.sh/> — broad public Agent Skills index useful for finding existing anti-pattern, language, testing, security, and workflow skills. Do not treat popularity or install count as correctness.

The JVM Skills jOOQ knowledge-builder is also a useful process reference: it processes newer material first, deduplicates older entries, explicitly records supersession, and logs unresolved uncertainty rather than guessing. See <https://github.com/jvm-skills/jvm-skills/blob/main/ralph/jooq-skill-creator/process-jooq-article.md>. Preserve those ideas, not its jOOQ-specific storage implementation.

## Useful community corpora to mine

- `actionbook/rust-skills`, especially `m15-anti-pattern`: <https://github.com/actionbook/rust-skills/blob/main/skills/m15-anti-pattern/SKILL.md>. Useful inventory of Rust smells, but several entries are intentionally broad and require narrowing before promotion.
- `leonardomso/rust-skills`: <https://github.com/leonardomso/rust-skills>. Large Rust rule corpus useful for candidate discovery and taxonomy, not automatic policy.
- `wshobson/agents` `python-anti-patterns`: <https://github.com/wshobson/agents/blob/main/plugins/python-development/skills/python-anti-patterns/SKILL.md>, plus its error-handling, resource-management, and type-safety skills. Useful failure inventory; validate architectural prescriptions independently.
- JVM Skills listings such as Hibernate/JPA validation, jOOQ, Gradle, migration, and testing skills: mine domain-specific failure mechanisms against Hibernate, jOOQ, Gradle, Spring, OpenJDK, and vendor documentation.

## First-party starting points

- Rust: Clippy <https://rust-lang.github.io/rust-clippy/stable/>, the Rust documentation, Async Book, and Rust API Guidelines.
- Java: current Java API docs <https://docs.oracle.com/en/java/javase/> plus first-party framework documentation for Spring, Hibernate, Gradle, jOOQ, Quarkus, and other applicable stacks.
- Python: Python documentation <https://docs.python.org/3/> and PEPs <https://peps.python.org/>; use Ruff/type-checker rules as deterministic candidates when appropriate.
- Elixir: official Code-related <https://hexdocs.pm/elixir/code-anti-patterns.html> and Process-related <https://hexdocs.pm/elixir/process-anti-patterns.html> anti-pattern guides, language docs, and OTP/Erlang documentation.

When a community skill says “always” or “never”, actively search for the safe counterexample before making it an `eewo` rule.
