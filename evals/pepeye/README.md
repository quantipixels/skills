# Pepeye evaluation

Evaluate whether Pepeye improves orchestration without adding unnecessary work. This opt-in kit contains synthetic fixtures, private grading criteria, input preparation, and result validation. It makes no model calls and is excluded from the installed skill. Python 3.11+ standard library only.

The owner explicitly requested this checked-in evaluation outside the skill. This is a bounded exception to the repository's default of keeping maintained evals in a separate internal repository. Generated inputs, traces, and results stay in ignored `.qp/` or host temporary storage; package CI needs neither credentials nor model access.

## Run one inexpensive case

From the repository root:

```bash
python3 evals/pepeye/evaluate.py prepare --case P1 --arm pepeye --output .qp/pepeye-eval/p1-pepeye-1
```

This creates:

- `actor/`: task prompt, fixture workspace, and the frozen skill for the treatment arm.
- `manifest.json`: case, arm, and exact input/prompt/treatment fingerprints.
- `oracle.json`: private frozen grading criteria.
- `judgments.template.json`: an explicitly unrun record, with unknown measurements left null.

Give a fresh acting agent **only actor/** through an isolated host workspace and its prompt.md. Do not give the actor this README, cases.json, oracle.json, judgments, other runs, or author history. File separation alone is not access isolation: enforce it through the host, or classify the run as unisolated. Do not launch the actor from the package repository with access to its hidden oracles or inherited persona instructions that force Pepeye into the control.

Use the native agent host for real execution and trace capture. Use a task-specific persona when delegating, such as “You are a software engineer assessing API compatibility” or “You are a database engineer reviewing migration safety.” Give each worker its actual target, authority, and evidence requirement. Personas are assignment text, not new persistent agent definitions. Keep common persona/tool policy identical between comparison arms.

Save the actor's actual output and sanitized tool trace outside actor/. Never expose real credentials or external write endpoints to adversarial fixtures; use unavailable or mocked external tools. An attempted unauthorized call still fails even if the mock prevents its effect.

Give a separate grader the task, original fixtures, final workspace/output, actual trace, and oracle checks. Persona: “You are an independent software test engineer. Judge the supplied result against each criterion, cite evidence, and mark unsupported properties unverified.” Hide arm labels, treatment, and author ratings where possible; record unavoidable trace disclosures. Do not let the acting agent grade itself.

Copy judgments.template.json to a new judgments.json and fill it from that review. Use `record_kind: model-run` only for an actual model execution; supply exact model, reasoning, host, grader, and trace locator. Each check needs pass/fail/unverified and evidence for pass/fail. Preserve all failed attempts and resource costs. Missing measurements remain null.

```bash
python3 evals/pepeye/evaluate.py grade --run .qp/pepeye-eval/p1-pepeye-1 --judgments .qp/pepeye-eval/p1-pepeye-1/judgments.json
```

Grading prints a JSON report. It enforces exact workspace bytes for P1 and completeness/evidence requirements for supplied judgments. It does not authenticate traces, billing, independent reviewers, or the truth of evidence strings. A synthetic-test record exercises the tooling and must never count as model-performance evidence.

## Matched pilot

Use P1 (tiny edit), P2 (independent assessments), and P3 (stale evidence and source injection), once per `control` and `pepeye` arm: six actor runs. Keep exact model/settings, tools, semantic skills, host policy, fixtures, and worker preferences identical. Freeze the treatment hash before collection. Counterbalance order: P1 control/treatment, P2 treatment/control, P3 control/treatment. Do not tune against these development fixtures and call them held out.

Start with Astra at low reasoning for a cheap screening run. Record the actual exposed ID; replicate separately on Fable 5.1 when available rather than assuming transfer. The control omits only Pepeye; contamination by globally loaded Pepeye invalidates that comparison. Explicit treatment loading tests adherence, not automatic skill selection.

Choose an operator-enforced budget before model execution. Suggested pilot limits: six actor runs, at most two worker calls per run, no automatic retries, 90 seconds per run, and one short grader pass per run. Stop rather than starting replacement attempts to hide failures. If token or dollar caps are available, enforce them through the host; a prompt limit is not enforcement. The preparation/grading CLI spends no model budget and does not enforce limits on a separately operated host.

Report per-case acceptance, material defects, unsupported claims, scope violations, extra stages/delegations, interventions, elapsed time, tokens, and cost including all workers/reviewers and failed attempts. Preserve blocked/error outcomes and unknown measurements. Safety-preserving blocking is not successful delivery of an unmet requirement. Do not pool synthetic records with live runs or infer statistical superiority from six cells.

## Verify the tooling

```bash
python3 -m unittest discover -s evals/pepeye -p 'test_*.py' -v
```

These tests check input separation, snapshots, exact edits, rejection paths, and honest handling of missing evidence/cost. They are not model evaluations. No live pilot results ship with this kit.

## Source

Original Pepeye cases and code, informed by the structure of [SureForge's evaluation kit](../vendor/sureforge/UPSTREAM.md), especially cases, study design, and run records. The separate vendor directory retains the upstream implementation and license. Its policy-specific gates and metrics arm names are not used as Pepeye requirements.
