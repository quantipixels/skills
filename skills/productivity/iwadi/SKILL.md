---
name: iwadi
description: Investigate one substantial, reusable, or audit-worthy question against high-trust primary sources and capture the conclusion as a sourced Markdown research record. Use when several sources must be reconciled, the conclusion should survive the current task/session, or the user explicitly requests a research record; exclude one/few routine facts that can be consumed immediately.
---

# Ìwádìí

Investigate one question whose sourced conclusion deserves independent persistence, and capture that conclusion as a Markdown research record. Pin the question, intended downstream use, freshness/version boundary, required evidence, and destination before collecting sources.

## Admission

Use Ìwádìí when at least one is true:

- several primary sources must be reconciled into one conclusion;
- the result is independently reusable, auditable, or likely to outlive the immediate task/session;
- a material standards, security, compatibility, policy, or ecosystem conclusion needs durable provenance; or
- the user explicitly requests a persistent research report.

Do not create a research record for one or a few routine facts, a small known documentation read, or transient source lookup whose result is immediately consumed by another owner. Let the active agent/owner perform that bounded lookup directly. When an explicitly accepted Experimental `orisun` result owns an exact-version upstream-source question, consume that result rather than duplicating its source-grounding workflow.

## Context isolation

Delegate collection only when the investigation is substantially noisier than its durable conclusion and the active host/repository rules permit it. The purpose is to keep source-search volume out of the primary reasoning context, not to delegate merely because subagents exist. Do not delegate a small known read or raw material the current agent must immediately edit.

When delegation is useful, require one compact evidence packet:

- direct conclusion;
- exact primary-source URLs or identities plus relevant sections, symbols, or locations;
- what each source proves;
- conflicts, surprises, caveats, and coverage gaps; and
- checks performed and freshness.

The current agent owns source selection, synthesis, the durable report, and any task action that consumes the findings. A delegated packet is evidence, not the report itself.

## Research contract

1. Investigate against **primary sources** — official docs, source code, specs, standards, first-party APIs — not a secondary write-up of them. Follow every material claim back to the source that owns it.
2. Pin a source version, revision, or retrieval date when its content can change materially.
3. Cite each material claim's source and state what the evidence supports without stretching it.
4. State material conflicts between primary sources and any evidence gap that limits the conclusion.
5. Lead with the question and direct conclusion/verdict, then present supporting evidence and limits without reproducing the discovery transcript.
6. Save the report where the repository already keeps research notes. If no convention exists, persist a QP research record through `akosile` with `owner: iwadi`, `record_type: research`, and the stable research topic as subject. State the selected path.
