# Ktor authentication and security boundaries

Use when the candidate changes authentication, authorization, sessions/cookies, CSRF/CORS, rate limits, or sensitive request handling.

<a id="ktor-sec-auth-boundary"></a>
## `ktor-sec-auth-boundary` — Authenticate at the transport boundary, authorize at the sensitive owner

Authentication plugins establish identity for the request; sensitive operations should still enforce authorization at the narrowest adapter-independent owner when multiple paths can reach them.

<a id="ktor-sec-session-cookie"></a>
## `ktor-sec-session-cookie` — Align session/cookie policy with deployment reality

Set cookie scope, secure/same-site behavior, signing/encryption, proxy/HTTPS assumptions, and session lifetime deliberately. Do not rely on development defaults for production trust boundaries.

<a id="ktor-sec-csrf-cors"></a>
## `ktor-sec-csrf-cors` — Match CSRF and CORS to the actual credential model

Browser credential semantics determine CSRF exposure. Keep CORS centralized and specific; CORS is not an authorization mechanism.

<a id="ktor-sec-bounds"></a>
## `ktor-sec-bounds` — Bound attacker-controlled work

Apply explicit limits to bodies, multipart parts, decompression, WebSocket/session count, message rate, expensive validation, and authentication work where one client can amplify resource use.

<a id="ktor-sec-redaction"></a>
## `ktor-sec-redaction` — Keep secrets and request bodies out of default diagnostics

Redact tokens, cookies, credentials, and sensitive payloads. Log enough identity/correlation context to diagnose failures without reproducing private data.

## Sources

- Ktor authentication: <https://ktor.io/docs/server-auth.html>
- Ktor sessions: <https://ktor.io/docs/server-sessions.html>
- Ktor CORS: <https://ktor.io/docs/server-cors.html>
