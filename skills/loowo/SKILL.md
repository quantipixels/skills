---
name: loowo
description: Lò ó wò (try using it). Produces a dogfood result by using the running product the way its real users would, one whole journey at a time. Use after a change builds and its tests pass, when a user-facing surface (web page, app screen, CLI flow) changed, or when asked to try it, dogfood it or QA it.
---

# Lò ó wò

**Output:** a dogfood result: a check matrix with one result per journey, fixes made, what needs a human or a decision, the suite result, and a ready or not-ready verdict. Scope is this change only, not the whole app. It finds what green tests miss: the change as a person meets it.

**Needs:** a change (branch diff against the project's real base, a PR, or uncommitted work) and a way to run the product. If there is no change, nothing user-facing changed, or the product cannot be started, return to the caller and say which is missing. Do not guess a start command.

## Method

**Workflow** (`asoju`): drive each mapped journey through a `cheap-browser` runner following the recipe exactly; you judge the results and decide fixes.

Derive journeys from what the diff changes, then walk each one whole: from where the user starts, through the change, to the outcome they came for. A page that renders is not a journey.

Say who is using it. Use the project's own words on users first (README, product or strategy docs, personas, design notes, tickets); if none, infer a few plausible users and label them inferred. Judge each journey for correctness and for how it feels to that user: confusion, dead ends, slow or silent steps, wrong or missing copy, lost state.

If the project has a verify skill, use its launch, doctor, drive and cleanup. If the same journeys will be needed again and there is none, say so in the result; do not build it here.

Before driving, write a short check matrix (journey, user, start state, expected outcome, what could go wrong) in the [matrix and report shape](references/matrix.md). Update it after every journey so an interrupted run can resume.

Driving:

- On SIGIDI, use native previews first: `preview_*` for web, `device_*` for mobile and simulators. Elsewhere use the project's driver, or a browser tool the host already has. Do not install a browser stack.
- One owner drives each browser or device at a time. Do not mix drivers inside one run. Delegated readers may inspect source; they do not touch the live surface.
- Use the public paths a user would. Read the console and the visible result, and check a second view of any saved effect when you can.
- Start the server yourself only if you own it; never stop one you did not start.
- No real payments, messages, emails or other external effects. Use test modes and fixtures; a journey that needs one is `needs a human to verify`.

Mark every journey with exactly one result:

| Result | Meaning |
|---|---|
| pass | Works and feels right for its user |
| fixed | Broken, fixed, and re-driven to pass |
| skipped | Not driven, with the reason |
| needs a human to verify | Needs an outside step you cannot take (real login provider, payment, device you lack) |
| needs a user decision | The fix changes product or design intent, or has competing answers |

A small fix clearly within intended behaviour may be made and re-checked, with a test that fails before and passes after where one is meaningful and no change to scope. A product, design or architecture choice stops for the user; never slip one in to turn a row green. Do not rerun a blocked row on your own.

After the matrix, run the project's test suite once and record the result. A green matrix with a failing suite is not ready. Do not chase the suite green here.

Keep screenshots and notes in OS temp, or as a report record when they must outlive the session. Put only the evidence a reader needs into the report. Never write the report into the main checkout or commit it unless the user asks.

## Done

Every journey has one result, the suite was run once, and the verdict follows from them.

## Return

Return the matrix with results, fixes made, items for a human or a decision, the suite result and the verdict. If a design doubt or failing journey needs rework, say so in one line.
