#!/usr/bin/env bash
set -euo pipefail
for arg in "$@"; do
  case "$arg" in
    --dry-run) ;;
    --help|-h) echo 'Usage: uninstall.sh [--dry-run]'; echo 'Removes only this direct QP installation. Use the original manager for other installations.'; exit 0 ;;
    *) echo "Unknown argument: $arg" >&2; exit 2 ;;
  esac
done
command -v python3 >/dev/null || { echo 'Python 3.10+ is required' >&2; exit 1; }
python3 -c 'import sys; sys.exit(sys.version_info < (3, 10))' || { echo 'Python 3.10+ is required' >&2; exit 1; }
root="${XDG_DATA_HOME:-$HOME/.local/share}/qp-skills"
[[ "$root" = /* ]] || { echo 'XDG_DATA_HOME must be absolute' >&2; exit 2; }
implementation="$root/current/scripts/distribution.py"
if [[ -f "${BASH_SOURCE[0]:-}" ]]; then
  candidate=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/distribution.py
  [[ ! -f "$candidate" ]] || implementation=$candidate
fi
if [[ ! -f "$implementation" ]]; then
  if [[ -f "$root/transaction.json" ]]; then
    echo 'Interrupted removal needs recovery: run uninstall.sh from a QP checkout.' >&2
    exit 1
  fi
  echo 'No active direct QP installation. Native plugins and other managers are unchanged.'
  exit 0
fi
python3 "$implementation" uninstall "$@" </dev/null
