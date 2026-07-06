# AGENTS.md

## Project

This repository packages Codex skills for sharing through GitHub.

Current skills:

- `skill-finder`
- `knowledge-concept-distiller`

## Rules

- Keep install paths stable: `skill-finder/` and `knowledge-concept-distiller/`.
- Do not commit API keys, browser session data, local caches, or personal search results.
- Validate the skill before publishing changes:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill-finder
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge-concept-distiller
python3 -m py_compile skill-finder/scripts/github_skill_search.py
```

## Install Command

```bash
curl -fsSL https://raw.githubusercontent.com/medgrey123-prog/skill-finder/main/install.sh | bash
```

The root `install.sh` must stay self-contained and must not depend on Codex's system skill installer being present.
