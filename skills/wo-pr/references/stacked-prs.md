# Stacked PRs

Read when the requested PR depends on another open layer or the user requests a whole stack. Use current provider stack metadata or exact open head/base relationships, never branch names alone. Incomplete topology is a gap; observe only enough surrounding context to establish dependencies and safe next work.

One requested PR grants no mutation authority over its ancestors or descendants. An explicit whole-stack request includes its open layers, subject to the same operation limits. Do not run competing loops on interdependent layers.

Work bottom-up on the lowest requested layer needing action whose ancestors are stable. Hold descendants while an ancestor has a source-changing blocker. An ancestor can be ready and still open; do not require or perform its merge to advance. When every layer is ready, refresh the stack once and finish rather than restarting on the lowest layer.

After a layer changes, invalidate only dependent evidence in the affected descendant suffix. Current head **and base commit** determine whether prior checks, conflicts, or review conclusions still apply; preserve independent proof.

Once the changed layer and its lower ancestors are stable, reconcile the affected suffix once, in order, before reviewing descendants. Read back provider-driven synchronization if it occurred. Otherwise hand off the ordered suffix, expected parent relationships, old/new base commits, scoped changes to preserve, and known conflicts to an authorized reconciliation path. Babysitting alone does not authorize rebase, force-push, retargeting, or stack restructuring. Do not simulate reconciliation with repeated per-layer fix/review cycles.

Re-read affected heads, bases, and relationships after reconciliation. Readiness for the stack requires every open requested layer to meet the main skill's readiness conditions under the refreshed topology. Report the blocking ancestor or outstanding reconciliation when that prevents progress; no separate stack-state vocabulary is required.
