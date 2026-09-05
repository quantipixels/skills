# Failures and feedback

Read exact failed-job logs and full unresolved feedback against the current candidate before acting. A red title, green bot badge, or resolved thread alone does not prove a defect, acceptance, or correction.

- **Branch defect:** reproduce or directly trace the failure to the changed behavior. Use `alaga` for the scoped source correction, proof, and review, then resume babysitting with its verified result.
- **Likely flake:** require evidence of a transient failure and no candidate change to its mechanism. With correction authority, rerun once per candidate/job; resuming does not reset that allowance. Diagnose a repeat instead of retrying until green.
- **Infrastructure/policy:** report the runner, quota, permission, dependency, or provider blocker. Do not change CI, dependencies, or tests to mask an unrelated failure.
- **Unclear cause:** make a bounded diagnosis attempt, then report decisive missing evidence and the next action. Use `root-cause` when causal investigation is itself the needed result.

Validate review claims directly when the evidence is clear; use `se-triage` only for material uncertainty. Check whether older feedback still applies rather than discarding it merely because the head moved. Fix valid in-scope findings; explain false positives, duplicates, or out-of-scope requests with evidence. An out-of-scope request that still blocks approval remains a blocker, not a silently dismissed success. Refresh the candidate before replying/resolving, and verify the provider effect. Read-only watching never authorizes these mutations.
