---
name: reporting-narrative-suite
description: "Use to turn project history, architecture, a design artifact, or a document into a human-facing narrative output: a full timeline report, week-by-week digests, a slide deck, a plain-English explainer, a Dieter Rams design audit, or a unified-architecture flowchart. Route by which output format and source material the user wants."
---

# Reporting & Narrative Suite

## Purpose

Six original skills whose job is producing a readable artifact for a human, not editing code. Grouped because they share a shape: read some source of truth (claude-mem timeline, a codebase, a document, a UI), then generate a report/deck/explainer/diagram — several of them (`design-is`, `pathfinder`) end by handing off a `/make-plan` prompt rather than doing the plan themselves.

## Source aliases

Recognize these original skill names as explicit aliases: `timeline-report`, `weekly-digests`, `wowerpoint`, `what-the`, `design-is`, `pathfinder`.

| Original alias | Read | Use when |
|---|---|---|
| `timeline-report` | `timeline-report/SKILL.md` | Want one comprehensive "Journey Into [Project]" narrative covering the whole claude-mem history in a single report. |
| `weekly-digests` | `weekly-digests/SKILL.md` | Want the same history as `timeline-report` but split into one chapter per ISO week, with carry-forward continuity between chapters. Chapter count is driven by the number of weeks in the data, not fixed. |
| `wowerpoint` | `wowerpoint/SKILL.md` | Want one existing document turned into a slide-deck PDF. Slide decks only — refer the user to the `notebooklm` CLI directly for video/podcast output. |
| `what-the` | `what-the/SKILL.md` | Want a plain-English who/what/where/why/when breakdown of something technical, with no report artifact needed. |
| `design-is` | `design-is/SKILL.md` | Want a UI/design artifact audited against Dieter Rams' ten principles, ending in a `/make-plan` handoff for new-design/refine/redesign. Not for routine code review or copy edits. |
| `pathfinder` | `pathfinder/SKILL.md` | Want the codebase mapped into feature-grouped flowcharts with duplication identified and a proposed unified architecture, ending in per-system `/make-plan` handoff prompts. Does not write implementation code itself. |

Read only the skill that matches the current request — each is self-contained.

## Routing precedence

1. Full single-document history narrative → `timeline-report`.
2. Same history but chaptered week-by-week → `weekly-digests`.
3. One document → slide deck → `wowerpoint`.
4. Quick plain-English explanation, no artifact → `what-the`.
5. Critiquing a design/UI against Rams' principles → `design-is`.
6. Mapping/unifying codebase architecture → `pathfinder`.

`design-is` and `pathfinder` both terminate in a `/make-plan` handoff — that handoff belongs to `planning-execution-suite`; do not attempt to execute the resulting plan from within this suite.

## Non-goals

- Actually implementing any plan these skills hand off — see `planning-execution-suite`.
- Searching or querying claude-mem memory directly (as opposed to narrating it) — see `memory-core-suite`.

## Completion gate

Before finishing, confirm the output format matches what was asked (single report vs. weekly chapters vs. deck vs. explainer vs. audit vs. flowchart), and that any `/make-plan` handoff prompt is complete enough to hand off without the next session re-deriving context.
