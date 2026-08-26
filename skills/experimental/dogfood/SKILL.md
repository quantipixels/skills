---
name: dogfood
description: Exercise the user journeys changed by one branch, pull request, or candidate in a real browser and report functional, responsive, accessibility, and experiential evidence. Exclude source review, autonomous fixing, and whole-product audit.
disable-model-invocation: true
---

# Dogfood

Verify what the changed product actually does and how the affected journeys feel. Stay diff-scoped, evidence-first, and read-only with respect to source code.

## 1. Pin the candidate and safe environment

Resolve the exact branch, PR, commit, or supplied candidate; comparison base; changed files; current head; plan or acceptance criteria; application start command and URL; test identities and data; browser capability; and external-effect authority.

Never test an unpinned moving candidate. Use a local, preview, or explicitly authorized test environment. Do not use production data or trigger real payments, emails, messages, account changes, or third-party effects without separate explicit authority.

Prefer a browser surface integrated into the active host when it can navigate, inspect rendered and interactive state, click, fill, press keys, capture screenshots, and inspect console or network failures. Otherwise use one already available companion browser capability. Do not install or bundle a third browser stack for this skill.

## 2. Map the changed journeys

Map changed code and supplied acceptance to the smallest complete set of user journeys affected by the candidate. A changed component is not automatically a journey; identify the user goal, entry, meaningful states, critical interactions, and completion condition.

Create a matrix with one row per journey and status `Pass`, `Fail`, `Blocked`, or `Skipped`. A skipped or blocked row must state why and what would clear it. Do not silently drop an unreachable route.

For each journey, exercise applicable:

- primary success path;
- empty, loading, validation, error, and recovery states;
- navigation, back behavior, state retention, and cancellation;
- narrow and wide responsive forms, long content, and overflow;
- keyboard operation, focus visibility/order, labels, and reduced motion;
- copy and hierarchy at the point of action;
- console errors, failed requests, and unexpected external calls; and
- boundaries changed by authentication, permissions, persistence, or integration behavior.

Capture screenshots, reproduction steps, console output, and request evidence only where they prove a result. Transient evidence belongs in OS temp unless a durable report is authorized.

## 3. Keep evidence and correction ownership separate

Dogfood does not edit source, commit, push, publish, or declare code quality. For each failure, state the journey, exact repro, expected and observed behavior, candidate/head identity, evidence, user impact, and whether the failure is deterministic.

Route an unverified report or ambiguous symptom to `se-triage`. Route a confirmed bounded correction to `alaga`. Route a code-quality concern without a runtime failure to `atunwo`. When the missing outcome is causal diagnosis, offer the explicit Experimental `root-cause` route and wait for acceptance; do not silently invoke another experiment.

After a correction owner returns, refresh the exact candidate and rerun only affected journeys plus any credible interaction seam. A successful fix does not erase the original evidence or convert untested rows to `Pass`.

## 4. Report the candidate experience

Return the candidate and environment, changed-journey map, matrix, evidence locators, blocking findings, non-blocking observations, skipped/blocked rationale, external effects, browser and viewport coverage, candidate freshness, and readiness implication. Dogfood supplies experience-verification evidence; the plan or delivery owner decides acceptance.

Return inline for a small run. For a material run, resolve one record through `akosile`:

```text
owner: dogfood
record_type: experience-verification
subject: <candidate or head identity>
```

Keep the matrix and exact evidence boundary in `record.md`; retain selected screenshots, console, or network evidence under the bundle's `evidence/` slot. Create a terminal `index.html` only when a human visual report materially improves review. Dogfood does not maintain continuous HTML from the first step.

Under an active Atọ́nà plan, keep detailed evidence in the Dogfood record and return a compact receipt with candidate/head, covered journeys, status counts, blocking findings, proof freshness, record locator, and plan effect. Do not copy the full QA record into the initiative plan.
