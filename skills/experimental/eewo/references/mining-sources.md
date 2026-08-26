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

- `https://jvmskills.com/` — strong JVM discovery index, especially for focused Java/Kotlin/Spring/Gradle/database/testing skills. Treat listing trust and author metadata as discovery evidence, then inspect the source repository and primary framework documentation.
- `https://skills.sh/` — broad public Agent Skills index useful for finding existing anti-pattern, language, testing, security, and workflow skills. Do not treat popularity or install count as correctness.

The JVM Skills jOOQ knowledge-builder is also a useful process reference: it processes newer material first, deduplicates older entries, explicitly records supersession, and logs unresolved uncertainty rather than guessing. Preserve those ideas, not its jOOQ-specific storage implementation.

## Useful community corpora to mine

- `actionbook/rust-skills`, especially `m15-anti-pattern`: useful inventory of Rust smells, but several entries are intentionally broad and require narrowing before promotion.
- `leonardomso/rust-skills`: large Rust rule corpus useful for candidate discovery and taxonomy, not automatic policy.
- `wshobson/agents` `python-anti-patterns`, `python-error-handling`, `python-resource-management`, and `python-type-safety`: useful Python failure inventory; validate architectural prescriptions independently.
- JVM Skills listings such as Hibernate/JPA validation, jOOQ, Gradle, migration, and testing skills: mine domain-specific failure mechanisms against Hibernate, jOOQ, Gradle, Spring, OpenJDK, and vendor documentation.

## First-party starting points

- Rust: Clippy, the Rust Reference/Book, Async Book, and Rust API Guidelines.
- Java: current OpenJDK/Oracle Java API docs plus first-party framework documentation for Spring, Hibernate, Gradle, jOOQ, Quarkus, and other applicable stacks.
- Python: Python documentation and PEPs; use Ruff/type-checker rules as deterministic candidates when appropriate.
- Elixir: official Code-related and Process-related anti-pattern guides, language docs, and OTP/Erlang documentation.

When a community skill says “always” or “never”, actively search for the safe counterexample before making it an `eewo` rule.
