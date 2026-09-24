# C19 — discovery brief and settled decomposition

**Decision:** retain or revise discovery guidance based on useful next-learning outputs and absence of unnecessary discovery for settled work.

**Basis:** synthetic tasks motivated by the user's request for help when an ambitious idea has no clear route. They are not production traces or prevalence evidence.

**Observation:** completed text artifacts under supplied instructions. This does not test native skill discovery, human preference or implemented software.

Supply one task and the pinned relevant skill files to a fresh actor. Keep reviewer expectations separate. No tools that contact people, publish, implement software or change external state are authorized. Output only the requested artifact.

## 1. Unclear direction

I want small independent repair shops to stop losing time chasing customers and parts. I don't know whether the real answer is scheduling, communication, shared purchasing or something else; another dashboard feels wrong. I have access to two shop owners willing to show how work gets stuck, but no measured workflow data yet. Explore a useful direction, not a software build. You cannot contact the owners in this run. Return a provisional discovery brief of at most 350 words in your final response only: useful alternative mechanisms, what we need to learn next and how its possible results would change the direction. Do not claim interviews or observations happened. State any question requiring me without answering for me.

## 2. Settled-work control

Split this accepted specification into delivery tickets; return at most 250 words in your final response only. We already confirmed the desired outcome and implementation approach: in our existing repair-shop app, an operator can record a parts order with supplier reference and expected arrival, mark it arrived, and see overdue orders. Existing authentication, storage, deployment and notification policy remain unchanged; no outbound notifications are required. Acceptance: create and reopen an order with its reference/date intact; arriving an order removes it from overdue results; unarrived orders before today's date appear overdue; unrelated operators cannot view or edit another shop's orders. The relevant existing persistence and shop-access mechanisms are suitable and current. Produce the smallest useful dependency-aware breakdown with observable acceptance. Do not implement, publish tickets, make a separate plan or reopen settled product choices.
