# Alárinà behavioral cases

Use one relevant case and a nearby control when selection, routing, authority or completion may change. These cases are optional model probes, outside package CI. Actor prompts and private expectations are paired by stable ID.

| Lane | Cases | What it can establish |
| --- | --- | --- |
| [Native selection](triggers/cases.json) | T01, T05, T08; N01, N04; E01, E02 | Whether a clean host selects Alárinà for an engineering task, leaves an unrelated fact or uninvoked private-serving utility alone, and accepts exact qualified entry. |
| [Routing](dispatch/cases.json) | D01, D02, D05, D09; B01, B02, B06; C33, C34, C39 | Whether a loaded entry chooses the correct owner and stopping point, resists quoted instructions, and enforces explicit-only utility scope. |
| [Outcome](outcomes/cases.json) | O01–O05 | Whether supplied-entry writing, specification, decomposition and isolated implementation meet concrete acceptance criteria. O05 covers a replay repair and local/CI check inventory in a [small initial fixture](outcomes/fixtures/ledger-replay). |

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
