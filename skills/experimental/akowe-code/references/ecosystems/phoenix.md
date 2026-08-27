# Phoenix, LiveView, and Ecto-facing web code

Research baseline: Phoenix 1.8.12 at the 2026-08-27 cutoff. Detect Phoenix, Plug, LiveView, Ecto, Elixir, and OTP versions independently.

Load only categories controlling the touched mechanism:

| Category | Use for |
| --- | --- |
| [Routing, controllers, and contexts](../phoenix/routing-controllers-contexts.md) | pipelines, HTTP translation, public models, context boundaries, scoped access |
| [Ecto transactions and data](../phoenix/ecto-transactions-data.md) | local atomicity, remote effects, query shape, changesets, concurrency |
| [Security and authentication](../phoenix/security-auth.md) | identity, authorization, browser/session/CSRF, untrusted events, redaction |
| [Channels, PubSub, and Presence](../phoenix/channels-pubsub-presence.md) | channel/resource bounds, event protocols, ephemeral fan-out, presence, reconnects |
| [LiveView and background work](../phoenix/liveview-background.md) | assigns, streams, events, supervised work, component boundaries |
| [Testing, observability, and runtime](../phoenix/testing-observability-runtime.md) | Phoenix/LiveView proof, SQL Sandbox, telemetry, runtime config, migrations/readiness |

Elixir/OTP guidance remains underneath Phoenix. Phoenix may specialize web/process/data lifecycle behavior but must not weaken process ownership, supervision, resource bounds, or caller/security contracts.

Primary sources: <https://phoenix.hexdocs.pm/changelog.html>, <https://hexdocs.pm/phoenix/overview.html>, <https://hexdocs.pm/phoenix_live_view/>, <https://hexdocs.pm/ecto/>.
