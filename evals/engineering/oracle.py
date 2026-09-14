#!/usr/bin/env python3
"""Frozen functional oracle. It is copied outside the actor workspace."""

import json
from pathlib import Path
import sqlite3
import sys
import tempfile


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


if case == "settlement":
    for name in ("retry", "completed_mismatch", "uncertain_mismatch", "distinct", "legacy"):
        check(name, lambda name=name: settlement(name))
elif case == "batching":
    check("partial-empty-identity-order-invalid-nonmutation", batching)
else:
    raise SystemExit(f"unknown case: {case}")
print(json.dumps(out, indent=2))
raise SystemExit(any(item["status"] != "pass" for item in out))
