#!/usr/bin/env bash
# Native Git fetches a snapshot; Python owns only QP's files and host links.
set -euo pipefail
ref=ori
source_dir=
ref_set=false
args=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --ref|--source)
      [[ $# -ge 2 && -n "$2" && "$2" != -* ]] || { echo "$1 requires a value" >&2; exit 2; }
      if [[ "$1" == --ref ]]; then ref=$2; ref_set=true; else source_dir=$2; fi
      shift ;;
    --codex|--claude|--dry-run) args+=("$1") ;;
    --help|-h)
      echo 'Usage: install.sh [--source CHECKOUT | --ref REF] [--codex] [--claude] [--dry-run]'
      echo 'Requires Git and Python 3.10+ on macOS/Linux. Default: local checkout, or ori when piped.'
      echo 'Installs a QP-owned snapshot and verified host links, not hooks or startup defaults.'
      echo 'Updates retain selected hosts and remove only retired links owned by this installation.'
      exit 0 ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done
command -v python3 >/dev/null || { echo 'Python 3.10+ is required' >&2; exit 1; }
python3 -c 'import sys; sys.exit(sys.version_info < (3, 10))' || { echo 'Python 3.10+ is required' >&2; exit 1; }
command -v git >/dev/null || { echo 'Git is required' >&2; exit 1; }
if $ref_set && [[ -n "$source_dir" ]]; then echo 'Choose --source or --ref, not both' >&2; exit 2; fi
# A downloaded/piped script has no sibling implementation; fetch one exact snapshot.
if [[ -z "$source_dir" ]] && ! $ref_set && [[ -f "${BASH_SOURCE[0]:-}" ]]; then
  candidate=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
  [[ ! -f "$candidate/scripts/distribution.py" ]] || source_dir=$candidate
fi
if [[ -z "$source_dir" ]]; then
  git check-ref-format "refs/heads/$ref" >/dev/null || { echo 'Invalid Git ref' >&2; exit 2; }
  source_dir=$(mktemp -d)
  trap 'rm -rf -- "$source_dir"' EXIT
  git -C "$source_dir" init -q
  git -C "$source_dir" remote add origin https://github.com/quantipixels/skills.git
  git -C "$source_dir" fetch -q --depth=1 origin "$ref" </dev/null
  git -C "$source_dir" checkout -q --detach FETCH_HEAD
fi
python3 "$source_dir/scripts/distribution.py" install --source "$source_dir" "${args[@]}" </dev/null
