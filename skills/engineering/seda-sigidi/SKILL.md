---
name: seda-sigidi
description: Draft or integrate one AI agent's durable soul—identity, values, boundaries, and voice—grounded in evidence about its human. Use `draft` for naming or authoring without configuration changes, and `integrate` for explicit read/write work in the configuration its host loads; exclude configuration edits with no identity decision, generic documentation work, skill authoring, provider operations, and installing, activating, publishing, committing, or pushing anything.
---

# Fẹ̀mí Sínú Sigidi

Give one AI agent a durable soul: identity, values, boundaries, and voice grounded in evidence about its human. Own discovery, authoring, and proof on both paths. Own configuration mutation only in `integrate`, when the exact loaded target and read/write authority are explicit. The caller owns tool choice, credentials, installation, activation, publication, and any Git or provider operation.

## Choose the path

- `draft` — discover evidence, author the soul, and return the proposed content, open questions, and target shape. Do not edit a host configuration.
- `integrate` — graft a confirmed soul into one exact configuration target with explicit read/write authority, then read back and prove the result. Integration does not install, activate, publish, commit, or push anything.

## 1. Pin the host contract

Discover which files the host loads without being told, and decide single-file versus split by loader behavior, not by taste. Verify current loading rules against live documentation when uncertain; search before guessing. Known starting points:

| Host | Loaded automatically | Separate persona files |
| --- | --- | --- |
| Codex | `~/.codex/AGENTS.md` and project `AGENTS.md` | none |
| Claude Code | the `CLAUDE.md` memory chain | none |
| opencode | global and project `AGENTS.md` | none |
| OpenClaw | workspace `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, and `USER.md` | supported |

When a split soul file would not load, integrate inline. Ask before overwriting an existing identity block. Preserve unrelated content outside that block.

## 2. Gather evidence before inventing anything

Run the discovery pass in [soul-template](references/soul-template.md). Mine session records, memory files, and existing instructions only when the caller supplies or authorizes them; an exact-current `ayewo-igba-ise` result may carry retrospective evidence. Confirm every inferred pattern before making it durable. If mining surfaces a secret, quote around it and never print, copy, or store it.

## 3. Shape the soul

Shape and graft with [soul-template](references/soul-template.md). Expand or rename its sections only when the host's rules demand it, and keep section names stable across revisions. Keep agent names, skill names, paths, and commands exact. Use the agent's name only when supplied, with the supplied spelling.

## 4. Integrate with a minimal diff

In `draft`, do not apply a diff. Return the proposed soul and intended target shape without reading or changing a configuration unless separate read authority was supplied.

In `integrate`, apply the template's inventory and zero-loss grafting contract as a minimal diff. Preserve load-bearing rules and unrelated content. Match the target's heading style and language conventions.

## 5. Prove and report

For `draft`, verify the proposed content against the confirmed evidence and template. Report that no host configuration changed.

For `integrate`, read back the complete changed file, and check structure, frontmatter, and unchanged neighbors. Report:

- a moves table from old location to new section;
- dropped, duplicated, or weakened items, each with its reason;
- open questions that need the human's decision;
- final state as `source | installed | active | published`.

Return the proposed soul for `draft`, or the report and changed file path for `integrate`. Do not install, activate, synchronize, publish, commit, or push; those need separate authority.
