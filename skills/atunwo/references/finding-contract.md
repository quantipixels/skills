# Finding contract

Report only material, actionable findings supported by evidence. Use this shape:

<!-- prettier-ignore -->
```markdown
### <severity> — <consequence-oriented title>

**Location:** <file:line, hunk, API, scenario, or artifact>
**Evidence and mechanism:** <observation, governing source, and candidate-to-defect path>
**Failure scenario:** <concrete conditions that expose the defect>
**Consequence:** <user, system, security, compatibility, delivery, or operational impact>
**Confidence:** confirmed | high | medium | low
**Correction direction:** <smallest credible correction>
```

Severity is independent of correction effort:

- **Critical:** credible severe security impact, irreversible data loss, or broad outage.
- **High:** major incorrect behavior, contract failure, or compatibility break in a realistic path.
- **Medium:** material correctness, delivery, security, compatibility, or operability defect.
- **Low:** bounded candidate-caused issue worth correcting.

Reject generic style, unrelated debt, deterministic-tool noise, unsupported speculation, and findings without a candidate-caused or candidate-dependent mechanism. Send maintainability-only concerns to `pare` in `review` mode.

## Proof-gap gate

Do not recommend a new test merely because a method, class, branch, or line lacks dedicated coverage. Before reporting a proof gap that needs new or changed proof, record:

```text
Invariant: <what must remain true>
Current proof owner(s): <compiler, type/schema/static rule, unit/contract, integration, acceptance, runtime, or none>
Escaping regression: <realistic incorrect behavior current proof would miss>
Cheapest stable seam: <best proof owner>
Why existing proof is insufficient: <specific missing detection>
```

If compiler/type/schema/static/architecture/integration/acceptance evidence completely owns the invariant, do not request duplicate unit proof. Conversely, a broad integration test does not replace a focused contract when it cannot reliably detect the same failure.

Test count, line/branch coverage, mock choreography, or a missing one-test-per-method pattern is not itself a defect. Preserve distinct public, security, money/data-integrity, transaction/locking/idempotency, concurrency/cancellation, recovery/migration, external-adapter, accessibility/interaction, and historically recurrent contracts when no stronger complete owner exists.
