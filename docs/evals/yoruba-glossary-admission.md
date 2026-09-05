# Behavioral admission pack: Yorùbá Glossary

Evaluator-owned public-owner boundary proof for `yoruba-glossary`. This file is not runtime guidance and must not be injected into the model under test.

Use fresh host contexts and the exact current installed/public candidate surface. Do not force `yoruba-glossary` into context for the selection cases. Record host, model/tier, exact candidate SHA, date, result, and material notes using `PASS | FAIL | BLOCKED | NOT_RUN | STALE`.

Experimental maturity does not waive this admission proof. Real-use recurrence/incremental-value evidence is a later disposition/promotion question.

## Y1 — positive term/glossary outcome

**Prompt:** “We need a confirmed Yorùbá equivalent for this new technical concept. Once I accept the term, add it to the glossary file I’ve given you.”

**Pass:** select `yoruba-glossary` as the narrowest owner; distinguish proposal from confirmation; do not write before term acceptance and explicit glossary authority; preserve the supplied target/format rather than inventing global persistence.

**Failure:** route ordinary glossary/term ownership to `technical-writing` or `amose`; invent a default glossary path/schema; treat a proposed term as confirmed; or broaden into general translation/documentation.

## Y2 — adjacent negative: technical prose

**Prompt:** “Improve the clarity and structure of this English technical procedure. Keep all established project terminology exactly as it is.”

**Pass:** select `technical-writing`; do not invoke `yoruba-glossary` merely because terminology appears in technical prose.

**Failure:** start term confirmation/glossary maintenance or require a bilingual terminology pass when no actual term decision is requested.

## Y3 — adjacent negative: domain semantics

**Prompt:** “In this project, do `account owner` and `billing owner` refer to the same domain concept? Clarify the model; I’m not asking for translation or a glossary artifact.”

**Pass:** select `amose`; keep `yoruba-glossary` out of the path because no Yorùbá/English term decision or glossary result is requested.

**Failure:** route domain-model clarification through the glossary owner solely because terminology is involved.

## Host requirement

Run Y1-Y3 on Codex and Claude Code because #85 proposes ordinary public selection on both currently supported host surfaces. A PASS on one host does not upgrade the other.

## Admission gate

- Y1 must pass: positive selection/result value is proved at the current boundary.
- Y2 and Y3 must pass: the closest stable-owner boundaries remain intact.
- If any required host/case is `FAIL`, correct the owner boundary or keep/fold the capability behind the natural owner before merging #85.
- If a required run is unavailable, #85 remains `NEEDS_EVIDENCE`; structural/compatibility CI does not substitute.

Portfolio-discovery Arm B is a separate unshipped presentation experiment and is not part of this admission gate. If #85 is later promoted/folded/removed, use representative real-use evidence under Kọ Skill's Experimental disposition contract.

## Evidence log

| Case | Codex | Claude Code | Gate |
| --- | --- | --- | --- |
| Y1 positive term/glossary | NOT_RUN | NOT_RUN | required |
| Y2 technical-writing negative | NOT_RUN | NOT_RUN | required |
| Y3 amose negative | NOT_RUN | NOT_RUN | required |
