# Ktor

Research baseline: Ktor 3.5.2 at the 2026-08-27 cutoff. Detect the project's exact Ktor/Kotlin version and server/client engine before applying version-sensitive APIs.

- Treat Application/plugin lifecycle as ownership: install/configure a plugin once at the narrowest application/route scope that needs it and understand pipeline ordering.
- Keep routing explicit and non-overlapping; make HTTP method, status, headers, content negotiation, and error semantics part of the contract.
- Keep request/response transport models separate from persistence/internal models when their lifecycle or compatibility differs.
- Validate external input at the boundary and map failures through one owned StatusPages/error contract rather than scattered catches.
- Configure authentication/authorization at the appropriate pipeline boundary; keep sessions/cookies/CSRF/CORS/rate limits aligned with the actual client/authentication model.
- Bound request bodies, multipart uploads, WebSockets, SSE sessions, channels, and per-client work; client/process cheapness does not remove resource limits.
- Match engine choice to deployment constraints; configure shutdown/drain and avoid engine-specific assumptions leaking through application code.
- Reuse one configured `HttpClient` per lifecycle/remote contract rather than constructing a client per call. Own the engine and close it at the correct lifecycle boundary.
- Set connect/request/socket/pool deadlines as supported by the engine and classify response/protocol/transport failures before retrying.
- Retry only bounded, classified, idempotent operations with caller budget and cancellation. Avoid nested retry owners.
- Preserve coroutine structured concurrency and request cancellation; do not launch detached work from handlers unless a separate application worker owns it.
- Test routing/plugins/auth/client behavior with Ktor's test facilities at the smallest useful boundary; use real external infrastructure only when its semantics matter.
- Keep metrics/logging/tracing dimensions bounded and avoid logging secrets or whole request bodies by default.

Primary sources:

- Ktor releases: <https://ktor.io/docs/releases.html>
- Ktor server docs: <https://ktor.io/docs/server-create-and-configure.topic>
- Ktor client docs: <https://ktor.io/docs/client-create-new-application.html>
