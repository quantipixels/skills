# Check matrix and report shape

## Matrix

One row per journey. Fill it before driving; update the last two columns after each journey.

| # | Journey (start -> outcome) | User (stated or inferred) | Start state | Expected | Risks to probe | Result | Note and evidence |
|---|---|---|---|---|---|---|---|

Cover for each journey where they apply: the normal path, an empty or first-time state, bad or missing input, going back or reloading mid-way, slow or failed network, a narrow screen or small device, keyboard-only use, and long or unusual content. Drop what the change cannot touch and say so in one line rather than padding rows.

## Where the criteria come from

Accepted behaviour (spec, ticket, project docs) is the bar. If a criterion you would apply conflicts with what the change clearly intends, report it as a question for the user; do not redefine the product.

## Report

Short, in plain words, readable at a glance:

1. Verdict: ready or not ready, in one line, and why.
2. Matrix with results.
3. Fixes made: what and how it was re-checked.
4. Needs a human to verify, and needs a user decision, each with the exact question.
5. Suite result and the command used.
6. Evidence: only the screenshots or notes a reader needs, with paths.

Save as a report record (named by date and branch) or in OS temp. It stays out of git.
