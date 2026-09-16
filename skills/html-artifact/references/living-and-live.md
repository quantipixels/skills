# Living reports and live views

Distinguish:

- **Living report** — its owner updates meaning at material milestones.
- **Live preview** — a development host refreshes changed files; this proves neither source freshness nor ongoing work.
- **Live data view** — an active service delivers new source data; name producer, update mechanism and freshness bound.

A clock, spinner or “live” badge proves none of these. Use ordinary revision updates for milestone reporting and an existing preview when available. A requested live view may reuse an established transport; a new service remains with its implementation/deployment owner. Do not start a daemon or add monitoring merely because a report is living.

Show source revision, last successful data update and connection state separately. Preserve a visibly stale last-good view on failure. Recover a coherent snapshot or resume from an acknowledged sequence; ignore duplicates/older revisions and never mix summary/detail from different cuts.

Preserve stable targets, scroll, focus, open details and unsent feedback through updates. Reconcile feedback against its authored revision. Treat incoming values as data, constrain fragment updates to the accepted trust boundary, send only authorized fields, and freeze a readable final snapshot when work ends.

A live-data claim requires observing a real producer update. Test disconnection/recovery, ordering where material, and preservation of active reading/feedback. If the host cannot sustain the producer or refresh the open artifact, state the limit and deliver the last verified snapshot.
