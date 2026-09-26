# Rollout readiness

Use when a changeover, backfill or deployment can materially disrupt consumers, corrupt data or require recovery. Keep this section in the existing plan/runbook; it supplies operational acceptance, not a separate release workflow. [architect-design](../../../commands/architect-design.md) resolves consequential sequencing or reversibility choices; [alaga-deliver](../../../commands/alaga-deliver.md) or the applicable project specialist supplies executable checks and authorized execution evidence.

For each material invariant, establish the preflight observation, expected result or justified tolerance, and stop condition. Use actual queries, commands or observable signals from the project. Retain the baseline and candidate/environment identity needed for comparison. Compare compatible snapshots or account for legitimate intervening writes; unchanged row counts are not a universal invariant.

Order only the necessary changeover steps, with prerequisites and ownership. Include backfill progress, lock/resource bounds, supported old/new coexistence and restart points where they control safety. Reuse [alaga-deliver](../../../commands/alaga-deliver.md)'s populated-data audit and migration proof rather than specifying another test suite. An empty-database pass does not establish launch readiness.

Distinguish the available recovery actions:

- reverting code or disabling a feature;
- reversing a data transform without losing required information;
- restoring or repairing data, including how later legitimate writes survive; and
- irreversible effects needing reconciliation or an explicitly accepted recovery limit.

A rollback command or available backup alone does not prove recovery. Require a checkable recovery result and its material prerequisites. Surface an unresolved recovery choice before the dependent destructive step.

Specify post-change observations that can detect the actual failure: mapping distributions, missing relationships, errors, latency or consumer results as relevant. Name the observation window, responsible owner and action on breach only when ongoing monitoring is needed. Derive thresholds and timing from the contract and operating evidence; do not invent defaults or promise monitoring the host cannot sustain.

For package releases, pin the version and artifact being published, relevant consumer/runtime compatibility and the project's publication process. Verify an actual consumer can resolve and use that version from the intended destination. For services, observe the deployed candidate through the affected user boundary. On a partial release, establish which artifacts or environments changed before resuming; version immutability and irreversible effects constrain recovery. An upload receipt or locally installed package does not establish consumer acceptance of the published version.

Return readiness from current evidence: checks satisfied, a material stop condition, or the exact missing observation/decision. Proposed commands remain proposed until executed. Planning readiness, deployed state and live acceptance are distinct. Publication or review readiness does not authorize deployment, and this method does not replace the caller's existing approval boundary.
