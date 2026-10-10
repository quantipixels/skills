# Living and live views

A living document is updated in its Markdown source and regenerated for a reader. A development preview may reload those files. A live data view receives new values from an active producer. Only the last needs a data connection; animation or a clock proves none of them.

Reuse the existing source and preview. Keep source revision separate from generation and last successful data update. Default generated documents are static, self-contained and offline; opening one does not start a watcher, daemon or service. A requested live view still starts with the QP template and plain JS; a framework needs the same capability and dependency justification as any other page.

For explicitly requested live data, name the producer, transport and freshness bound. Use the project's supported mechanism, preserve the last good view as visibly stale on failure, and recover through a coherent snapshot or supported sequence. Reject duplicate/older revisions and mixed-revision summaries.

Keep scroll, focus, open details and unsent feedback stable. Pause or offer an update notice when replacement would disrupt reading. Bind feedback to its source revision and announce material changes without narrating every event.

Treat incoming values as data in trusted templates; send only authorized fields. Keep secrets out of exports. Finish with a labelled offline snapshot and stop connections. For a document, retain the Markdown source and regenerate the shared HTML; for a custom editor, export the reader's choices as text.

Prove a live-data claim with a real producer update, disconnection/recovery and relevant ordering/reading-state checks. If the host cannot sustain updates, state that limit and deliver the last verified snapshot.
