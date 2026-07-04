#!/usr/bin/env python3
"""Search GitHub for skill-like repositories and rank first-pass candidates."""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import math
import os
import sys
import textwrap
from typing import List, Optional
import urllib.error
import urllib.parse
import urllib.request


API = "https://api.github.com"
UTC = dt.timezone.utc


def request_json(path: str, token: Optional[str]) -> dict:
    req = urllib.request.Request(API + path)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "codex-skill-finder")
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"GitHub API error {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Network error: {exc}") from exc


def parse_time(value: Optional[str]) -> Optional[dt.datetime]:
    if not value:
        return None
    return dt.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC)


def recency_score(updated_at: Optional[str]) -> int:
    updated = parse_time(updated_at)
    if not updated:
        return 0
    age_days = (dt.datetime.now(UTC) - updated).days
    if age_days <= 30:
        return 25
    if age_days <= 90:
        return 22
    if age_days <= 180:
        return 18
    if age_days <= 365:
        return 12
    if age_days <= 730:
        return 6
    return 2


def stars_score(stars: int) -> int:
    if stars <= 0:
        return 0
    return min(25, round(math.log10(stars + 1) / 4 * 25))


def text_fit_score(repo: dict, query: str) -> int:
    haystack = " ".join(
        [
            repo.get("full_name") or "",
            repo.get("description") or "",
            " ".join(repo.get("topics") or []),
        ]
    ).lower()
    terms = [term.lower() for term in query.replace('"', " ").split() if len(term) > 2]
    if not terms:
        return 0
    hits = sum(1 for term in terms if term in haystack)
    return min(20, round(hits / len(terms) * 20))


def metadata_score(repo: dict) -> int:
    score = 0
    if repo.get("license"):
        score += 5
    if repo.get("homepage"):
        score += 3
    if repo.get("topics"):
        score += 4
    if not repo.get("archived"):
        score += 8
    return score


def rank_repo(repo: dict, query: str) -> int:
    if repo.get("archived"):
        archived_penalty = 15
    else:
        archived_penalty = 0
    return max(
        0,
        stars_score(repo.get("stargazers_count", 0))
        + recency_score(repo.get("pushed_at") or repo.get("updated_at"))
        + text_fit_score(repo, query)
        + metadata_score(repo)
        - archived_penalty,
    )


def fetch_readme_summary(full_name: str, token: Optional[str]) -> str:
    try:
        data = request_json(f"/repos/{full_name}/readme", token)
    except SystemExit:
        return ""
    content = data.get("content")
    if not content:
        return ""
    try:
        text = base64.b64decode(content).decode("utf-8", errors="replace")
    except Exception:
        return ""
    compact = " ".join(text.split())
    return textwrap.shorten(compact, width=220, placeholder="...")


def search(query: str, limit: int, token: Optional[str], include_readme: bool) -> List[dict]:
    q = urllib.parse.quote(query)
    per_page = min(max(limit * 2, 10), 50)
    data = request_json(f"/search/repositories?q={q}&sort=stars&order=desc&per_page={per_page}", token)
    repos = []
    for item in data.get("items", []):
        repo = {
            "rank_score": rank_repo(item, query),
            "full_name": item.get("full_name"),
            "url": item.get("html_url"),
            "description": item.get("description") or "",
            "stars": item.get("stargazers_count", 0),
            "forks": item.get("forks_count", 0),
            "open_issues": item.get("open_issues_count", 0),
            "language": item.get("language") or "",
            "pushed_at": item.get("pushed_at"),
            "updated_at": item.get("updated_at"),
            "archived": bool(item.get("archived")),
            "license": (item.get("license") or {}).get("spdx_id") if item.get("license") else "",
            "topics": item.get("topics") or [],
        }
        if include_readme and repo["full_name"]:
            repo["readme_excerpt"] = fetch_readme_summary(repo["full_name"], token)
        repos.append(repo)
    repos.sort(key=lambda repo: repo["rank_score"], reverse=True)
    return repos[:limit]


def print_markdown(repos: List[dict]) -> None:
    print("| Score | Repository | Stars | Updated | Notes |")
    print("|---:|---|---:|---|---|")
    for repo in repos:
        updated = (repo.get("pushed_at") or repo.get("updated_at") or "")[:10]
        flags = []
        if repo.get("archived"):
            flags.append("archived")
        if repo.get("license"):
            flags.append(f"license: {repo['license']}")
        if repo.get("language"):
            flags.append(repo["language"])
        desc = repo.get("description") or "No description"
        notes = "; ".join(flags + [desc])
        print(
            f"| {repo['rank_score']} | [{repo['full_name']}]({repo['url']}) | "
            f"{repo['stars']} | {updated} | {notes} |"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Search GitHub for skill-like repositories.")
    parser.add_argument("query", help="GitHub repository search query")
    parser.add_argument("--limit", type=int, default=10, help="number of candidates to print")
    parser.add_argument("--json", action="store_true", help="print JSON instead of Markdown")
    parser.add_argument("--readme", action="store_true", help="include short README excerpts")
    parser.add_argument("--token-env", default="GITHUB_TOKEN", help="environment variable holding a GitHub token")
    args = parser.parse_args()

    token = os.environ.get(args.token_env)
    repos = search(args.query, args.limit, token, args.readme)
    if args.json:
        print(json.dumps(repos, ensure_ascii=False, indent=2))
    else:
        print_markdown(repos)
    return 0


if __name__ == "__main__":
    sys.exit(main())
