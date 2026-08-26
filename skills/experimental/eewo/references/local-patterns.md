# Local Èèwọ̀ patterns

Local patterns extend the shipped references without editing or publishing the skill.

## Scopes

- Repository: `<repository>/.qp/records/eewo/`
- Personal: `${QP_HOME:-$HOME/.qp}/records/eewo/`

Repository scope is the default local destination. Read or write personal scope only after the user explicitly authorizes personal/cross-project pattern access for the task.

Use `akosile` for path allocation, safe writes, revisions, indexing, Git exclusion, and personal permissions.

## Record schema

Each pattern is one `record.md`:

```yaml
---
owner: eewo
record_type: pattern
title: <short human title>
updated_at: <offset-aware timestamp>
revision: <positive integer>
candidate: <stable pattern id>
status: active | superseded | retired

pattern_id: <stable dotted id>
effect: BLOCK | WARN
languages: [rust | java | python | elixir]
frameworks: []
versions: []
repositories: []
paths: []
phases: [implementation, review]
supersedes: []
---

## Avoid

<semantic prohibited behavior>

## Failure mechanism

<trigger → failure → caller/operational consequence>

## Safe paths

- <credible alternative>
- <documented exception and required proof, if any>

## Evidence

- <user correction, incident, review, test, official source, or code path>
```

Use frontmatter `status` as the only lifecycle state. Do not duplicate it in the body.

## Update rules

Create or change a local pattern only when the user explicitly requests durable local memory or an authorized repository policy already establishes it.

Before activation, require:

1. a concrete failure mechanism;
2. the smallest scope supported by evidence;
3. at least one credible safe path;
4. any legitimate exception;
5. a stable ID that does not encode private data.

Prefer updating/superseding an existing rule with the same failure mechanism over adding a duplicate. A one-off correction may remain ordinary conversation/project evidence instead of becoming a pattern.

## Resolution

Load only `status: active` records matching the current language/framework/version/repository/path/phase. Repository patterns may narrow a shipped generic rule. Personal patterns may add a user preference but cannot override current user or repository instructions.

On conflict, report the exact rules and stop applying that rule family. Do not silently pick the stricter or newer record.

## Publication boundary

Never stage or publish `.qp` or personal QP records.

When a local pattern should become a shipped Èèwọ̀ reference, pass its sanitized semantic content and public evidence to `ko-skill`. `ko-skill` owns the skill change and validation; `seda-pr` owns the later authorized Git publication.
