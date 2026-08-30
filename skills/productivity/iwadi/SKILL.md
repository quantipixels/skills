---
name: iwadi
description: Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent.
---

Investigate one question and capture a sourced Markdown report in the repository. Pin the question, intended use, freshness or version boundary, required evidence, and destination before collecting sources.

Delegate collection only when the investigation is substantially noisier than its durable conclusion and the active host and repository rules permit it. Do not delegate a small known read or raw material the current agent must immediately edit. When delegation is useful, require one compact evidence packet:

- direct conclusion;
- exact primary-source URLs or identities plus relevant sections, symbols, or locations;
- what each source proves;
- conflicts, surprises, caveats, and coverage gaps; and
- checks performed and freshness.

The current agent owns source selection, synthesis, the durable report, and any task action that consumes the findings. A delegated packet is evidence, not the report itself.

The research owner must:

1. Investigate the question against **primary sources** — official docs, source code, specs, first-party APIs — not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Pin a source version, revision, or retrieval date when its content can change materially.
3. Cite each material claim's source and state what the evidence supports without stretching it.
4. State material conflicts between primary sources and any evidence gap that limits the conclusion.
5. Lead the report with the question and direct conclusion or verdict, then present the supporting evidence and limits without reproducing the discovery transcript.
6. Save the report where the repository already keeps research notes. If no convention exists, persist a QP research record through `akosile` with `owner: iwadi`, `record_type: research`, and the stable research topic as subject. State the selected path.
