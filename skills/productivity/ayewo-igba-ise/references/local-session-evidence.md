# Local coding-agent session evidence

Use only when a session or bounded multi-session postmortem depends on persisted local Codex or Claude Code history.

The bundled adapter is a **read-only evidence indexer**, not an analytics engine. Its deterministic seam is: given local session stores plus optional explicit corpus filters and skill-signal focus, emit a privacy-preserving structural inventory that Àyẹ̀wò can use to choose and inspect the smallest relevant sample.

## Boundary

The adapter may:

- discover current local Codex and Claude Code session roots;
- inventory JSONL session files without modifying them;
- normalize exact session/root-session relationships when the host record or storage path proves them;
- emit host/session/root IDs, cwd/project evidence, host version when present, observed time range, event/role counts, parse gaps, and source line references for structural skill signals;
- filter the corpus by explicitly supplied host, project, session/root ID, or time range;
- focus skill-signal extraction on explicitly supplied skill names without removing sessions that have no matching signal; and
- mark a corpus-filter dimension `UNCERTAIN` instead of silently excluding a record whose required metadata is absent.

It must not:

- emit raw prompt, response, source-code, tool-output, credential, or pasted-content text in the index;
- infer that a skill was eligible, useful, missed, mis-triggered, or available merely from task similarity;
- infer the QP version active in a historical session when the record does not prove it;
- count a fork/copy/subagent as an independent user task merely because another JSONL file exists; or
- turn the normalized index into a promotion, fold, removal, or skill-edit verdict.

Those judgments stay with [corpus analysis](corpus-analysis.md) and Kọ Skill.

## Run the inventory

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

`--since` and `--until` accept explicit ISO-8601 corpus bounds; omitting them means no date cutoff. `--session` accepts a session or normalized root-session ID. `--skill` is repeatable and **focuses emitted skill-use signals; it is not a session filter**. Sessions with no matching signal remain in the inventory so Àyẹ̀wò can still identify possible missed opportunities from raw sampled evidence. When `--skill` is omitted, the adapter discovers current QP skill names from the available `skills` tree for broad structural signal extraction. When running outside a full QP checkout, pass `--skills-root <path-to-qp-skills/skills>` for that auto-discovery path.

The default roots are current host conventions, not QP-owned state:

- Codex: `$CODEX_HOME` when set, otherwise `~/.codex`; full persisted rollouts are discovered below its session store. `history.jsonl` is deliberately not treated as a full session transcript.
- Claude Code: `$CLAUDE_CONFIG_DIR` when set, otherwise `~/.claude`; transcripts are discovered below `projects/`.

Redirect output only when a durable local index is useful. Generated evidence stays local and out of Git by default.

## Skill-use evidence strength

The adapter emits only observed evidence for the selected signal focus:

- `EXPLICIT_INVOKE` — direct user-input text explicitly names/invokes the skill;
- `HOST_ROUTED` — a structured host record names the selected skill; and
- `SKILL_LOADED` — the persisted record contains a structural path to that skill's `SKILL.md`.

These signals establish different facts. A load does not prove the skill's result was needed or useful. No emitted signal does not prove the skill was unavailable or ineligible. Eligibility, missed opportunity, incremental value, and mis-triggering require Àyẹ̀wò to inspect the bounded session evidence.

## Corpus use

1. Inventory the full permitted local population first.
2. Pin the corpus from the decision being made: host, project/repository, QP snapshot/version evidence, session roots, or caller-supplied time range as relevant. Use `--skill` only to reduce signal noise/cost for the skill(s) under investigation; do not shrink the denominator to sessions that already show a skill signal.
3. Normalize root sessions before counting opportunities. Treat resumed/copied/forked/subagent records as related evidence and establish independence before using them as separate denominator units.
4. Select representative and risk-weighted root sessions from the inventory.
5. Read raw transcript lines only for the selected records and only to the extent needed to reconstruct the contract, owner selection, user corrections, proof, rework, recovery, or incremental value.
6. Apply the Experimental opportunity classifications in `corpus-analysis.md` only after that reconstruction. Stable-skill improvement uses the same evidence but asks which recurring contract/selection failures justify a change.

## Schema drift and provenance

Host session storage is upstream-owned and can change. The parser intentionally uses tolerant structural extraction and reports unreadable/invalid records instead of declaring absence.

- **Codex evidence basis:** `openai/codex` at commit `773f0b081de689b0d54f2809e7b17bfdb4c9f341` exposes `CODEX_HOME`, persisted `history.jsonl` configuration, session storage, and rollout session metadata including identifiers, cwd, CLI version, originator, and parent-thread metadata. QP copies no upstream code; it adopts only the local evidence fields needed for this index. Refresh when those storage/metadata contracts change or a real corpus exposes parser gaps.
- **Claude Code evidence basis:** official Claude Code "Manage sessions" documentation retrieved 2026-09-04 documents local JSONL transcripts under `~/.claude/projects/<project>/<session-id>.jsonl`, `CLAUDE_CONFIG_DIR`, and explicitly states that transcript entry format is internal and changes between versions. QP therefore treats field extraction as best-effort evidence, not a stable Claude transcript API. Refresh on host-path changes, material session-format changes, or observed parse gaps.

Do not add hooks, receipts, or background telemetry merely to improve future evidence. First use the native historical records. Add instrumentation only when a concrete recurring decision remains materially unanswerable from those records.
