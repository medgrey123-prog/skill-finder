# Skill Finder

Skill Finder is a Codex skill for finding, comparing, and recommending AI agent skills from live sources such as GitHub, web search, and X/Twitter when available.

It is designed to answer requests like:

- "Find me the best Codex skill for publishing projects to GitHub."
- "Compare available Karpathy-inspired skills."
- "Is this GitHub skill maintained and worth installing?"

## Install

### Easiest: Paste This Into Codex

Ask Codex:

```text
Please install this Codex skill from GitHub:
https://github.com/medgrey123-prog/skill-finder

Use the one-line installer:
curl -fsSL https://raw.githubusercontent.com/medgrey123-prog/skill-finder/main/install.sh | bash
```

### Terminal Install

Run:

```bash
curl -fsSL https://raw.githubusercontent.com/medgrey123-prog/skill-finder/main/install.sh | bash
```

The installer is self-contained. It downloads this repository, copies `skill-finder/` into `${CODEX_HOME:-~/.codex}/skills/skill-finder`, and backs up an existing install before replacing it.

Restart Codex after installing so the new skill is picked up.

## Use

In Codex, ask:

```text
Use $skill-finder to find the best skill for publishing a local project to GitHub.
```

The skill will search live sources, inspect candidate repositories, score them, and return a shortlist with evidence and risks.

## Requirements

- macOS or Linux shell for the one-line installer
- `unzip`
- `curl` or `python3`
- Codex skills directory at `${CODEX_HOME:-~/.codex}/skills`

Public GitHub search works without credentials, but GitHub rate limits may apply. Set `GITHUB_TOKEN` only if you need higher GitHub API limits or private repository access. Do not use someone else's token.

## Troubleshooting

- If Codex does not see the skill after install, restart Codex.
- If `unzip` is missing, install it first or ask Codex to install the skill manually from this repository.
- If the installer says it backed up an existing install, that is expected during updates.
- If GitHub blocks download due to network restrictions, open the repository page and ask Codex to copy the `skill-finder/` folder into `~/.codex/skills/skill-finder`.

## Contents

- `skill-finder/SKILL.md`: skill workflow and trigger instructions
- `skill-finder/scripts/github_skill_search.py`: GitHub repository search helper
- `skill-finder/references/source-evaluation.md`: scoring rubric for candidate evaluation
