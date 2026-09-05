# Local coding-agent session evidence

Use only when a session or bounded multi-session postmortem depends on persisted local Codex or Claude Code history.

The bundled adapter is a **read-only evidence indexer**, not an analytics engine. Its deterministic seam is: given local session stores plus optional explicit corpus filters and skill-signal focus, emit a privacy-preserving structural inventory that Àyẹ̀wò can use to choose and inspect the smallest relevant sample.

## Boundary

The adapter may:

- discover current local Codex and Claude Code session roots;
- inventory JSONL session files without modifying them;
- normalize session/root relationships only when host metadata or storage layout proves them;
- preserve unresolved ancestry instead of manufacturing independent roots when a referenced parent is absent;
- emit host/session/root evidence, cwd/project evidence, host version when present, observed time range, event/role counts, parse gaps, and source line references for conservative skill references;
- filter the corpus by explicitly supplied host, project, session/root/ancestor ID, or time range;
- focus emitted skill references on explicitly supplied skill names without removing sessions that have no matching signal; and
- mark uncertain filter/root evidence explicitly instead of silently inventing certainty.

It must not:

- emit raw prompt, response, source-code, tool-output, credential, or pasted-content text in the index;
- infer skill eligibility, usefulness, missed opportunity, mis-triggering, availability, selection, loading, or routing from a textual/path reference alone;
- infer the QP version active in a historical session when the record does not prove it;
- count a fork/copy/subagent or unresolved child as an independent root merely because another JSONL file exists; or
- turn the normalized index into a promotion, fold, removal, or skill-edit verdict.

Those judgments stay with [corpus analysis](corpus-analysis.md) and Kọ Skill.

## Run the inventory

When persisted local history is the selected evidence source, **Àyẹ̀wò runs this adapter itself** through the active host's local shell/filesystem capability. The command below is an agent execution primitive, not a prerequisite for the user. Ask the user to run or export it only when the active host genuinely cannot access the local session stores and no equivalent local capability is available.

From a QP checkout:

```bash
python3 skills/productivity/ayewo-igba-ise/scripts/session-evidence.py
```

No time boundary is assumed. Narrow the corpus only when the analysis question calls for it:

```bash
python3 skills/productivity/ayewo-igba-ise/scripts/session-evidence.py \
  --host codex \
  --project /path/to/repository \
  --skill root-cause
```

`--since` and `--until` accept explicit ISO-8601 corpus bounds; omitting them means no date cutoff. `--session` accepts a session ID or any proved root/ancestor ID. `--skill` is repeatable and **focuses emitted skill-reference signals; it is not a session filter**. Sessions with no matching signal remain in the inventory so Àyẹ̀wò can still identify possible missed opportunities from sampled raw evidence.

When `--skill` is omitted, the adapter discovers current QP skill names from the available `skills` tree. When running outside a full QP checkout, pass `--skills-root <path-to-qp-skills/skills>` for that auto-discovery path.

The default roots are current host conventions, not QP-owned state:

- Codex: `$CODEX_HOME` when set, otherwise `~/.codex`; full persisted rollouts are discovered below its session store. `history.jsonl` is deliberately not treated as a full session transcript.
- Claude Code: `$CLAUDE_CONFIG_DIR` when set, otherwise `~/.claude`; transcripts are discovered below `projects/`.

Redirect output only when a durable local index is useful. Generated evidence stays local and out of Git by default.

## Skill-reference evidence

The adapter deliberately distinguishes references from stronger semantic claims:

- `EXPLICIT_INVOKE` — direct user input uses an explicit host-style `/<skill>` or `$<skill>` invocation form;
- `USER_SKILL_REFERENCE` — direct user input names the skill, including wording that may request, discuss, or prohibit it;
- `STRUCTURED_SKILL_REFERENCE` — a top-level event/payload field names the skill, without assuming that field proves routing semantics; and
- `SKILL_PATH_REFERENCE` — the persisted record contains a path to that skill's `SKILL.md`, without assuming that the host loaded it.

Only `EXPLICIT_INVOKE` is a high-confidence invocation observation. The other signals are locators for selective inspection. A reference does not prove selection, loading, routing, availability, eligibility, or value.

## Root-session evidence

For Codex, parent-thread metadata is followed only through records present in the indexed corpus. If a referenced parent is absent, `root_session_id` remains unresolved and the known ancestor ID is retained. Such a member must not increase the independent-root denominator until Àyẹ̀wò can prove independence from additional evidence.

For Claude Code, a subagent storage path may directly prove its root-session ID; retain that relationship while treating the event schema as version-sensitive.

## Corpus use

1. Inventory the full permitted local population first.
2. Pin the corpus from the decision being made: host, project/repository, QP snapshot/version evidence, session relationships, or caller-supplied time range as relevant. Do not bake a repository inception date or rolling-window default into the analyser.
3. Resolve or explicitly preserve uncertain root relationships before counting independent opportunities.
4. Select representative and risk-weighted root sessions from the inventory.
5. Read raw transcript lines only for selected records and only to reconstruct contract, owner selection, user corrections, proof, rework, recovery, or incremental value.
6. Apply Experimental/stable-skill classifications in `corpus-analysis.md` only after that reconstruction.

## Schema drift and provenance

Host session storage is upstream-owned and can change. The parser intentionally uses tolerant structural extraction and reports unreadable/invalid records instead of declaring absence.

- **Codex evidence basis:** `openai/codex` at commit `773f0b081de689b0d54f2809e7b17bfdb4c9f341` exposes `CODEX_HOME`, persisted `history.jsonl` configuration, session storage, and rollout session metadata including identifiers, cwd, CLI version, originator, and parent-thread metadata. QP copies no upstream code; it adopts only the local evidence fields needed for this index. Refresh when those storage/metadata contracts change or a real corpus exposes parser gaps.
- **Claude Code evidence basis:** official Claude Code "Manage sessions" documentation retrieved 2026-09-04 documents local JSONL transcripts under `~/.claude/projects/<project>/<session-id>.jsonl`, `CLAUDE_CONFIG_DIR`, and explicitly states that transcript entry format is internal and changes between versions. QP therefore treats field extraction as best-effort evidence, not a stable Claude transcript API. Refresh on host-path changes, material session-format changes, or observed parse gaps.

Do not add hooks, receipts, or background telemetry merely to improve future evidence. First use the native historical records. Add instrumentation only when a concrete recurring decision remains materially unanswerable from those records.
