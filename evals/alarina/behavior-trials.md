# Optional executable behavior trials

`scripts/skills/run_behavior_trial.py` prepares disposable local projects for A02, A06, A07, A09, A10 and O06. These are optional model probes outside package CI. It reads existing case prompts but does not pass expectations to the actor. The actor receives a prompt path and a disposable project path. This runner is not an operating-system sandbox; use an actor whose filesystem permissions fit the trial.

```sh
python3 scripts/skills/run_behavior_trial.py prepare O06 /private/tmp/o06-trial
```

To drive a CLI actor, create a JSON file with its exact argument vector, for example `["python3", "/absolute/path/to/actor.py", "{prompt_file}", "{project_dir}", "{response_file}"]`. Placeholders must be complete array elements. The runner invokes no shell. Do not put secrets in the argv file because the receipt records the expanded vector.

```sh
python3 scripts/skills/run_behavior_trial.py run /private/tmp/o06-trial --argv-json /private/tmp/actor-argv.json --timeout 120 --host local --model example-model
python3 scripts/skills/run_behavior_trial.py assess /private/tmp/o06-trial
```

`prepare` supplies the candidate entry path in the actor prompt and pins the selected prompt, initial fixture and complete skill directory by SHA-256. Use `--skill-source` only when evaluating a different explicit candidate. `run` rejects changed prepared inputs, records actor argv plus any supplied host and model labels, and returns a failure status for a failed, timed-out or unlaunchable actor. `assess` also returns a failure status for invalid trials and failed mechanical assertions. The result `assertions-pass` means the checks passed; it is not an entire behavioral-case verdict.

The assessor probes replay behavior and label normalization from the final files. For planning cases, it permits edits to `plan.md` and rejects source or history mutation. It reports output presence without judging whether the wording preserves the unresolved decision. A07 permits plan updates and leaves semantic plan retention to human review. A09 includes a relevant incomplete migration session and a newer unrelated documentation session. A10 has a missing plan link, a relevant handoff, an unrelated session and stale proof; its initial implementation is correct, so only verification remains. A06 and O06 start with a synthetic returned candidate whose claimed pass is false. No case represents a live native worker.

For manual host driving, `prepare` creates the same prompt and project. The automatic assessor requires a completed `run`; record native host observations separately with the exact host, model, candidate revision, invocation and artifacts. Native selection and installed-host behavior remain unobserved by this runner.

`private/assessment.json` records changed files and independent local probes. A passing assertion does not establish that the actor ran its own tests or followed the right reasoning path; inspect actor logs and response for those claims. Actor stdout and stderr are streamed and retained up to 64 KiB each, including on failure. Run time is bounded to 1–600 seconds, and the owned POSIX process group is cleaned up after success, timeout or interruption. Assessment probes use the same bounded collector.

Run the deterministic runner tests with:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts/skills -p test_behavior_trial.py -v
```
