# Separate solution architecture from lifecycle planning

Status: Partially superseded by [Use owner records as semantic sources for HTML projections](20260824-use-owner-records-for-html-projections.md). Outcome ownership remains accepted; the later decision replaces HTML-only plan state with canonical owner records and derived HTML views.

QP publishes `solution-architect` as the Engineering owner for portable technical architecture design and read-only architecture review. It reports `IMPLEMENTATION_READY`, `NOT_READY`, or `UNPROVED` and uses the active stack/domain naturally rather than maintaining a platform catalog.

QP keeps `atona` as the full-lifecycle owner: turn unclear intent into one startable initiative plan, keep it exact-current across design/delivery, and reconcile it at closure. Atọ́nà owns plan identity, scope, decision state, lifecycle readiness, dependencies, risks, deferrals, delivery summary, closure state, and next action.

A material plan uses a canonical Atọ́nà record under `.qp/records/atona/<record-id>/record.md`; a material architecture packet uses its own Solution Architect record under `.qp/records/solution-architect/<record-id>/record.md`. HTML views are derived from pinned record revisions. The plan links the architecture record and consumes a compact receipt rather than copying the packet.

Supporting skills retain their judgment, authority gates, and local mechanics. Àròjinlẹ̀ resolves material decisions, Solution Architect judges technical sufficiency, and Alága delivers settled jobs through proof/review. Atọ́nà integrates their exact-current receipts without absorbing their procedures.

Keeping architecture inside Atọ́nà was rejected because technical design/review is independently useful without a lifecycle plan and the combined owner repeated specialist state. Moving architecture into Àròjinlẹ̀ was rejected because decision closure is not technical sufficiency. Moving it into Alága was rejected because architecture can precede implementation and review must remain read-only.

The split gives each readiness result one meaning: `solution-architect: IMPLEMENTATION_READY` means the technical design is sufficient; `atona: Planned` means the complete initiative plan is startable.
