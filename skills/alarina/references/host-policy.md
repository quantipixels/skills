# Native host policy

Read when coordination depends on model selection, reasoning effort, provider-native configuration, worker reuse, or lifecycle claims. This is the repository's supported policy profile for Codex and Claude; it is not a portable model registry or a substitute for current host documentation.

User and host settings own model and effort choices. Choose the lowest supported effort adequate for ambiguity, consequence, interacting constraints, inference difficulty, and verification cost. Raise effort when those factors earn it; no failed low-effort trial is required.

## QP policy profile

| Assignment level | Codex | Claude | Typical boundary | Relative user weight |
| --- | --- | --- | --- | --- |
| Conductor | `gpt-6-astra` | Fable 5.1 (`claude-fable-5-1`) | scope, architecture, consequential decisions, acceptance, communication | Astra 8 |
| Substantial worker | `gpt-5.6-sol` | Opus 5 (`claude-opus-5`) | integration, difficult debugging, sustained judgment | Sol 5 |
| Bounded worker | `gpt-5.6-terra` | Sonnet 5 (`claude-sonnet-5`) | bounded implementation or investigation with local proof | Terra 3 |
| Small evidence worker | `gpt-5.6-luna` | Haiku 4.5 (`claude-haiku-4-5-20251001`) | extraction, small reads, deterministic work, easy-to-check evidence | Luna 0.5; Haiku 1 |

These are role counterparts selected by the user, not benchmark equivalence or API prices. Do not invent unprovided Claude weights. Luna fan-out is encouraged for useful independent bounded evidence and deterministic tasks, within actual concurrency and task authority. Haiku does not inherit Luna's fan-out preference or effort exception.

Reasoning ceilings:

- Astra, Sol, Terra, and all Claude models stay below `max`.
- Luna may use supported effort through `max`, never above it.
- Haiku uses its supported thinking controls without an invented named-effort translation.

A default model or effort is not a ceiling. Verify the effective host configuration when enforcement matters.

## Codex

Codex subagent files may set `model` and `model_reasoning_effort`; those file values override spawn values. Otherwise resolution follows explicit spawn values, `[agents]` defaults, then the parent. The `[agents]` table supports `default_subagent_model`, `default_subagent_reasoning_effort`, and `max_concurrent_threads_per_session`.

No documented native hard ceiling for reasoning effort was found as of 14 September 2026. Do not claim defaults enforce this profile's caps. Keep model and effort settings in user/host configuration and verify effective behavior through `irinse` when required.

Primary source: [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Claude Code

Claude subagent model resolution is per-invocation model, then agent-frontmatter model, then `CLAUDE_CODE_SUBAGENT_MODEL`, then the main model. Reuse an agent ID for supported resumption; built-in Explore and Plan workers are one-shot. Verify lifecycle behavior in the installed host rather than promising background continuation.

Claude Code 2.1.267 and later supports `maxEffortLevel` as a lower ceiling from any settings scope, with the lowest applicable value winning. The cap includes skills and subagents; unsupported levels clamp to the next lower supported level. A host/user-owned profile can therefore set:

```json
{"maxEffortLevel":"xhigh"}
```

This package does not install or edit that setting. Verify the installed version, effective scopes, selected models, and resulting cap through `irinse`.

Primary sources: [subagents](https://code.claude.com/docs/en/sub-agents), [settings precedence and managed exceptions](https://code.claude.com/docs/en/settings#exceptions-to-managed-settings-precedence), and [model configuration](https://code.claude.com/docs/en/model-config).
