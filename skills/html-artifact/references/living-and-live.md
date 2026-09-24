# Living and live views

A living report is updated by its author. A live preview refreshes files through a development host. A live data view receives new source data from an active producer. Only the last requires a data connection; a clock or spinner proves none of these.

Use ordinary revision updates for milestones and reuse an existing preview. For explicitly requested live data, name producer, transport and freshness bound; use the project's supported mechanism. Do not create a daemon, deployment or monitoring system merely because a report is living.

Show source revision and last successful data update separately from connection state. Preserve the last good view as visibly stale on failure. Reconnection must recover missed updates through a supported sequence or coherent snapshot; reject duplicate/older revisions and mixed-revision summaries.

Preserve scroll, focus, open details and requested unsent feedback. Offer pause or an update notice when replacement would disrupt reading. Bind feedback to its authored revision. Announce material changes without narrating every event.

Treat incoming values as data. Constrain fragment updates to trusted templates and send only authorized fields; reactive tooling may transmit local state. Keep secrets out of exported snapshots. Freeze a labelled final snapshot and stop connections when finished.

Prove a live-data claim by observing a real producer update, disconnection/recovery and relevant ordering and reading-state behavior. Animation is not live evidence. If the host cannot sustain updates, state the limit and deliver the last verified snapshot.
