# Elixir configuration, contracts, diagnostics, and testing

Use for release configuration, behaviours/protocols, specs/static evidence, and concurrent proof.

<a id="ex-ops-config"></a>
## `ex-ops-config` — Separate compile-time and runtime configuration

In releases, environment-owned secrets/endpoints/runtime sizing belong to runtime configuration. Do not bake deployment-specific values into compile-time config without a deliberate reason.

<a id="ex-ops-behaviour"></a>
## `ex-ops-behaviour` — Use behaviours/protocols for real polymorphic contracts

Introduce them when multiple implementations or callback contracts are meaningful. Avoid one-implementation abstractions that add indirection without substitutability or ownership value.

<a id="ex-ops-specs"></a>
## `ex-ops-specs` — Treat typespecs/static diagnostics as evidence, not runtime validation

Use compiler/type-system diagnostics and Dialyzer where they add signal, but validate untrusted runtime data independently.

<a id="ex-ops-test-sync"></a>
## `ex-ops-test-sync` — Test concurrent behavior with deterministic synchronization

Assert messages, monitored exits, state/result transitions, and supervision behavior rather than sleeps or arbitrary wall-clock delays.

<a id="ex-ops-observe"></a>
## `ex-ops-observe` — Observe owning process/resource boundaries

Expose bounded telemetry/logging around queue/mailbox pressure, external calls, restart/failure paths, and resource saturation without high-cardinality labels or secret payloads.

## Sources

- Config: <https://hexdocs.pm/elixir/Config.html>
- Typespecs: <https://hexdocs.pm/elixir/typespecs.html>
- ExUnit: <https://hexdocs.pm/ex_unit/ExUnit.html>
