---
name: iwadi
description: Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent.
---

Investigate one question and capture a sourced Markdown report in the repository. Delegate the research to a background agent only when the active host and repository rules permit it and independent research can run alongside useful work. Otherwise, the current agent owns the research.

The research owner must:

1. Investigate the question against **primary sources** — official docs, source code, specs, first-party APIs — not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Cite each claim's source.
3. State material conflicts between primary sources and any evidence gap that limits the conclusion.
4. Save the report where the repository already keeps research notes. If no convention exists, persist a QP research record through `akosile` with `owner: iwadi`, `record_type: research`, and the stable research topic as subject. State the selected path.
