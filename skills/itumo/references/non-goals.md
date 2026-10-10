# Maintain the README Non-goals section

Keep durable project-wide exclusions in a `## Non-goals` section of the project README: directions, features, responsibilities or concerns the project rules out for all current and future work. Amose maintains it. Do not create a separate non-goals file; if the project already keeps one, keep using it.

It is not a backlog and not a place for task-local scope. Before adding an entry, classify the outcome:

- durable project rejection: belongs here;
- temporary deferral: keep with its plan and a reactivation trigger;
- already-implemented behavior: point to current behavior;
- task-local exclusion: keep with its feature or plan.

## Calibration

Belongs:

```text
Do not operate a marketplace for third-party plugins; integrations remain first-party or explicitly partnered.
```

It is a lasting boundary that should constrain proposals across initiatives.

Does not belong: "Do not build dark mode in this sprint." (task-local), "Offline export waits for the sync model; revisit after AD-17." (deferral), "Use PostgreSQL instead of DynamoDB." (a choice between alternatives, not a permanent rejection; it is an ADR only if it passes the ADR bar).

## Writing and changing entries

Add the section only when the first qualifying entry exists. Use a plain bullet list. Phrase each entry by lasting concept, not by one issue or file, and add a short reason or ADR link when it is not obvious. Do not append request history.

Add, remove or reinterpret an entry only with explicit authority over the project boundary. When authority reconsiders an entry, record whether it grants one exception or changes the boundary, then update only the maintained sources that became stale (ADRs, active plans, domain docs).

## Checking

When scoping or planning, read the section. Absence of an entry does not prove a direction is in scope. If requested work conflicts with an entry, pause that work and ask whether the user grants a one-time exception or a boundary change.
