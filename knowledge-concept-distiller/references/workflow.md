# KCLM Knowledge Distillation Workflow

## Step 1: Corpus Intake

Ask for or inspect:

- Target person or source corpus.
- Available materials: video transcripts, article text, notes, course text, interviews, screenshots, links, folders.
- Desired reuse direction:
  - Concept library.
  - Methodology library.
  - Case-analysis library.
  - Viewpoint and judgment library.
  - Comprehensive reusable Skill.

If the user does not choose, default to comprehensive reusable Skill.

Recommended corpus size:

- 5-10 items: early hypothesis only.
- 30-60 items: stable first version.
- 80+ items: stronger knowledge-system distillation.

## Step 2: Build Knowledge Map

Identify:

- 3-8 theme clusters.
- High-frequency questions under each cluster.
- Relationships between clusters.
- What is central knowledge vs examples, jokes, hooks, or packaging.
- Where the author's knowledge boundaries appear.

Output pattern:

```markdown
## Knowledge Map

| Theme Cluster | Core Questions | Repeated Claims | Evidence | Boundary |
|---|---|---|---|---|
```

## Step 3: Build Concept System

For each concept, extract:

- Concept name.
- Author-style definition.
- Universal translation.
- Applicable scenes.
- Opposite misconception.
- Source evidence.

Do not treat a frequently repeated word as a concept unless it performs explanatory work.

Output pattern:

```markdown
| Concept | Author-Style Definition | Universal Translation | Use Case | Common Misuse | Evidence |
|---|---|---|---|---|---|
```

## Step 4: Restore Logic Chains

Extract how the author reasons, not just what they conclude.

Use this sequence:

```text
Phenomenon -> Problem Definition -> Key Variables -> Causal Mechanism -> Judgment -> Boundary -> Transferable Use
```

Separate:

- Directly stated reasoning.
- Inferred reasoning.
- Unconfirmed gaps.

## Step 5: Build Method Library

Convert reusable knowledge into methods.

Each method must include:

- Method name.
- Problem it solves.
- Required inputs.
- Steps.
- Judgment standard.
- Output.
- Applicable scenes.
- Non-applicable scenes.
- Case evidence.
- Transfer use.

Method output pattern:

```markdown
### Method: [Name]

- Solves:
- Inputs:
- Steps:
- Judgment Standard:
- Output:
- Works When:
- Fails When:
- Evidence:
- Transfer Use:
```

## Step 6: Identify Blind Spots

Always include:

- Evidence-sufficient conclusions.
- Hypotheses needing more corpus.
- Risks of overgeneralization.
- Missing source types.
- Concepts that may be user or model-inferred rather than author-defined.

## Step 7: Confirm Before Final Packaging

Before creating the final Knowledge Skill prompt, ask the user to confirm or correct:

- Knowledge map.
- Concept system.
- Logic-chain reconstruction.
- Method library.
- Scope boundaries.

Then generate the two final artifacts.
