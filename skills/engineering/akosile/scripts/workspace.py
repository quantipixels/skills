#!/usr/bin/env python3
"""Deterministic operations for one repository-local QP workspace."""

try:
    from akosile_workspace.cli import main
except ImportError as error:  # pragma: no cover - dependency gate
    raise SystemExit(
        "Akọsílẹ̀ requires scripts/requirements.txt (PyYAML and filelock)."
    ) from error


if __name__ == "__main__":
    main()
