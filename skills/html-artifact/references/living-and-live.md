# Living reports and live views

Use when an artifact is maintained through work or receives updates while open. These are different contracts:

- **Living report:** the owner updates its meaning at material milestones; the HTML reflects that revision. For an HTML initiative plan, update the same file without an equivalent Markdown companion. Reopening or refreshing may be needed.
- **Live preview:** the development host refreshes the rendered page when its file changes. This proves neither source freshness nor ongoing agent execution.
- **Live data view:** an active service delivers new source data to an open page. Name the producer, update mechanism and freshness bound.

Retain [source composition](source-composition.md)'s stable identity and delta-first view. A clock, spinner or “live” badge is not evidence of connection, new work or freshness.

## Choose the smallest useful update mechanism

Use ordinary revision updates for milestone-level reporting. Reuse an existing preview's refresh capability when available. For a requested service-backed view, use the project's existing transport; bounded periodic refresh can suit slow changes, server-sent events suit one-way updates, and WebSockets earn their cost when bidirectional exchange is required. Reading an adjacent file through `file://` is not a portable live-update mechanism.

Native `EventSource` can serve a small one-way view. Existing htmx or Datastar can apply scoped HTML updates without introducing a React application. Consult current selected-version documentation rather than copying setup from another major version. A streaming library still needs a running producer and does not make a static artifact self-updating. Use the implementation/deployment owner's supported setup path for any new service. Do not start a daemon, publish a server or add monitoring merely because a report is living.

Useful technical entry points: [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events), [htmx SSE](https://htmx.org/extensions/sse/), [Datastar element patches](https://data-star.dev/reference/sse_events).

## Preserve the reader and evidence cut

Show source revision and last successful data update separately from connection state. Keep the last good view on failure, visibly stale; never replace it with empty success. Reconnection does not prove missed updates were recovered: resume from an acknowledged sequence when supported, otherwise obtain a coherent snapshot. Ignore duplicate/older revisions and avoid mixed-revision summaries and details.

Patch the affected region while preserving stable targets, scroll, focus, open details and unsent feedback. Offer “updates available” or pause/resume when automatic replacement would disrupt active reading or editing. Reconcile feedback against the revision it was authored on. Announce concise material changes politely, not every streamed event or the whole document.

Treat incoming values as data. Render trusted, validated templates rather than arbitrary source HTML; constrain any fragment-patching capability to the accepted trust boundary. Send only authorized fields—some reactive libraries transmit local state by default. Keep credentials and private traces out of exported snapshots. Freeze a labelled, readable final snapshot when work ends; stop connections when no longer needed.

## Prove the claimed liveness

For a live-data claim, observe a real producer update reaching the page. Exercise disconnection and recovery, duplicate/out-of-order handling where applicable, and preservation of active reading/feedback. A scripted animation or local button is a simulation, not live-service verification. If the host cannot keep the producer running or refresh an already-open artifact, state that limitation and deliver the last verified snapshot.
