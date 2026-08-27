# Known-bad pattern layer

This is the useful runtime core of the retired Èèwọ̀ experiment. It is a candidate-triggered guard layer inside Akọ̀wé Code, not a second public skill.

Report a pattern only when the candidate demonstrates the trigger and a credible consequence. Use `BLOCK` only for a correctness, security, data-integrity, compatibility, resource, or lifecycle hazard; use `WARN` for material craft/maintenance cost with a safer shape.

Common patterns:

- **Boolean-state cross products** — several flags/nullables encode mutually invalid states. Prefer one explicit state model.
- **Hidden unbounded work** — unbounded collection, queue, retry, fan-out, recursion, buffering, upload/read-all, channel/process creation, or task submission.
- **Swallowed cancellation/interruption/cause** — async/concurrent work cannot stop or diagnose correctly.
- **Remote side effect inside local atomic transaction** — local rollback cannot undo the external effect and locks/resources remain held.
- **Ambient/global mutable context** — request/user/tenant/security/transaction state leaks across calls or tasks.
- **Pass-through abstraction pile** — wrappers/interfaces/services merely relocate calls and increase navigation without owning policy.
- **Entity/domain object as transport contract** — persistence/lifecycle or internal fields leak into external API serialization.
- **Retry without idempotency/classification/budget** — duplicate effects and outage amplification.
- **Framework lifecycle bypass** — manually constructing/interacting with an object whose proxy/scope/config/lifecycle belongs to the framework.
- **Tests coupled to choreography** — assertions on private calls or mock sequences instead of stable behavior.
- **Configuration/security secrets in source/logs/errors** — disclosure and difficult rotation.
- **Metric-driven refactor** — split or indirection added only to lower complexity/coverage numbers while semantic complexity is unchanged.

When a reliable deterministic detector exists, prefer a project-native static/tool rule through `irinse`; keep the semantic consequence with the owning skill. Do not maintain duplicate prompt and tool enforcement unless each proves a different boundary.
