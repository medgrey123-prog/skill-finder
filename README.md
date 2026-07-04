# Skill Finder

Skill Finder is a Codex skill for finding, comparing, and recommending AI agent skills from live sources such as GitHub, web search, and X/Twitter when available.

It is designed to answer requests like:

- "Find me the best Codex skill for publishing projects to GitHub."
- "Compare available Karpathy-inspired skills."
- "Is this GitHub skill maintained and worth installing?"

## Install

Use Codex's built-in skill installer:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo medgrey123-prog/skill-finder --path skill-finder
```

Or use the one-line installer:

```bash
curl -fsSL https://raw.githubusercontent.com/medgrey123-prog/skill-finder/main/install.sh | bash
```

Restart Codex after installing so the new skill is picked up.

## Use

In Codex, ask:

```text
Use $skill-finder to find the best skill for publishing a local project to GitHub.
```

The skill will search live sources, inspect candidate repositories, score them, and return a shortlist with evidence and risks.

## Contents

- `skill-finder/SKILL.md`: skill workflow and trigger instructions
- `skill-finder/scripts/github_skill_search.py`: GitHub repository search helper
- `skill-finder/references/source-evaluation.md`: scoring rubric for candidate evaluation

## Notes

- Public GitHub search works without credentials, but GitHub rate limits may apply.
- Set `GITHUB_TOKEN` if you need higher GitHub API limits or private repository access.
- X/Twitter evidence is optional and depends on available API credentials, browser login, or public web snippets.
