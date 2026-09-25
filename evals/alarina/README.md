# Alárinà one-entry evaluation

Use these cases only when a change affects Alárinà discovery, route selection, bundled owner loading, provider packaging, or the one-entry migration. They are not a standing certification suite for every owner edit.

## Keep the evidence layers separate

| Lane | Condition | Claim it can support |
| --- | --- | --- |
| Package | Deterministic generated artifact | Bundle identity, paths, links, provenance, metadata and one-entry shape |
| Native manager | Disposable host install/update/uninstall | Manager acceptance and exact installed inventory |
| Trigger | Ordinary prompt in a clean plugin-only native session | Whether the host selected Alárinà |
| Dispatch/loading | Alárinà is already loaded; stop at the routing checkpoint | Playbook, owner mode, stopping point and successful required file loads |
| Outcome | Matched routed and direct-owner work | Whether Alárinà preserves owner acceptance and authority |
| Full workflow | Selected multi-stage task through verified completion | End-to-end behavior for that exact workflow and environment |

Supplying `SKILL.md` bypasses native discovery. Mentioning a command path does not prove a successful read. A correct answer without Alárinà selection is not a trigger pass. A route checkpoint is not a completed engineering outcome. A description-only Luna test assesses selection reasoning, not native host activation.

## Native trigger lane

Use [trigger actors](triggers/cases.json) without the private [expectations](triggers/expectations.json). Run them in disposable host state containing only the candidate plugin, with no independently installed QP skills and no Alárinà agent profile selected. Record host, host version, model, effort, plugin version, source revision, prompt ID, selection evidence, competing selection, completion state and interventions.

Run the explicit controls separately because they test deterministic entry rather than implicit selection. Keep invalid, blocked, interrupted and unauthenticated trials distinct from failures. Freeze any numeric threshold before the final candidate run; inspect failures by route family and negative class.

## Dispatch and loading lane

Use [dispatch actors](dispatch/cases.json) without the private [expectations](dispatch/expectations.json). Start with Alárinà supplied or natively selected and stop after the required playbook/owner checkpoint. The harness must retain successful read results for the exact bundled files; filename mentions and attempted reads are insufficient.

The privacy-preserving session adapter may record qualified invocation and reference-path signals, but it deliberately does not copy tool arguments or result content. Use a disposable evaluation harness trace for successful-read assertions. The dispatch corpus covers all 38 focused commands, named playbook composition, bare entry, advice, resumption, agent scope, unknown commands, qualified prefixes and explicit-only utility boundaries. The updater and private-serving methods are bundled; they cannot be inferred from ordinary task context.

## Outcome lane

The [bounded outcome actors](outcomes/cases.json) exercise human writing, specification, work decomposition and an actual isolated Python fix. Keep [their acceptance criteria](outcomes/expectations.json) separate from actor context. Also reuse the smallest applicable existing QP cases:

- ordinary fix: coordination C03 or an executable engineering fixture;
- diagnosis-only: coordination C02;
- architecture recommendation: an engineering architecture scenario;
- data-change plan: coordination C06;
- PR status: coordination C05;
- documentation sync: coordination C16.

For each selected task, compare the direct canonical owner, explicit Alárinà entry, and implicit Alárinà entry only when native selection has been established. Keep project snapshot, model, effort, permissions, acceptance and budget compatible. Report coordination overhead and interventions.

## Release blockers

- wrong merge, publication, deployment, destructive action, or implementation beyond the requested stop;
- missing required playbook or owner load on a must-pass dispatch case;
- a public family with no demonstrated implicit reach and no documented explicit-only fallback;
- stale individually discoverable plugin-owned skills after migration;
- a provider artifact carrying another provider's invocation or unsupported metadata;
- a routed outcome that loses a direct owner's required acceptance or stopping point.

Run the repository-wide evaluation method in [the parent README](../README.md). Preserve failed and inconclusive evidence; do not retune prompts or thresholds against the final case set and report the same run as held out.
