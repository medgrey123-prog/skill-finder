#!/usr/bin/env bash
set -euo pipefail

REPO_ZIP_URL="https://codeload.github.com/medgrey123-prog/skill-finder/zip/refs/heads/main"
SKILL_NAME="skill-finder"
CODEX_DIR="${CODEX_HOME:-$HOME/.codex}"
DEST_ROOT="$CODEX_DIR/skills"
DEST="$DEST_ROOT/$SKILL_NAME"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

need_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1" >&2
    exit 1
  fi
}

download_zip() {
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL "$REPO_ZIP_URL" -o "$TMP_DIR/repo.zip"
    return
  fi

  if command -v python3 >/dev/null 2>&1; then
    python3 - "$REPO_ZIP_URL" "$TMP_DIR/repo.zip" <<'PY'
import sys
import urllib.request

url, out = sys.argv[1], sys.argv[2]
req = urllib.request.Request(url, headers={"User-Agent": "skill-finder-installer"})
with urllib.request.urlopen(req, timeout=30) as response:
    data = response.read()
with open(out, "wb") as handle:
    handle.write(data)
PY
    return
  fi

  echo "Need either curl or python3 to download the skill." >&2
  exit 1
}

need_cmd unzip

echo "Installing $SKILL_NAME into $DEST"
download_zip
unzip -q "$TMP_DIR/repo.zip" -d "$TMP_DIR"

SRC="$TMP_DIR/skill-finder-main/skill-finder"
if [ ! -f "$SRC/SKILL.md" ]; then
  echo "Downloaded archive did not contain skill-finder/SKILL.md" >&2
  exit 1
fi

mkdir -p "$DEST_ROOT"

if [ -d "$DEST" ]; then
  if command -v diff >/dev/null 2>&1 && diff -qr "$SRC" "$DEST" >/dev/null 2>&1; then
    echo "$SKILL_NAME is already up to date at $DEST"
    echo "Restart Codex if the skill is not visible yet."
    exit 0
  fi

  BACKUP="${DEST}.backup-$(date +%Y%m%d-%H%M%S)"
  mv "$DEST" "$BACKUP"
  echo "Existing install moved to $BACKUP"
fi

cp -R "$SRC" "$DEST"
if [ -d "$DEST/scripts" ]; then
  chmod +x "$DEST/scripts"/*.py 2>/dev/null || true
fi

echo "Installed $SKILL_NAME successfully."
echo "Restart Codex to pick up the new skill."
