# Local coding-agent session evidence

Use only when a session or bounded multi-session postmortem depends on persisted local Codex or Claude Code history.

The bundled adapter inventories session stores read-only and can append coverage to a separate mining ledger. Its deterministic seam is: given local session stores plus optional explicit corpus filters and skill-signal focus, emit a privacy-preserving structural inventory that Ìrònú can use to choose and inspect the smallest relevant sample.

## Boundary

The adapter may:

- discover current local Codex and Claude Code session roots;
- inventory JSONL session files without modifying them;
- normalize session/root relationships only when host metadata or storage layout proves them;
- preserve unresolved ancestry instead of manufacturing independent roots when a referenced parent is absent;
- emit host/session/root evidence, cwd/project evidence, host version when present, observed time range, event/role counts, parse gaps, and source line references for conservative skill references;
- emit structural tool activity when the host record exposes it: call/result counts, explicit structured failure flags, consecutive same-tool-call counts, tool names, and result-byte totals without tool arguments or result text;
- filter the corpus by explicitly supplied host, project, session/root/ancestor ID, or time range;
- focus emitted skill references on explicitly supplied skill names without removing sessions that have no matching signal; and
- mark uncertain filter/root evidence explicitly instead of silently inventing certainty.

It must not:

- emit raw prompt, response, source-code, tool-input, tool-output, credential, or pasted-content text in the index;
- infer that repeated tool calls are retries, waste, navigation failure, or a tooling defect without inspecting the task context;
- infer skill eligibility, usefulness, missed opportunity, mis-triggering, availability, selection, loading, or routing from a textual/path reference alone;
- infer the installed skill-set version active in a historical session when the record does not prove it;
- count a fork/copy/subagent or unresolved child as an independent root merely because another JSONL file exists; or
- turn the normalized index into a promotion, fold, removal, environment-change, or skill-edit verdict.

Historical reconstruction and evidence-backed improvement judgments stay with [agent session](agent-session.md) and [corpus analysis](corpus-analysis.md). Revising agent-facing instructions is separate work for the caller to authorize.

## Run the inventory

Read known transcripts directly when they suffice. When inventory or relationship normalization is needed, run this adapter through the active host's local shell/filesystem capability; reuse a suitable existing inventory. Ask the user to run or export evidence only when local access and equivalent capabilities are unavailable.

Anchor the installed skill, then run it:

```bash
SKILL_DIR="<absolute path of the directory containing the SKILL.md you just read>";
python3 "$SKILL_DIR/scripts/session-evidence.py"
```

No time boundary is assumed. Narrow the corpus only when the analysis question calls for it:

```bash
python3 "$SKILL_DIR/scripts/session-evidence.py" \
  --host codex \
  --project /path/to/repository \
  --skill akole
```

`--since` and `--until` accept explicit ISO-8601 corpus bounds; omitting them means no date cutoff. `--session` accepts a session ID or any proved root/ancestor ID. `--skill` is repeatable and **focuses emitted skill-reference signals; it is not a session filter**. Sessions with no matching signal remain in the inventory so Ìrònú can still identify possible missed opportunities from sampled raw evidence.

Project, session, and time filters apply after parsing; they do not reduce scan work. Where the corpus is already located, pass `--codex-root` or `--claude-root` pointing to its containing directory. Report that boundary and preserve unresolved ancestry; broaden collection only when needed for the question or independent-root counts.

When `--skill` is omitted, the adapter discovers current skill names from the available `skills` tree. When running outside a full repository checkout, pass `--skills-root <path-to-skills>` for that auto-discovery path.

The default roots are current host conventions, not package-owned state:

- Codex: `$CODEX_HOME` when set, otherwise `~/.codex`; full persisted rollouts are discovered below its session store. `history.jsonl` is deliberately not treated as a full session transcript.
- Claude Code: `$CLAUDE_CONFIG_DIR` when set, otherwise `~/.claude`; transcripts are discovered below `projects/`.

Leave output on stdout for one-session use. Save a durable local index only when reuse needs it, at an existing or user-selected destination, otherwise a working report location chosen by the caller.

## Mining ledger

A reader records one JSON object per session in a JSONL file, using the fingerprint of the transcript it read:

```json
{"path":"/absolute/path/to/rollout.jsonl","host":"codex","session":"session-id","bytes":1234,"mtime":1790000000.0,"covered":"full"}
```

`host` is `codex` or `claude`; `session` is the inventory's `session_id`; `bytes` and `mtime` are its file size and Unix modification time in seconds. The inventory emits those fields and `snapshot_stable`, which tells whether the file stayed unchanged during the scan. `covered: "full"` or `all_user_messages_read: true` records enough coverage to count as mined; a skim alone leaves the session unmined. Record the fingerprint from the read, so later writes remain visible as changed history.

With `SKILL_DIR` anchored as above, run:

```bash
python3 "$SKILL_DIR/scripts/session-evidence.py" --record-mined /path/to/reader.jsonl
python3 "$SKILL_DIR/scripts/session-evidence.py" --coverage
python3 "$SKILL_DIR/scripts/session-evidence.py" --removal-candidates --older-than-days 90
```

`--record-mined` appends accepted records with a mining time to `~/.qp/reflection/mined.jsonl`; `--ledger /path/to/mined.jsonl` chooses another ledger outside the session stores. The transcript files stay read-only. Missing or unreadable ledgers mean nothing has been mined; malformed or incomplete entries give no coverage.

`--coverage` reports each host's mining runs with session date bounds, gaps between those bounds, never-mined history before the first range with counts and bytes, and changed sessions. Bounds describe what each run reached; the `unmined` list also shows holes within a range and sessions with unknown dates. A size or modification-time change makes a session unmined until a reader covers it again. Without a dated run, all never-mined history appears before the first pending run.

`--removal-candidates` prints JSON for mined sessions whose fingerprint still matches and whose last modification was more than 90 days ago by default. The agent passes another `--older-than-days` value only when the user asks or `sessions_keep_days` in project `.agents/qp.yaml` or user `~/.agents/qp.yaml` sets it, following the project's settings precedence. The script takes the number directly; the agent reads settings. History indexes and sessions without accepted ledger entries stay outside the list. The command only lists candidates; cleanup authority and removal stay with the caller. Host, root and corpus filters work as for inventory.

## Structural activity evidence

`activity` is deliberately descriptive. It records only structure that can help Ìrònú choose where to inspect next:

- `tool_calls` and `tool_results` — structurally identified tool-use/result events;
- `tool_failures` — only failures explicitly marked by a structured `is_error` or failure status field;
- `repeated_same_tool_calls` — consecutive calls carrying the same tool name, without claiming why they repeated;
- `tool_result_bytes` — encoded size of structurally identified result records/blocks; and
- `*_by_name` maps — the same counts/bytes grouped by observed tool name when the host exposes one.

These counters can under-report when an upstream host uses a different event shape. A high count can represent legitimate iterative work; a low count does not prove efficiency. Treat them as locators for selective transcript/tool inspection, not performance metrics, retry detection, or a basis for changing tools by themselves.

## Skill-reference evidence

The adapter deliberately distinguishes references from stronger semantic claims:

- `EXPLICIT_INVOKE` — direct user input uses an explicit host-style `/<skill>` or `$<skill>` invocation form;
- `USER_SKILL_REFERENCE` — direct user input names the skill, including wording that may request, discuss, or prohibit it;
- `STRUCTURED_SKILL_REFERENCE` — a top-level event/payload field names the skill, without assuming that field proves routing semantics; and
- `SKILL_PATH_REFERENCE` — the persisted record contains a path to that skill's `SKILL.md`, without assuming that the host loaded it.

Only `EXPLICIT_INVOKE` is a high-confidence invocation observation. The other signals are locators for selective inspection. A reference does not prove selection, loading, routing, availability, eligibility, or value.

## Root-session evidence

For Codex, parent-thread metadata is followed only through records present in the indexed corpus. If a referenced parent is absent, `root_session_id` remains unresolved and the known ancestor ID is retained. Such a member must not increase the independent-root denominator until Ìrònú can prove independence from additional evidence.

For Claude Code, a subagent storage path may directly prove its root-session ID; retain that relationship while treating the event schema as version-sensitive.

## Corpus use

1. Pin the corpus from the question: host, project/repository, skill snapshot/version evidence, session relationships, or caller-supplied time range. Do not assume a date cutoff.
2. Inventory only that population when sampling or population claims require it; reuse known transcript locators for a fixed-session review.
3. Resolve or explicitly preserve uncertain root relationships before counting independent opportunities.
4. Select representative and risk-weighted root sessions from the inventory, using structural activity only to focus inspection where it can answer the postmortem question.
5. Read raw transcript lines only for selected records and only to reconstruct contract, owner selection, user corrections, proof, rework, recovery, tool/environment friction, or incremental value.
6. Apply opportunity/use and instruction-failure classifications in `corpus-analysis.md` only after that reconstruction.

## Schema drift and provenance

Host session storage is upstream-owned and can change. The parser intentionally uses tolerant structural extraction and reports unreadable/invalid records instead of declaring absence.

- **Codex evidence basis:** `openai/codex` at commit `773f0b081de689b0d54f2809e7b17bfdb4c9f341` exposes `CODEX_HOME`, persisted `history.jsonl` configuration, session storage, and rollout session metadata including identifiers, cwd, CLI version, originator, and parent-thread metadata. The adapter copies no upstream code; it adopts only the local evidence fields needed for this index. Refresh when those storage/metadata contracts change or a real corpus exposes parser gaps.
- **Claude Code evidence basis:** official Claude Code "Manage sessions" documentation retrieved 2026-09-04 documents local JSONL transcripts under `~/.claude/projects/<project>/<session-id>.jsonl`, `CLAUDE_CONFIG_DIR`, and explicitly states that transcript entry format is internal and changes between versions. Field extraction is therefore best-effort evidence, not a stable Claude transcript API. Refresh on host-path changes, material session-format changes, or observed parse gaps.

Do not add hooks, receipts, or background telemetry merely to improve future evidence. First use the native historical records. Add instrumentation only when a concrete recurring decision remains materially unanswerable from those records.
