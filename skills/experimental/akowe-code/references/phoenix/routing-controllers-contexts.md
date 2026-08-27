# Phoenix routing, controllers, and contexts

**Research baseline:** Phoenix 1.8.12 at the 2026-08-27 cutoff. Detect Phoenix/Plug/LiveView/Ecto/Elixir/OTP versions independently.

<a id="phx-web-pipelines"></a>
## `phx-web-pipelines` — Keep router pipelines semantically explicit

Compose browser/API/auth/session concerns deliberately. Avoid broad plugs whose hidden behavior applies to unrelated routes or duplicates another boundary.

<a id="phx-web-controller"></a>
## `phx-web-controller` — Keep controllers focused on HTTP translation

Parse/validate transport input, call the owning application/context operation, and translate the result. Avoid embedding domain/data workflows in controller actions.

<a id="phx-web-contract"></a>
## `phx-web-contract` — Keep public transport models stable

Do not leak internal schemas/changesets merely because they are convenient. Own request/response/error semantics separately when wire compatibility or redaction differs.

<a id="phx-web-context"></a>
## `phx-web-context` — Use contexts where they hide meaningful capability or data policy

A context should offer a coherent capability boundary. Avoid pass-through context functions that merely mirror `Repo` with no policy, coordination, or stable public value.

<a id="phx-web-scope"></a>
## `phx-web-scope` — Carry authorization scope explicitly where the application model uses it

When generated/application patterns support scoped access, keep actor/tenant/authorization context visible through data operations rather than recovering it implicitly from process/global state.

## Sources

- Phoenix routing/controllers/contexts: <https://hexdocs.pm/phoenix/overview.html>
- Plug: <https://hexdocs.pm/plug/readme.html>
