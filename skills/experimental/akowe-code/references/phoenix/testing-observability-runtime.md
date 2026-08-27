# Phoenix testing, observability, and runtime operations

Use when proof depends on Phoenix/LiveView/Ecto concurrency, telemetry, endpoint/release configuration, migrations, or clustered runtime behavior.

<a id="phx-ops-test-web"></a>
## `phx-ops-test-web` — Use Phoenix/LiveView test APIs at the semantic seam

Test controller/connection/LiveView event/render/redirect behavior through the framework test APIs rather than coupling to incidental implementation details.

<a id="phx-ops-sandbox"></a>
## `phx-ops-sandbox` — Respect Ecto SQL Sandbox ownership in concurrent tests

When tests spawn Tasks/processes/LiveViews that touch the DB, configure ownership/shared allowances according to the real process topology instead of masking failures with sleeps.

<a id="phx-ops-telemetry"></a>
## `phx-ops-telemetry` — Use telemetry/query evidence to diagnose hot paths

Measure request/event/query latency, N+1 behavior, mailbox/resource pressure, and failure paths with bounded dimensions. Avoid high-cardinality labels or sensitive payloads.

<a id="phx-ops-runtime-config"></a>
## `phx-ops-runtime-config` — Keep endpoint/release/deployment settings environment-owned

Runtime host/URL/proxy/secret/database/pool/cluster settings belong to the deployment/release boundary, not hard-coded application modules.

<a id="phx-ops-migrations"></a>
## `phx-ops-migrations` — Give production migrations and readiness one owner

Coordinate migrations before dependent traffic, make multi-instance execution safe, and expose readiness only after required initialization. Own graceful shutdown for sockets/background work.

## Sources

- Phoenix testing: <https://hexdocs.pm/phoenix/testing.html>
- Phoenix Telemetry: <https://hexdocs.pm/phoenix/telemetry.html>
- Ecto SQL Sandbox: <https://hexdocs.pm/ecto_sql/Ecto.Adapters.SQL.Sandbox.html>
