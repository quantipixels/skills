# Provider-specific orchestration guidance

Load this reference only when the active host exposes provider-specific worker model, reasoning/effort, or invocation controls that can materially affect a Pepeye assignment. The portable coordination method remains in `../SKILL.md`; this file holds host policy that can change independently.

## Shared provider rules

Keep the main session's selected model unless the user explicitly asks to change it. Explicit user choices and applicable host/project instructions override these worker preferences.

Apply preferences through the host's native per-worker controls using model identifiers actually supported by the active host. Do not change global/user configuration merely to obtain a worker model or reasoning level. If a requested or preferred setting is unavailable, distinguish the intended preference from the setting that actually ran; never claim a model or effort was used when it was unsupported or inherited.

When launching workers under provider-specific controls, report the worker's role/responsibility and the requested or preferred versus observed model/effort when that distinction is material or the user asked for it. Do not hide fallback/inheritance behind the preferred setting.

These defaults are workload-shaping preferences, not measured quality, latency, or cost claims. Revisit them when provider capabilities materially change.

## Codex

When Codex exposes per-worker model and reasoning controls, prefer:

| Role | Model | Reasoning |
| --- | --- | --- |
| explorer | GPT-5.6 Luna | max |
| worker | GPT-5.6 Sol | high |
| researcher | GPT-5.6 Luna | max |
| reviewer | GPT-6 Astra | xhigh |

Use the exact model identifiers supported by the installed/current Codex host. If `max`, `high`, `xhigh`, or an equivalent control is unavailable for a selected model, use the closest host-supported/inherited setting only when the user did not require an exact pin, and report the observed setting when material.

Keep discovery/research workers read-only where the host can enforce it. Reviewer independence matters more than matching this table; preserve a fresh review context even when the preferred reviewer model is unavailable.

## Claude Code

When Claude Code exposes per-worker model and effort controls, prefer:

| Role | Model | Effort |
| --- | --- | --- |
| explorer | Haiku | inherited |
| worker | Sonnet | high |
| researcher | Haiku | inherited |
| reviewer | Opus | xhigh |

Use the host's current supported aliases/identifiers rather than freezing a historical provider string when the interface has changed. Do not rewrite global Claude configuration merely to make a worker match this table.

Keep exploration/research lightweight and read-only where enforceable. Give implementation enough capability for the bounded job, and keep consequential review on an independent context. If Opus/xhigh is unavailable, preserve review independence and surface the capability difference rather than silently claiming the preferred reviewer ran.

## Provider capability gaps

A provider-specific default is optional orchestration policy. When the host cannot express it:

1. preserve the assignment, authority, specialist method, and evidence contract;
2. use the host's supported worker/default capability when that does not violate an explicit user pin;
3. report any material difference between requested/preferred and observed settings; and
4. escalate resources only for an evidenced capability gap, not merely because a preferred model name is unavailable.

Provider choice never changes the worker's authority or the owning QP skill's completion criteria.
