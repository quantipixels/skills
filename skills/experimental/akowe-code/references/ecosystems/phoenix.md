# Phoenix, LiveView, and Ecto-facing web code

Research baseline: Phoenix 1.8.12 at the 2026-08-27 cutoff; detect Phoenix, Plug, LiveView, Ecto, Elixir, and OTP versions independently.

- Keep router pipelines and Plug boundaries explicit; authentication/session/browser/API concerns should be composed deliberately rather than hidden in controllers.
- Keep controller actions thin around HTTP translation and application/context operations; use stable request/response/error contracts rather than leaking schemas/changesets unintentionally.
- Use Phoenix scopes/authorization context to make secure data access the default where the generated/application model supports it; recheck authorization at the owner of sensitive operations.
- Keep CSRF/session/cookie configuration aligned with browser credential behavior and deployment proxy/HTTPS settings.
- Use contexts as meaningful capability boundaries when they hide domain/data policy; do not create context functions that merely forward Repo calls without ownership value.
- Ecto transactions own local DB atomicity only. Keep remote side effects outside or use explicit durable coordination; bound query cardinality and preload/select intentionally to avoid hidden N+1 work.
- Channels/Sockets are process/resource boundaries. Bound channels per client/transport and message rates; Phoenix 1.8.9 introduced channel-count hardening after process-exhaustion vulnerabilities.
- PubSub delivers messages, not durable exactly-once workflows. Presence has distributed/eventual semantics; do not treat it as a transactional source of truth.
- LiveView state lives in a server process. Keep assigns minimal/derived where possible, use streams for large dynamic collections, and avoid storing heavy or secret data unnecessarily.
- Re-authorize LiveView events that mutate protected state; a connected socket does not make later client events trustworthy.
- Own background work outside the LiveView process when it can outlive/disrupt the view; use supervised Tasks/workers and explicit message/result handling.
- Keep components focused on rendering/local interaction contracts; avoid hidden database/network effects inside function components.
- Test controllers/LiveView/events/authorization through Phoenix/LiveView test APIs and use SQL Sandbox/Ecto ownership correctly for concurrent tests.
- Use Telemetry and query/log evidence to find hot paths; bound metric labels and avoid logging tokens/passwords/sensitive params.
- Keep runtime endpoint/config/release settings environment-owned; coordinate migrations and clustered startup/shutdown explicitly.

Primary sources:

- Phoenix changelog: <https://phoenix.hexdocs.pm/changelog.html>
- Phoenix guides: <https://hexdocs.pm/phoenix/overview.html>
- LiveView guide: <https://hexdocs.pm/phoenix_live_view/>
- Ecto docs: <https://hexdocs.pm/ecto/>
