# Research: consolidate expert coding guidance behind Akọ̀wé Code

Date: 2026-08-27

## Result

The Java/Spring catalogue experiment is better expressed as one task-scoped coding-companion outcome with compact internal ecosystem packs plus bounded current primary-source lookup. This preserves useful research while avoiding public skill proliferation and large default runtime context.

## Current first-party baselines at the cutoff

- Java guidance remains baseline-aware across Java 17–26; project `--release`/runtime/consumer constraints are authoritative.
- Kotlin's current release line is 2.4 and 2.4.10 is the latest bug-fix release: <https://kotlinlang.org/docs/releases.html>.
- Ktor 3.5.2 is the current documented release: <https://ktor.io/docs/releases.html>.
- Elixir 1.20 requires Erlang/OTP 27+ and is compatible with OTP 29: <https://elixir.hexdocs.pm/changelog.html>.
- Phoenix 1.8.12 is the current changelog line; Phoenix 1.8.9 added channel-count hardening against per-client process exhaustion: <https://phoenix.hexdocs.pm/changelog.html>.
- Spring Framework documentation lists stable 7.0.9 and 6.2.19 lines. Spring Framework 7.0 supports Kotlin 2.2+ and documents first-class Kotlin support: <https://docs.spring.io/spring-framework/reference/languages/kotlin.html>.

## Durable versus volatile knowledge

Keep durable locally:

- language/runtime ownership, failure, cancellation, state, type, resource, and interoperability mechanisms;
- framework proxy/container/transaction/request/process lifecycle semantics;
- known-bad patterns with stable failure mechanisms;
- complexity/proof interpretation principles.

Resolve at task time:

- newer/EAP/preview APIs;
- changed compatibility matrices;
- security fixes/default changes;
- unfamiliar libraries/frameworks;
- version-specific integration details whose answer can change the implementation.

## Research boundary

One/few task-local facts use bounded owning-source lookup and are cited in the Code Craft Brief. Multi-source/reusable/auditable research uses `iwadi`. Neither path changes published packs automatically.

## Source heritage

The compact Java and Spring packs were distilled from:

- `docs/akowe-java-research-2026-08-26.md`;
- `docs/akowe-spring-research-2026-08-26.md`;
- primary Java/OpenJDK/Spring/Hibernate/Jakarta documentation;
- earlier community-corpus discovery used only for candidate/counterexample generation.

Kotlin/Ktor/Elixir/Phoenix packs use their owning first-party documentation as controlling evidence. Community conventions do not override repository or owning-project contracts.
