# Corpus analysis

Load this reference only when the evidence unit is a bounded multi-session corpus. Keep the common causal method, recommendation standard, and final judgment in `SKILL.md`.

## Pin the corpus

Pin the time range, session roots, repositories, inclusion and exclusion rules, selection method, and requested output before drawing conclusions.

Inventory the corpus before sampling. Distinguish a user task, root session, resumed or copied history, rollout file, and subagent rollout. Do not treat rollout count as task count, first-to-last span as labour time, or repeated transcript content as independent evidence.

For a large corpus, use deterministic extraction for counts and metadata, then read the smallest representative and risk-weighted sample that can answer the question. Record the population, sample, exclusions, and evidence gaps.

## Reconstruct bounded causal records

Reconstruct bounded causal records for the sampled sessions. Do not invent one global timeline or infer the same contract across different tasks. Include contrasting successful or uneventful records when they can disprove a claimed pattern.

Call a pattern repeated only when the same material mechanism appears in at least two independent root sessions. Report its supporting records, eligible denominator when known, counterevidence, and coverage limit. Keep a single incident labeled as an incident even when it produced many subagent rollouts or repeated recovery attempts.

Normalize corpus counts to the pinned unit and report the numerator, denominator, and exclusions when they matter. Use counts and elapsed time only when the record supports them.

### Experimental opportunity ledger

When the corpus is being used to evaluate Experimental skills, reconstruct opportunity separately from invocation.

For each root session and experiment in scope, classify only when evidence supports it:

- `ELIGIBLE_SELECTED` — the experiment was installed/active/discoverable, its owned result was materially needed, and it was selected;
- `ELIGIBLE_MISSED` — the experiment was installed/active/discoverable and its owned result was materially needed, but it was not selected;
- `MIS_TRIGGERED` — it was selected without the owned result being materially needed or outside its intent/authority/cost boundary;
- `INELIGIBLE` — the owned result was not needed;
- `UNAVAILABLE` — the result was needed but the skill was not installed/active/discoverable or a named capability blocked it; or
- `UNCERTAIN` — evidence cannot responsibly establish opportunity or availability.

For `ELIGIBLE_SELECTED`, record what materially changed because the experiment ran, its incremental cost, and whether it preserved the stable owner's lifecycle/result/authority. For `ELIGIBLE_MISSED`, identify the observed consequence only when the record supports it—for example duplicated specialist work, weaker evidence, rework, or a later correction. Do not invent counterfactual time/token savings.

Raw invocation count is never the denominator. A rare experiment may be healthy with very few uses if it was selected in the few genuinely eligible sessions. Conversely, frequent invocation can be negative evidence when it is repeatedly mis-triggered or adds no independent value.

Do not manufacture experiment invocations during real user work to improve sample size. The corpus observes natural eligible opportunities; temporary controlled steering comparisons belong to skill evaluation only when selection behavior remains materially uncertain.

## Report the corpus

Return the executive verdict, population and unit definitions, inventory and sampling ledger, repeated-pattern matrix with independent supporting records and counterevidence, representative causal chains, ranked frictions, effective recoveries, recommendation assessment, rejected recommendations, and residual limits.

When Experimental evaluation is in scope, also return the opportunity ledger per experiment: eligible denominator, selected/missed/mis-triggered/unavailable counts, incremental value/cost evidence, boundary-health observations, and unresolved evidence gaps. Leave promotion/narrow/fold/replace/remove disposition to `ko-skill` unless that judgment is explicitly requested through the owning workflow.

When the corpus spans projects, include one dossier for every normalized project in the population, not only sampled or problematic projects. Each dossier must state:

- aliases and evidence coverage;
- outcomes and verified current state;
- user actions and decisions;
- effective work;
- failures, inefficiencies, and gaps;
- applicable lessons;
- recommendations and no-change findings;
- counterevidence; and
- limits.

Classify each durable decision or lesson as implemented, still applicable, superseded, or unresolved, and name its owning project document, skill, test, or workflow when known. Link aggregate patterns to their project dossiers; do not use the aggregate to replace project-level analysis.

When skill corrections are authorized, distinguish source, installed, published, and active states.
