# Incident recovery

Use during an active incident when the request authorizes bounded mitigation or recovery. This method does not authorize diagnosis-only work to become delivery, or grant live access, deployment, rollback, data mutation, retrospective or permanent-fix authority that the request and current operating context do not provide.

## Pin the active boundary

Identify the affected environment and candidate or deployed revision, current user-visible impact, affected users or operations, known start and latest observation, and any backlog, partial work, data consequence or external effect already present. Distinguish direct observations from reports and hypotheses.

Read the applicable current runbook and establish who may execute each live action. Reuse its prerequisites, communication path and recovery checks where they fit the observed event; a runbook is guidance, not evidence that its assumptions hold. If required access, authority or a safe operator is unavailable, return the exact executable handoff rather than implying that recovery occurred.

Define one bounded mitigation target in observable terms and its known stop or rollback condition before acting. Prefer a reversible, scoped intervention whose result can be checked at the affected boundary. Confirmed cause is not required before an authorized reversible mitigation when current evidence supports its safety and likely benefit.

Preserve decisive logs, identifiers, timestamps, state snapshots or traces when they are available without materially delaying recovery. Capture only what can distinguish the event, intervention and result; evidence collection must not become a prerequisite that prolongs harm.

## Mitigate and verify recovery

Refresh current state immediately before an intervention and execute only within the established authority. Observe its direct result and the stop or rollback condition before progressing. Stop when impact worsens, the action leaves its safe bound, state becomes unverifiable, the rollback condition occurs or further action needs new authority.

Verify recovery through the boundary affected users depend on, not only a process, health check or control-plane acknowledgement. Check whether queued, retried, delayed or partially completed work drains or needs reconciliation, and inspect material data or external-effect consequences. Treat ambiguous completion as an identity and reconciliation problem: do not blindly replay requests, jobs or writes that may duplicate effects.

Do not promise unattended or background monitoring. Observe for the bounded interval available in the current execution, record the last observation and its limits, and assign any continuing watch to an actual operational owner.

Keep these states distinct:

- **Mitigation** — impact is reduced or contained; the user boundary may still be impaired.
- **Recovery** — the affected user boundary meets the stated recovery check, including material backlog or data consequences.
- **Cause** — a causal mechanism is supported through [diagnosis](diagnosis.md); mitigation success alone does not establish it.
- **Permanent fix** — a separately authorized coding or operational change prevents recurrence and receives its own verification.

## Return the current state

Report the environment and candidate, observed impact, runbook and execution authority, actions taken, stop or rollback conditions, affected-boundary checks, backlog or data reconciliation, decisive preserved evidence, and remaining uncertainty. State `MITIGATED`, `RECOVERED`, `STOPPED` or `BLOCKED` according to the strongest observed result.

Name the next owner for every unfinished result: the current operator for continuing recovery or observation, Alága diagnosis mode for an unresolved cause when requested, Alága delivery for an accepted permanent correction, and `ayewo-igba-ise` for a requested evidence-backed postmortem. Do not collapse those outcomes into an incident-closed claim.
