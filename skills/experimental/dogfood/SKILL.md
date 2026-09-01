---
name: dogfood
description: Exercise the changed user journeys of one exact branch, pull request, or candidate in a real browser and report functional, responsive, accessibility, and experiential evidence. Exclude source review, autonomous fixing, invented product expectations, and whole-product audit.
---

# Dogfood

Verify what the changed product actually does and how the affected journeys feel. Stay candidate-pinned, behaviour-scoped, evidence-first, and read-only with respect to source code.

## 1. Pin the candidate, environment, and expected behaviour

Resolve the exact branch, PR, commit, or supplied candidate; comparison base; current head; changed behaviour; acceptance criteria; application start command and URL; test identities and data; browser capability; and external-effect authority.

Never test an unpinned moving candidate. Use a local, preview, or explicitly authorized test environment. Do not use production data or trigger real payments, emails, messages, account changes, or third-party effects without separate explicit authority.

Establish expected behaviour from the strongest available evidence:

```text
explicit user direction and accepted criteria
→ confirmed product, plan, design, or domain contract
→ exact-current documented behaviour
→ pinned baseline behaviour
→ stated reporter expectation
→ unresolved expectation gap
```

Do not convert common UI convention or personal preference into a product failure. When the expected result remains unresolved, test the observable behaviour and report the expectation gap separately.

Prefer a browser surface integrated into the active host when it can navigate, inspect rendered and interactive state, click, fill, press keys, capture screenshots, and inspect console or network failures. Otherwise use one already available companion browser capability. Do not install or bundle a third browser stack for this skill.

## 2. Map the changed journeys and credible blast radius

Map the changed behaviour and supplied acceptance to the smallest complete set of affected user journeys. Do not limit reach to changed files when shared components, routing, authentication, permissions, persistence, data shape, integration, or global state creates a credible interaction seam.

A changed component is not automatically a journey. Identify the user goal, entry, meaningful states, critical interactions, expected completion, and why the candidate can affect it.

Create one row per journey with status `Pass`, `Fail`, `Blocked`, or `Skipped`. A blocked or skipped row must state why, user impact, and what would clear it. Do not silently drop an unreachable route.

When one representative fixture, document, account, dataset, or scenario can cheaply exercise several material changed states together, use it for the final integrated journey instead of proving only isolated controls. Derive the specimen from accepted behavior and credible risk; do not create or maintain a universal fixture schema. Ensure it contains both positive and negative/alternate states when those materially affect the experience.

Exercise only coverage justified by acceptance and risk. Applicable dimensions may include:

- primary success and critical alternate paths;
- loading, empty, validation, error, cancellation, and recovery;
- navigation, back behaviour, state retention, and repeat use;
- narrow/wide layouts, long content, zoom, and overflow;
- keyboard operation, focus visibility/order, labels, and reduced motion;
- copy and hierarchy at the point of action;
- console errors, failed requests, and unexpected external calls; and
- changed authentication, authorization, persistence, integration, or offline boundaries.

Do not mechanically run every dimension for every candidate. State dimensions not exercised and why.

Capture screenshots, reproduction steps, console output, and request evidence only where they prove a result. Transient evidence belongs in OS temp unless a durable result is authorized.

## 3. Classify evidence without absorbing correction

Classify each material result as:

- `PRODUCT_FAILURE` — observed behaviour contradicts a controlling expectation;
- `ENVIRONMENT_BLOCKER` — environment, identity, data, credential, or capability prevented proof;
- `EXPERIENCE_OBSERVATION` — usability, accessibility, responsiveness, copy, or hierarchy evidence without a proved product failure; or
- `UNVERIFIED_CONCERN` — a credible issue whose expected behaviour or reproduction remains incomplete.

For each failure or concern, state the journey, exact reproduction, expected and observed behaviour, candidate/head identity, evidence, user impact, determinism, and classification.

Dogfood does not edit source, commit, push, publish, diagnose source causality, or declare code quality. Use `se-triage` for an ambiguous report, `root-cause` when causal diagnosis is the missing result and its observation boundary is satisfied, `alaga` for an accepted correction, and `atunwo` for code-quality review. Respect each owner's trigger and authority boundary.

After a correction owner returns, refresh the exact candidate and rerun only affected journeys plus credible interaction seams. A successful correction does not erase original evidence or convert untested rows to `Pass`.

## 4. Return the candidate experience

Return:

```text
Candidate and environment
Expected-behaviour evidence
Changed journeys and blast radius
Journey matrix
Representative integrated specimen when used
Material findings and classifications
Evidence locators
Blocked/skipped rationale
Coverage and explicit exclusions
External effects
Candidate freshness
Readiness implication
```

Readiness implication is evidence for the caller; Dogfood does not set plan or delivery acceptance.

Return inline for a small run. Persist a material durable result through `akosile` only when requested or needed downstream. Use `html-artifact` when supplied terminal evidence needs a distinct human visual report. Under an active plan, return Dogfood's native exact-current result rather than defining a plan-specific receipt.
