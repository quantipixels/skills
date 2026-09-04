#!/usr/bin/env python3
"""Inventory local Codex/Claude sessions without copying transcript content."""
from __future__ import annotations

import argparse, json, os, re, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

SCHEMA = "qp.session-evidence/v1"
HOSTS = ("codex", "claude")
SKILL_KEYS = {"skill", "skill_name", "skillname", "selected_skill", "selectedskill"}
SKILL_PATH = re.compile(r"(?:^|[/\\])skills(?:[/\\][^/\\]+)?[/\\]([a-z0-9-]+)[/\\]SKILL\.md", re.I)


def args(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--host", action="append", choices=HOSTS)
    p.add_argument("--codex-root", type=Path); p.add_argument("--claude-root", type=Path)
    p.add_argument("--project", action="append", type=Path, default=[])
    p.add_argument("--since"); p.add_argument("--until")
    p.add_argument("--session", action="append", default=[])
    p.add_argument("--skill", action="append", default=[]); p.add_argument("--skills-root", type=Path)
    return p.parse_args(argv)


def timestamp(v: Any) -> datetime | None:
    if isinstance(v, (int, float)):
        n = float(v); n = n / 1000 if abs(n) > 10_000_000_000 else n
        try: return datetime.fromtimestamp(n, tz=timezone.utc)
        except (OSError, OverflowError, ValueError): return None
    if not isinstance(v, str) or not v.strip(): return None
    s = v.strip().replace("Z", "+00:00") if v.strip().endswith("Z") else v.strip()
    try: d = datetime.fromisoformat(s)
    except ValueError: return None
    return (d.replace(tzinfo=timezone.utc) if d.tzinfo is None else d).astimezone(timezone.utc)


def bound(v, flag):
    if v is None: return None
    d = timestamp(v)
    if d is None: raise ValueError(f"{flag} must be ISO-8601")
    return d


def iso(d): return d.isoformat().replace("+00:00", "Z") if d else None


def dicts(v: Any) -> Iterator[dict]:
    if isinstance(v, dict):
        yield v
        for x in v.values(): yield from dicts(x)
    elif isinstance(v, list):
        for x in v: yield from dicts(x)


def strings(v: Any) -> Iterator[str]:
    if isinstance(v, str): yield v
    elif isinstance(v, dict):
        for x in v.values(): yield from strings(x)
    elif isinstance(v, list):
        for x in v: yield from strings(x)


def first(v: Any, keys: set[str]):
    if isinstance(v, dict):
        for k, x in v.items():
            if k.lower() in keys and x not in (None, "", [], {}): return x
        for x in v.values():
            found = first(x, keys)
            if found not in (None, "", [], {}): return found
    elif isinstance(v, list):
        for x in v:
            found = first(x, keys)
            if found not in (None, "", [], {}): return found
    return None


def kind(o):
    v = o.get("type")
    return v if isinstance(v, str) and v else str(first(o.get("payload"), {"type", "event_type"}) or "unknown")


def role(o):
    v = first(o, {"role"})
    return v.lower() if isinstance(v, str) and v.lower() in {"user", "assistant", "system", "tool"} else None


def direct_user_text(o):
    if role(o) != "user": return []
    m = o.get("message")
    if not isinstance(m, dict) and isinstance(o.get("payload"), dict):
        p = o["payload"]; m = p if p.get("role") == "user" else p.get("message")
    if not isinstance(m, dict): return []
    c = m.get("content")
    if isinstance(c, str): return [c]
    if not isinstance(c, list): return []
    out = []
    for x in c:
        if isinstance(x, str): out.append(x)
        elif isinstance(x, dict) and str(x.get("type", "")).lower() in {"text", "input_text"}:
            t = x.get("text") or x.get("content")
            if isinstance(t, str): out.append(t)
    return out


def skill_patterns(names):
    return {
        n: {
            "explicit": re.compile(rf"(?<![\w/.-])/{re.escape(n)}(?![\w-])|(?<![\w-])\${re.escape(n)}(?![\w-])", re.I),
            "reference": re.compile(rf"(?<![\w-]){re.escape(n)}(?![\w-])", re.I),
        }
        for n in names
    }


def signals(o, line, names, patterns):
    found = set()
    for text in direct_user_text(o):
        for n, p in patterns.items():
            if p["explicit"].search(text): found.add((n, "EXPLICIT_INVOKE"))
            elif p["reference"].search(text): found.add((n, "USER_SKILL_REFERENCE"))
    for source in (o, o.get("payload")):
        if not isinstance(source, dict): continue
        for k, v in source.items():
            if k.lower() in SKILL_KEYS and isinstance(v, str):
                n = v.rsplit(":", 1)[-1]
                if n in names: found.add((n, "STRUCTURED_SKILL_REFERENCE"))
    for text in strings(o):
        for m in SKILL_PATH.finditer(text):
            n = m.group(1)
            if n in names: found.add((n, "SKILL_PATH_REFERENCE"))
    rank = {"SKILL_PATH_REFERENCE": 1, "STRUCTURED_SKILL_REFERENCE": 2, "USER_SKILL_REFERENCE": 3, "EXPLICIT_INVOKE": 4}
    best = {}
    for n, strength in found:
        if n not in best or rank[strength] > rank[best[n]]: best[n] = strength
    return [(n, s, line) for n, s in sorted(best.items())]


def roots(a):
    selected = set(a.host or HOSTS); out = {}
    if "codex" in selected: out["codex"] = (a.codex_root or Path(os.environ.get("CODEX_HOME", "~/.codex"))).expanduser()
    if "claude" in selected: out["claude"] = (a.claude_root or Path(os.environ.get("CLAUDE_CONFIG_DIR", "~/.claude"))).expanduser()
    return out


def files(host, root):
    base = root / ("sessions" if host == "codex" else "projects")
    if not base.is_dir(): base = root
    if not base.is_dir(): return []
    return [p for p in sorted(base.rglob("*.jsonl")) if p.is_file() and not (host == "codex" and p.name == "history.jsonl")]


def shown(p):
    r = p.expanduser().resolve(strict=False); home = Path.home().resolve(strict=False)
    try: return str(Path("~") / r.relative_to(home))
    except ValueError: return str(r)


def parse(host, path, names):
    counts = Counter(); roles = Counter(); sig = {}; times = []; invalid = 0; total = 0
    sid = root_id = parent = cwd = version = None; relation = "root"; root_resolution = "RESOLVED"
    if host == "claude":
        if path.parent.name == "subagents": sid, root_id, relation = path.stem, path.parent.parent.name, "subagent"
        else: sid = root_id = path.stem
    patterns = skill_patterns(names)
    with path.open(encoding="utf-8", errors="replace") as f:
        for line, raw in enumerate(f, 1):
            if not raw.strip(): continue
            try: o = json.loads(raw)
            except json.JSONDecodeError: invalid += 1; continue
            if not isinstance(o, dict): continue
            total += 1; k = kind(o); counts[k] += 1
            r = role(o); roles.update([r] if r else [])
            t = timestamp(o.get("timestamp") or o.get("time") or first(o.get("payload"), {"timestamp", "time", "created_at"}))
            if t: times.append(t)
            for n, strength, ln in signals(o, line, names, patterns): sig.setdefault((n, strength), set()).add(ln)
            if host == "codex" and k.lower() == "session_meta":
                p = o.get("payload", o)
                v = first(p, {"id", "session_id", "sessionid", "thread_id", "threadid"}); sid = sid or (v if isinstance(v, str) else None)
                v = first(p, {"parent_thread_id", "parentthreadid", "parent_session_id"})
                if isinstance(v, str) and v != sid: parent, relation = parent or v, "subagent"
                v = first(p, {"cwd"}); cwd = cwd or (v if isinstance(v, str) else None)
                v = first(p, {"cli_version", "cliversion", "version"}); version = version or (v if isinstance(v, str) else None)
            elif host == "claude":
                v = o.get("sessionId") or o.get("session_id")
                if relation == "root" and isinstance(v, str): sid = root_id = v
                cwd = cwd or (o.get("cwd") if isinstance(o.get("cwd"), str) else None)
                version = version or (o.get("version") if isinstance(o.get("version"), str) else None)
    sid = sid or path.stem
    if host == "codex":
        root_id = sid if parent is None else None
        root_resolution = "RESOLVED" if parent is None else "PENDING_PARENT"
    else: root_id = root_id or sid
    return {"host": host, "session_id": sid, "root_session_id": root_id, "root_resolution": root_resolution,
            "ancestor_session_ids": [], "relation": relation, "parent_session_id": parent, "source_path": shown(path),
            "cwd": cwd, "host_version": version, "started_at": iso(min(times)) if times else None,
            "ended_at": iso(max(times)) if times else None, "event_count": total, "invalid_json_lines": invalid,
            "event_types": dict(sorted(counts.items())), "roles": dict(sorted(roles.items())),
            "skill_signals": [{"skill": n, "strength": s, "lines": sorted(ls)} for (n, s), ls in sorted(sig.items())],
            "filter_state": "MATCH", "filter_uncertainty": []}


def normalize_codex_roots(sessions):
    codex = {s["session_id"]: s for s in sessions if s["host"] == "codex"}
    for s in codex.values():
        parent = s.get("parent_session_id")
        if not parent:
            s["root_session_id"] = s["session_id"]; s["root_resolution"] = "RESOLVED"; s["ancestor_session_ids"] = []; continue
        ancestors = []; seen = {s["session_id"]}; current_parent = parent; resolved = None; resolution = "UNRESOLVED_PARENT"
        while current_parent:
            ancestors.append(current_parent)
            if current_parent in seen: resolution = "CYCLE"; break
            seen.add(current_parent); node = codex.get(current_parent)
            if node is None: break
            next_parent = node.get("parent_session_id")
            if not next_parent: resolved = node["session_id"]; resolution = "RESOLVED"; break
            current_parent = next_parent
        s["ancestor_session_ids"] = ancestors; s["root_session_id"] = resolved; s["root_resolution"] = resolution


def skill_names(a):
    explicit = {x.strip() for x in a.skill if x.strip()}
    if explicit: return explicit
    out = set(); root = a.skills_root
    if root is None:
        for parent in Path(__file__).resolve().parents:
            if (parent / "skills").is_dir(): root = parent / "skills"; break
    if root and root.expanduser().is_dir(): out.update(p.parent.name for p in root.expanduser().glob("*/*/SKILL.md"))
    return out


def norm(p): return os.path.normcase(os.path.normpath(str(Path(p).expanduser())))


def keep_session(s, a, since, until):
    if a.session:
        related = {s["session_id"], s.get("root_session_id"), s.get("parent_session_id"), *s.get("ancestor_session_ids", [])}
        if not related.intersection(a.session): return False
    uncertain = []
    if a.project:
        if not s["cwd"]: uncertain.append("project")
        else:
            c = norm(s["cwd"]); matches = False
            for p in a.project:
                try: matches |= os.path.commonpath([c, norm(p)]) == norm(p)
                except ValueError: pass
            if not matches: return False
    start, end = timestamp(s["started_at"]), timestamp(s["ended_at"])
    if since and end is None: uncertain.append("time")
    elif since and end < since: return False
    if until and start is None: uncertain.append("time")
    elif until and start >= until: return False
    s["filter_uncertainty"] = sorted(set(uncertain)); s["filter_state"] = "UNCERTAIN" if uncertain else "MATCH"
    return True


def build(a):
    since, until = bound(a.since, "--since"), bound(a.until, "--until")
    if since and until and since >= until: raise ValueError("--since must be earlier than --until")
    rs, names, sessions, observed = roots(a), skill_names(a), [], []
    for host, root in rs.items():
        fs = files(host, root); observed.append({"host": host, "path": shown(root), "status": "scanned" if root.exists() else "missing", "files": len(fs)})
        for p in fs:
            try: sessions.append(parse(host, p, names))
            except OSError as e: observed.append({"host": host, "path": shown(p), "status": "unreadable", "files": 0, "error": str(e)})
    normalize_codex_roots(sessions)
    sessions = [s for s in sessions if keep_session(s, a, since, until)]
    sessions.sort(key=lambda s: (s["started_at"] is None, s["started_at"] or "", s["host"], s["root_session_id"] or "", s["session_id"]))
    resolved_roots = {(s["host"], s["root_session_id"]) for s in sessions if s["root_session_id"] is not None}
    return {"schema": SCHEMA, "filters": {"hosts": sorted(rs), "since": iso(since), "until": iso(until), "projects": [str(p.expanduser()) for p in a.project], "session_ids": sorted(a.session), "skills": sorted(names)},
            "privacy": {"raw_transcript_content_emitted": False, "source_files_modified": False}, "roots": observed,
            "summary": {"sessions": len(sessions), "resolved_root_sessions": len(resolved_roots), "unresolved_root_members": sum(s["root_session_id"] is None for s in sessions), "subagent_sessions": sum(s["relation"] == "subagent" for s in sessions), "invalid_json_lines": sum(s["invalid_json_lines"] for s in sessions)},
            "sessions": sessions}


def main(argv=None):
    try: report = build(args(argv))
    except ValueError as e: print(f"session-evidence: {e}", file=sys.stderr); return 2
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2, sort_keys=True); print(); return 0

if __name__ == "__main__": raise SystemExit(main())
