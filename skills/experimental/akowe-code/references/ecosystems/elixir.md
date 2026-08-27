# Elixir and OTP

Research baseline: Elixir 1.20 requires Erlang/OTP 27+ and is compatible with OTP 29 at the 2026-08-27 cutoff. Treat Elixir and OTP as one runtime baseline.

Load only categories controlling the touched mechanism:

| Category | Use for |
| --- | --- |
| [Language, data, and failure](../elixir/language-data-failure.md) | patterns/guards, tagged results, pipelines, binaries/atoms, Enum/Stream |
| [Processes, GenServer, and state](../elixir/processes-genserver-state.md) | process ownership, callbacks, messages, state, call/cast semantics |
| [Supervision, Tasks, and failure](../elixir/supervision-tasks-failure.md) | restart strategy, retry storms, Tasks, Task.Supervisor, timeout semantics |
| [Concurrency and resources](../elixir/concurrency-resources.md) | cardinality, mailboxes, Registry, ETS, external resource ownership |
| [Configuration, contracts, and testing](../elixir/config-contracts-testing.md) | runtime config, behaviours/protocols, specs/static evidence, ExUnit/telemetry |

Phoenix may specialize HTTP/process/data lifecycle rules, but generic OTP process, supervision, failure, and resource ownership remain controlling unless the framework contract explicitly changes the mechanism.

Primary sources: <https://elixir.hexdocs.pm/changelog.html>, <https://hexdocs.pm/elixir/code-anti-patterns.html>, <https://www.erlang.org/doc/system/design_principles.html>.
