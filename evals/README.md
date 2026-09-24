# Focused checks and optional comparisons

Use evaluations to expose consequential regressions and misdirection, not to certify every skill or preserve a preferred workflow. Keeping a case, running it now, and maintaining its execution machinery are separate decisions.

## Retain useful cases

Before maintaining or running a case, be able to name the failure it detects, the decision its result changes, and why a cheaper check is insufficient. Record these in the existing case or run notes where not obvious; no new registry or mandatory metadata schema is needed. Separate observed failures, synthetic probes and never-run expectations.

Keep a case when it captures a relevant failure mechanism, important contract or useful control, has a clear way to judge the result, and repays its maintenance. Small, synthetic or unrun cases can be useful; none is evidence of success until executed. A simple control can detect unnecessary work just as a difficult case can detect missing work.

Consolidate duplicated setup and genuinely overlapping questions. Retire obsolete obligations, intentionally unsupported coverage and low-signal quizzes that only repeat the requested owner or tool. For a claimed replacement, identify the surviving check and its scope; sharing a topic does not make a routing probe, direct invocation and executed outcome equivalent. Keep actor inputs and private expectations aligned, preserve stable case IDs, and reconcile live references. There is no target case count or deletion percentage.

## Run only the relevant boundary

Start with the actual change and the bad decision or regression it could cause. Prefer source inspection, direct script execution or existing project proof when those can answer it. Use a model eval for a material judgment, routing/completion change, model-dependent regression or comparative claim that simpler checks cannot settle.

Select one relevant task and its necessary contrast: authorized versus unauthorized action, adequate versus missing evidence, or work versus justified inaction. Do not run a whole omnibus file merely because it contains that task. Supply only the selected request and necessary setup, not neighboring requests, answers or reviewer criteria. Keep distinctions between direct invocation, routed work and native discovery explicit; do not quietly substitute one for another.

Use safe disposable inputs. Record the source, invocation condition, actual outcome, interventions and material limits in the existing task record. Judge consequences and artifacts, not skill-name mentions, tool-call choreography or preferred phrasing.

Use actual corrections and successful controls to select cases before inventing more categories. Review the relevant input, actions and results when final-output inspection cannot locate the failure. Targeted or diversity-based samples help discover failures; representative sampling is needed to estimate prevalence.

End a comparison with the concrete keep/change/reject/inconclusive decision it supports. If both candidates meet acceptance, report no demonstrated advantage rather than inventing a winner from wording or length. Retire a case when its obligation is obsolete; otherwise distinguish justified dormant coverage from a routine gate nobody needs to run.

`qp-update`, `system-cleanup`, `pese` and similar utilities have no standing model-eval requirement. Native checks can establish mechanical behavior; a targeted model probe may establish whether the agent chooses or declines an operation appropriately. Never test by mutating the user's real installation, home directory or serving configuration. Effective permissions, privacy and cleanup need operational evidence, not promised actions.

Use selected [coordination and judgment cases](coordination/README.md), [PR evidence cases](pr-review/README.md), [engineering tasks](engineering/README.md), [project-backed protocols](engineering/scenarios/README.md), or a more representative real task. Retain useful counterexamples without putting them in routine CI. An inconclusive or no-improvement result is valid.

## Controlled comparisons

This repository owns its evaluation method here. Installable skills supply capabilities; `oro` authors instructions, and the requesting workflow decides whether evidence justifies retention. A one-off comparison needs no new framework or permanent benchmark.

1. **Freeze the question.** Pin baseline, candidate, task, acceptance, useful improvement threshold and finite run budget. Name the claim: discovery, selection, loading, execution or incremental benefit. Supplying guidance bypasses discovery; a plausible answer or source check is not a model trial.
2. **Control the run.** Vary the intended factor; keep other model, effort, tool, permission and workload conditions compatible. Use fresh sessions or host-controlled equivalents. Separate directories alone do not isolate history. Supply only realistic inputs and necessary contracts; withhold private criteria and other actors' answers. Include a nearby inactive case when testing selection.
3. **Inspect evidence.** Prefer executable acceptance for objective properties. For interpretation, judge concrete failure conditions with cited artifacts or traces. Self-reports do not prove loading or tool use. Inspect changes to tests that could hide failures. Keep completed, failed, blocked and invalid runs distinct; a checker defect requires reassessing every affected arm. Rechecking an artifact is not a fresh run.
4. **Decide within the evidence.** Record retries, corrections, interventions and costs; unavailable telemetry is unknown. Allow for variability and confirm promising results on fresh or held-out tasks before broad claims. Both arms passing demonstrates no advantage. Report keep/change/reject/inconclusive, limitations and adoption state. Stop at the declared budget or a supported decision; final edits that change the tested behavior invalidate affected comparisons.

For a small review, explicit acceptance and decisive evidence are enough; label uncalibrated model judgment as advisory. Before relying on a model judge at scale, compare it against qualified human labels on separate development and held-out examples. Keep related variants in one split. Inspect false passes, false failures and human disagreement separately. Choose tolerances from consequences, report counts and uncertainty, and revisit calibration when the judge or task distribution changes. No universal sample quota or overall quality score substitutes for this evidence.

## Mechanical checks

For a script, run its real command on representative disposable inputs and inspect output and exit status. Retain a narrow rejection check when a good-input run could hide false success, data loss, an authority violation or failed process cleanup. A help command or exit zero alone cannot establish these properties.

The regular package workflow runs:

```sh
python scripts/skills/check_package.py
python tests/smoke_package.py
python scripts/skills/test_session_evidence.py
python scripts/plugins/test_verify_native_install.py
```

The session check executes the actual script on temporary transcripts. Installer checks protect identity, timeout and process cleanup; they are not model evaluations of `qp-update`. These commands neither install a plugin nor run a model.

The existing engineering evaluator owns summaries, independent oracles and evidence-integrity checks. Keep its stale, tampered, empty-result and incorrect-candidate rejection tests; one successful candidate cannot establish rejection behavior. Its separate workflow runs for checker/fixture changes or manual dispatch without model credentials, not as a skill-effectiveness gate.

Historical observations retain their original evidence cut and provenance. Generated runs and private traces stay ignored in `.qp/` or external storage. Changing a task, rubric or invocation condition invalidates direct comparison with older runs; record the new source rather than updating historical verdicts. Earlier structure drew on [SureForge](vendor/sureforge/UPSTREAM.md); attribution and license remain.
