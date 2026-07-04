---
name: skill-finder
description: Find, compare, and recommend Codex/AI agent skills, plugins, reusable workflows, or installable GitHub repositories using live GitHub, X/Twitter, and web research. Use when the user asks for the best skill for a task, wants objective recommendations, wants to discover installable skills from GitHub or social discussions, or asks whether a skill/plugin/workflow is credible, maintained, popular, or worth installing.
---

# Skill Finder

## Goal

Recommend a small set of credible skills or skill-like repositories for the user's task using current evidence. Prefer fewer, better recommendations over broad lists.

Always treat popularity claims, latest versions, repository status, and social sentiment as time-sensitive. Verify them live before making a recommendation.

## Source Order

1. Use official or structured sources first:
   - GitHub app/connector if available.
   - `gh` CLI if already authenticated.
   - Public GitHub REST API, using `scripts/github_skill_search.py` when a repository search is needed.
2. Use web search for broader discovery, including GitHub, docs, blogs, and package pages.
3. Use X/Twitter only when available through one of these paths:
   - X API credentials supplied by the user or present in the environment.
   - A browser session where the user is already logged in and explicitly asks to use it.
   - Public web-search snippets as a weaker signal.

Do not ask for passwords. If a login is required, open the relevant site and let the user enter credentials directly. Do not store secrets in the skill or repository.

## Workflow

1. Restate the user's need as a search brief:
   - task the skill should perform
   - target runtime, if known (Codex, Claude Code, OpenAI Apps SDK, MCP, etc.)
   - must-have constraints such as local-only, free, GitHub-installable, Chinese docs, or no API key
2. Generate 3-6 search queries:
   - exact task terms
   - synonyms
   - framework/tool names
   - `"skill"`, `"agent"`, `"mcp"`, `"plugin"`, `"codex"`, `"claude"` when relevant
3. Search GitHub:
   - Run `scripts/github_skill_search.py "<query>" --limit 10` for candidate discovery when appropriate.
   - Inspect the top candidates manually before recommending.
   - Check README, install instructions, last update, license, issues, and whether the repository actually contains a reusable skill.
4. Search the web and social sources:
   - Look for independent usage examples, docs, changelogs, discussions, and recent complaints.
   - Use X/Twitter as trend or sentiment evidence, not as the sole source of truth.
5. Score candidates using `references/source-evaluation.md`.
6. Recommend 3-5 options. If no candidate is good enough, say so and propose building a custom skill.

## GitHub Helper

Use the bundled helper for quick candidate discovery:

```bash
python3 /Users/megrey/.codex/skills/skill-finder/scripts/github_skill_search.py "codex skill github publisher" --limit 10
```

Optional environment variables:

- `GITHUB_TOKEN`: raises GitHub API rate limits and can access private repositories if the token has permission.

The helper is a first pass only. Do not recommend a repository solely because the helper ranks it highly.

## Output Format

Use this structure by default:

```markdown
**Best Pick**
[name](url) - one sentence reason.

**Shortlist**
| Rank | Candidate | Why it fits | Evidence | Risk |
|---|---|---|---|---|

**Not Recommended**
- [name](url): concise reason, if relevant.

**Next Step**
Recommended install/test action.
```

Include source links for every recommended candidate. Mention when X/Twitter was not available or was only used through web-search snippets.

## Decision Rules

- Prefer maintained repositories over abandoned high-star repositories.
- Prefer clear install instructions over vague demos.
- Prefer skills with narrow, repeatable workflows over broad prompt dumps.
- Penalize repos with no license, no README, archived status, stale commits, or many unresolved breakage reports.
- Treat stars as a weak signal. Use them to find candidates, not to decide alone.
- If the user's task is highly specific and available options are weak, recommend creating a custom local skill instead of forcing a third-party recommendation.
