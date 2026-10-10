# Behavior contract

Use when the spec must work as a behavior contract: a fresh person or agent can use it to build and to review, without the author. It adds to the spec in `SKILL.md`; it does not replace it. Keep the same file, the same acceptance-check ids and the same place.

## Pin the boundary

Name the inputs the contract rests on (conversation, issue, policy, existing spec) and who uses the behavior. State today's behavior or gap and the outcome a person can see. Note any version, compatibility or changeover limit that matters. Use settled context as it is; do not restart discovery because the source was a conversation.

What the code does today is evidence of current behavior, not authority for the desired behavior. Do not turn an implementation detail into a requirement unless the user confirmed it.

## What to specify

Only what is material, in observable terms:

- triggers and preconditions;
- visible results and state changes that matter outside the system;
- normal, failure, misuse, recovery and changeover cases that apply;
- invariants and boundary conditions;
- a concrete example wherever a rule is ambiguous without one (label it normative or illustrative);
- for each acceptance check, the most stable place to prove it.

Give each material behavior a short stable id when tickets, tests or review need to point at it. Shorter is better when the contract is already unambiguous; no user-story phrasing or case lists for their own sake.

When a flow is unclear, walk one real actor from its entry point through the branches to success, rejection, cancellation and recovery, and compare each step with the stated behavior and the project's shared handling. Example: a request times out after the remote side finished; what may the caller retry, and what should it see? Name the specific open decision and its consequence. Do not add generic edge-case questions, and do not fill a gap with a plausible requirement.

A contract says what must be true. It does not pick modules, algorithms, schemas, deployment or order of work unless that is an outside-visible constraint the user confirmed.

## Gaps

Keep confirmed behavior apart from inference. Return domain meaning or rule gaps, outside facts, unsettled wants or trade-offs, and structure or technical fitness questions to the caller. If a material behavior cannot be written without inventing it, keep the gap visible.

## Ready or not

- **Ready**: every in-scope material behavior is observable, consistent, traceable to a source, and has a believable proof place; no blocking question remains.
- **Not ready**: name each blocking ambiguity, conflict or missing authority, and who or what can resolve it.

Tests are one kind of evidence against the contract; do not reverse-engineer the wanted behavior from them.

## Keeping it

While planning, build or review depends on the contract, keep its identity and current text stable; when downstream work depends on it, return its id and revision. If it must stay normative after delivery, move it to the project's lasting home and mark it superseded when it is replaced instead of deleting it. Older contract records, wherever kept, are still valid inputs.
