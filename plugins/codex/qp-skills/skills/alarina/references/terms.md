# Terms and names

Use this as a lookup when a concept changes a decision; it is not a mandatory reading stage. These working definitions support human and agent collaboration. Project-specific domain language belongs in the project's own glossary or `CONTEXT.md`.

| Concept | Meaning and practical consequence |
| --- | --- |
| DX — developer experience | How readily a developer can understand, change, run and debug the system. Improve actual setup, feedback and recovery friction; measure the affected workflow. |
| AX — agent experience | How readily an agent can discover the right owner, obtain relevant context, act within authority and verify completion. Clear interfaces, runnable checks and useful failures matter more than extra instruction files. |
| Deep module | A small, useful interface hiding substantial complexity. Depth is the capability offered relative to what callers must understand, not file size. See [module design](architect/module-design.md). |
| Cohesion / coupling | Cohesion is how closely responsibilities serve one purpose; coupling is what must change or be understood together across boundaries. Group by shared knowledge and change reasons, not one function per file. |
| Seam | A stable boundary through which behavior can be replaced or observed. Test meaningful public behavior there without exposing internals solely to tests. |
| SDLC — software development lifecycle | The connected work of discovery, design, delivery, operation and learning. Enter at the unresolved result; it is not a compulsory sequence of ceremonies. |
| Vertical slice | A narrow observable outcome across the necessary layers. Implementation, proof and affected documentation can belong to the same slice. |
| Tracer bullet | The smallest working path through important boundaries that tests an architectural assumption and can grow into delivery. A disposable prototype instead answers uncertainty without promising production readiness. |
| Feedback loop | Act, observe a relevant result, adjust. Prefer the shortest faithful loop that could expose the failure; passing unrelated checks adds little confidence. |
| HITL — human in the loop | A person participates in consequential choices or review. Use their input where judgment is needed; do not ask them to rediscover facts the agent can inspect. |
| AFK — away from keyboard | Work progresses while the person is unavailable. It needs settled scope, sufficient authority, observable acceptance and recoverable execution. It never grants extra permissions or resolves missing decisions. |
| Accepting evidence | Current evidence tied to the actual candidate that establishes the requested result. A plan, tool submission or worker's completion claim is not enough. |
| ADR — architecture decision record | A durable explanation of a consequential architectural choice and its tradeoffs. Admission rules belong to [amose-adrs](../commands/amose-adrs.md), not every routine change. |

## Project names

These are project names. The slugs are stable ASCII identifiers; the marked Yorùbá forms explain the intended sense. They do not claim a language-wide standard for software terms. Keep this table aligned with `routes.yaml`, the command menu, and the agent profile when a name changes.

| Identifier | Marked form and plain meaning | Why the name fits |
| --- | --- | --- |
| `alarina` skill and agent | **Alárinà**, intermediary or go-between | Routes a request to the command that owns the next result and carries evidence back; the agent profile uses the same method within its assignment. |
| `amose-context` | **Amọ̀ṣẹ́**, the project's name for its domain modeller; `context` names the bounded language source | Captures resolved domain terms in the project's canonical glossary and places legacy knowledge with its proper owner. |
| `iwadi` | **Ìwádìí**, research or investigation | Answers a defined question with evaluated evidence and references. |
| `sawari` | **Ṣàwárí**, discover or explore | Maps an unfamiliar technical area, including a repository dive, before a direction or implementation is chosen. |
| `seda-pr` | **Ṣẹ̀dá**, create | Creates or updates the authorized PR/MR publication artifact. |
| `wo-pr` | **Wò**, look or observe | Inspects the current PR/MR and, when authorized, stewards its checks and feedback through the requested stop. |

The research and exploration pair differs by result: `iwadi` resolves a stated question; `sawari` discovers the shape of an unfamiliar area and the questions worth resolving. `seda-pr` publishes; `wo-pr` observes or stewards the published item. Command names never grant authority by themselves.

Sources for the ordinary word senses: [Alárinà as intermediary](https://noyam.org/wp-content/uploads/2026/05/EHASS2026748.pdf), [Ìwádìí in a Yorùbá research-methods title](https://openlibrary.org/books/OL22682502M/O%CC%A3gbo%CC%81%CC%A3n_i%CC%80wa%CC%81di%CC%80i%CC%81_i%CC%80mo%CC%80%CC%A3_I%CC%80ji%CC%80nle%CC%80%CC%A3_Yoru%CC%80ba%CC%81), [Ṣàwárí](https://kaikki.org/dictionary/Yoruba/meaning/%E1%B9%A3/%E1%B9%A3a/%E1%B9%A3awari.html), [Ṣẹ̀dá](https://kaikki.org/dictionary/Yoruba/meaning/%E1%B9%A3/%E1%B9%A3%E1%BA%B9/%E1%B9%A3%E1%BA%B9da.html), and [wò as look or observe](https://yorubadictionary.com/browse/view/watch/v/observe). The command meanings in the third column are this project's usage, not dictionary definitions.
