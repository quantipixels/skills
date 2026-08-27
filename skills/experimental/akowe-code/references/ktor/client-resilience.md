# Ktor client, resilience, and resource ownership

Use when code creates/configures `HttpClient`, remote calls, deadlines, retries, or protocol failure mapping.

<a id="ktor-client-lifecycle"></a>
## `ktor-client-lifecycle` — Reuse an owned client

Create clients at a lifecycle boundary that can reuse connections/engine resources and close them deterministically. Per-call clients are appropriate only for truly short-lived isolated tooling/tests.

<a id="ktor-client-timeouts"></a>
## `ktor-client-timeouts` — Set finite deadlines at the correct layer

Configure connect/request/socket/pool limits as supported by the selected engine and caller budget. A coroutine timeout alone may not configure every underlying network timeout.

<a id="ktor-client-failures"></a>
## `ktor-client-failures` — Classify transport, protocol, and domain failures

Separate network/timeout/TLS failures from HTTP status responses and application-level rejection. Map them into the caller's stable failure contract once.

<a id="ktor-client-retry"></a>
## `ktor-client-retry` — Give retries one owner

Retry only bounded, classified, idempotent/replay-safe operations within the caller's latency/cancellation budget. Avoid nested retry layers between client, service, queue, and infrastructure.

<a id="ktor-client-config"></a>
## `ktor-client-config` — Share stable configuration without hiding call-specific policy

Centralize engine, serialization, auth, telemetry, and base transport configuration; keep endpoint-specific deadlines, idempotency, request bodies, and error handling visible where they vary.

## Sources

- Ktor client: <https://ktor.io/docs/client-create-new-application.html>
- Client timeouts: <https://ktor.io/docs/client-timeout.html>
- HttpRequestRetry: <https://ktor.io/docs/client-request-retry.html>
