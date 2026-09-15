#!/usr/bin/env python3
"""Frozen functional oracle. It is copied outside the actor workspace."""

import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import time


workspace = Path(sys.argv[1]).resolve()
case = sys.argv[2]
sys.path.insert(0, str(workspace))
out = []


def check(name, function):
    try:
        function()
        out.append({"check": name, "status": "pass"})
    except AssertionError as error:
        out.append({"check": name, "status": "fail", "detail": f"{type(error).__name__}: {error}"})
    except BaseException as error:
        out.append({"check": name, "status": "error", "detail": f"{type(error).__name__}: {error}"})


def settlement(mode):
    from settlement import Settlement
    from provider import LostReply, Provider

    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        provider = Provider(root / "provider.db")
        service = Settlement(root / "service.db", provider)
        key, amount = "S7", 4913
        if mode == "legacy":
            old = provider.transfer("old-per-attempt-key", amount)
            service.db.execute("INSERT INTO completed VALUES (?,?,?)", (key, amount, old))
            service.db.commit()
            service.close()
            provider.close()
            provider = Provider(root / "provider.db")
            service = Settlement(root / "service.db", provider)
        elif mode in ("retry", "uncertain_mismatch"):
            provider.drop_next_reply = True
            try:
                service.settle(key, amount)
            except LostReply:
                pass
            else:
                raise AssertionError("lost reply not propagated")
            service.close()
            provider.close()
            provider = Provider(root / "provider.db")
            service = Settlement(root / "service.db", provider)
        else:
            service.settle(key, amount)
        if mode.endswith("mismatch"):
            try:
                service.settle(key, amount + 1)
            except ValueError:
                pass
            else:
                raise AssertionError("changed intent accepted")
        else:
            first = service.settle(key, amount)
            assert service.settle(key, amount) == first
            if mode == "legacy":
                assert first == old
        with sqlite3.connect(root / "provider.db") as database:
            rows = database.execute("SELECT cents FROM transfers").fetchall()
            assert rows == [(amount,)], rows
        if mode == "distinct":
            assert service.settle("S8", amount) != first
            with sqlite3.connect(root / "provider.db") as database:
                assert database.execute("SELECT COUNT(*) FROM transfers").fetchone()[0] == 2
        service.close()
        provider.close()


def batching():
    from batching import chunks

    examples = [
        ([], 2, []),
        ([1], 4, [[1]]),
        ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
        ([0, 0, None], 1, [[0], [0], [None]]),
        ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
    ]
    for sequence, size, expected in examples:
        before = sequence.copy()
        assert chunks(sequence, size) == expected
        assert sequence == before
    for size in (0, -1, -20):
        for sequence in ([], [1]):
            try:
                chunks(sequence, size)
            except ValueError:
                pass
            else:
                raise AssertionError("nonpositive size accepted")


def verification():
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        database_path = root / "state.db"
        servers = []

        def stop_server(process):
            if process.poll() is not None:
                return
            process.terminate()
            try:
                process.wait(timeout=0.5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=0.5)

        def start_server(name, environment=None):
            port_file = root / f"{name}.port"
            process = subprocess.Popen(
                [
                    sys.executable,
                    str(workspace / "project_app.py"),
                    "serve",
                    "--db",
                    str(database_path),
                    "--port-file",
                    str(port_file),
                    "--max-requests",
                    "1",
                ],
                cwd=workspace,
                env=environment,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            servers.append(process)
            deadline = time.monotonic() + 3
            while not port_file.is_file():
                if process.poll() is not None:
                    stdout, stderr = process.communicate()
                    raise AssertionError(("server exited before readiness", stdout, stderr))
                if time.monotonic() >= deadline:
                    raise AssertionError("server readiness timeout")
                time.sleep(0.01)
            return process, f"http://127.0.0.1:{port_file.read_text().strip()}"

        def run_driver(operation, url, owned):
            owned.mkdir()
            result = subprocess.run(
                [
                    sys.executable,
                    str(workspace / "verify_project.py"),
                    "--workdir",
                    str(owned),
                    "--url",
                    url,
                    operation,
                ],
                cwd=workspace,
                text=True,
                capture_output=True,
            )
            assert owned.is_dir() and not list(owned.iterdir()), list(owned.iterdir())
            return result

        def require_server_exit(process):
            try:
                process.wait(timeout=1)
            except subprocess.TimeoutExpired as error:
                raise AssertionError("protected service received no public request") from error

        def returned_value(result, operation):
            assert result.returncode == 0, (result.stdout, result.stderr)
            lines = [line for line in result.stdout.splitlines() if line.strip()]
            assert len(lines) == 1, lines
            value = json.loads(lines[0])
            assert value == {
                "status": "passed",
                "operation": operation,
                "value": {"id": "alpha", "text": "persistent"},
            }, value

        try:
            first, url = start_server("first")
            put = run_driver("put", url, root / "put-owned")
            require_server_exit(first)
            returned_value(put, "put")
            with sqlite3.connect(database_path) as database:
                assert database.execute("SELECT id, text FROM items").fetchall() == [
                    ("alpha", "persistent")
                ]
                assert database.execute(
                    "SELECT event, item_id FROM request_log ORDER BY sequence"
                ).fetchall() == [("put", "alpha")]

            second, url = start_server("second")
            get = run_driver("get", url, root / "get-owned")
            require_server_exit(second)
            returned_value(get, "get")
            with sqlite3.connect(database_path) as database:
                assert database.execute(
                    "SELECT event, item_id FROM request_log ORDER BY sequence"
                ).fetchall() == [("put", "alpha"), ("get", "alpha")]

            failed_environment = os.environ.copy()
            failed_environment["QP_FAIL_GET"] = "1"
            failed_server, url = start_server("failed", failed_environment)
            failed = run_driver("get", url, root / "failed-owned")
            require_server_exit(failed_server)
            assert failed.returncode != 0, (failed.stdout, failed.stderr)
            with sqlite3.connect(database_path) as database:
                assert database.execute(
                    "SELECT event, item_id FROM request_log ORDER BY sequence"
                ).fetchall() == [
                    ("put", "alpha"),
                    ("get", "alpha"),
                    ("get_failed", "alpha"),
                ]
        finally:
            for server in servers:
                stop_server(server)


def migration():
    from migration import migrate

    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        path = root / "populated.db"
        with sqlite3.connect(path) as database:
            database.executescript((workspace / "legacy.sql").read_text(encoding="utf-8"))
            expected = database.execute(
                "SELECT p.slug, a.login, m.role "
                "FROM project_members m "
                "JOIN projects p ON p.id = m.project_id "
                "JOIN accounts a ON a.id = m.account_id "
                "ORDER BY p.slug, a.login"
            ).fetchall()
            accounts = database.execute(
                "SELECT id, login, display_name FROM accounts ORDER BY id"
            ).fetchall()
        migrate(path)
        with sqlite3.connect(path) as database:
            assert database.execute("PRAGMA user_version").fetchone()[0] == 2
            columns = [row[1] for row in database.execute("PRAGMA table_info(project_members)")]
            assert columns == ["project_id", "account_login", "role"], columns
            actual = database.execute(
                "SELECT p.slug, m.account_login, m.role "
                "FROM project_members m JOIN projects p ON p.id = m.project_id "
                "ORDER BY p.slug, m.account_login"
            ).fetchall()
            assert actual == expected, (expected, actual)
            assert database.execute(
                "SELECT id, login, display_name FROM accounts ORDER BY id"
            ).fetchall() == accounts
            assert database.execute(
                "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='project_members_legacy'"
            ).fetchone()[0] == 0
            assert database.execute("PRAGMA foreign_key_check").fetchall() == []
        migrate(path)
        with sqlite3.connect(path) as database:
            reopened = database.execute(
                "SELECT p.slug, m.account_login, m.role "
                "FROM project_members m JOIN projects p ON p.id = m.project_id "
                "ORDER BY p.slug, m.account_login"
            ).fetchall()
            assert reopened == expected

        unsupported = root / "unsupported.db"
        with sqlite3.connect(unsupported) as database:
            database.execute("CREATE TABLE marker (value TEXT NOT NULL)")
            database.execute("INSERT INTO marker VALUES ('keep')")
            database.execute("PRAGMA user_version = 3")
        try:
            migrate(unsupported)
        except ValueError:
            pass
        else:
            raise AssertionError("unsupported schema version accepted")
        with sqlite3.connect(unsupported) as database:
            assert database.execute("PRAGMA user_version").fetchone()[0] == 3
            assert database.execute("SELECT value FROM marker").fetchall() == [("keep",)]


def profile():
    capture = json.loads((workspace / "capture.json").read_text(encoding="utf-8"))
    diagnosis = json.loads((workspace / "diagnosis.json").read_text(encoding="utf-8"))
    total = sum(sample["weight"] for sample in capture["samples"])
    frames = {}
    branch_counts = {}
    for sample in capture["samples"]:
        weight = sample["weight"]
        for index, frame in enumerate(sample["stack"]):
            key = (frame["symbol"], frame["file"], frame["line"])
            frames[key] = frame
            if index == 2 and frame["file"].startswith("app/"):
                branch_counts[key] = branch_counts.get(key, 0) + weight
    hottest_application = max(branch_counts, key=branch_counts.get)
    hottest_samples = branch_counts[hottest_application]
    descendants = {}
    for sample in capture["samples"]:
        keys = [
            (frame["symbol"], frame["file"], frame["line"])
            for frame in sample["stack"]
        ]
        if hottest_application in keys:
            start = keys.index(hottest_application) + 1
            for key in keys[start:]:
                descendants[key] = descendants.get(key, 0) + sample["weight"]
    hottest_descendant = max(descendants, key=descendants.get)
    assert diagnosis.get("capture_id") == capture["capture_id"]
    assert diagnosis.get("format") == capture["format"]
    assert diagnosis.get("sample_count") == total
    assert diagnosis.get("capture_conditions") == {
        "candidate": capture["candidate"],
        "command": capture["command"],
        "duration_ms": capture["duration_ms"],
        "interval_ms": capture["interval_ms"],
    }
    reduced = {
        (item.get("symbol"), item.get("file"), item.get("line")): item.get("inclusive_samples")
        for item in diagnosis.get("reduced_path", [])
    }
    assert reduced.get(hottest_application) == hottest_samples, reduced
    assert reduced.get(hottest_descendant) == descendants[hottest_descendant], reduced
    attribution = diagnosis.get("source_attribution")
    assert attribution == {
        **frames[hottest_application],
        "inclusive_samples": hottest_samples,
    }, attribution
    assessment = diagnosis.get("causal_assessment", {})
    assert assessment.get("status") == "DIAGNOSED_BUT_UNPROVED", assessment
    assert assessment.get("confirmed_root_cause") is None, assessment
    assert set(assessment.get("live_hypotheses", [])) == {
        "single_large_snapshot", "repeated_snapshot_parse"
    }, assessment
    probe = diagnosis.get("next_probe", {})
    assert isinstance(probe.get("scope"), str) and probe["scope"].strip(), probe
    assert set(probe.get("metrics", [])) == {"parse_calls", "snapshot_bytes"}, probe
    assert set(probe.get("distinguishes", [])) == {
        "single_large_snapshot", "repeated_snapshot_parse"
    }, probe


if case == "settlement":
    for name in ("retry", "completed_mismatch", "uncertain_mismatch", "distinct", "legacy"):
        check(name, lambda name=name: settlement(name))
elif case == "batching":
    check("partial-empty-identity-order-invalid-nonmutation", batching)
elif case == "verification":
    check("public-cli-http-persistence-and-cleanup", verification)
elif case == "migration":
    check("populated-mapping-idempotence-and-version-rejection", migration)
elif case == "profile":
    check("capture-attribution-and-causal-abstention", profile)
else:
    raise SystemExit(f"unknown case: {case}")
print(json.dumps(out, indent=2))
raise SystemExit(any(item["status"] != "pass" for item in out))
