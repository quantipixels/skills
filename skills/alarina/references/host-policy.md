# Native host policy

Read when coordination depends on model selection, reasoning effort, or host-native worker behavior. This is the repository's supported policy profile, not a provider tutorial or substitute for current host documentation.

User and host settings own model and effort choices. Choose the lowest supported effort adequate for ambiguity, consequence, interacting constraints, inference difficulty, and verification cost. Raise effort when those factors earn it; no failed low-effort trial is required.

Check prerequisites only for the selected worker and required capabilities; do not preflight an unused roster. Reuse current evidence until the relevant configuration, host or assignment requirement changes. Use `irinse` when discovery or enforcement needs investigation. Block only work depending on an unmet requirement; report unavailable runtime evidence rather than treating requested settings as observed behavior.

## QP policy profile

| Typical assignment | Codex | Claude | Typical boundary | Relative user weight |
| --- | --- | --- | --- | --- |
| Exceptional specialist | `gpt-6-astra` | Fable 5.1 (`claude-fable-5-1`) | bounded investigation or independent judgment beyond the other workers' demonstrated capability | Astra 8 |
| Substantial worker | `gpt-5.6-sol` | Opus 5 (`claude-opus-5`) | integration, difficult debugging, sustained judgment | Sol 5 |
| Bounded worker | `gpt-5.6-terra` | Sonnet 5 (`claude-sonnet-5`) | bounded implementation or investigation with local proof | Terra 3 |
| Small evidence worker | `gpt-5.6-luna` | Haiku 4.5 (`claude-haiku-4-5-20251001`) | extraction, small reads, deterministic work, easy-to-check evidence | Luna 0.5; Haiku 1 |

These are role counterparts selected by the user, not benchmark equivalence or API prices. Assignments are defaults, not capability ceilings. Choose by task fit and total effort, including coordination, repeated context and rework. Do not invent unprovided Claude weights. Low model cost alone does not justify delegation. Choose workers within actual concurrency and task authority without a separate approval. Haiku does not inherit Luna's effort exception.

Reasoning ceilings:

- Astra, Sol, Terra, and all Claude models stay below `max`.
- Luna may use supported effort through `max`, never above it.
- Haiku uses its supported thinking controls without an invented named-effort translation.

A default model or effort is not a ceiling. Keep settings user/host-owned and verify effective behavior through `irinse` when enforcement matters. Use current host help or official documentation only for the configuration detail needed by the task; do not preserve provider command or precedence tutorials here.
