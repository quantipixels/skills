# Provider integration

Read when provider-native agents, per-spawn model/effort controls, isolation, reusable agent definitions, or other native multi-agent capability can materially improve a Pepeye run.

## Let the assignment specify the worker

Do not classify delegated work into a maintained agent-role or posture taxonomy before spawning it.

For each useful delegation, derive the worker directly from the actual assignment:

- **outcome** — the bounded result needed now;
- **context/candidate** — exact code, artifact, source, or question boundary;
- **instructions/constraints** — only what materially changes how this worker should approach the task;
- **capability** — model/reasoning depth appropriate to this assignment when the host exposes a native control;
- **execution boundary** — requested tools, read/write authority, isolation, workspace, and mutation/publication authority;
- **independence** — whether fresh context or separate judgment is required;
- **evidence** — what must be returned to support integration;
- **stop condition** — what makes the assignment complete; and
- **method** — a semantic skill when one is already selected or materially improves the result.

The assignment is the worker specification. Keep task-specific scope, acceptance criteria, and workflow position out of reusable provider configuration.

## Prefer dynamic native execution

Use the strongest suitable execution context already available:

1. a native/general host agent shaped through the assignment and current per-spawn controls;
2. a suitable existing user agent definition when it already provides a useful persistent constraint;
3. a package-managed provider-native agent definition only when a recurring capability cannot be expressed adequately through the first two.

Judge suitability by behavior and capability, not name matching. Do not create a custom definition merely to obtain a stable role name or to mirror a conceptual worker type.

## Keep persistent definitions exceptional

A provider-native agent definition earns a file only when all are true:

- the required behavior/runtime constraint is recurring and stable rather than task-specific;
- the current host cannot express it adequately through normal per-spawn controls, assignment instructions, or existing configuration;
- no suitable native or user-owned definition already provides it; and
- persisting the definition materially improves reliability, enforcement, reuse, or cost over shaping each worker dynamically.

Examples that may qualify depending on the host include a stable tool/permission envelope, required isolation mode, provider-specific environment/configuration, or an intentionally persistent model/effort pin.

Exploration, analysis, writing, implementation, verification, research, and review do **not** by themselves justify reusable definitions. Pepeye can describe those approaches directly in the assignment when they matter.

Treat provider model/effort/permission precedence as host-specific. A definition-level value may be a stronger pin than a spawn-time default. Do not promise dynamic override semantics the provider does not expose.

## Adapt capability to the assignment

Prefer the current/native model and reasoning defaults when they are sufficient. Increase or reduce capability only for the bounded work whose consequence, ambiguity, difficulty, latency, or cost warrants it.

Do not encode provider model names or a fake cross-provider capability ladder in Pepeye. Request the useful property through the current host's actual controls and report observed runtime values when they matter.

## Use councils when diversity earns the cost

A council is temporary orchestration topology, not a permanent agent type or definition.

Use multiple independent judgments when consequence, uncertainty, competing hypotheses, or model blind spots make diversity worth the extra cost. Prefer differentiated passes—for example broad/lightweight and deep/strong review, or independent analyses with different evidence boundaries—over duplicated identical workers.

Keep contexts independent. Pepeye integrates the findings: agreement is evidence, disagreement is a question to resolve, and majority vote is not proof.

Do not create a council for routine work merely because parallel agents are available.

## Leave orchestration mechanics to the harness

Pepeye expresses semantic topology, assignments, and staffing intent, not a replacement provider runtime.

Let the host own its native:

- spawn/invocation syntax;
- parallel execution and joins;
- agent lifecycle/status delivery;
- retries and failure transport;
- worktree/session mechanics;
- Code Mode or equivalent programmatic orchestration;
- agent teams/shared task machinery; and
- supported model/effort/permission override mechanisms.

Do not add instructions that poll workers, call provider tool names, manually emulate joins, or reproduce native scheduling simply because another host uses different mechanics.

Tune **when/how much** delegation, independence, capability, and judgment are useful; do not teach a capable harness how to run its own agents.

## Keep skills dynamic

Do not hardcode semantic skill identifiers into provider-native agent definitions.

If Pepeye already knows the semantic owner and that method materially helps the assignment, name the skill in the assignment. Otherwise let the worker use ordinary installed capabilities without adding a generic “discover/use skills” instruction whose behavior is already native.

An assignment remains valid when no skill is needed.

## Use names for observability, not routing

When a user-visible team snapshot benefits from a worker name, prefer a concise natural Yorùbá label derived from the assignment when one is obvious—for example **Olùyẹ̀wò** for an independent review worker or **Olùwádìí** for a research worker. The label is presentation only: it does not select behavior, model, tools, permissions, or an agent definition.

Do not maintain a canonical name catalogue merely to support observability. Add a short task discriminator when several workers would otherwise have the same label.

## Treat setup as a response to a concrete limitation

Missing package-managed definitions are not degraded mode when the host can already perform the work well.

Only call out `qp-setup` when a concrete persistent host/configuration limitation materially constrains the current work and setup could remove it. Show that notice once per run; do not advertise setup merely because no package-managed definition exists.
