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

Reject generic style, maintainability-only concerns, unrelated debt, deterministic-tool noise, unsupported speculation, and findings without a candidate-caused or candidate-dependent mechanism. Route maintainability-only concerns to `simplify`.
