#!/usr/bin/env python3
"""Build, install and verify this checkout in the current Codex home."""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

from verify_native_install import (
    ROOT, SELECTOR, NativeVerificationError, compare_installed_files,
    load_json, run, stage_package,
)


def main() -> int:
    env = os.environ.copy()
    try:
        if not shutil.which("codex"):
            raise NativeVerificationError("codex executable is unavailable")
        for arguments in ([], ["--check"]):
            run([sys.executable, str(ROOT / "scripts/plugins/build_alarina_bundle.py"),
                 *arguments], env)
        run([sys.executable, str(ROOT / "scripts/skills/check_package.py")], env)
        # Keep the clean source available for native manager records and diagnosis.
        packages = Path.home() / ".qp/alarina/packages"
        packages.mkdir(parents=True, exist_ok=True)
        package = Path(tempfile.mkdtemp(prefix="local-", dir=packages))
        stage_package(package)
        installed = load_json(run([
            "codex", "-c", 'marketplaces.qp-skills.source_type="local"',
            "-c", f"marketplaces.qp-skills.source={json.dumps(str(package))}",
            "plugin", "add", SELECTOR, "--json",
        ], env), "Codex plugin add")
        location = installed.get("installedPath") or installed.get("installPath")
        if installed.get("pluginId") != SELECTOR or not isinstance(location, str):
            raise NativeVerificationError(f"unexpected Codex install result: {installed}")
        count = compare_installed_files(Path(location), package)
        print(f"Installed {SELECTOR}; verified {count} runtime files.\n"
              f"Installed path: {location}\nClean source: {package}\n"
              "Restart Codex to load the updated instructions.")
        return 0
    except (OSError, ValueError) as error:
        print(f"Local installation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
