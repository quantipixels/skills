# Engineering playbooks

Start with the result you need. With `alarina` active, describe the work normally: “Find and fix this defect,” “Explain this profile,” or “Make this service repeatably verifiable.” Alárinà selects and loads the applicable playbook, invokes the existing owners, and carries the work to your requested stopping point.

You can steer it explicitly: “Use alarina's Data change playbook; planning only,” or “Use the Bug fix playbook to verify this existing repair.” Playbook names select routes inside Alárinà; they are not separately installed skills or new slash commands. The host still controls how Alárinà itself is loaded. See the [session setup](../README.md) if you want its operating method throughout a session.

The supported paths are Feature delivery, Investigation, Bug fix, Performance improvement, Data change, Project verification, Architecture evolution and PR readiness. Feature delivery and PR readiness use their existing workflow owners. The other compositions live with [Alárinà](../skills/alarina/SKILL.md); specialist methods stay with their skills.

Existing plans, accepted decisions and current proof carry forward. A settled coding change can go directly to `alaga` with its existing tests; selecting a playbook does not require another plan, agent or review. The examples below also work as direct specialist requests.

## Make the project repeatably verifiable

> Use alaga to establish a repeatable journey through this service's public API, including persisted effects and cleanup. Reuse the existing harness. Use oro if reusable project verification instructions are needed.

A useful result includes the actual startup/readiness command, safe fixtures, public operation, expected effect and owned-resource cleanup. If repeated work warrants a project-local verification skill, its instructions should be grounded in the working harness and exercised before handoff. `irinse` helps with a non-obvious tool or readiness problem.

For example, call the API to create an item, restart the service against the same test database and retrieve the item through the API. That checks a public journey and persistence across restart. It does not establish every transaction or recovery guarantee of another database engine.

> Audit the affected verification recipes after these API changes. Separate stale instructions, harness limitations and product regressions.

Correct a stale route or selector from evidence. If the product stopped preserving required data, keep that failure visible and return it to `alaga`; do not make the recipe green by deleting its expectation. A full verification-map audit covers its requested map. An ordinary change needs affected journeys, not a new full-product test cycle.

Owners: [Alága](../skills/alaga/SKILL.md), [Oro](../skills/oro/SKILL.md), [Irinṣẹ](../skills/irinse/SKILL.md).

## Explain a slowdown, then test a worthwhile improvement

> Use alaga to diagnose this CPU profile and thread dump. Use irinse for capture interpretation if needed. Return the supported mechanism and evidence limits; stop before changing code.

A profile shows where sampled time was spent. A heap capture can show what retains an object; a thread dump can show a blocked wait. These observations narrow an investigation. Neither a hot function nor an improved second capture alone proves the cause. Useful output identifies the capture, relevant path, source attribution and any missing discriminator.

> Use adanwo to compare a bounded improvement to the measured bottleneck. Preserve the existing correctness and response-time obligations.

Let the cost suggest the experiment. Repeated fixed network overhead may justify batching; repeated identical work may justify caching with an invalidation rule. Batching can improve throughput while worsening the latency someone waits for. A useful result compares the same representative workload, rejects broken candidates and reports a supported improvement or an honest inconclusive result.

Owners: [Alága](../skills/alaga/SKILL.md), [Irinṣẹ](../skills/irinse/SKILL.md), [Àdánwò](../skills/adanwo/SKILL.md).

## Prepare a safe data change

> Use atona to make this backfill plan ready to execute. Include the existing-data mapping audit, rollout order, stop conditions and recoverability. Planning only.

Walk the affected contract before choosing machinery: how does an old record become a new one, what can readers see during partial completion, and what must a retry preserve? A precise question such as “Does this timed-out request already have a completed remote effect?” is more useful than a generic request for more edge cases.

Ask `alaga` for checks against representative populated data. Verify each old/new mapping, nulls, relationships and lossy conversions. Compare generated schema changes with the actual migrations in the diff. Account for legitimate concurrent writes when comparing counts; an unchanged count is not automatically the invariant.

The plan should contain executable preflight and post-change checks with expected results, plus the conditions that stop progression. Reverting code is different from restoring data. A backup needs a workable recovery path that accounts for later writes. Existing migration/restart tests remain useful, but a test on an empty database cannot establish preservation of historical meaning.

Return the current human-readable plan and unresolved decisions. Commands in a planning result have not been executed, and planning does not authorize a live rollout.

Owners: [Atọ́nà](../skills/atona/SKILL.md), [Alága](../skills/alaga/SKILL.md), [Architect](../skills/architect/SKILL.md) when sequencing or recovery design remains open.

## Resolve a difficult failure without guessing

> Use alaga to diagnose why this request succeeds at the API boundary but produces the wrong worker result. Keep the probe bounded to the affected path.

Use an existing correlation identity to compare the relevant inputs and outputs across the API, queue and worker. The first observed divergence narrows the failing boundary; further evidence must establish its mechanism. Capture only safe, necessary fields.

> This test passes alone but fails in the suite. Find the smallest repeatable preceding sequence and explain the cause.

Pin the seed, runner mode and environment. Reduce the sequence while preserving the same failure and interacting prerequisites. State leakage is one candidate; resource pressure or concurrency can also explain the difference. A minimized reproducer is useful because it makes those alternatives cheaper to test.

> Check whether this existing PR fixes the reported failure. Search relevant prior attempts if they can change the investigation. Verification only.

Use exact baseline and repaired candidates with comparable inputs and reset state. Show the original failure and the required repaired behavior. If the baseline no longer reproduces, report the missing comparison rather than presenting a positive-only demonstration as proof. Search relevant open work before authoring a duplicate repair.

Owner: [Alága](../skills/alaga/SKILL.md); [Àtúnwò](../skills/atunwo/SKILL.md) supplies independent judgment when requested or useful.

## Improve a design while preserving its contract

> Use architect to assess this workaround. Recover the constraint it serves and determine whether it still applies. Do not implement a replacement yet.

Follow the substantive change through relevant history, review discussion, incidents and tests. Distinguish stated rationale from inference. A strange implementation may protect an uncommon supported case; its age alone is not a reason to remove it.

> Use architect to reduce the repeated guards around these state fields. Explain which invalid combination the proposed representation prevents.

For example, a completed variant can carry its required completion time, avoiding disagreement between a boolean and an optional timestamp. Strengthen a type where a real operation requires it. A summation function can still accept an ordinary empty collection; precision that protects nothing adds burden.

> Use alaga to refactor this accepted boundary, preserving its public behavior and reducing the identified caller burden.

Name retained behavior and reuse current proof. Add characterization or differential checks only for a real gap, move in bounded verified steps and account for dynamic callers during renames. Keep supported compatibility paths until their consumers can migrate. Explain the responsibility, repeated work or unnecessary state removed; fewer lines alone does not prove a better design.

Owners: [Architect](../skills/architect/SKILL.md), [Alága](../skills/alaga/SKILL.md), [Àtúnwò](../skills/atunwo/SKILL.md).

## Finish review and retrieve useful lessons

> Use wo-pr to resolve the PR's feedback. Investigate comments sharing an invariant together, then correct confirmed in-scope defects.

A shared premise may invalidate several comments, or reveal one correction spanning several changed sites. Keep each discussion's disposition and evidence. Reviewer agreement does not establish correctness, and grouping does not turn unrelated cleanup into required work. PR readiness remains distinct from approval, merge and deployment.

> Check existing project knowledge for constraints relevant to this retry change. Read substantive matches and verify that they still apply.

Search with the project's actual vocabulary and the condition being considered. Return the lesson's effect on this task, not an archive summary. No match is a valid result. `amose` maintains durable governing knowledge; `iwadi` owns independently useful research. Existing code, tests or decisions may already preserve the lesson, so completion does not automatically require a new entry.

Owners: [Wò PR](../skills/wo-pr/SKILL.md), [Amọ̀ṣẹ](../skills/amose/SKILL.md), [Ìwádìí](../skills/iwadi/SKILL.md).

## Check whether a method helps

Use the [opt-in engineering evaluations](../evals/README.md) for bounded comparisons. Preserve failed and blocked attempts and compare actual results, unnecessary mechanisms, human intervention and total work. Package validation proves structure; it does not establish that instructions improve engineering outcomes.
