---
name: alaga
description: Deliver one supplied build job from settled outcome through implementation, proof, review, and handoff. Use for a bounded test-first feature/fix or any build/migration requiring an exact reviewed candidate. Exclude pure explanation, bare review, monitoring, and provider publication except where they support delivery.
---

# Alága

Deliver one supplied job as a coherent proved result. Use `test-first` for a bounded behavior change that warrants TDD; otherwise use `job`. A job is the complete requested outcome; delivery units are only useful existing slices inside it.

## 1. Map the job

Pin outcome, current/desired behavior, scope, exclusions, acceptance, proof, documentation destinations, workspace, and authority. Name the minimum real user/operational path that must pass.

Respect explicit owner/tool choices. Use the shortest combination of current specialists and direct work. Supporting owners retain their native procedures/results; Alága owns integration and job acceptance.

Derive one session policy only where it changes execution: horizon, commit granularity when authorized, continuation boundary, and extra research/evidence needs. Repository/Git state never grants commit, history-rewrite, publication, provider-write, or destructive authority.

Read relevant root `.learnings` and complete `.nongoals` when present. Use `arojinle` for unresolved material user choices, `solution-architect` for material technical architecture, `atona` when an initiative plan must remain live, and `seda-ticket` only when supplied work benefits from consumable vertical tickets.

Read [job report](references/job-report.md) when the job is multi-candidate, blocked/handoff-prone, migration/security/recovery sensitive, externally destructive, or otherwise meets that reference's report gate. Reuse an active Atọ́nà plan instead of creating a parallel job report.

## 2. Deliver and prove

Prepare the workspace without disturbing unrelated changes. Continue through the confirmed horizon until completion, a material decision/authority gap, or no safe independent work remains.

Use the proof owner for each unit. When production behavior changes or test-first work is requested, apply [TDD](references/tdd.md) in coherent green slices. Run focused/affected proof per unit, then job-level integration/acceptance proof.

Before a planned stateful refactor/rewrite can change transitions, ordering, locking, retries, idempotency, ownership, or cross-entry behavior, require exact-current Àtúnwò `audit` and consume its contract/guardrails as implementation input.

If one unit blocks, continue independent in-scope work and record the blocker, affected dependencies, proof, and exact resume trigger.

Dispatch a subagent for bounded independent delivery, analysis, etc support when it materially improves progress or evidence.

## Exact uncommitted candidate identity

Use Git's native content-addressed tree rather than a QP fingerprint runtime. For selected uncommitted paths, create a temporary index/object directory so the real index, refs, and ambient worktree remain untouched:

Before creating the temporary index, query the real index for selected unmerged entries:

```bash
git ls-files -u -- <selected-paths...>
```

If any selected path has stage 1, 2, or 3 entries, stop and record the conflict paths. Do not turn conflict-marker worktree content into an ordinary stage-0 review candidate.

```bash
tmp=$(mktemp -d)
real_objects=$(git rev-parse --git-path objects)
real_objects=$(cd "$real_objects" && pwd)
mkdir "$tmp/objects"
export GIT_INDEX_FILE="$tmp/index"
export GIT_OBJECT_DIRECTORY="$tmp/objects"
export GIT_ALTERNATE_OBJECT_DIRECTORIES="$real_objects"

git read-tree HEAD
git add -A -- <selected-paths...>
candidate_tree=$(git write-tree)
```

Record:

```text
HEAD: <git rev-parse HEAD>
Tree: <candidate_tree>
Paths: <exact selected paths>
Ambient: <other uncommitted paths, if any>
```

`git add -A -- <paths>` captures modified, deleted, untracked, binary, and symlink entries inside the selected boundary. It writes temporary Git objects only under `$tmp/objects`; it does not stage the real index or create a commit/ref. When concurrent work could change the selected paths during capture, build the temporary tree twice and require identical tree SHA before review. Remove the temporary directory after the candidate identity is recorded.

Use the whole worktree only when the whole worktree is intentionally the candidate. Keep unrelated/ambient changes outside the selected path set.

Before review, update required ordinary documentation in the candidate and use `amose` when verified delivery changes durable project knowledge.

## 3. Review and converge

Review each stable, understandable, verifiable, reversible candidate once. Keep dependent changes together when separation creates a broken intermediate result; split independent candidates.

After implementation proof is green, source code/tests require broad `atunwo`. Other candidates use their native verification/review owner. Findings remain hypotheses until verified.

Apply behavior-changing corrections through TDD/proof owner, recapture the exact candidate, rerun invalidated proof/review, and do not finish with a blocking finding or material evidence gap.

Close a candidate only after acceptance, proof, documentation, and required review pass. Close the job only when every in-scope unit maps to the requested outcome and job-level integration/acceptance passes.

## 4. Report

Return job boundary/session policy, delivered units, documentation, proof/review, commit state, exact candidate identities, blockers/residual limits, remaining work, and next safe action. Return generated artifact paths from their owning skill. Publication remains with `seda-pr`.
