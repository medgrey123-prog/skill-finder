# Source Evaluation

Use this rubric when comparing skills, plugins, and skill-like repositories.

## Candidate Score

Score out of 100:

- Fit to task: 30
  - 30: directly solves the requested workflow
  - 20: solves most of it with small adaptation
  - 10: adjacent but requires meaningful work
  - 0: mostly unrelated
- Maintenance: 20
  - 20: updated in the last 90 days or clearly active
  - 14: updated in the last year
  - 6: older than one year but still usable
  - 0: archived, broken, or abandoned
- Installability: 15
  - 15: explicit install steps and expected paths
  - 10: installable with minor inference
  - 5: code exists but packaging is unclear
  - 0: no practical install path
- Evidence quality: 15
  - 15: official docs, README, release notes, and independent discussion align
  - 10: README plus observable repository activity
  - 5: only self-claims or social posts
  - 0: no reliable evidence
- Community signal: 10
  - 10: strong usage, stars, forks, citations, or active discussion
  - 5: some visible interest
  - 0: no visible adoption
- Safety and trust: 10
  - 10: clear license, low permission needs, no suspicious install behavior
  - 5: minor unknowns
  - 0: opaque binaries, credential harvesting risk, or unsafe instructions

## Evidence Rules

- Cite repository URLs and documentation URLs directly.
- Do not quote long README passages. Summarize.
- Distinguish facts from inference:
  - Fact: "The repository was updated on 2026-06-20."
  - Inference: "This suggests it is still maintained."
- For GitHub, check at least:
  - README
  - last push or release date
  - archived status
  - license
  - install instructions
  - open issues when the repository is a serious candidate
- For X/Twitter, use it mainly for:
  - recent enthusiasm
  - recurring complaints
  - author announcements
  - examples of real usage

## Recommendation Labels

- Best Pick: highest confidence for this user's task.
- Good Alternative: useful, but with a tradeoff.
- Watchlist: interesting but not ready to rely on.
- Not Recommended: clear reason to avoid.

## When to Build a Custom Skill

Recommend building a custom local skill when:

- available repositories are stale or vague
- the user's workflow depends on local paths, private data, or personal habits
- the best solution is a short repeatable procedure rather than a full external tool
- authentication or paid APIs make third-party skills hard to reuse
