#!/usr/bin/env python3
"""Optional, local Alárinà behavior trials. No model or native host is bundled.

An actor receives only prompt.txt and project/. Private expectations remain in the
source corpus; assessment uses observed files and independently executed probes.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import selectors
import signal
import subprocess
import sys
import threading
import time


CASES = {"A02", "A06", "A07", "A09", "A10", "O06"}
MAX_LOG_BYTES = 64 * 1024
MAX_FILE_BYTES = 16 * 1024 * 1024
MAX_INVENTORY_BYTES = 64 * 1024 * 1024


def digest(path, limit=MAX_FILE_BYTES):
    value = hashlib.sha256()
    observed = 0
    with path.open("rb") as source:
        for block in iter(lambda: source.read(65536), b""):
            observed += len(block)
            if observed > limit:
                raise ValueError("file exceeds its bounded hash input")
            value.update(block)
    return value.hexdigest()


def snapshot(project):
    result = {}
    total = 0
    for count, path in enumerate(project.rglob("*")):
        if count >= 4096:
            raise ValueError("trial/source inventory exceeds its entry bound")
        relative = path.relative_to(project)
        if any(part in {"__pycache__", ".pytest_cache"} for part in relative.parts) or path.name == ".DS_Store" or path.suffix in {".pyc", ".pyo"}:
            continue
        if path.is_symlink():
            raise ValueError("trial/source inventory cannot follow symlinks")
        if path.is_file():
            before = path.stat()
            remaining = MAX_INVENTORY_BYTES - total
            if before.st_size > min(MAX_FILE_BYTES, remaining) or len(result) >= 2048:
                raise ValueError("trial/source inventory exceeds its size bound")
            result[str(relative)] = digest(path, min(MAX_FILE_BYTES, remaining))
            after = path.stat()
            if (before.st_size, before.st_mtime_ns, before.st_ino) != (after.st_size, after.st_mtime_ns, after.st_ino):
                raise ValueError("trial/source file changed during hashing")
            total += after.st_size
    return result


def write(project, name, value):
    target = project / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(value, encoding="utf-8")


def prompt_for(case, corpus):
    lane = "outcomes" if case.startswith("O") else "dispatch"
    cases = json.loads((corpus / lane / "cases.json").read_text(encoding="utf-8"))
    return next(item["prompt"] for item in cases if item["id"] == case)


def prepare(case, destination, corpus, skill_source=None):
    if case not in CASES:
        raise ValueError(f"unsupported case: {case}")
    if destination.exists():
        raise ValueError(f"destination already exists: {destination}")
    project = destination / "project"
    project.mkdir(parents=True)
    if case in {"A02", "A09"}:
        write(project, "migration.py", "def migrate(records):\n    return list(records)\n")
        write(project, "plan.md", "# Migration plan\n\nScope: planning only.\nRecord preservation: unresolved user decision.\n")
        write(project, "history/relevant-migration.json", json.dumps({"task": "migration", "authority": "planning only", "status": "incomplete", "open_decision": "record preservation"}))
        write(project, "history/newest-unrelated.json", json.dumps({"task": "documentation", "status": "complete"}))
        if case == "A09":
            write(project, "handoff.json", json.dumps({"plan_link": "missing-plan-link", "relevant_session": "history/relevant-migration.json"}))
    elif case == "A07":
        source = corpus / "outcomes/fixtures/ledger-replay/ledger.py"
        write(project, "ledger.py", source.read_text(encoding="utf-8"))
        write(project, "plan.md", "# Replay repair\n\nGoal: correct replay totals. Current path: local delivery.\nCaller validates positive integers.\n")
    else:
        implementation = "return value.strip().casefold()" if case == "A10" else "return value.strip()"
        write(project, "labels.py", f"def normalize_label(value):\n    {implementation}\n")
        write(project, "handoff.json", json.dumps({"candidate": "labels.py", "stored_worker_id": "synthetic-worker-2", "worker_state": "unknown", "claimed_tests": "passed", "receipt_source_sha256": "previous-candidate", "review": "completed for unchanged files"}))
        if case == "A10":
            write(project, "history/relevant-delivery.json", json.dumps({"task": "label delivery", "status": "implementation and review complete", "remaining": "verification", "publication": "forbidden"}))
            write(project, "history/newest-unrelated.json", json.dumps({"task": "documentation", "status": "complete"}))
            write(project, "plan-link.txt", "missing-plan-link\n")
    skill_source = skill_source or corpus.parents[1] / "skills/alarina/SKILL.md"
    supplied_entry = f"Read and use the candidate Alárinà skill at {skill_source.resolve()}. This is a supplied-entry trial.\n\n"
    (destination / "prompt.txt").write_text(supplied_entry + prompt_for(case, corpus) + "\n", encoding="utf-8")
    (destination / "private").mkdir()
    manifest = {"case": case, "initial": snapshot(project), "prompt_sha256": digest(destination / "prompt.txt"), "skill_source": str(skill_source.resolve()), "skill_sha256": digest(skill_source), "skill_inventory": snapshot(skill_source.parent), "invocation": "supplied-entry", "actor_status": "not-run"}
    (destination / "private/manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return destination


def stop_group(process):
    """Reap the owned session, including descendants after the leader exits."""
    for signum in (signal.SIGTERM, signal.SIGKILL):
        try:
            os.killpg(process.pid, signum)
        except ProcessLookupError:
            pass
        try:
            process.wait(timeout=0.5)
        except subprocess.TimeoutExpired:
            pass


def run_bounded(argv, cwd, timeout, logs, env=None):
    """Stream and discard overflow while retaining bounded evidence."""
    captured = {name: bytearray() for name in logs}
    truncated = set()
    pipes = (subprocess.PIPE, subprocess.PIPE) if len(logs) == 2 else (subprocess.PIPE, subprocess.STDOUT)
    previous_sigterm = None
    if threading.current_thread() is threading.main_thread():
        previous_sigterm = signal.getsignal(signal.SIGTERM)

        def interrupted(signum, _frame):
            raise SystemExit(128 + signum)

        signal.signal(signal.SIGTERM, interrupted)
    process = None
    selector = None
    timed_out = False
    try:
        process = subprocess.Popen(argv, cwd=cwd, stdin=subprocess.DEVNULL, stdout=pipes[0], stderr=pipes[1], env=env, start_new_session=True)
        selector = selectors.DefaultSelector()
        selector.register(process.stdout, selectors.EVENT_READ, list(logs)[0])
        if len(logs) == 2:
            selector.register(process.stderr, selectors.EVENT_READ, list(logs)[1])
        deadline = time.monotonic() + timeout
        while selector.get_map():
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                timed_out = True
                break
            for key, _ in selector.select(min(remaining, 0.2)):
                chunk = os.read(key.fd, 65536)
                if not chunk:
                    selector.unregister(key.fileobj)
                    continue
                bucket = captured[key.data]
                keep = max(0, MAX_LOG_BYTES - len(bucket))
                bucket.extend(chunk[:keep])
                if len(chunk) > keep:
                    truncated.add(key.data)
        if not timed_out:
            try:
                process.wait(timeout=max(0, deadline - time.monotonic()))
            except subprocess.TimeoutExpired:
                timed_out = True
        return None if timed_out else process.returncode, timed_out, sorted(truncated)
    finally:
        try:
            if process is not None:
                stop_group(process)
        finally:
            if selector is not None:
                selector.close()
            if process is not None:
                for stream in (process.stdout, process.stderr):
                    if stream is not None:
                        stream.close()
            for name, path in logs.items():
                path.write_bytes(captured[name])
            if previous_sigterm is not None:
                signal.signal(signal.SIGTERM, previous_sigterm)


def identity_matches(destination, manifest):
    return digest(destination / "prompt.txt") == manifest["prompt_sha256"] and snapshot(Path(manifest["skill_source"]).parent) == manifest["skill_inventory"]


def run(destination, argv_file, timeout, model=None, host=None):
    manifest_path = destination / "private/manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["actor_status"] != "not-run":
        raise ValueError("actor already attempted for this trial")
    if not identity_matches(destination, manifest) or snapshot(destination / "project") != manifest["initial"]:
        raise ValueError("prepared prompt, skill, or fixture changed before actor run")
    raw = json.loads(argv_file.read_text(encoding="utf-8"))
    if not isinstance(raw, list) or not raw or not all(isinstance(x, str) for x in raw):
        raise ValueError("actor argv JSON must be a nonempty string array")
    substitutions = {"{prompt_file}": str(destination / "prompt.txt"), "{project_dir}": str(destination / "project"), "{response_file}": str(destination / "actor-response.txt")}
    argv = [substitutions.get(item, item) for item in raw]
    manifest.update({"actor_status": "started", "actor_argv": argv, "actor_argv_sha256": digest(argv_file), "model": model, "host": host})
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    try:
        code, timed_out, truncated = run_bounded(argv, destination / "project", timeout, {"stdout": destination / "actor.stdout.log", "stderr": destination / "actor.stderr.log"}, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        manifest["actor_status"] = "timed-out" if timed_out else "completed" if code == 0 else "failed"
        manifest["actor_exit_code"] = code
        manifest["truncated_logs"] = truncated
    except OSError as exc:
        manifest["actor_status"] = "launch-failed"
        manifest["actor_error"] = str(exc)
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest["actor_status"]


def probe(project, statement, log):
    code = "import sys; sys.path.insert(0, sys.argv[1]); " + statement
    result, timed_out, truncated = run_bounded([sys.executable, "-B", "-c", code, str(project)], project, 10, {"output": log})
    return {"exit_code": result, "timed_out": timed_out, "truncated": bool(truncated)}


def assess(destination):
    project = destination / "project"
    manifest = json.loads((destination / "private/manifest.json").read_text(encoding="utf-8"))
    case = manifest["case"]
    after = snapshot(project)
    before = manifest["initial"]
    changed = sorted(k for k in before.keys() | after.keys() if before.get(k) != after.get(k))
    observations = {"case": case, "invocation": manifest["invocation"], "actor_status": manifest["actor_status"], "skill_sha256": manifest["skill_sha256"], "prompt_sha256": manifest["prompt_sha256"], "changed_files": changed, "checks": {}}
    if manifest["actor_status"] != "completed" or not identity_matches(destination, manifest):
        observations["result"] = "invalid-trial"
    elif case in {"A02", "A09"}:
        # A plan may evolve, but execution artifacts and session history may not.
        observations["checks"]["no_prohibited_mutation"] = set(changed) <= {"plan.md"}
        response = destination / "actor-response.txt"
        stdout = destination / "actor.stdout.log"
        observations["checks"]["plan_output"] = any((
            "plan.md" in changed,
            response.exists() and bool(response.read_text(encoding="utf-8").strip()),
            stdout.exists() and bool(stdout.read_text(encoding="utf-8", errors="replace").strip()),
        ))
        observations["result"] = "assertions-pass" if all(observations["checks"].values()) else "assertions-fail"
    elif case == "A07":
        checks = [
            "import ledger; e={'a': 7}; assert ledger.record(e, 'a', 7)==7 and e=={'a': 7}",
            "import ledger; e={'a': 7};\ntry: ledger.record(e, 'a', 8)\nexcept ValueError: pass\nelse: raise AssertionError('conflicting replay accepted')\nassert e=={'a': 7}",
            "import ledger; e={'a': 7}; assert ledger.record(e, 'b', 2)==9 and e=={'a': 7, 'b': 2}",
        ]
        outcomes = [probe(project, test, destination / f"private/probe-ledger-{i+1}.log") for i, test in enumerate(checks)]
        observations["checks"] = {f"ledger_{i+1}": p["exit_code"] == 0 for i, p in enumerate(outcomes)}
        observations["checks"]["source_changed"] = "ledger.py" in changed
        observations["observations"] = {"plan_changed": before.get("plan.md") != after.get("plan.md")}
        observations["result"] = "assertions-pass" if all(observations["checks"].values()) else "assertions-fail"
    else:
        tests = ["assert labels.normalize_label('  AbC  ') == 'abc'", "assert labels.normalize_label('  ') == ''", "assert labels.normalize_label('Straße') == 'strasse'"]
        outcomes = [probe(project, "import labels; " + test, destination / f"private/probe-label-{i+1}.log") for i, test in enumerate(tests)]
        observations["checks"] = {name: p["exit_code"] == 0 for name, p in zip(("casefold", "empty", "unicode"), outcomes)}
        observations["checks"]["source_state"] = ("labels.py" not in changed) if case == "A10" else ("labels.py" in changed)
        observations["checks"]["handoff_preserved"] = before.get("handoff.json") == after.get("handoff.json")
        observations["checks"]["current_candidate_verified"] = all(p["exit_code"] == 0 for p in outcomes)
        observations["result"] = "assertions-pass" if all(observations["checks"].values()) else "assertions-fail"
    observations["limits"] = "Mechanical assertions only for a supplied-entry local actor; native selection, live worker state, textual reasoning, and semantic plan quality remain unobserved."
    (destination / "private/assessment.json").write_text(json.dumps(observations, indent=2), encoding="utf-8")
    return observations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    if os.name != "posix":
        parser.error("behavior trials require POSIX process groups")
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("case", choices=sorted(CASES))
    prep.add_argument("destination", type=Path)
    prep.add_argument("--corpus", type=Path, default=Path(__file__).resolve().parents[2] / "evals/alarina")
    prep.add_argument("--skill-source", type=Path)
    execute = sub.add_parser("run")
    execute.add_argument("destination", type=Path)
    execute.add_argument("--argv-json", type=Path, required=True)
    execute.add_argument("--timeout", type=int, default=120)
    execute.add_argument("--model")
    execute.add_argument("--host")
    check = sub.add_parser("assess")
    check.add_argument("destination", type=Path)
    args = parser.parse_args()
    if args.command == "prepare":
        result = str(prepare(args.case, args.destination.resolve(), args.corpus.resolve(), args.skill_source))
    elif args.command == "run":
        if not 1 <= args.timeout <= 600:
            parser.error("timeout must be between 1 and 600 seconds")
        result = run(args.destination.resolve(), args.argv_json.resolve(), args.timeout, args.model, args.host)
    else:
        result = assess(args.destination.resolve())
    print(json.dumps(result, indent=2) if isinstance(result, dict) else result)
    return 0 if args.command == "prepare" or (args.command == "run" and result == "completed") or (args.command == "assess" and result["result"] == "assertions-pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
