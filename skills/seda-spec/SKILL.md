---
name: seda-spec
description: Writes a spec or behavior contract from a settled interview, brief or request - the problem, who it is for, outcome, acceptance checks, scope, non-goals and open questions. Use when the "what and why" is decided and needs one written source, or someone asks for a behavior specification.
---

# Seda Spec

**Output:** a spec: one short document a person who was not in the conversation can act on. It is a working record (kind: spec); update an existing spec for this work in place. It stays out of the "how": keep modules, schemas, algorithms and order of work out unless the user fixed one as a requirement.

**Needs:** a settled need: a finished interview result, a clear brief, or a request whose purpose, user and success are known. Use what is in context; do not replay answered questions. If a key decision is open (who it is for, what success is, a trade-off that changes scope), do not guess: return the open questions to the caller. If the request is not spec work, return it and say what is missing.

## Method

Use [the spec template](references/spec-template.md). Keep these parts; drop one only when empty:

- **Problem**: what is wrong or missing today, and for whom.
- **Outcome**: what is true when done, in terms the user can see.
- **Acceptance checks**: statements a person or test can verify without asking the author; each observable, one clear pass or fail, with a short id so plans, tickets and tests can point at it.
- **Scope** and **Non-goals for this work**: what is in, and what is left out now (not forever). Name non-goals a reader might assume.
- **Open questions**: what is unknown, who can answer, whether it blocks the plan. A blocking question means the spec is not ready.
- **Sources**: the interview, issue, document or code facts it rests on.

Use the project's own terms (check the project glossary, `CONTEXT.md`). Mark what the user confirmed apart from what you inferred; never turn an inference into a requirement.

When the spec must serve as the contract a builder and reviewer both work from (the user asks for a behavior specification, or material behavior would otherwise be invented later), read [behavior contract](references/behavior-contract.md). It adds the observable-behavior rules, the flow walk, gap routing and a ready or not-ready result. A request for only the contract ends at that result.

## Done

Every confirmed decision appears, nothing new was invented, no acceptance check needs an implementation detail to be understood, and a stranger can read it once and act. Ready means no blocking question remains; otherwise it is a draft, and say so.

## Return

Return the spec, its acceptance-check ids, and any open question that still matters.
