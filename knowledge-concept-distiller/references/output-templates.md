# Output Templates

## Knowledge Identification Report

Use before user confirmation.

```markdown
# Knowledge Identification Report

## 0. Corpus Status
- Source:
- Number of items:
- Text extraction status:
- Known quality issues:

## 1. Knowledge Map
| Theme Cluster | High-Frequency Questions | Role in System | Evidence | Boundary |
|---|---|---|---|---|

## 2. Core Concept Table
| Concept | Author-Style Definition | Universal Translation | Use Case | Misuse / Anti-Concept | Evidence |
|---|---|---|---|---|---|

## 3. Core Viewpoint Table
| Viewpoint | Hidden Assumption | Reasoning Logic | Boundary | Evidence |
|---|---|---|---|---|

## 4. Logic Chains
### Chain 1: [Name]
Phenomenon -> Problem Definition -> Key Variables -> Causal Mechanism -> Judgment -> Boundary -> Transferable Use

## 5. Method List
| Method | Solves | Inputs | Steps | Output | Does Not Work When |
|---|---|---|---|---|---|

## 6. Evidence Strength
- Strongly supported:
- Medium confidence:
- Weak or needs more data:

## 7. Confirmation Questions
1. Should this knowledge system focus more on concepts, methods, cases, viewpoints, or comprehensive reuse?
2. Which concepts or judgments feel wrong or over-inferred?
3. Which use cases should the final Skill prioritize?
```

## Static Knowledge Asset Report

Use after user confirmation.

```markdown
# [Target Person] Knowledge Concept Distillation Report

## 1. One-Sentence Knowledge Positioning
[What problem does this person's knowledge system fundamentally solve?]

## 2. Knowledge Map
- Theme clusters.
- Topic relationships.
- Scope boundaries.

## 3. Core Concept Library
For each concept:
- Name:
- Definition:
- Universal translation:
- Use scenes:
- Opposite misconception:
- Evidence:

## 4. Core Viewpoint Library
For each viewpoint:
- Judgment:
- Assumption:
- Reasoning:
- Boundary:
- Evidence:

## 5. Logic Chain Library
For each chain:
- Phenomenon:
- Problem definition:
- Variables:
- Mechanism:
- Conclusion:
- Transfer scene:

## 6. Method Library
For each method:
- Solves:
- Inputs:
- Steps:
- Standard:
- Output:
- Non-use cases:
- Evidence:

## 7. Case Analysis Template
- What the author observes first:
- What variables they isolate:
- What theory/concept they invoke:
- How they evaluate success/failure:
- How they derive a transferable lesson:

## 8. Misuse and Boundary Rules
- Do not use when:
- Needs additional data when:
- High-risk extrapolations:
```

## Validation Output

Use after creating the final Skill prompt and receiving a test problem.

```markdown
# Validation: Applying the Distilled Knowledge System

## One-Sentence Judgment

## Problem Definition

## Concepts Called
- Concept:
- Why relevant:

## Logic Chain Used
Phenomenon -> Problem Definition -> Variables -> Mechanism -> Judgment -> Boundary

## Method Applied
- Method:
- Inputs:
- Steps:
- Output:

## Recommendation

## Boundary and Uncertainty
- Based on source:
- Migrated inference:
- Need more data:
```
