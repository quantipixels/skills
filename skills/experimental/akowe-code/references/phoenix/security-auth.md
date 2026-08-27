# Phoenix security, authentication, and browser boundaries

Use when changing authenticated scopes, sessions/cookies, CSRF, authorization, credentials, or sensitive operations.

<a id="phx-sec-authn"></a>
## `phx-sec-authn` — Establish identity at the web boundary without making it the sole authorization owner

Plugs/socket connection establish actor identity/context; sensitive use cases should still enforce the current authorization rule where protected state changes are owned.

<a id="phx-sec-reauthorize"></a>
## `phx-sec-reauthorize` — Re-authorize sensitive operations when state may have changed

Long-lived sockets/LiveViews can outlast permissions or resource state. Do not assume connection-time authorization proves every later mutation.

<a id="phx-sec-csrf-session"></a>
## `phx-sec-csrf-session` — Align CSRF/session/cookie policy with browser credentials and deployment HTTPS

Keep secure/same-site/domain/path/proxy assumptions deliberate and preserve Phoenix protections unless the authentication model provides an explicit alternative.

<a id="phx-sec-input"></a>
## `phx-sec-input` — Treat client params/events as untrusted

Validate identifiers, ownership, allowed fields, cardinality, and operation semantics server-side. Client rendering/state cannot authorize an action.

<a id="phx-sec-redaction"></a>
## `phx-sec-redaction` — Redact credentials and sensitive parameters from logs/telemetry

Do not log tokens/passwords/session secrets or whole sensitive params. Keep diagnostics sufficient for correlation without reproducing private data.

## Sources

- Phoenix security guidance: <https://hexdocs.pm/phoenix/security.html>
- Plug session/CSRF: <https://hexdocs.pm/plug/Plug.Session.html>
- Phoenix authentication generators/guides: <https://hexdocs.pm/phoenix/mix_phx_gen_auth.html>
