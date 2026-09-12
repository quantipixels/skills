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

Portfolio-wide routing footprint matters because many installed skill names/descriptions may be visible together. Treat total routing words/characters and lexical overlap between descriptions as audit leads, not thresholds or redundancy verdicts. A pair that shares vocabulary can still be well separated by result ownership; a pair with little lexical overlap can still collide behaviorally.

## Keep the entrypoint focused

Every instruction in the entrypoint should do at least one useful job:

- change a recurring non-obvious decision;
- establish an execution/completion gate;
- provide expertise the model would otherwise guess poorly;
- protect an authority, safety, evidence, ownership, routing, compatibility, or recovery boundary; or
- point reliably to selectively loaded depth.

A sentence is a **no-op candidate** when removing it is unlikely to change selection, action, evidence, or a necessary boundary on the target hosts/models. Do not delete it by intuition alone when behavior matters: compare realistic tasks in the internal evaluation path. Conversely, do not retain prose merely because it sounds prudent.

Prefer stating the positive target behavior. Keep explicit prohibitions when they protect a hard safety/authority boundary or when the positive form does not prevent a demonstrated failure.

## Compare skill value with native frontier capability

Do not assume an instruction earns its place merely because older models needed it. For a material claim that guidance is redundant, or that a simplified skill preserves quality, compare the same realistic task across:

1. the ordinary/current frontier host or model **without the skill**;
2. the current skill; and
3. the candidate skill.

Hold task, evidence, permissions, tools, and host configuration constant enough to isolate the behavioral claim. Judge the owned outcome, domain decisions, authority/safety compliance, proof quality, unnecessary tool/subagent work, context pressure, premature stopping, and scope drift as applicable.

An adequate no-skill baseline is evidence that generic diligence, planning, delegation, verification, or recovery prose may add no marginal value. It is not evidence that skill-specific expertise, workflow topology, project conventions, completion semantics, or authority boundaries are unnecessary.

When behavior differs materially across model families, prefer one portable semantic contract plus thin host/provider policy over copying whole skills into model-specific variants. Preserve model-specific instructions only when evidence shows the difference matters.

## Optimize semantic load, not contract count

Compression is not successful merely because the entrypoint is shorter. Before pruning, compare the old and proposed semantic contracts and classify every meaningful loss as **redundant**, **relocated**, **compatibility-only**, or **retired**.

A rule is not redundant merely because another sentence sounds similar. Verify that the replacement preserves the same trigger, authority, evidence requirement, exceptional case, and loading path. Pay particular attention to:

- safety and mutation/publication authority;
- proof/evidence admission and contamination rules;
- routing/selection and missing-owner behavior;
- provider, candidate, base, or source identity semantics;
- recovery, retry, cancellation, liveness, and operational safeguards;
- explicit legacy invocation/result compatibility; and
- negative boundaries whose absence would cause consequential guesswork.

When detail moves behind a reference, the entrypoint must still state a reliable load condition. When a public or explicit legacy behavior stops driving normal selection, preserve it as compatibility-only unless an intentional breaking change/versioning decision retires it.

For a material refocus or pruning change, perform a **loss audit** as part of the diff review: ask what the old skill could do, protect, distinguish, or accept that the candidate no longer can. Record meaningful dispositions in the PR/discussion so reviewers can distinguish deliberate retirement from accidental deletion. This is change evidence, not a new documentation artifact.

## Separate semantic workflow from runtime mechanics

A recurring multi-stage outcome may justify explicit workflow topology even when a capable model can infer many intermediate actions. Keep declared workflow information when it changes ownership, ordering, branch/recovery behavior, independence, acceptance, or terminal closure. Do not duplicate the method of each stage inside the workflow.

Likewise, an assignment may need exact authority, workspace, candidate identity, evidence, and independence boundaries without needing a permanent declared agent persona or detailed worker choreography. Prefer skill-owned semantics + workflow progression + runtime-selected agents unless a persistent identity or durable orchestration program has independently earned its place.

## Place pressure where it is cheapest

Different agents or phases carry different context pressure. An implementer often needs exploration, source, tests, failures, and edits in the same window; a reviewer can usually start from a bounded candidate and review contract. Put review-only standards and smell catalogues in review context rather than taxing implementation, unless the implementer genuinely needs the rule to produce the required result safely.

Likewise, keep setup, provider, platform, or language-specific detail behind a condition that selects it. Do not move independently loaded safety/authority rules behind an optional reference merely to reduce tokens.

## Use structural evidence carefully

`../scripts/skill-doctor.py` can inventory routing-pointer size, entrypoint size, supporting-resource shape, entrypoint reference links, unreferenced Markdown candidates, script/test presence, explicit related-skill mentions, portfolio routing footprint, and description-overlap leads. Use it when those structural facts could change a portfolio or placement decision.

The output is **not** a quality, focus, cost, routing-behavior, or redundancy score. A long skill may be appropriately deep; an unreferenced file may have a non-Markdown consumer; a related-skill mention may be necessary composition; lexical overlap may be justified terminology. Trace the actual loading/execution path before changing anything.

Standing model-behavior scenarios, judges, and run artifacts remain in the internal evaluation repository. Use those evaluations for selection/no-op/compression claims that deterministic structure cannot prove.
