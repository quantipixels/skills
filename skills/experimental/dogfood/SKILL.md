---
name: dogfood
description: Exercise the changed user journeys of one exact branch, pull request, or candidate in a real browser and report functional, responsive, accessibility, and experiential evidence. Exclude source review, autonomous fixing, invented product expectations, and whole-product audit.
---

# Dogfood

Verify what the changed product actually does and how the affected journeys feel. Stay candidate-pinned, behavior-scoped, evidence-first, and read-only with respect to source code.

## 1. Pin the candidate, environment, and expected behavior

Resolve the exact branch, PR, commit, or supplied candidate; comparison base; current head; changed behavior; acceptance criteria; application entry point; test identities/data; browser capability; and external-effect authority.

Never test an unpinned moving candidate. Use a local, preview, or explicitly authorized test environment. Do not use production data or trigger real payments, emails, messages, account changes, or third-party effects without separate explicit authority.

Establish controlling expected behavior only from normative authority:

```text
explicit user direction and accepted criteria
→ confirmed product, plan, specification, design, or domain contract
→ exact-current documentation only when that documentation is itself authoritative
→ unresolved expectation gap
```

Pinned baseline behavior, reporter expectations, convention, and historical behavior are comparison or hypothesis evidence, not normative product truth. When no controlling expectation resolves a mismatch, classify the result as an experience observation or `UNVERIFIED_CONCERN`, not `PRODUCT_FAILURE`.

Use an existing browser capability that can exercise and inspect the affected journey. Do not install or bundle another browser stack merely for this result.

## 2. Map the changed journeys and credible blast radius

Map the changed behavior and supplied acceptance to the smallest complete set of affected user journeys. Do not limit reach to changed files when shared components, routing, authentication, permissions, persistence, data shape, integration, or global state creates a credible interaction seam.

A changed component is not automatically a journey. Identify the user goal, entry, meaningful states, critical interactions, expected completion, and why the candidate can affect it.

Track each material journey as `Pass | Fail | Blocked | Skipped`; a blocked or skipped journey must state why and what would clear it.

Exercise only coverage justified by acceptance and risk. Applicable dimensions may include success/alternate paths, loading/error/recovery, navigation/state retention, responsive/overflow behavior, keyboard/focus/accessibility, copy/hierarchy, console/request failures, and changed auth/persistence/integration boundaries. Do not mechanically run every dimension for every candidate.

Capture screenshots, reproduction steps, console output, and request evidence only where they prove a result.

## 3. Classify evidence without absorbing correction

Classify each material result as:

- `PRODUCT_FAILURE` — observed behavior contradicts a controlling normative expectation;
- `ENVIRONMENT_BLOCKER` — environment, identity, data, credential, or capability prevented proof;
- `EXPERIENCE_OBSERVATION` — usability, accessibility, responsiveness, copy, hierarchy, baseline comparison, or other observed evidence without a proved product failure; or
- `UNVERIFIED_CONCERN` — a credible issue whose controlling expectation or reproduction remains incomplete.

For each failure or concern, state the journey, exact reproduction, expected and observed behavior, candidate/head identity, evidence, user impact, determinism, and classification.

Dogfood does not edit source, commit, push, publish, diagnose source causality, or declare code quality. When a corrected candidate is supplied, refresh its identity and rerun only affected journeys plus credible interaction seams.

## 4. Return the candidate experience

Return:

```text
Candidate and environment
Expected-behavior authority and comparison evidence
Changed journeys and blast radius
Journey results
Material findings and classifications
Evidence locators
Blocked/skipped rationale
Coverage and explicit exclusions
External effects
Candidate freshness
Readiness implication
```

Readiness implication is evidence for the caller; Dogfood does not set another owner's acceptance or lifecycle state. Persist or create a separate visual report only when that distinct result is requested or materially needed downstream.
