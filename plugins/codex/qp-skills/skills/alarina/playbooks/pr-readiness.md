# PR readiness

Use when an existing PR or MR needs status, description, publication, feedback handling, or work toward provider readiness. Approval and merge remain human decisions.

1. Choose [seda-pr-description](../commands/seda-pr-description.md) for description, [seda-pr](../commands/seda-pr.md) for publication, or [wo-pr](../commands/wo-pr.md) for status/stewardship. Give it the exact item or candidate, requested operation, known head/base, evidence, and authority. A status-only request remains read-only, including the body.
2. For description work, return or update the reviewer brief at that stopping point. Before publication, consume [local readiness](../references/atunwo/local-readiness.md) for the final candidate; reuse sufficient review and checks. Then commit and push only the scoped authorized work and read back the provider state.
3. For stewardship, let [wo-pr](../commands/wo-pr.md) establish checks, conflicts, feedback, and current discussions. Route supported code fixes to [alaga-deliver](../commands/alaga-deliver.md) and material contested claims to [atunwo](../commands/atunwo.md), then return evidence to the same item.
4. Recheck the current head and provider state after changes. A prior-head result, green CI alone, or unresolved published feedback cannot establish readiness.

Finish with the current item URL or draft text, readiness state, decisive evidence, material risk, and blocker or next action. Stop before approval or merge.
