---
"qp-skills": minor
---

Clarify Alárinà as the routing interface to the skills published in this repository: inventory current QP skills, list them when requested, route only repository QP owners, and return `NO_QP_ROUTE` instead of maintaining external-skill fallback catalogues. Let `hitl-review` consume Alárinà for QP specialist routing and let `seda-pr` consume `technical-writing` for zero-context PR/MR prose while retaining factual/publication ownership.
