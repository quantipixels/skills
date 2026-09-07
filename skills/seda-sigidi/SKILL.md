---
name: seda-sigidi
description: Draft or integrate one AI agent's durable soul—identity, values, boundaries, and voice—grounded in evidence about its human. Use `draft` for naming or authoring without configuration changes, and `integrate` for explicit read/write work in the configuration its host loads; exclude configuration edits with no identity decision, generic documentation work, skill authoring, provider operations, and installing, activating, publishing, committing, or pushing anything.
disable-model-invocation: true
---

# Fẹ̀mí Sínú Sigidi

Give one AI agent a durable soul: identity, values, boundaries, and voice grounded in evidence about its human. Own discovery, authoring, and proof on both paths. Own configuration mutation only in `integrate`, when the exact loaded target and read/write authority are explicit. The caller owns tool choice, credentials, installation, activation, publication, and any Git or provider operation.

## Choose the path

- `draft` — discover evidence, author the soul, and return the proposed content, open questions, and target shape. Do not edit a host configuration.
- `integrate` — graft a confirmed soul into one exact configuration target with explicit read/write authority, then read back and prove the result. Integration does not install, activate, publish, commit, or push anything.

## 1. Pin the host contract

Identify:

- actual agent host/product;
- material version/configuration when it affects loading; and
- current instruction, memory, workspace, or persona loading contract from host-owned documentation, installed help/diagnostics, and exact current configuration.

Establish:

- which targets are actually loaded;
- their precedence and scope;
- whether the host supports a dedicated persona/soul file or requires identity content inline in an already-loaded instruction file; and
- single-file versus split placement from loader behavior rather than taste.

Existing loaded project/user instructions outrank a generic starter shape.

Use a host-provided diagnostics or inspection surface when available to confirm what actually loaded rather than inferring activation from a file existing on disk. Treat current loader paths, fallback filenames, precedence, limits, and host-specific capabilities as volatile host evidence.

If `integrate` cannot establish an exact loaded target responsibly, return the loader/configuration evidence gap instead of guessing a familiar filename.

When a split soul file would not load, integrate inline. Ask before overwriting an existing identity block. Preserve unrelated content outside that block.

## 2. Gather evidence before inventing anything

Run the discovery pass in [soul-template](references/soul-template.md). Mine session records, memory files, and existing instructions only when the caller supplies or authorizes them; an exact-current `ayewo-igba-ise` result may carry retrospective evidence.

- Confirm every inferred pattern before making it durable.
- If mining surfaces a secret, quote around it and never print, copy, or store it.

## 3. Shape the soul

Shape and graft with [soul-template](references/soul-template.md).

- Expand or rename its sections only when the host's rules demand it.
- Keep section names stable across revisions.
- Keep agent names, skill names, paths, and commands exact.
- Use the agent's name only when supplied, with the supplied spelling.

## 4. Integrate with a minimal diff

- In `draft`, do not apply a diff. Return the proposed soul and intended target shape without reading or changing a configuration unless separate read authority was supplied.
- In `integrate`, apply the template's inventory and zero-loss grafting contract as a minimal diff. Preserve load-bearing rules and unrelated content. Match the target's heading style and language conventions.

## 5. Prove and report

### Draft

Verify the proposed content against the confirmed evidence and template. Report that no host configuration changed.

### Integrate

Read back the complete changed file and check structure, frontmatter, and unchanged neighbors.

Report:

- host/loading evidence that establishes the edited target is active;
- moves table from old location to new section;
- dropped, duplicated, or weakened items, each with its reason;
- open questions that need the human's decision; and
- final state as `source | installed | active | published`.

Return the proposed soul for `draft`, or the report and changed file path for `integrate`. Do not install, activate, synchronize, publish, commit, or push; those need separate authority.
