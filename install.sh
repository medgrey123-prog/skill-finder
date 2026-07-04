#!/usr/bin/env bash
set -euo pipefail

INSTALLER="${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py"

if [ ! -f "$INSTALLER" ]; then
  echo "Codex skill installer not found at: $INSTALLER" >&2
  echo "Install from inside Codex, or make sure Codex's system skills are available." >&2
  exit 1
fi

python3 "$INSTALLER" --repo medgrey123-prog/skill-finder --path skill-finder
echo "Installed skill-finder. Restart Codex to pick up the new skill."
