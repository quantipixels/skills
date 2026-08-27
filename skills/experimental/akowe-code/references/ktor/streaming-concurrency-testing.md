# Ktor streaming, concurrency, and testing

Use for request streaming/uploads, WebSockets/SSE, channels, detached/background work, or Ktor-specific proof.

<a id="ktor-stream-cancellation"></a>
## `ktor-stream-cancellation` — Preserve request/session cancellation

Handler and stream work should stop when the request/session owner ends unless a durable application worker explicitly accepts handoff.

<a id="ktor-stream-bounds"></a>
## `ktor-stream-bounds` — Bound long-lived and streaming work

Set explicit limits for body size, multipart parts, WebSocket/SSE sessions, channels/buffers, message rate, concurrent fan-out, and per-client work.

<a id="ktor-stream-background"></a>
## `ktor-stream-background` — Hand durable work to an application owner

Do not launch important detached coroutines from handlers. Queue or start work under an application-owned supervisor/worker when it may outlive the request.

<a id="ktor-test-smallest"></a>
## `ktor-test-smallest` — Use Ktor test facilities at the smallest useful seam

Test routes/plugins/auth/content/error behavior with Ktor's application/client testing tools when those semantics are what matter. Avoid booting unrelated infrastructure.

<a id="ktor-test-real-boundary"></a>
## `ktor-test-real-boundary` — Use real infrastructure when external semantics control correctness

TLS/proxy/network engine/database/provider behavior needs integration proof only when the candidate depends on those exact semantics.

## Sources

- Ktor server testing: <https://ktor.io/docs/server-testing.html>
- WebSockets: <https://ktor.io/docs/server-websockets.html>
- Server requests/uploads: <https://ktor.io/docs/server-requests.html>
