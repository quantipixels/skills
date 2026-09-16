# Incident recovery

Use during an active incident within existing live-access and mutation authority. Mitigation/recovery does not grant deployment, rollback, retrospective or permanent-fix authority.

## Pin the active boundary

Identify environment/revision, user-visible impact, affected users/operations, latest observation and existing backlog, partial work, data consequence or external effect. Separate observation from report and hypothesis.

Use the current runbook and actual operator authority; its assumptions still need evidence. If access or a safe operator is unavailable, return an executable handoff.

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

Report impact, actions, stop/rollback conditions, affected-boundary checks, reconciliation, decisive evidence and uncertainty. State `MITIGATED`, `RECOVERED`, `STOPPED` or `BLOCKED` by the strongest observed result.

Name the actual owner of continuing recovery, diagnosis, permanent correction or requested postmortem. Do not collapse mitigation/recovery into permanent repair.
