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

Before editing host configuration, distinguish user-editable host policy from hard runtime configuration and user-owned configuration from package-managed text. Preserve unrelated settings and permissions.

## Keep worker shaping separate from host policy

For multi-agent integrations, keep these layers distinct:

- **host harness** — spawn/join mechanics, concurrency, scheduling, lifecycle, native isolation, teams, and provider-specific invocation;
- **host policy** — user-editable delegation/model/reasoning/context preferences;
- **assignment** — this worker's outcome, context/candidate, instructions, capability request, authority, independence, evidence, and stop condition;
- **skill** — reusable semantic method/expertise when one materially helps the result;
- **workflow/router** — topology between independently owned results.

Do not add a maintained role/posture layer or a second model/config registry between host policy and assignments. A provider-specific hard setting belongs in ordinary host/tool configuration only when dynamic controls cannot satisfy an actual requirement.

An assignment may name a skill when already selected; otherwise do not add generic “discover skills” instructions merely because skills exist.

Treat model/reasoning/permission controls according to the provider's actual surface and precedence. Do not invent one portable precedence contract.

When high-volume input would waste expensive capability, collate it with cheaper workers and preserve exact locators in the handoff. Stronger workers should independently reopen decisive material before consequential acceptance. Do not fork conversation history to avoid constructing the handoff.

Do not reproduce native spawn, wait, join, polling, retry, or team mechanics in portable skill instructions. State the semantic/evidence requirement and let each host use its strongest native mechanism.

## Decide by consequence

Ask what this resource uniquely improves and what fails if it disappears. Keep resources that protect real expertise, safe mechanics, or independently selectable branches. Remove resources that mostly mirror information the agent can inspect cheaply at use time.
