# C12 — desire, domain applicability and technical fitness

**Observation:** selection probe

**Instruction source:** supplied candidate

**Workspace:** none; no implementation or provider actions

Use the supplied QP definitions. For each independent request, state the first unresolved result, what evidence or answer would settle it, what can proceed, and where the result returns. Do not execute the proposed work or create workers.

1. “Build a leaderboard so staff compete more.” The brief identifies no beneficiary, desired outcome, success measure or accepted incentive trade-off. What must be settled before treating a leaderboard as the requirement?
2. “Implement the accepted leaderboard contract.” It already identifies the beneficiary, success, privacy policy, ranking behavior, failure cases and technical approach; all remain current. What work should proceed?
3. A transfer feature uses the familiar word “account,” but one context treats it as a legal customer and another as a billing balance. A historical policy is cited outside its original lifecycle. The requested behavior depends on identity and transfer eligibility. What needs resolving?
4. The same feature has a current domain record explicitly covering both contexts, their distinct identities and the requested transition. No conflicting evidence exists. What can be reused?
5. An existing single-process lock is proposed for a now multi-replica payment flow. The accepted requirement is at-most-one charge across replicas. No evidence establishes the mechanism's fitness. What judgment is missing?
6. The existing design has current evidence covering the same replicas, failure/retry paths and invariant. No driver changed. Does the request require a new design exercise?
7. During a read-only review, an implementation silently selects a disputed refund eligibility rule. Explain the return path and authority boundary.
8. A tightly coupled bounded change needs clarification of one identity, confirmation of a technical invariant, and implementation. All source evidence is locally available and the decisions are settled. Does using several skills require several agents or separate initiatives?
