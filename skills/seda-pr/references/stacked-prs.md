# Stacked PRs

Use current provider metadata or exact head/base relationships to establish dependencies; branch names alone are insufficient. One PR request does not authorize changes to adjacent layers; a whole-stack request covers its open layers under the same operation limits.

Work bottom-up through requested layers with stable ancestors. An ancestor may be ready while still open; merging it is not a prerequisite. Hold descendants while an ancestor has a source-changing blocker, and avoid competing loops on dependent layers.

After a layer changes, invalidate only dependent evidence. Reconcile its affected descendants once, in order, before reviewing them; preserve independent proof. Babysitting does not authorize rebase, force-push, retargeting, or stack restructuring. Use existing reconciliation authority or report the required action.

Refresh affected heads, bases and relationships after reconciliation. Finish when every requested layer meets the main skill's readiness conditions; otherwise identify the blocking ancestor or reconciliation. Do not restart completed layers or simulate reconciliation with repeated fix/review cycles.
