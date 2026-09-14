# Resource boundaries

Read when agent-facing guidance needs references, scripts, templates, bundled data, or host adapters.

Prefer the least burdensome resource that preserves the capability. Fewer files is not the objective; clear responsibility and justified load are.

## References

A reference earns its place when it improves a recurring non-obvious decision and has a reliable load condition. Keep examples, counterexamples, exceptions, and named conceptual/retrieval anchors when they sharpen judgment.

Remove copied official documentation, cheap repository facts, stale version inventories, task history, and material that cannot change behaviour. Split by independently selectable branches, not line count.

## Deterministic code

Keep bundled code only when it owns a bounded mechanical result and materially improves correctness, reuse, or safe invocation over native/project tooling. Validators, exact transforms, safe compare-and-swap mechanics, and safe installation/bootstrap entrypoints can qualify.

Ordinary search/filter wrappers, Git/filesystem recipes, provider normalization solely for model consumption, executable checklists, and renderers for artifacts a capable agent can produce directly usually do not. Interpretation, acceptance, routing, and authority remain with the responsible agent/skill.

Code that ships must have falsifiable tests for its mechanical contract. Do not add state, locks, retries, schemas, daemons, or another runtime without a demonstrated need.

## Templates and data

Keep a template when a stable recurring shape prevents meaningful omissions and no existing project/native scaffold owns it. Remove arbitrary defaults and optional-empty ceremony.

Bundle data only when maintaining it materially supports the result. Give volatile data a freshness boundary; do not turn a convenience snapshot into an authority source.

## Host adapters

Keep one portable semantic contract and thin host-specific adapters. Do not duplicate the whole instruction set merely because hosts expose different metadata or invocation controls.

Before editing host configuration, distinguish primary-session instructions from agent definitions and user-owned configuration from package-owned assets. Preserve unrelated settings and permissions.

## Keep worker shaping separate from durable configuration

For multi-agent integrations, keep these layers distinct:

- **host harness** — spawn/join mechanics, scheduling, Code Mode/team primitives, lifecycle, native isolation, and provider-specific invocation;
- **assignment** — the worker specification for this task: outcome, context/candidate, instructions, capability request, execution boundary, authority, independence, evidence, and stop condition;
- **agent definition** — optional provider-native reusable configuration only when a recurring persistent delta cannot be expressed adequately through native/per-spawn controls, the assignment, host defaults, or existing user configuration;
- **skill** — reusable semantic method/expertise when one materially helps the result;
- **workflow/router** — topology between independently owned results.

Do not add a maintained role/posture layer between an assignment and the worker it needs. Derive the worker directly from the actual task.

An agent definition should not hardcode semantic skill identities, task-specific instructions, or fixed workflow stages. Prefer adequate native/general agents and existing user definitions; add a package-managed definition only when it contributes durable value that dynamic worker shaping cannot.

An assignment may name a skill when already selected; otherwise do not add generic “discover skills” instructions merely because skills exist.

Treat model/effort/permission fields according to the provider's actual precedence. A definition-level value may be a pin rather than an overridable default. Do not invent one portable precedence contract.

Do not reproduce native spawn, wait, join, polling, retry, or team mechanics in portable skill instructions. State the semantic/evidence requirement and let each host use its strongest native mechanism.

## Decide by consequence

Ask what this resource uniquely improves and what fails if it disappears. Keep resources that protect real expertise, safe mechanics, or independently selectable branches. Remove resources that mostly mirror information the agent can inspect cheaply at use time.
