# model-efficiency-router

## When this workflow applies

Use at a task boundary when the user asks to conserve token usage, choose an appropriate reasoning depth, or wants more work done within a given quota. Classify task complexity, risk, ambiguity, and verification burden, then recommend a configuration only when it would actually change something. Do not claim to change the active model, raise native intelligence, monitor in the background, or invoke a control that isn't real on the current host.

## Execution boundary

This package provides analysis, recommendations, and verification guidance. It does not imply that a scanner, cloud account, repository, endpoint, or other external system is connected. It cannot switch models, set API parameters, or change host settings — those require the user or the calling harness to act.

## Purpose

Recommend the configuration that gets the **next distinct task** done correctly using the fewest tokens — where "configuration" covers both *which model/reasoning depth to use* and *how to structure the work itself* to avoid spending tokens that don't improve the outcome. Model choice is one lever, not the only one; the second half of this workflow is often the larger saving.

## Two levers, not one

**Lever A — model tier and reasoning depth.** Getting a hard task right the first time on a stronger model is usually cheaper than a wrong answer on a cheaper one that needs redoing. This is the lever the original version of this skill focused on exclusively.

**Lever B — how the work is structured**, independent of model choice: avoiding redundant tool calls, retrieving only what's needed instead of bulk context dumps, caching repeated context instead of re-sending it, and not asking for more output than the task needs. For most real workloads, Lever B saves more tokens than Lever A, because it applies on every single call rather than once per task boundary. Route on both.

## Lever A — model tier and reasoning depth

### Model tier — optimize for lowest sufficient capability

The governing principle: use the **least capable (cheapest) tier that can correctly complete the task without needing to be redone.** Not "which tier sounds about right for this kind of task" — the actual question is what capability level this specific task's ambiguity, stakes, and reasoning depth genuinely require, then stopping there. Overshooting wastes tokens on capability the task didn't need; undershooting wastes more once a wrong or incomplete answer has to be redone on a stronger tier anyway, plus the cost of the first attempt.

Judge the requirement from the task, not from a fixed name-to-tier mapping:

- **Low capability need** — quick lookups, mechanical/templated edits, high-volume repetitive sub-tasks, low-risk and low-ambiguity work where a wrong answer is cheap and obvious to catch.
- **Moderate capability need** — most implementation, debugging, and analysis work with a reasonably clear specification.
- **High capability need** — architecture-level decisions, genuine ambiguity requiring judgment calls, multi-step reasoning under uncertainty, anything where a wrong first answer is expensive or slow to unwind.
- **Specialized need** — narrative/tone-sensitive generation or another distinct capability a host may offer separately from its general-reasoning line, when the task specifically calls for that, not general reasoning depth.

**Do not name a specific current model as a fixed label for one of these bands anywhere — not even as an illustrative example.** Which model currently occupies "cheapest" or "most capable" changes over time (this skill has already gotten a specific name wrong once by asserting it from memory), and pairing a tier with a specific name repeatedly is itself a soft form of hardcoding even when hedged as an example. At the point of actually choosing, check the host's current lineup and current documentation, and pick by matching the task's actual capability need to what's available now — not by recalling which name this document associated with which band.

### Extended thinking and effort — current mechanics, verified

Two related but distinct controls exist, and the underlying mechanism has been changing — verify current per-model support before assuming either is available:

- **Effort** (low/medium/high/xhigh/max) — the primary current control on models that support it. Higher effort means Claude thinks on more requests and at greater length; lower effort skips thinking for simpler problems. This is the control Claude Code exposes directly to the person using it. Current docs recommend starting from `xhigh` for long-running coding/agentic work.
- **Extended thinking with a manual token budget** (`budget_tokens`) — the older mechanism, being phased out: it's deprecated on some current-generation models and rejected outright on newer ones, which use adaptive thinking (Claude decides whether and how much to think) governed by the effort parameter instead. Don't assume manual budget-token tuning is available going forward; check per-model docs.
- Effort support itself is **model-specific, not universal** — don't assume a model supports it without checking.

**The cost fact that matters most here, and that the original version of this skill missed entirely: thinking tokens are billed as output tokens even though only a summary is shown.** A response that displays a short reasoning digest may have billed for several times that in actual thinking tokens underneath. Higher effort is not a free quality dial — it's a real, sometimes large, token cost, separate from and additional to the visible response.

A second concrete failure mode worth avoiding: **too-high effort increases the chance of hitting the `max_tokens` ceiling** before Claude finishes, producing a truncated, wasted response that then needs a retry — the opposite of saving tokens. For straightforward tasks, lower effort isn't just cheaper, it's also less likely to fail this way.

**No verified `/fast` toggle exists.** A prior revision of this skill asserted one without checking; it could not be confirmed against current documentation and has been removed. If a host genuinely exposes a similarly-named control, verify it directly against that host's own docs before recommending it — don't carry this specific name forward from memory.

## Lever B — structural token-saving practices

These apply regardless of which model is in use, and compound across every call in a session:

- **Don't re-fetch what's already in context.** If a search, a file read, or a tool result already happened this session, reuse it rather than calling again for the same information.
- **Retrieve narrowly.** Read the specific file, section, or page the task needs rather than pulling in a whole document or repository when only part of it is relevant. This cuts both the tokens spent reading and the tokens spent re-processing that content on every subsequent turn of the conversation.
- **Prompt caching, for API/scripted workflows.** Content that repeats across calls unchanged — a long system prompt, a large reference document, a stable set of tool definitions — can be cached so it isn't re-billed at full price on every request. Relevant when building automation or long scripted sessions (Claude Code, direct API use); not something to reason about for a single interactive chat. Note that changes to thinking configuration can invalidate cache breakpoints — a cost interaction worth knowing about if combining caching with effort/thinking tuning.
- **Batch processing for bulk, non-urgent work.** For large volumes of independent, non-interactive tasks (classify N items, summarize N documents), a batch-style workflow processed asynchronously is usually both cheaper and the correct tool — distinct from an interactive conversation, and worth naming as an option when the task shape is "many similar small jobs" rather than one conversation.
- **Match output length to the task.** Requesting exhaustive detail by default when a short, direct answer would fully satisfy the request wastes output tokens on every single call — this is the same discipline `ponytail` applies to code, extended to response length itself.
- **Manage conversation length.** A long-running conversation re-processes its accumulated history on every turn. When a task is genuinely finished and an unrelated new one is starting, a fresh session avoids continuing to pay for context that's no longer relevant to the work at hand.

## Output

Emit a compact recommendation block only at a real task boundary or when directly asked — not on every message, which would itself be the overhead this workflow exists to avoid:

> **Next step:** `<what's coming>`
> **Recommendation:** `<model tier and/or effort level, and/or a structural practice from Lever B>`
> **Why:** `<the specific signal — ambiguity, blast radius, redundant-call risk, output-length mismatch — not a generic restatement>`
> **Switch back when:** `<the condition that ends this recommendation's relevance>`

If the current configuration and approach already fit the next task, say nothing about routing — a silent pass is the correct output more often than a recommendation is.

## Completion gate

- Recommendation is based on the next task's actual demands, not general caution or the perceived importance of the project.
- Any named model, control, or parameter either exists and was verified against current documentation, or is clearly described as a generic category rather than asserted as a specific current name.
- Both levers were considered — a Lever-B structural fix was not skipped in favor of jumping straight to a model-tier answer when the cheaper fix was structural.
- Necessary reasoning depth or verification was never cut just to save tokens on work where a wrong answer costs more to redo than the tokens saved.
- No background monitoring or automatic switching is implied — this workflow recommends; only the user or host actually changes configuration.

## Required output discipline

- Separate observed evidence, source-supported facts, inference, assumptions, and recommendations.
- State tool and data limitations explicitly.
- Preserve exact technical literals, measurements, citations, and user-approved constraints.
- Never claim execution, access, containment, compliance, certification, or verification that was not observed.

## Overlap with `model-tier-advisor`

If a separate `model-tier-advisor` skill is also installed on this account: it covers substantially the same ground as Lever A above (checkpoint-triggered model-tier recommendations, the same compact output-block format). That overlap was created when `model-tier-advisor` was built without checking whether this skill already existed. Recommendation: keep this skill as the single source for model/effort/token-efficiency routing, and remove `model-tier-advisor` to avoid two skills competing for the same trigger — same reasoning already applied elsewhere in this account's skill set (e.g. `caveman` and `anti-ai-tells` were kept separate because they govern different axes; this and `model-tier-advisor` govern the *same* axis, which argues for consolidation rather than coexistence).

_Source workflow alias: model-efficiency-router. Originally condensed from a Codex/ChatGPT source; revised 2026-08-28 to verify Claude-specific claims against current documentation (correcting stale/unverified `/fast` and generic "effort tier" language), correct model-name volatility handling, and add Lever B (structural token-saving practices), which the prior revision did not cover despite being asked to optimize total token usage, not just model choice._
