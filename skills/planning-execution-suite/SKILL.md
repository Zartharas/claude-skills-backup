---
name: planning-execution-suite
description: "Use for the plan-then-build loop on a codebase: priming full understanding of an unfamiliar repo, fast structural search instead of brute-force reading, authoring a phased implementation plan, or executing an existing plan with subagents. Route by which stage of that loop the user is in."
---

# Planning & Execution Suite

## Purpose

Covers the four original skills that make up the standard build loop: get oriented (`learn-codebase` or `smart-explore`), write the plan (`make-plan`), then run it (`do`).

## Source aliases

Recognize these original skill names as explicit aliases: `make-plan`, `do`, `learn-codebase`, `smart-explore`.

| Original alias | Read | Use when |
|---|---|---|
| `learn-codebase` | `workflows/learn-codebase.md` | Starting cold on a new/unfamiliar project and need deep, full-file understanding before doing anything else. Reads every source file — expensive, use deliberately. |
| `smart-explore` | `workflows/smart-explore.md` | Need a structural map of code (functions, symbols, call sites) without full-file reads. Overrides default Read/Grep/Glob behavior in favor of `smart_search`/`smart_outline`/`smart_unfold` while active. |
| `make-plan` | `workflows/make-plan.md` | Asked to plan a feature or multi-step implementation. Produces a phased, LLM-friendly plan; orchestrator delegates fact-gathering to subagents but keeps synthesis itself. |
| `do` | `workflows/do.md` | Asked to execute, run, or carry out a plan — especially one `make-plan` produced. Orchestrator deploys subagents for all actual work. |

Read only the workflow that matches the current request. Do not load every workflow in the family.

## Routing precedence

1. Unfamiliar repo, no plan yet, need full understanding → `learn-codebase`.
2. Need to locate/understand specific code without reading everything → `smart-explore`.
3. Have enough understanding, need a plan → `make-plan`.
4. Already have a plan (from `make-plan` or supplied by the user) → `do`.

`smart-explore` and `learn-codebase` are not mutually exclusive with the other two — `make-plan` and `do` will often invoke `smart-explore`-style structural search internally rather than reading full files, unless `learn-codebase` was explicitly requested first.

## Non-goals

- PR/issue/release process work — see `repo-governance-suite`.
- Producing human-readable narrative reports — see `reporting-narrative-suite`.

## Completion gate

Before finishing, confirm the plan or execution stayed inside its declared scope, subagents (for `make-plan`/`do`) actually did the delegated work rather than the orchestrator doing it inline, and any plan produced is ready to hand to `do` without further clarification.
