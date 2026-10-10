# Maintain, drive and recover

## Maintain

Limit edits to the selected verification skill, its map and helpers. Compare expectations with accepted behavior as well as implementation; source alone cannot establish that a changed behavior is intended.

1. Reconcile the README index with feature files and current public entry points. Require concrete source evidence before adding a missing feature or retiring a path.
2. Use delegated read-only readers to inspect separate feature slices. Each brief names the feature, source scope and required return: current behavior and entry points with citations, suspected drift, and a concrete live recipe. Readers neither edit nor drive the product. Account for every required slice; if the host cannot delegate, inspect the same slices directly.
3. Reconcile the findings and combine compatible setup states. One coordinator owns the live browser, device or service. Drive every mapped feature, including its listed entry points and sub-features; report a blocked path separately rather than substitute another entry point for it.
4. Classify every discrepancy before changing it:

   - **Instruction drift:** accepted behavior works, but a recipe, prerequisite or expectation is wrong. Correct the recipe from evidence.
   - **Harness gap:** accepted behavior works, but the driver cannot reach or observe it. Repair the owned harness within scope.
   - **Product regression:** actual behavior violates the accepted contract. Report it to the caller; preserve the expectation and keep product changes out of this pass.

Re-drive corrections before calling them verified. Unsettled intent or reachability stays blocked with the attempted path and missing prerequisite. Continue independent coverage; missing results, skips and regressions are not passes.

## Drive and recover

Drive browsers and devices/simulators with the host's tools, using current tool documentation and snapshot handles; otherwise use the project driver or a suitable browser tool. Preserve device launcher/configuration/session details.

Run Doctor before first drive, on fresh sessions and after surprises. A healthy process may hold a stuck UI: reset or relaunch owned state to a known baseline. Remove failed-attempt residue and preserve proof. Missing access, intent or safe reset is a named boundary; retry only with new evidence.

Exercise public user paths rather than internal setters or verification-only endpoints. Inspect material side effects through a second view where possible. An isolated external substitute leaves that external boundary unproven; say so. Before relying on a dry-run, establish what it actually omits. Keep evidence usable without leaking credentials or private data.

