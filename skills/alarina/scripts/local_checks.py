"""Local command checks with explicit proof and candidate freshness.

This module has no import-time I/O. It does not discover project policy, approve
publication, or contact a remote provider. Callers supply checks and a private
output directory for one run.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import selectors
import signal
import stat
import subprocess
import threading
import time
import xml.etree.ElementTree as ET

SCHEMA_VERSION = 1
LOG_LIMIT = 128 * 1024
_TEST_PROOFS = {"unittest", "pytest", "tap", "junit"}
_PROOFS = _TEST_PROOFS | {"exit"}


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _json_digest(value: object) -> str:
    return _digest(json.dumps(value, sort_keys=True, separators=(",", ":")).encode())


def _git(project: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    try:
        return subprocess.run(
            ["git", "-C", str(project), *args], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, check=False, timeout=20,
        )
    except FileNotFoundError:
        return subprocess.CompletedProcess(["git", *args], 127, b"", b"git unavailable")


def _within(path: Path, root: Path) -> bool:
    return path == root or root in path.parents


def _relative_path(project: Path, value: str, *, directory: bool) -> Path:
    if not isinstance(value, str) or not value or "\x00" in value:
        raise ValueError("path must be a nonempty repo-relative string")
    raw = Path(value)
    if raw.is_absolute() or ".." in raw.parts:
        raise ValueError("path must be repo-relative without traversal")
    resolved = (project / raw).resolve(strict=False)
    if not _within(resolved, project):
        raise ValueError("path resolves outside the project")
    resolved_parts = resolved.relative_to(project).parts
    if (raw.parts and raw.parts[0] == ".git") or (resolved_parts and resolved_parts[0] == ".git"):
        raise ValueError("path may not enter .git")
    if directory:
        if not resolved.is_dir():
            raise ValueError("check cwd is not a directory")
    elif resolved.exists() and not resolved.is_file():
        raise ValueError("proof path is not a regular file")
    return resolved


def _file_state(path: Path, project: Path, *, allow_deleted: bool = False) -> dict:
    rel = path.relative_to(project).as_posix()
    parent_fd = None
    try:
        parent_fd = os.open(project, os.O_RDONLY | os.O_DIRECTORY)
        for part in path.relative_to(project).parts[:-1]:
            next_fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                              dir_fd=parent_fd)
            os.close(parent_fd)
            parent_fd = next_fd
        name = path.name
        st = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        result = {"path": rel, "mode": stat.S_IMODE(st.st_mode)}
        if stat.S_ISLNK(st.st_mode):
            result.update(kind="symlink", target=os.readlink(name, dir_fd=parent_fd))
        elif stat.S_ISREG(st.st_mode):
            fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd)
            with os.fdopen(fd, "rb") as stream:
                if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                    raise ValueError("file changed while reading")
                h = hashlib.sha256()
                while block := stream.read(1024 * 1024):
                    h.update(block)
            result.update(kind="file", sha256=h.hexdigest(), size=st.st_size)
        elif stat.S_ISDIR(st.st_mode):
            result.update(kind="directory")
        else:
            result.update(kind="unsupported")
        return result
    except FileNotFoundError:
        if allow_deleted:
            return {"path": rel, "kind": "deleted"}
        return {"path": rel, "kind": "unreadable", "error": "FileNotFoundError"}
    except (OSError, ValueError) as error:
        return {"path": rel, "kind": "unreadable", "error": type(error).__name__}
    finally:
        if parent_fd is not None:
            os.close(parent_fd)


def _snapshot_files(project: Path, paths: list[str],
                    tracked: set[str] | None = None) -> list[dict]:
    tracked = tracked or set()
    return [_file_state(project / name, project, allow_deleted=name in tracked)
            for name in sorted(set(paths))]


def candidate_snapshot(project: Path, base: str | None = None) -> dict:
    """Identify HEAD, optional integration base, index and the complete visible tree.

    Git ignored artifacts and submodule interiors are deliberately not claimed as
    complete. An unreadable file, unmerged index or unresolved base limits proof.
    """
    project = Path(project).resolve(strict=True)
    if not project.is_dir():
        raise ValueError("project must be a directory")
    root = _git(project, "rev-parse", "--show-toplevel")
    is_git = root.returncode == 0 and Path(os.fsdecode(root.stdout.strip())).resolve() == project
    limitations: list[str] = []
    incomplete = False
    if is_git:
        head_run = _git(project, "rev-parse", "--verify", "HEAD^{commit}")
        head = os.fsdecode(head_run.stdout.strip()) if head_run.returncode == 0 else None
        if head is None:
            limitations.append("HEAD could not be resolved")
            incomplete = True
        common_run = _git(project, "rev-parse", "--path-format=absolute", "--git-common-dir")
        common_dir = (os.fsdecode(common_run.stdout.strip()) if common_run.returncode == 0 else None)
        if common_dir is None:
            limitations.append("common Git directory could not be resolved")
            incomplete = True
        base_oid = None
        if base is not None:
            base_run = _git(project, "rev-parse", "--verify", f"{base}^{{commit}}")
            base_oid = os.fsdecode(base_run.stdout.strip()) if base_run.returncode == 0 else None
            if base_oid is None:
                limitations.append("integration base could not be resolved")
                incomplete = True
        staged = _git(project, "ls-files", "--stage", "-z")
        others = _git(project, "ls-files", "--others", "--exclude-standard", "-z")
        if staged.returncode or others.returncode:
            limitations.append("Git file inventory failed")
            incomplete = True
        index: list[dict] = []
        tracked: list[str] = []
        for entry in staged.stdout.split(b"\x00"):
            if not entry:
                continue
            meta, _, name = entry.partition(b"\t")
            fields = meta.split()
            if len(fields) != 3 or not name:
                limitations.append("malformed Git index entry")
                incomplete = True
                continue
            decoded = os.fsdecode(name)
            index.append({"path": decoded, "mode": os.fsdecode(fields[0]),
                          "object": os.fsdecode(fields[1]), "stage": os.fsdecode(fields[2])})
            tracked.append(decoded)
            if fields[2] != b"0":
                limitations.append("unmerged index")
                incomplete = True
            if fields[0] == b"160000":
                limitations.append("submodule interior is not included")
                incomplete = True
        untracked = [os.fsdecode(name) for name in others.stdout.split(b"\x00") if name]
        files = _snapshot_files(project, tracked + untracked, set(tracked))
        if any(item["kind"] in {"unreadable", "unsupported"} for item in files):
            limitations.append("unreadable or unsupported file")
            incomplete = True
        limitations.append("Git-ignored artifacts are outside this candidate inventory")
        identity = {"kind": "git", "project": str(project), "common_git_dir": common_dir,
                    "head": head, "base": base, "base_oid": base_oid,
                    "index": sorted(index, key=lambda x: (x["path"], x["stage"])),
                    "files": files}
    else:
        if base is not None:
            limitations.append("integration base requires a Git repository")
            incomplete = True
        paths: list[str] = []
        for root_dir, dirs, filenames in os.walk(project, followlinks=False):
            dirs[:] = [d for d in dirs if d != ".git"]
            directory = Path(root_dir)
            paths.extend(str((directory / name).relative_to(project)) for name in filenames)
            paths.extend(str((directory / name).relative_to(project))
                         for name in dirs if (directory / name).is_symlink())
        files = _snapshot_files(project, paths)
        if any(item["kind"] in {"unreadable", "unsupported"} for item in files):
            limitations.append("unreadable or unsupported file")
            incomplete = True
        limitations.append("non-Git inventory has no HEAD, index, ignore rules or integration base")
        identity = {"kind": "non-git", "project": str(project), "files": files, "base": base}
    return {"schema_version": SCHEMA_VERSION, **identity,
            "candidate_digest": _json_digest(identity),
            "complete": not incomplete,
            "limitations": sorted(set(limitations))}


def _validate_output(project: Path, output: Path, is_git: bool) -> Path:
    output = Path(output).resolve(strict=False)
    if output.exists():
        raise FileExistsError(f"run output already exists: {output}")
    if _within(output, project):
        if output.relative_to(project).parts[0] == ".git":
            raise ValueError("run output may not enter .git")
        if not is_git:
            raise ValueError("run output inside a non-Git project is not private")
        rel = output.relative_to(project).as_posix()
        ignored = _git(project, "check-ignore", "-q", "--no-index", rel)
        tracked = _git(project, "ls-files", "-z", "--", rel)
        if ignored.returncode != 0 or tracked.stdout:
            raise ValueError("run output inside project must be ignored and untracked")
    return output


def _validate_check(project: Path, item: dict, seen: set[str]) -> dict:
    if not isinstance(item, dict):
        raise ValueError("check must be an object")
    if set(item) - {"id", "argv", "cwd", "timeout_seconds", "proof"}:
        raise ValueError("unknown check field")
    name = item.get("id")
    if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,79}", name):
        raise ValueError("check id must be a short safe identifier")
    if name in seen:
        raise ValueError("duplicate check id")
    seen.add(name)
    argv = item.get("argv")
    if not isinstance(argv, list) or not argv or any(
        not isinstance(arg, str) or not arg or "\x00" in arg for arg in argv
    ):
        raise ValueError("argv must be a nonempty list of literal strings")
    timeout = item.get("timeout_seconds", 300)
    if type(timeout) is not int or not 1 <= timeout <= 3600:
        raise ValueError("timeout_seconds must be an integer from 1 to 3600")
    cwd = _relative_path(project, item.get("cwd", "."), directory=True)
    proof = item.get("proof")
    if not isinstance(proof, dict) or proof.get("type") not in _PROOFS:
        raise ValueError("proof.type must be exit, unittest, pytest, tap or junit")
    if set(proof) - {"type", "path"}:
        raise ValueError("unknown proof field")
    kind = proof["type"]
    if kind == "junit":
        if "path" not in proof:
            raise ValueError("junit proof needs a path")
        proof_path = _relative_path(project, proof["path"], directory=False)
    elif "path" in proof:
        raise ValueError("only junit proof accepts path")
    else:
        proof_path = None
    return {"id": name, "argv": argv, "cwd": cwd, "timeout_seconds": timeout,
            "proof_type": kind, "proof_path": proof_path}


def _stop_owned_group(proc: subprocess.Popen) -> None:
    """Stop the process and its descendants after timeout or interrupted collection."""
    try:
        os.killpg(proc.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    try:
        proc.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass
    # The leader may have exited while a child ignored TERM.
    try:
        os.killpg(proc.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    proc.wait(timeout=2)


def _run_command(argv: list[str], cwd: Path, timeout: int, log: Path) -> tuple[int | None, bool, str, bool]:
    """Drain bounded output and reap the owned group on timeout or interruption."""
    captured = bytearray()
    truncated = False
    previous_sigterm = None
    if threading.current_thread() is threading.main_thread():
        previous_sigterm = signal.getsignal(signal.SIGTERM)

        def interrupted(signum, _frame):
            raise SystemExit(128 + signum)

        signal.signal(signal.SIGTERM, interrupted)
    try:
        try:
            proc = subprocess.Popen(argv, cwd=cwd, stdin=subprocess.DEVNULL,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    start_new_session=True)
        except FileNotFoundError:
            return None, False, "", False
        selector = None
        deadline = time.monotonic() + timeout
        timed_out = False
        stopped = False
        try:
            selector = selectors.DefaultSelector()
            assert proc.stdout is not None
            selector.register(proc.stdout, selectors.EVENT_READ)
            while selector.get_map():
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    timed_out = True
                    break
                for key, _ in selector.select(min(remaining, 0.2)):
                    chunk = os.read(key.fd, 65536)
                    if not chunk:
                        selector.unregister(key.fileobj)
                        break
                    keep = max(0, LOG_LIMIT - len(captured))
                    captured.extend(chunk[:keep])
                    if len(chunk) > keep:
                        truncated = True
            if not timed_out:
                try:
                    proc.wait(timeout=max(0, deadline - time.monotonic()))
                except subprocess.TimeoutExpired:
                    timed_out = True
            if timed_out:
                _stop_owned_group(proc)
                stopped = True
        except BaseException:
            _stop_owned_group(proc)
            stopped = True
            raise
        finally:
            # A successful leader can leave descendants with closed stdout.
            # Verification owns that process group only for this check's lifetime.
            if not stopped:
                _stop_owned_group(proc)
            if selector is not None:
                selector.close()
            if proc.stdout is not None:
                proc.stdout.close()
        text = captured.decode("utf-8", errors="replace")
        log.write_text(text + ("\n[log truncated]\n" if truncated else ""), encoding="utf-8")
        return proc.returncode, timed_out, text, truncated
    finally:
        if previous_sigterm is not None:
            signal.signal(signal.SIGTERM, previous_sigterm)


def _parse_unittest(text: str) -> dict:
    runs = list(re.finditer(r"(?m)^Ran (\d+) tests? in [^\n]+$", text))
    if not runs:
        raise ValueError("missing unittest run summary")
    totals = {"total": 0, "passed": 0, "failed": 0, "skipped": 0}
    for index, run in enumerate(runs):
        tail = text[run.end():runs[index + 1].start() if index + 1 < len(runs) else len(text)]
        status = re.search(r"(?m)^(OK(?: \([^\n]+\))?|FAILED \([^\n]+\))\s*$", tail)
        if not status:
            raise ValueError("missing unittest result")
        summary = status.group(1)
        values = {key: int(value) for key, value in re.findall(
            r"(failures|errors|skipped|expected failures|unexpected successes)=(\d+)", summary)}
        ran = int(run.group(1))
        failed = values.get("failures", 0) + values.get("errors", 0) + values.get("unexpected successes", 0)
        skipped = values.get("skipped", 0) + values.get("expected failures", 0)
        passed = ran - failed - skipped
        if passed < 0 or ran < failed + skipped:
            raise ValueError("inconsistent unittest counts")
        for key, value in (("total", ran), ("passed", passed),
                           ("failed", failed), ("skipped", skipped)):
            totals[key] += value
    return totals


def _parse_pytest(text: str) -> dict:
    summaries = re.findall(
        r"(?m)^\s*(?:=+\s*)?([^\n]*\b(?:passed|failed|error|errors|skipped)\b[^\n]*?)(?:\s*=+)?\s*$",
        text,
    )
    summaries = [line for line in summaries if re.search(
        r"\b\d+\s+(?:passed|failed|errors?|skipped|xfailed|xpassed)\b", line)]
    if not summaries:
        raise ValueError("missing pytest result summary")
    totals = {"total": 0, "passed": 0, "failed": 0, "skipped": 0}
    for line in summaries:
        values = {key: int(count) for count, key in re.findall(
            r"(\d+)\s+(passed|failed|error|errors|skipped|xfailed|xpassed|deselected)", line)}
        passed = values.get("passed", 0)
        failed = (values.get("failed", 0) + values.get("error", 0) +
                  values.get("errors", 0) + values.get("xpassed", 0))
        skipped = values.get("skipped", 0) + values.get("xfailed", 0)
        for key, value in (("total", passed + failed + skipped), ("passed", passed),
                           ("failed", failed), ("skipped", skipped)):
            totals[key] += value
    return totals


def _parse_tap(text: str) -> dict:
    plans = re.findall(r"(?m)^1\.\.(\d+)\s*$", text)
    if len(plans) != 1 or re.search(r"(?im)^Bail out!", text):
        raise ValueError("missing or invalid TAP plan")
    cases = re.findall(r"(?m)^(not ok|ok)\s+(\d+)([^\n]*)$", text)
    count = int(plans[0])
    numbers = [int(number) for _, number, _ in cases]
    if numbers != list(range(1, count + 1)):
        raise ValueError("TAP case numbering does not match plan")
    skipped = sum(1 for _, _, detail in cases if re.search(r"#\s*SKIP\b", detail, re.I))
    failed = sum(1 for status, _, detail in cases if status == "not ok" and not re.search(r"#\s*SKIP\b", detail, re.I))
    return {"total": count, "passed": count - skipped - failed,
            "failed": failed, "skipped": skipped}


def _parse_junit(data: bytes) -> dict:
    try:
        root = ET.fromstring(data)
    except ET.ParseError as error:
        raise ValueError(f"invalid JUnit XML: {error}") from error
    if root.tag not in {"testsuite", "testsuites"}:
        raise ValueError("invalid JUnit root")
    cases = list(root.iter("testcase"))
    if not cases:
        raise ValueError("JUnit has no testcase entries")
    failed = sum(any(child.tag in {"failure", "error"} for child in case) for case in cases)
    skipped = sum(not any(child.tag in {"failure", "error"} for child in case)
                  and any(child.tag == "skipped" for child in case) for case in cases)
    counts = {"total": len(cases), "passed": len(cases) - failed - skipped,
              "failed": failed, "skipped": skipped}
    # Suite summaries may include nested suites. Validate leaf suites only, then
    # root when it supplies a total; never add parent and child suite totals.
    def validate_summary(suite: ET.Element, subset: list[ET.Element]) -> None:
        expected = {
            "tests": len(subset),
            "skipped": sum(any(child.tag == "skipped" for child in item) and
                           not any(child.tag in {"failure", "error"} for child in item)
                           for item in subset),
            "failures": sum(any(child.tag == "failure" for child in item)
                            for item in subset),
            "errors": sum(any(child.tag == "error" for child in item)
                          for item in subset),
        }
        for key, value in expected.items():
            if key in suite.attrib:
                try:
                    observed = int(suite.attrib[key])
                except ValueError as error:
                    raise ValueError(f"invalid JUnit {key} count") from error
                if observed != value:
                    raise ValueError(f"JUnit {key} summary disagrees with cases")

    for suite in root.iter("testsuite"):
        if not any(child.tag == "testsuite" for child in suite):
            leaf_cases = list(suite.iter("testcase"))
            validate_summary(suite, leaf_cases)
    if root.tag == "testsuites" or any(child.tag == "testsuite" for child in root):
        validate_summary(root, cases)
    return counts


def _safe_proof(project: Path, path: Path | None) -> tuple[tuple, bytes] | None:
    """Open each proof component without following symlinks; no outside reads."""
    if path is None:
        return None
    relative = path.relative_to(project)
    if not relative.parts or ".git" in relative.parts:
        raise ValueError("proof path may not enter .git")
    parent_fd = os.open(project, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        for part in relative.parts[:-1]:
            try:
                next_fd = os.open(part, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) |
                                  getattr(os, "O_NOFOLLOW", 0), dir_fd=parent_fd)
            except FileNotFoundError:
                return None
            os.close(parent_fd)
            parent_fd = next_fd
        try:
            file_fd = os.open(relative.parts[-1], os.O_RDONLY |
                              getattr(os, "O_NOFOLLOW", 0), dir_fd=parent_fd)
        except FileNotFoundError:
            return None
        try:
            st = os.fstat(file_fd)
            if not stat.S_ISREG(st.st_mode):
                raise ValueError("proof is not a regular file")
            if st.st_size > 8 * 1024 * 1024:
                raise ValueError("proof exceeds 8 MiB parser bound")
            with os.fdopen(file_fd, "rb", closefd=False) as stream:
                data = stream.read(8 * 1024 * 1024 + 1)
            if len(data) > 8 * 1024 * 1024:
                raise ValueError("proof exceeds 8 MiB parser bound")
            return ((st.st_ino, st.st_mtime_ns, st.st_size, _digest(data)), data)
        finally:
            os.close(file_fd)
    finally:
        os.close(parent_fd)


def _evaluate_proof(kind: str, text: str, project: Path, path: Path | None,
                    before: tuple | None, started_ns: int) -> dict | None:
    if kind == "exit":
        return None
    if kind == "unittest":
        return _parse_unittest(text)
    if kind == "pytest":
        return _parse_pytest(text)
    if kind == "tap":
        return _parse_tap(text)
    assert path is not None
    opened = _safe_proof(project, path)
    if opened is None:
        raise ValueError("JUnit report missing or stale")
    after, data = opened
    if after == before or after[1] < started_ns:
        raise ValueError("JUnit report missing or stale")
    return _parse_junit(data)


def check_freshness(project: Path, receipt: dict, config_digest: str = "",
                    base: str | None = None) -> dict:
    """Compare current candidate and config to the receipt; never approve publishing."""
    if not isinstance(receipt, dict) or receipt.get("schema_version") != SCHEMA_VERSION:
        return {"status": "unknown", "fresh": False, "reasons": ["invalid receipt schema"]}
    if base is None:
        base = receipt.get("base")
    run_before = receipt.get("snapshot_before")
    before = receipt.get("snapshot_after")
    if not isinstance(before, dict) or not isinstance(run_before, dict):
        return {"status": "unknown", "fresh": False,
                "reasons": ["missing receipt snapshot"]}
    if (receipt.get("gate_status") == "stale" or
            run_before.get("candidate_digest") != before.get("candidate_digest")):
        return {"status": "stale", "fresh": False,
                "reasons": ["candidate changed during recorded run"]}
    current = candidate_snapshot(project, base)
    reasons = []
    if before.get("project") != current["project"]:
        reasons.append("project changed")
    if before.get("candidate_digest") != current["candidate_digest"]:
        reasons.append("candidate changed")
    if receipt.get("config_digest") != config_digest:
        reasons.append("check configuration changed")
    if receipt.get("base") != base:
        reasons.append("integration base selection changed")
    if reasons:
        return {"status": "stale", "fresh": False, "reasons": reasons,
                "gate_status": receipt.get("gate_status"), "current_snapshot": current}
    if not current["complete"] or current["kind"] != "git":
        return {"status": "unknown", "fresh": False,
                "reasons": ["candidate inventory is limited"],
                "current_snapshot": current}
    return {"status": "current", "fresh": True, "reasons": [],
            "gate_status": receipt.get("gate_status"), "current_snapshot": current}


def run_checks(project: Path, checks: list[dict], output: Path, *,
               base: str | None = None, config_digest: str = "") -> dict:
    """Execute caller-selected checks once and write a non-overwriting JSON receipt."""
    if os.name != "posix":
        raise ValueError("local check process isolation requires macOS/Linux; use the native project runner on this platform")
    project = Path(project).resolve(strict=True)
    if not project.is_dir():
        raise ValueError("project must be a directory")
    before = candidate_snapshot(project, base)
    output = _validate_output(project, output, before["kind"] == "git")
    output.mkdir(parents=True, exist_ok=False, mode=0o700)
    if not isinstance(checks, list):
        checks = []
        config_error = "checks must be a list"
    else:
        config_error = None
    results = []
    seen: set[str] = set()
    for index, item in enumerate(checks):
        try:
            check = _validate_check(project, item, seen)
        except (ValueError, TypeError) as error:
            results.append({"id": item.get("id") if isinstance(item, dict) else None,
                            "result": "blocked", "reason": f"invalid check: {error}",
                            "exit_code": None, "timed_out": False, "observed_counts": None})
            continue
        log = output / f"{index:03d}-{check['id']}.log"
        try:
            old_proof = _safe_proof(project, check["proof_path"])
            old_stamp = old_proof[0] if old_proof is not None else None
            started_ns = time.time_ns()
            exit_code, timed_out, text, truncated = _run_command(
                check["argv"], check["cwd"], check["timeout_seconds"], log)
            record = {"id": check["id"], "argv": check["argv"],
                      "cwd": str(check["cwd"]), "proof_type": check["proof_type"],
                      "log": str(log) if log.exists() else None,
                      "log_truncated": truncated, "exit_code": exit_code,
                      "timed_out": timed_out, "observed_counts": None}
            if exit_code is None:
                record.update(result="blocked", reason="executable not found")
            elif timed_out:
                record.update(result="failed", reason="timeout")
            else:
                try:
                    if check["proof_path"] is not None:
                        _relative_path(project, str(check["proof_path"].relative_to(project)),
                                       directory=False)
                    if truncated and check["proof_type"] in {"unittest", "pytest", "tap"}:
                        raise ValueError("command output truncated before complete test proof")
                    counts = _evaluate_proof(check["proof_type"], text, project,
                                             check["proof_path"],
                                             old_stamp, started_ns)
                    record["observed_counts"] = counts
                    if exit_code != 0 or (counts is not None and
                                          (counts["passed"] <= 0 or counts["failed"] > 0)):
                        record.update(result="failed", reason="command or test proof failed")
                    else:
                        record.update(result="passed", reason=None)
                except (ValueError, OSError, ET.ParseError) as error:
                    record.update(result="failed", reason=f"invalid proof: {error}")
            results.append(record)
        except (OSError, subprocess.SubprocessError) as error:
            results.append({"id": check["id"], "result": "blocked",
                            "reason": f"command could not start or finish: {error}",
                            "exit_code": None, "timed_out": False,
                            "observed_counts": None})
    after = candidate_snapshot(project, base)
    proven_tests = any(r.get("result") == "passed" and r.get("proof_type") in _TEST_PROOFS
                       for r in results)
    stale = before["candidate_digest"] != after["candidate_digest"]
    if stale:
        gate = "stale"
    elif any(r["result"] == "failed" for r in results):
        gate = "failed"
    elif any(r["result"] == "blocked" for r in results):
        gate = "blocked"
    elif config_error or not checks or not before["complete"] or not after["complete"]:
        gate = "incomplete"
    elif before["kind"] != "git":
        gate = "incomplete"
    else:
        gate = "passed"
    receipt = {"schema_version": SCHEMA_VERSION, "gate_status": gate,
               "project": str(project), "base": base, "config_digest": config_digest,
               "snapshot_before": before, "snapshot_after": after,
               "checks": results, "config_error": config_error,
               "test_proof_observed": proven_tests,
               "limitations": ["test counts establish execution, not test quality or product acceptance",
                               "ignored/generated artifacts and submodule interiors need project-specific proof"]}
    receipt_path = output / "receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return receipt
