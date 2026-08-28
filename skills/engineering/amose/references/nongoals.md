# Maintain `.nongoals`

Reserve the optional root `.nongoals` file for durable project-level exclusions: directions, features, responsibilities, ideas, or concerns that the project excludes from all current and future work. Do not store session-, conversation-, task-, plan-, feature-, phase-, or iteration-local non-goals there; keep them with their owning artifact. It is not a backlog. Leave storage and version-control policy to the project. Ignore similarly named files unless the user explicitly supplies one as input.

Before adding an entry, classify the outcome as a durable project rejection, temporary deferral, already-implemented behavior, or task-local exclusion. Only a durable project rejection belongs in `.nongoals`. Keep a deferral with its owning plan and reactivation trigger, point already-implemented requests to current behavior, and keep task-local exclusions with their feature or plan.

## Calibration

Good `.nongoals` entry:

```text
Do not operate a marketplace for third-party plugins; integrations remain first-party or explicitly partnered.
```

Why it belongs: it is a durable project boundary that should constrain future proposals across initiatives.

Bad `.nongoals` entry:

```text
Do not build dark mode in this sprint.
```

Why it does not belong: this is task/iteration-local scope and should stay with the owning plan.

Good deferral, not `.nongoals`:

```text
Offline export is deferred until the synchronization model is settled; re-enter after architecture decision AD-17.
```

Why: the direction remains potentially in scope and has a re-entry trigger.

Good ADR/decision matter, not `.nongoals`:

```text
Use PostgreSQL instead of DynamoDB.
```

Why: selecting one credible architecture alternative does not necessarily create a permanent project-wide rejection of the other technology.

Preserve any existing readable format. Create no empty file. When creation is authorized and no format exists, use a bare list with no heading or schema. Phrase each entry by durable domain concept, not by one issue, file, implementation proposal, or current capacity constraint. Include a concise durable reason or ADR link when the exclusion is not self-explanatory. Do not append request or issue history; those records stay with their owning issue, provider, or local artifact.

Add, remove, or reinterpret an entry only with explicit project-boundary authority. Treat each entry as out of scope for future work until that authority removes or changes it. Absence from `.nongoals` does not prove a direction is in scope. When authority reconsiders an entry, record whether it grants one exception or changes the durable project boundary, then reconcile dependent ADRs, plans, and knowledge packets.

When requested work conflicts with `.nongoals`, pause that work and ask whether the user authorizes a one-time exception or a boundary change.
