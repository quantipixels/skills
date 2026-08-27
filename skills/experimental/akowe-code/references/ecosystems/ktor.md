# Ktor

Research baseline: Ktor 3.5.2 at the 2026-08-27 cutoff. Detect the project's exact Ktor/Kotlin version and server/client engine before version-sensitive guidance.

Load only categories controlling the touched mechanism:

| Category | Use for |
| --- | --- |
| [Server lifecycle and plugins](../ktor/server-lifecycle-plugins.md) | plugin scope/order, engine boundary, startup/drain/shutdown |
| [Routing, HTTP contracts, and errors](../ktor/routing-http-errors.md) | routes, DTOs, validation, StatusPages, serialization/content negotiation |
| [Authentication and security](../ktor/auth-security.md) | authn/authz, sessions/cookies, CSRF/CORS, resource bounds, redaction |
| [Client, resilience, and resources](../ktor/client-resilience.md) | HttpClient ownership, timeouts, failures, retries, shared config |
| [Streaming, concurrency, and testing](../ktor/streaming-concurrency-testing.md) | request cancellation, uploads/WebSockets/SSE, background work, Ktor proof |

Kotlin coroutine/type guidance remains underneath Ktor. Ktor may specialize request/plugin/client lifecycle behavior but must not weaken structured concurrency, cancellation, resource bounds, or caller contracts.

Primary sources: <https://ktor.io/docs/releases.html>, <https://ktor.io/docs/server-create-and-configure.topic>, <https://ktor.io/docs/client-create-new-application.html>.
