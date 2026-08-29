# Historical research: Akọ̀wé catalogue consolidation experiment

Date: 2026-08-27
Status: Superseded by `docs/adr/20260827-adopt-adaptive-akowe-companion.md`

This document preserves the research behind the intermediate, unreleased `akowe-code` catalogue design. It is historical evidence only; the published Experimental identifier is `akowe`, and the runtime skill no longer loads the catalogue described below.

## Result at the time

The code-craft catalogue experiment was initially expressed as one task-scoped companion outcome with deep progressively disclosed internal references plus bounded current primary-source lookup. This reduced public skill proliferation and large default runtime context while retaining an embedded corpus.

```text
intermediate public ownership
→ one explicit Experimental akowe-code skill

knowledge depth
→ mechanism-level categories loaded only when the exact candidate needs them
```

Java/Spring deep categories were preserved from their former public skills. Kotlin, Ktor, Elixir, and Phoenix also used small ecosystem indexes backed by mechanism-level category trees. No runtime search/selector engine was required for this progressive disclosure.

## First-party baselines at the cutoff

- Java guidance remained baseline-aware across Java 17–26; project `--release`/runtime/consumer constraints were authoritative.
- Kotlin 2.4 / 2.4.10: <https://kotlinlang.org/docs/releases.html>.
- Ktor 3.5.2: <https://ktor.io/docs/releases.html>.
- Elixir 1.20 required Erlang/OTP 27+ and was compatible with OTP 29: <https://elixir.hexdocs.pm/changelog.html>.
- Phoenix 1.8.12 was the current changelog line; Phoenix 1.8.9 added channel-count hardening against per-client process exhaustion: <https://phoenix.hexdocs.pm/changelog.html>.
- Spring Framework documentation listed stable 7.0.9 and 6.2.19 lines; repository-managed Spring/Boot generations remained authoritative.

## Durable versus volatile knowledge considered

The experiment proposed keeping language/runtime ownership, failure, cancellation, state, type, resource, interoperability, framework lifecycle, known-bad, complexity, proof, examples, and exception guidance locally.

It proposed resolving newer APIs, changed compatibility matrices, security/default changes, unfamiliar libraries, and version-specific integration details at task time.

## Retrieval boundary used by the experiment

```text
exact candidate
→ establish stack from repository/native-tool evidence
→ open one ecosystem index
→ open only touched mechanism categories
→ use only applicable rule headings
→ bounded primary-source lookup for remaining material gaps
```

The model still owned candidate understanding, materiality, exceptions, recommendation, and final Code Craft Brief synthesis.

## Category shape used by the experiment

- Java — 21 retained mechanism categories.
- Spring — 18 retained mechanism categories.
- Kotlin — baseline/types; coroutines/lifecycle; Flow/state; JVM interop/ABI; multiplatform/testing.
- Ktor — server lifecycle/plugins; routing/HTTP/errors; auth/security; client/resilience; streaming/concurrency/testing.
- Elixir/OTP — language/data/failure; processes/GenServer/state; supervision/Tasks/failure; concurrency/resources; configuration/contracts/testing.
- Phoenix — routing/controllers/contexts; Ecto/data; security/auth; Channels/PubSub/Presence; LiveView/background work; testing/observability/runtime.

These counts were not quotas.

## Why it was superseded

The later experiment showed that Akọ̀wé's useful invariant is adaptive synthesis, not possession of this internal corpus. Relevant installed skills, exact repository/runtime evidence, and current owning sources provide a more extensible expertise boundary. The category trees and their runtime maintenance policy were therefore removed before release.
