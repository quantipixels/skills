# Phoenix LiveView, components, and background work

Use when the candidate changes LiveView assigns/events/streams/components/uploads/async or work that may outlive a view.

<a id="phx-lv-assigns"></a>
## `phx-lv-assigns` — Keep LiveView state minimal and intentional

Store only state the server process needs across events/renders. Derive values when cheap and avoid retaining large collections, duplicated data, or secrets unnecessarily.

<a id="phx-lv-streams"></a>
## `phx-lv-streams` — Use streams for large dynamic collections when their semantics fit

Streams can reduce retained state and render churn, but do not force them onto small static collections or when ordering/identity operations need a different model.

<a id="phx-lv-events"></a>
## `phx-lv-events` — Treat every client event as a fresh untrusted request

Validate event payloads and re-check authorization/invariants at the operation owner. The rendered DOM and connected socket do not make later input trustworthy.

<a id="phx-lv-background"></a>
## `phx-lv-background` — Move durable/long work to a supervised owner

Work that can outlive navigation/disconnect or block the LiveView process belongs in supervised Tasks/workers with explicit result/message handling and idempotency where needed.

<a id="phx-lv-components"></a>
## `phx-lv-components` — Keep components focused on rendering/local interaction contracts

Function/live components should not hide unrelated database/network side effects. Keep data fetching/mutations with the capability owner unless component lifecycle genuinely owns them.

## Sources

- Phoenix LiveView: <https://hexdocs.pm/phoenix_live_view/>
- LiveView streams: <https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.html>
- LiveView components: <https://hexdocs.pm/phoenix_live_view/Phoenix.Component.html>
