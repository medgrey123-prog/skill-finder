# AGENTS.md

## Project

This repository packages the `skill-finder` Codex skill for sharing through GitHub.

## Rules

- Keep the install path stable: `skill-finder/`.
- Do not commit API keys, browser session data, local caches, or personal search results.
- Validate the skill before publishing changes:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill-finder
python3 -m py_compile skill-finder/scripts/github_skill_search.py
```

## Install Command

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo medgrey123-prog/skill-finder --path skill-finder
```
