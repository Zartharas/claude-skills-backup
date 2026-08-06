# model-efficiency-router

## When this workflow applies

Use at a task boundary when the user asks to conserve model usage or choose an appropriate reasoning effort for the next phase. Classify task complexity, risk, ambiguity, and verification burden, then recommend a host-available model/effort only when useful. Do not claim to change the active model, raise native intelligence, monitor in the background, or rely on unavailable model names.

## Execution boundary

This package provides analysis, planning, review, templates, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, HSM, SIEM, SOAR, or other external system is connected. Begin read-only. Require explicit authorization, confirmed scope, available tools, and rollback conditions before any live action.

## Purpose

Recommend the least costly Claude configuration that is still appropriate for the **next distinct task**. This is advisory. A skill cannot switch the active model, raise native intelligence, or monitor work in the background — only the user (or the harness, when explicitly instructed) can change model or effort.

## Claude-specific controls to reason about

When judging what to recommend, weigh these against consequence, uncertainty, reversibility, and complexity:

- **Model tier** (pick the cheapest tier that won't need redone work):
  - Haiku 4.5 — quick lookups, mechanical/templated edits, low-risk and low-ambiguity tasks.
  - Sonnet 5 — default for most implementation, debugging, and analysis work.
  - Opus 5 — high-stakes, ambiguous, or architecture-level decisions; multi-step reasoning under uncertainty; anything where a wrong first answer is expensive to unwind.
  - Fable 5 — creative/narrative generation where that model is available and preferred over Opus/Sonnet for tone.
- **`/fast` toggle** — Opus 5 with faster output; suggest it when Opus-level judgment is needed but latency matters more than exhaustive deliberation.
- **Extended thinking / effort** — for tasks with real ambiguity or multi-step tradeoffs (design decisions, root-cause debugging, security review), suggest enabling deeper reasoning (extended thinking, or a higher effort tier where the host exposes one, e.g. this environment's `low/medium/high/xhigh/max` review-effort convention) rather than defaulting straight to a bigger model.
- **Tool/evidence budget** — independent of model choice: how many searches, reads, or subagent calls are proportionate before acting.

Never name a control that isn't actually exposed by the current host. If unsure whether a control exists here, say so instead of asserting it.

## Output

Emit one compact block only when a change is useful:

> **Suggested config:** `<model tier>` [+ `/fast` | + extended thinking/higher effort]
> **Why:** `<one line tying it to complexity/risk/reversibility/ambiguity>`
> **Applies to:** next task only — re-evaluate at the next boundary

If the current configuration already fits the next task, say nothing about routing.

## Completion gate

- Recommendation is based on the next task, not the prestige of the project.
- The named control actually exists or is clearly labeled as a generic category.
- Necessary validation is never removed to save tokens or cost.
- No background monitoring or automatic switching is implied.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Provide validation steps, unresolved issues, residual risk, and the next authorization gate.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

_Source workflow alias: model-efficiency-router. Originally condensed from a Codex/ChatGPT source; adapted 2026-08-05 to reference Claude's actual model tiers and reasoning controls for use in Claude Code._