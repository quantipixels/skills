# Focused checks and optional comparisons

Choose proof for the changed behavior, not a test suite for every skill. Routine wording, utility and documentation edits do not require model evaluations.

## Start with execution, not an eval

For a script, run its real command with representative disposable inputs and inspect its output and exit status. Add a small failure check when a happy-path run could falsely report success, cross a permission boundary, lose data or leak a process. A help command or exit zero alone does not establish those properties. Do not build a test framework around routine parsing or formatting.

The regular package workflow runs:

```sh
python scripts/skills/check_package.py
python tests/smoke_package.py
python scripts/skills/test_session_evidence.py
python scripts/plugins/test_verify_native_install.py
```

The session check already invokes the actual script on temporary transcripts. Installer tests retain identity, timeout and process-cleanup safeguards; they are mechanical tests, not evaluations of `qp-update`. These commands neither install a plugin nor run a model.

`qp-update`, `system-cleanup`, `pese`, and similar operational skills have no standing model-eval requirement. Inspect changed instructions and native invocation controls; use an authorized dry run or disposable fixture when execution evidence is needed. Never test a cleanup or update by mutating the user's actual installation, home directory or serving configuration. Printed plans do not prove effective permissions, privacy or cleanup.

## Use a model eval only when it can change a decision

A useful eval addresses a consequential unresolved judgment, a material routing/completion change, a model-dependent regression, or a comparative improvement claim that source inspection and script execution cannot settle. State the question and the result that would change the decision first. Reuse one relevant task and a useful counterexample; do not run the whole catalogue or create one pack per skill.

Examples worth retaining include causal diagnosis, populated-data migration, preserving accepted decisions on resumption, authorization versus requested action, independent review and reconciliation of conflicting sources. A utility can warrant a targeted safety probe after an observed failure or material authority change; that is an exception with a concrete question, not routine certification.

Use selected [coordination cases](coordination/README.md), [engineering tasks](engineering/README.md), [project-backed protocols](engineering/scenarios/README.md), or the actual project. `adanwo` owns a finite matched comparison when an improvement claim needs one. Judge artifacts and observed behavior, not skill names or preferred prose. Native hosts own execution and isolation. Record the exact source, actual run, counterevidence and limits; a source check, replay or plausible answer is not a fresh model result.

## Keep only useful machinery

Use the existing engineering evaluator's `summary` command for evidence; there is no extra report wrapper. Keep its independent oracles and integrity/rejection tests: running the checker successfully on one good candidate cannot show it rejects stale, tampered, empty or incorrect results. The separate engineering workflow runs those tests for checker/fixture changes or manual dispatch, without model credentials. It is not a skill-effectiveness gate.

Historical observations retain their original evidence cut. Generated runs and private traces stay in ignored `.qp/` or external storage. Do not add a permanent case unless a recurring decision or important regression earns it. Earlier structure drew on [SureForge](vendor/sureforge/UPSTREAM.md); attribution and license remain.
