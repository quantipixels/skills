# Instruction economics

Read when a skill's description, entrypoint, references, or always-loaded guidance may be affecting selection, focus, context pressure, or maintainability. The goal is not minimum words; it is to spend instruction/context load only where it changes a recurring decision or protects a necessary boundary.

## Treat each loading surface by its job

A skill has several different information surfaces:

- **Description** — routing pointer. It must make the skill selectable for its real trigger branches and reject adjacent owners without summarising the whole skill.
- **`SKILL.md`** — invocation entrypoint. Keep the focal result, universal method, completion evidence, and independently necessary boundaries here.
- **References** — selectively loaded expertise or branches. Move material here when only some invocations need it and the entrypoint can state a reliable condition for loading it.
- **Scripts/tools** — bounded deterministic mechanics. They earn their place only under the normal script/resource rules; executable convenience is not automatically cheaper than instructions.
- **Environment/project sources** — current facts, commands, configuration, schemas, directory shape, and other truth the agent can inspect directly. Do not duplicate a cheap authoritative lookup into instructions merely to make the skill look complete.

A short entrypoint with every invocation forced through many references can cost more and focus worse than a somewhat longer self-contained entrypoint. Inspect the actual loading path, not file length alone.

## Keep the routing pointer discriminative

Write the description around **distinct trigger branches**, not synonym coverage. Two phrases that select the same situation usually add load without adding a new branch. Preserve extra wording only when real host/model evidence shows it materially improves correct selection.

State the owned outcome and the nearest important exclusions. Do not put procedure, rationale, examples, result schemas, or every related skill into the description unless one of those facts is needed to route correctly.

When two skills attract the same realistic request, compare their owned result, decision surface, authority, and completion evidence. Fix the ownership/routing distinction before adding more trigger vocabulary.

## Keep the entrypoint focused

Every instruction in the entrypoint should do at least one useful job:

- change a recurring non-obvious decision;
- establish an execution/completion gate;
- provide expertise the model would otherwise guess poorly;
- protect an authority, safety, evidence, or ownership boundary; or
- point reliably to selectively loaded depth.

A sentence is a **no-op candidate** when removing it is unlikely to change selection, action, evidence, or a necessary boundary on the target hosts/models. Do not delete it by intuition alone when behavior matters: compare realistic tasks in the internal evaluation path. Conversely, do not retain prose merely because it sounds prudent.

Prefer stating the positive target behavior. Keep explicit prohibitions when they protect a hard safety/authority boundary or when the positive form does not prevent a demonstrated failure.

## Place pressure where it is cheapest

Different agents or phases carry different context pressure. An implementer often needs exploration, source, tests, failures, and edits in the same window; a reviewer can usually start from a bounded candidate and review contract. Put review-only standards and smell catalogues in review context rather than taxing implementation, unless the implementer genuinely needs the rule to produce the required result safely.

Likewise, keep setup, provider, platform, or language-specific detail behind a condition that selects it. Do not move independently loaded safety/authority rules behind an optional reference merely to reduce tokens.

## Use structural evidence carefully

`../scripts/skill-doctor.py` can inventory routing-pointer size, entrypoint size, supporting-resource shape, entrypoint reference links, unreferenced Markdown candidates, script/test presence, and explicit related-skill mentions. Use it when those structural facts could change a portfolio or placement decision.

The output is **not** a quality, focus, cost, or behavior score. A long skill may be appropriately deep; an unreferenced file may have a non-Markdown consumer; a related-skill mention may be necessary composition. Trace the actual loading/execution path before changing anything.

Standing model-behavior scenarios, judges, and run artifacts remain in the internal evaluation repository. Use those evaluations for selection/no-op/compression claims that deterministic structure cannot prove.
