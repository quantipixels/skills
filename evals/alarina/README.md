# Alárinà behavioral cases

Use one relevant case and a nearby control when selection, routing, authority or completion may change. These cases are optional model probes, outside package CI. Actor prompts and private expectations are paired by stable ID.

The [executable trial runner](behavior-trials.md) prepares disposable supplied-entry fixtures for A02/A06/A07/A09/A10/O06, captures bounded actor execution and independently checks the resulting artifacts. Its deterministic mechanics run in package CI; actual model trials and semantic judgments remain optional and separately evidenced. A13's container-selection scenario requires an actual suitable project container and remains distinct from fake-transport adapter tests.

| Lane | Cases | What it can establish |
| --- | --- | --- |
| [Native selection](triggers/cases.json) | T01, T05, T08; N01, N04; E01, E02 | Whether a clean host selects Alárinà for an engineering task, leaves an unrelated fact or uninvoked private-serving utility alone, and accepts exact qualified entry. |
| [Routing](dispatch/cases.json) | D01, D02, D05, D09; B01, B02, B06; C33, C34, C39 | Whether a loaded entry chooses the correct owner and stopping point, resists quoted instructions, and enforces explicit-only utility scope. |
| [Outcome](outcomes/cases.json) | O01–O05 | Whether supplied-entry writing, specification, decomposition and isolated implementation meet concrete acceptance criteria. O05 covers a replay repair and local/CI check inventory in a [small initial fixture](outcomes/fixtures/ledger-replay). |

Autonomous entry and handoff coverage adds native-selection cases T09–T11 and the incidental-keyword control N02; loaded-entry cases A01–A06 cover local delivery, planning-only scope, explicit PR publication, a missing human decision, advice-only questions and interrupted worker integration. Outcome O06 challenges a synthetic returned worker’s unsupported test claim and exercises hands-off continuation through an actual local repair. B06 remains the verification-only resumption control. Use the documented examples as actor requests, not as proof that the behavior occurred.

A07/A08 cover rough intent recovery and consequential scope clarification. A07 expects necessary in-scope work plus a concrete goal/current path in the existing plan; A08 must clarify the unresolved finish and data policy before dependent changes. These test the entrypoint’s inference boundary, not a requirement to ask for every omitted implementation step.

A09/A10 cover resumption from an incomplete planning task and from a relevant prior session when the plan link is missing. They require matching the intended work, reconciling current evidence and preserving the prior stopping point; the newest unrelated session does not replace the relevant one. Native history/workspace fixtures are needed for an executed recovery trial.

A11/A12 cover task-triggered check/lesson selection without command-name knowledge and the nearby recommendation-only exclusion. Scoped retrieval must establish current applicability; it must not replay stale recipes, search unrelated history or schedule a recurring job by implication.

These cases cover `autonomous`, `hands-off`, `AFK`, `end to end`, plain-name entry and resumption by meaning. Exact Codex/Claude qualification remains E01/E02; other native hosts need their own actual entry evidence. A word appearing in a prompt is not sufficient to select delivery: N02 and A02/A05 protect nearby exclusions. Keep missing-decision, real publication and native-selection results separate from an executed local outcome. A case added to this corpus is unexecuted until a result record identifies its candidate and observations.

The trigger lane requires a clean native host with only the candidate plugin and a trace showing actual selection. The routing lane begins after Alárinà has loaded; confirm successful reads of required methods rather than accepting filename mentions. The outcome lane checks the actual answer or artifact. No lane substitutes for another. Keep [expectations](triggers/expectations.json), [routing expectations](dispatch/expectations.json) and [outcome acceptance](outcomes/expectations.json) out of actor context.

Select a case for a consequential claim, use disposable inputs, and record host, model, candidate revision, invocation condition, tool results, interventions and the observed result. A correct answer without native selection is not a trigger pass. A supplied entrypoint does not establish implicit discovery. For comparative claims, run a compatible direct-owner arm and report no demonstrated advantage when both meet acceptance.

To inspect O05's starting state without changing the checked-in fixture, run from the repository root:

```sh
ledger_probe_dir=$(mktemp -d)
cp -R evals/alarina/outcomes/fixtures/ledger-replay "$ledger_probe_dir/ledger-replay"
cd "$ledger_probe_dir/ledger-replay"
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s unit
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s contracts
```

The starting state has two passing unit tests and one failing contract test. Supply only the copied fixture and O05 prompt to an actor; keep `outcomes/expectations.json` held out. The case stops at a local candidate: no publication, installation or network access. Local execution does not prove Linux/Python 3.12 CI or independent review.

[Prior bounded outcome observations](results/2026-09-25-luna-outcomes.md), the [historical selection probe](results/2026-09-25-luna-trigger.json), and [consolidation summary](results/2026-09-25-summary.md) retain their original candidate and limits. Those runs used the larger original corpora; their retired prompts remain in Git history. [Published-tag migration evidence](migration/2026-09-25-tagged-upgrade.md) and [local native manager evidence](migration/README.md) are historical operational proof, not new model trials.

The [bounded HTML and routing follow-up](results/2026-09-26-html-followups.md) records a six-run Codex workspace sample against the instructions at `34109b90`, including partial completion, unnecessary skill loading and invocation-namespace misses. It does not establish plugin activation or general improvement over v4.3.0.

The [planning and continuation check](results/2026-09-26-atona-boundaries.md) records four native Codex fixture runs around the `atona-plan` split. Both candidates respected planning-only scope and completed the requested implementation; the record preserves the collector failure and limits rather than claiming superiority.

The [engineering maturity evidence](results/2026-09-27-engineering-maturity.md) connects configuration, local gates, isolated records, workflow maintenance and provider mechanics to their executable tests and two supplied-entry observations. It records adopted and excluded mechanisms, review-driven corrections and remaining host/adoption limits.

The [CI-equivalence and adversarial follow-up](results/2026-09-27-assurance-followup.md) records fresh read-only assessments, an actual isolated replay repair, independent adversarial review and supplied-disagreement reconciliation, followed by targeted instruction revisions and an explicit-contract control. It separates parent-checked artifacts from worker reports, preserves inconclusive policy judgments caused by an ambiguous fixture, and compares this coverage with the inspected CE/PStack evaluation methods without claiming a comparative performance result.

The [release-readiness record](results/2026-09-27-release-readiness.md) joins the final policy limits, reproducible O05 fixture, retained CI evidence and current native-session observations. It preserves the distinction between a verified release candidate and a claim of long-term field reliability.

The [autonomous-entry and handoff follow-up](results/2026-09-27-autonomous-handoff.md) records the added selection/routing cases and one executed O06 integration probe. It distinguishes the parent-checked repair from unexecuted cases, native activation, live worker recovery and the later coordination-link clarification.
