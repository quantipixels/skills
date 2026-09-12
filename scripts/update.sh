#!/usr/bin/env bash
set -euo pipefail

script_dir=
if [[ -f "${BASH_SOURCE[0]:-}" ]]; then
  candidate=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
  [[ ! -f "$candidate/update.py" ]] || script_dir=$candidate
fi

if [[ -n "$script_dir" ]]; then
  exec python3 "$script_dir/update.py" "$@"
fi

command -v git >/dev/null || { echo 'Git is required' >&2; exit 1; }
command -v python3 >/dev/null || { echo 'Python 3 is required' >&2; exit 1; }
tmp=$(mktemp -d)
trap 'rm -rf -- "$tmp"' EXIT
git -C "$tmp" init -q
git -C "$tmp" remote add origin https://github.com/quantipixels/skills.git
git -C "$tmp" fetch -q --depth=1 origin ori </dev/null
git -C "$tmp" checkout -q --detach FETCH_HEAD
exec python3 "$tmp/scripts/update.py" "$@"
