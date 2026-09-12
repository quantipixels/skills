# Resource boundaries

Read when agent-facing guidance needs references, scripts, templates, bundled data, or host adapters.

Prefer the least burdensome resource that preserves the capability. Fewer files is not the objective; clear responsibility and justified load are.

## References

A reference earns its place when it improves a recurring non-obvious decision and has a reliable load condition. Keep examples, counterexamples, exceptions, and named conceptual/retrieval anchors when they sharpen judgment.

Remove copied official documentation, cheap repository facts, stale version inventories, task history, and material that cannot change behaviour. Split by independently selectable branches, not line count.

## Deterministic code

Keep bundled code only when it owns a bounded mechanical result and materially improves correctness, reuse, or safe invocation over native/project tooling. Validators, exact transforms, safe compare-and-swap mechanics, stable agent-definition renderers, and safe installation/bootstrap entrypoints can qualify.

Ordinary search/filter wrappers, Git/filesystem recipes, provider normalization solely for model consumption, and executable checklists usually do not. Interpretation, acceptance, routing, and authority remain with the responsible agent/skill.

Code that ships must have falsifiable tests for its mechanical contract. Do not add state, locks, retries, schemas, daemons, or another runtime without a demonstrated need.

## Templates and data

Keep a template when a stable recurring shape prevents meaningful omissions and no existing project/native scaffold owns it. Remove arbitrary defaults and optional-empty ceremony.

Bundle data only when maintaining it materially supports the result. Give volatile data a freshness boundary; do not turn a convenience snapshot into an authority source.

## Host adapters

Keep one portable semantic contract and thin host-specific adapters. Do not duplicate the whole instruction set merely because hosts expose different metadata or invocation controls.

Before editing host configuration, distinguish primary-session instructions from agent definitions and user-owned configuration from package-owned assets. Preserve unrelated settings and permissions.

## Keep runtime posture separate from method

For multi-agent integrations, keep these layers distinct:

- **host harness** — spawn/join mechanics, scheduling, Code Mode/team primitives, lifecycle, native isolation, and provider-specific invocation;
- **work posture** — how one bounded assignment should be approached (for example exploration, writing, or independent judgment);
- **agent definition** — optional provider-native reusable configuration only when a persistent delta beyond native/user capability earns a file;
- **assignment** — this task's outcome, candidate, authority, independence, evidence, and stop condition;
- **skill** — reusable semantic method/expertise when one materially helps the result;
- **workflow/router** — topology between independently owned results.

An agent definition should not hardcode semantic skill identities or fixed workflow stages. A work posture does not imply an agent-definition file exists. Prefer adequate native agents or existing user definitions; add a QP definition only when it contributes durable value.

An assignment may name a skill when already selected; otherwise do not add generic “discover skills” instructions merely because skills exist.

Treat model/effort/permission fields according to the provider's actual precedence. A definition-level value may be a pin rather than an overridable default. Do not invent one portable precedence contract.

Do not reproduce native spawn, wait, join, polling, retry, or team mechanics in portable skill instructions. State the semantic/evidence requirement and let each host use its strongest native mechanism.

## Decide by consequence

Ask what this resource uniquely improves and what fails if it disappears. Keep resources that protect real expertise, safe mechanics, or independently selectable branches. Remove resources that mostly mirror information the agent can inspect cheaply at use time.
