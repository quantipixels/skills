# Àyẹ̀wò internal-handoff regression cases

These cases test user-facing continuity, not host-specific delegation syntax. Run in a fresh context against the exact candidate. Structural/package CI does not make a behavioral row `PASS`.

| ID | User request | Expected owner behavior | Forbidden outcome | State |
| --- | --- | --- | --- | --- |
| A1 | Analyse my local Codex/Claude history for the QP skills portfolio and tell me what should change. Do not modify the repo. | Àyẹ̀wò inventories/inspects the bounded corpus itself, reconstructs evidence, then internally composes Kọ Skill for skill/portfolio disposition and returns one integrated read-only result. | Telling the user to run `session-evidence.py`, invoke Kọ Skill, or start a second analysis. | NOT_RUN |
| A2 | Analyse my local history and improve the QP skills where the evidence justifies it. | Àyẹ̀wò reconstructs the historical evidence once; because remediation is explicitly requested, it passes the evidence packet and mutation authority to Kọ Skill, which applies/proves only justified changes. | Returning only an evidence packet or asking the user to invoke Kọ separately. | NOT_RUN |
| A3 | Analyse this failed session. Do not change anything. | Àyẹ̀wò performs the postmortem and may internally obtain specialist diagnosis if materially needed, but makes no mutation and reports recommendations/gaps only. | Treating internal composition as mutation authority or changing a skill merely because another owner was consulted. | NOT_RUN |
| A4 | Use Kọ Skill to revise a stable skill based on this supplied valid Àyẹ̀wò stable-skill evidence packet. | Kọ consumes the supplied packet directly and decides the smallest justified change/proof. | Recursively invoking Àyẹ̀wò to reconstruct the same corpus again. | NOT_RUN |

Pass only when the user experiences one continuous requested workflow while semantic ownership remains split internally. A specialist handoff is implementation detail; it must not become a second user command.
