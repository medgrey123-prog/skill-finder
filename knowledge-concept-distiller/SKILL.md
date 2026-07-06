---
name: knowledge-concept-distiller
description: >-
  Use when Codex should distill a creator, expert, blogger, course, interview,
  article corpus, or video transcript corpus into a reusable knowledge-concept
  Skill rather than copying writing style. Extract the person's knowledge map,
  concepts, definitions, viewpoints, logic chains, methods, case-analysis
  patterns, boundaries, and a reusable AI prompt for applying that knowledge to
  new problems.
---

# Knowledge Concept Distiller

## Overview

Use this skill to create a reusable knowledge-system Skill from someone else's corpus. The goal is not style imitation. The goal is to recover what the person knows, how they define concepts, how they reason, and how their methods can be reused on new problems.

## Core Principle

Do not ask only “How does this person write?” Ask:

1. What problems does this person repeatedly solve?
2. What concepts does this person use to define those problems?
3. What beliefs and judgments appear repeatedly?
4. What logic chains connect phenomenon, mechanism, and conclusion?
5. What methods can be reused in a new context?
6. Where are the boundaries and misuse risks?

## Workflow Decision

- For a full distillation workflow, read `references/workflow.md`.
- For required report structures, read `references/output-templates.md`.
- For generating the final reusable Skill prompt, read `references/skill-prompt-template.md`.

If the user provides raw files, transcripts, screenshots, folders, or links, first build the corpus inventory and extract text if needed. Preserve raw transcripts or source notes separately from the distilled outputs.

## KCLM Framework

Always use this order:

1. **K | Knowledge Map**: Identify theme clusters, high-frequency questions, knowledge boundaries, and topic relationships.
2. **C | Concept System**: Extract concepts, author-style definitions, universal translations, use cases, errors, and evidence.
3. **L | Logic Chains**: Restore reasoning from phenomenon to problem definition, variables, causal mechanism, conclusion, and boundary.
4. **M | Method Library**: Convert knowledge into reusable methods with inputs, steps, standards, outputs, and non-use cases.

Do not generate the final Skill prompt before the user confirms the identification report.

## Required Outputs

### Before User Confirmation

Output a **Knowledge Identification Report** containing:

- Knowledge map.
- Core concept table.
- Core viewpoint table.
- Typical logic chains.
- Method list.
- Evidence and blind spots.

Wait for user confirmation or correction.

### After User Confirmation

Output two artifacts:

1. **For You | Static Knowledge Asset Report**
   - A complete Markdown report that the user can read and inspect.
2. **For AI | Callable Knowledge Skill Prompt**
   - A prompt template that lets another AI apply the distilled knowledge system to new problems.

Then produce a validation output on a new example if the user provides one.

## Evidence Rules

- Attach source evidence for every important concept, viewpoint, logic chain, and method.
- Distinguish direct source claims from inferred patterns.
- Mark insufficient data instead of forcing a clean model.
- Keep the author's original case conclusions separate from migrated judgments.

## Anti-Goals

- Do not imitate exact wording, catchphrases, or sentence rhythm unless explicitly requested.
- Do not make a “style copy” skill.
- Do not summarize only at the level of themes and opinions.
- Do not extract quotes without reconstructing definitions, logic, methods, and boundaries.
- Do not claim the author said something if it is only your extrapolation.

## Default Language

Use Chinese by default. Keep explanations structured, concrete, and evidence-grounded.
