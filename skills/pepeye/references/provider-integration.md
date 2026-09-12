# Provider integration

Read when provider-native agents, per-spawn model/reasoning controls, isolation, or other multi-agent capability can materially improve a Pepeye run.

## Let the assignment specify the worker

Do not classify delegated work into a maintained role/posture taxonomy. Derive the worker directly from the assignment:

- **outcome** — bounded result needed now;
- **context/candidate** — exact code, artifact, source, or question boundary;
- **instructions/constraints** — only what materially changes the work;
- **capability** — model/reasoning depth appropriate to the assignment;
- **execution boundary** — tools, workspace, authority, and mutation/publication limits;
- **independence** — whether fresh separate judgment is required;
- **evidence** — what must return for integration;
- **stop condition** — what makes the assignment complete; and
- **method** — a semantic skill only when one materially helps.

The assignment is the worker specification. Keep task-specific scope, acceptance criteria, and workflow position out of durable provider configuration.

## Never fork conversation context

Start delegated workers fresh. When upstream context matters, create a compact handoff instead of inheriting the conversation.

A useful handoff carries only what the receiver needs:

- outcome/question;
- accepted constraints and consequential decisions;
- decisive evidence with source/code locators;
- exact candidate/version identity;
- material uncertainty or disagreement; and
- the result the receiving worker must return.

Do not copy transcripts merely to avoid deciding what matters.

## Funnel information before expensive judgment

Spend capability according to the work being done, not the amount of available context.

- **cheap/high-volume capability** — broad reading, search, extraction, logs, source collection, repository mapping;
- **balanced capability** — structured synthesis, normal writing, comparison, routine transformations;
- **strong workhorse capability** — coding, diagnosis, technical synthesis, architecture development, difficult research synthesis;
- **highest judgment capability** — material planning, independent review, premortem, conflict resolution, consequential acceptance/integration decisions.

Do not spend the highest-capability model discovering which evidence it needs when a cheaper worker can collate the surface first. Compression is not authority: preserve locators and let the receiving worker reopen decisive evidence/candidate material before judging it.

Generation needs sufficient capability. **Consequential verification should receive equal or greater judgment capability than the work it accepts.** Apply that at material decision/integration boundaries, not after every cheap worker action.

## Current Codex starting preferences

When the active Codex host exposes these current models, use the user's host policy as authority and adapt per assignment:

| Work | Starting point | Adaptation |
| --- | --- | --- |
| bulk read, collection, exploration, routine research | `gpt-5.6-luna` / medium | low for deterministic collection; Terra when real synthesis begins |
| normal research synthesis, prose/writing | `gpt-5.6-terra` / medium | Luna low/medium for deterministic prose; Sol for difficult technical synthesis |
| coding, diagnosis, technical analysis, architecture development | `gpt-5.6-sol` / medium | Terra for simple bounded work; raise Sol effort for complexity/risk |
| material planning | `gpt-6-astra` / medium | keep context compact; do not spend Astra on bulk discovery first |
| review/judgment | `gpt-6-astra` / medium | high for plan premortem or difficult/high-risk review; xhigh only for exceptional unresolved judgment |

Astra is the quality ceiling, not the default worker. Sol should perform more substantive engineering work than Astra. Luna/Terra should absorb volume before expensive reasoning when that preserves correctness.

These are editable preferences, not semantic ownership. Resolve actual model IDs/reasoning support from the current host and user policy. For another provider, map by current capability/cost properties rather than pretending the model families are equivalent.

## Use councils only when diversity earns the cost

A council is temporary workflow topology, not a permanent agent type.

Use several independent judgments only when consequence, uncertainty, competing hypotheses, or model blind spots make diversity worth the extra cost. Prefer differentiated evidence/focus or capability over duplicate identical passes. Keep contexts independent. Agreement is evidence; disagreement is a question to resolve; majority vote is not proof.

## Leave mechanics to the harness

Pepeye expresses topology, assignments, capability intent, and evidence boundaries. Let the host own:

- spawn/invocation syntax;
- concurrency, scheduling, joins, and lifecycle;
- retries/failure transport;
- worktree/session mechanics;
- Code Mode or equivalent orchestration;
- teams/shared task machinery; and
- supported model/reasoning/permission controls.

Do not add portable instructions that poll workers, emulate joins, or reproduce provider scheduling. Tune when delegation, independence, capability, and judgment are useful; do not teach a capable harness how to run itself.

## Keep skills dynamic

Do not hardcode semantic skills into worker types or host model preferences. Name a skill in the assignment when Pepeye already knows the semantic owner and that method materially helps. Otherwise no skill is required.

## Use names for observability, not routing

When a team snapshot benefits from a worker name, prefer a concise natural Yorùbá label derived from the assignment when one is obvious. The label is presentation only; it does not select behavior, model, tools, permissions, or skills. Do not maintain a canonical worker-name catalogue merely for observability.

## Treat setup as policy/configuration, not a fleet installer

Missing package-managed workers are not degraded mode. `qp-setup` may audit or install user-editable host policy and ordinary host configuration when requested. Only surface setup when a concrete host capability/configuration limitation materially constrains the work.
