# Engineering playbooks

Start with the result you need. With `alarina` active, describe the work normally: “Find and fix this defect,” “Explain this profile,” or “Make this service repeatably verifiable.” Alárinà selects and loads the applicable playbook, invokes the existing owners, and carries the work to your requested stopping point.

You can steer it explicitly: “Use alarina's Data change playbook; planning only,” or “Use the Bug fix playbook to verify this existing repair.” Playbook names select routes inside Alárinà; they are not separately installed skills or new slash commands. The host still controls how Alárinà itself is loaded. See the [session setup](../README.md) if you want its operating method throughout a session.

The twelve supported paths are Feature delivery, Investigation, Bug fix, Performance improvement, Data change, Project verification, Test-suite improvement, Skill evaluation and improvement, Architecture evolution, Incident recovery, Release and rollout, and PR readiness. Feature delivery and PR readiness use their existing workflow owners. The other compositions live with [Alárinà](../skills/alarina/SKILL.md); specialist methods stay with their skills.

Existing plans, accepted decisions and current proof carry forward. A settled coding change can go directly to `alaga` with its existing tests; selecting a playbook does not require another plan, agent or review. The examples below also work as direct specialist requests.

## Make the project repeatably verifiable

> Use alaga to establish a repeatable journey through this service's public API, including persisted effects and cleanup. Reuse the existing harness. Use oro if reusable project verification instructions are needed.

A useful result includes the actual startup/readiness command, safe fixtures, public operation, expected effect and owned-resource cleanup. If repeated work warrants a project-local verification skill, its instructions should be grounded in the working harness and exercised before handoff. Resolve non-obvious command or readiness semantics from the project and host.

For example, call the API to create an item, restart the service against the same test database and retrieve the item through the API. That checks a public journey and persistence across restart. It does not establish every transaction or recovery guarantee of another database engine.

> Audit the affected verification recipes after these API changes. Separate stale instructions, harness limitations and product regressions.

Correct a stale route or selector from evidence. If the product stopped preserving required data, keep that failure visible and return it to `alaga`; do not make the recipe green by deleting its expectation. A full verification-map audit covers its requested map. An ordinary change needs affected journeys, not a new full-product test cycle.

Owners: [Alága](../skills/alaga/SKILL.md), [Oro](../skills/oro/SKILL.md), and the project's existing verification capability.

## Explain a slowdown, then test a worthwhile improvement

Build and CI optimization use this same path. For example: “Reduce this build's waiting time while preserving its required checks and outputs.” Compare the relevant clean and incremental workloads, include cache conditions, and verify that a real input change invalidates the affected output. A warm no-op build is insufficient evidence.

> Use alaga to diagnose this CPU profile and thread dump. Resolve capture interpretation from the project and host when needed. Return the supported mechanism and evidence limits; stop before changing code.

A profile shows where sampled time was spent. A heap capture can show what retains an object; a thread dump can show a blocked wait. These observations narrow an investigation. Neither a hot function nor an improved second capture alone proves the cause. Useful output identifies the capture, relevant path, source attribution and any missing discriminator.

> Use adanwo to compare a bounded improvement to the measured bottleneck. Preserve the existing correctness and response-time obligations.

Let the cost suggest the experiment. Repeated fixed network overhead may justify batching; repeated identical work may justify caching with an invalidation rule. Batching can improve throughput while worsening the latency someone waits for. A useful result compares the same representative workload, rejects broken candidates and reports a supported improvement or an honest inconclusive result.

Owners: [Alága](../skills/alaga/SKILL.md), [Àdánwò](../skills/adanwo/SKILL.md), and the relevant project measurement capability.

For sustained optimization, give Alárinà a target and budget: “Improve this pipeline within the available experiment budget, retaining only confirmed gains.” The same Performance improvement path records attempted hypotheses, confirms promising changes and stops at the target, budget or exhausted useful options.

## Improve an expensive or unreliable test suite

> Use alarina to reduce the maintenance and runtime cost of this suite while preserving its required behavior checks.

The Test-suite improvement playbook establishes what actually runs, where time or flakiness comes from, and which current proof protects each affected obligation. `atunwo` assesses suspected weakness or duplication, and `alaga` applies justified changes. Use the project's existing measurements when they can settle a specific proof question; they are not required for every cleanup.

For example, several tests may repeat the same receipt assertion while one slower integration test protects recovery after a lost reply. Similar names or higher runtime do not make that integration test redundant. Return the retained obligations, concrete changes and evidence of lower cost or better defect detection.

## Settle a choice with a disposable prototype

> Use alarina to help decide whether this API should expose a synchronous result or a job handle. Build only the smallest useful experiment; do not implement the product change.

This goes to `adanwo` in exploration mode. The result is an inspectable API exchange, interaction or other disposable artifact that settles the named uncertainty. Return its evidence to the deciding owner; a promising prototype does not itself authorize production adoption.

## Prepare a safe data change

> Use atona to make this backfill plan ready to execute. Include the existing-data mapping audit, rollout order, stop conditions and recoverability. Planning only.

Walk the affected contract before choosing machinery: how does an old record become a new one, what can readers see during partial completion, and what must a retry preserve? A precise question such as “Does this timed-out request already have a completed remote effect?” is more useful than a generic request for more edge cases.

Ask `alaga` for checks against representative populated data. Verify each old/new mapping, nulls, relationships and lossy conversions. Compare generated schema changes with the actual migrations in the diff. Account for legitimate concurrent writes when comparing counts; an unchanged count is not automatically the invariant.

The plan should contain executable preflight and post-change checks with expected results, plus the conditions that stop progression. Reverting code is different from restoring data. A backup needs a workable recovery path that accounts for later writes. Existing migration/restart tests remain useful, but a test on an empty database cannot establish preservation of historical meaning.

Return the current human-readable plan and unresolved decisions. Commands in a planning result have not been executed, and planning does not authorize a live rollout.

Owners: [Atọ́nà](../skills/atona/SKILL.md), [Alága](../skills/alaga/SKILL.md), [Architect](../skills/architect/SKILL.md) when sequencing or recovery design remains open.

## Recover an active disruption

> Use alarina to restore this affected service within the approved runbook. Verify the user journey and report any remaining data or backlog consequences.

Incident recovery uses `alaga`'s recovery method and the project's operational capability. Capture decisive evidence, choose a bounded intervention with a known stop condition, and verify the affected outcome. Reversible mitigation may be justified before the causal explanation is complete. A healthy process alone does not establish that users can complete their work or that delayed effects are safe.

Recovery, permanent repair and a later postmortem are separate results. Continue only the outcomes included in the request; uncertainty about an external effect calls for reconciliation before replay.

## Release an accepted candidate

> Use alarina's Release and rollout playbook to prepare this package release. Planning only; include consumer compatibility and how we will verify the published version.

Atọ́nà incorporates rollout readiness into the current plan. The project's release capability executes publication or deployment when authorized, and its verification capability checks the actual released candidate. A package consumer should resolve and use the intended published version; a service check should reach the deployed user boundary. Preserve actual effects when a release partially succeeds and recovery must be chosen.

PR status remains PR readiness. A data migration inside a release uses the existing Data change method within the same plan.

## Resolve a difficult failure without guessing

> Use alaga to diagnose why this request succeeds at the API boundary but produces the wrong worker result. Keep the probe bounded to the affected path.

Use an existing correlation identity to compare the relevant inputs and outputs across the API, queue and worker. The first observed divergence narrows the failing boundary; further evidence must establish its mechanism. Capture only safe, necessary fields.

> This test passes alone but fails in the suite. Find the smallest repeatable preceding sequence and explain the cause.

Pin the seed, runner mode and environment. Reduce the sequence while preserving the same failure and interacting prerequisites. State leakage is one candidate; resource pressure or concurrency can also explain the difference. A minimized reproducer is useful because it makes those alternatives cheaper to test.

> Check whether this existing PR fixes the reported failure. Search relevant prior attempts if they can change the investigation. Verification only.

Use exact baseline and repaired candidates with comparable inputs and reset state. Show the original failure and the required repaired behavior. If the baseline no longer reproduces, report the missing comparison rather than presenting a positive-only demonstration as proof. Search relevant open work before authoring a duplicate repair.

Owner: [Alága](../skills/alaga/SKILL.md); [Àtúnwò](../skills/atunwo/SKILL.md) supplies independent judgment when requested or useful.

## Improve a design while preserving its contract

Dependency and framework upgrades use Architecture evolution. For example: “Assess and carry out this accepted framework upgrade.” Recover the current integration's purpose, check official compatibility and migration requirements, account for affected consumers and transitive dependencies, and verify the migrated behavior. The useful result is a supported improvement with known migration and maintenance costs.

> Use architect to assess this workaround. Recover the constraint it serves and determine whether it still applies. Do not implement a replacement yet.

Follow the substantive change through relevant history, review discussion, incidents and tests. Distinguish stated rationale from inference. A strange implementation may protect an uncommon supported case; its age alone is not a reason to remove it.

> Use architect to reduce the repeated guards around these state fields. Explain which invalid combination the proposed representation prevents.

For example, a completed variant can carry its required completion time, avoiding disagreement between a boolean and an optional timestamp. Strengthen a type where a real operation requires it. A summation function can still accept an ordinary empty collection; precision that protects nothing adds burden.

> Use alaga to refactor this accepted boundary, preserving its public behavior and reducing the identified caller burden.

Name retained behavior and reuse current proof. Add characterization or differential checks only for a real gap, move in bounded verified steps and account for dynamic callers during renames. Keep supported compatibility paths until their consumers can migrate. Explain the responsibility, repeated work or unnecessary state removed; fewer lines alone does not prove a better design.

Owners: [Architect](../skills/architect/SKILL.md), [Alága](../skills/alaga/SKILL.md), [Àtúnwò](../skills/atunwo/SKILL.md).

## Finish review and retrieve useful lessons

> Use seda-pr to resolve the PR's feedback. Investigate comments sharing an invariant together, then correct confirmed in-scope defects.

A shared premise may invalidate several comments, or reveal one correction spanning several changed sites. Keep each discussion's disposition and evidence. Reviewer agreement does not establish correctness, and grouping does not turn unrelated cleanup into required work. PR readiness remains distinct from approval, merge and deployment.

> Check existing project knowledge for constraints relevant to this retry change. Read substantive matches and verify that they still apply.

Search with the project's actual vocabulary and the condition being considered. Return the lesson's effect on this task, not an archive summary. No match is a valid result. `amose` maintains durable governing knowledge; `iwadi` owns independently useful research. Existing code, tests or decisions may already preserve the lesson, so completion does not automatically require a new entry.

Owners: [Seda PR](../skills/seda-pr/SKILL.md), [Amọ̀ṣẹ](../skills/amose/SKILL.md), [Ìwádìí](../skills/iwadi/SKILL.md).

For “Explain why this session went wrong and apply the justified correction,” Alárinà first uses `ayewo-igba-ise` to establish the event and earned lesson, then routes the authorized correction to `alaga`, `oro` or `amose`. Reuse proof and maintained knowledge that already own the lesson. A retrospective-only request stops at its findings.

## Check whether a method helps

> Use alarina to compare this proposed skill change with the current instructions on representative tasks. Return the evidence before adopting it.

Skill evaluation and improvement connects `oro`'s instruction work to `adanwo`'s bounded comparisons, with host readiness resolved through the active environment. Use the [opt-in engineering evaluations](../evals/README.md) when their cases fit. Preserve failed and blocked attempts and compare actual results, unnecessary mechanisms, human intervention and total work. A directly supplied skill bypasses discovery; a routing answer does not establish execution. Package validation proves structure; it does not establish that instructions improve engineering outcomes.
