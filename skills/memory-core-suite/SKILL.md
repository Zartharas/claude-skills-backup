---
name: memory-core-suite
description: "Use for anything about claude-mem's own memory system: searching past-session history, explaining how capture/injection works, cloud sync setup, building queryable knowledge-agent corpora from observations, or customizing what gets remembered (modes, tags, Telegram alerts). Route by which of these five the user is actually asking for."
---

# Memory Core Suite

## Purpose

Everything that operates on claude-mem's own memory layer, rather than on the user's project code. Five original skills, unified here so one entry point covers "did we solve this before," "how does this thing work," "sync my memories," "build me a knowledge base of past work," and "change what gets remembered."

## Source aliases

Recognize these original skill names as explicit aliases: `mem-search`, `how-it-works`, `cloud-sync`, `knowledge-agent`, `mode-creator`.

| Original alias | Read | Use when |
|---|---|---|
| `mem-search` | `workflows/mem-search.md` | User asks about PREVIOUS sessions — "did we already solve this?", "how did we do X last time?" — not the current conversation. |
| `how-it-works` | `workflows/how-it-works.md` | User asks what claude-mem is doing or how observation capture/injection works, with no action requested. |
| `cloud-sync` | `workflows/cloud-sync.md` | User wants cmem.ai Pro cloud sync set up, checked, or troubleshot. Uses AskUserQuestion — this is an interactive setup flow, not a lookup. |
| `knowledge-agent` | `workflows/knowledge-agent.md` | User wants a filtered, conversational "brain" built from observation history on a specific topic, not a one-off search. |
| `mode-creator` | `workflows/mode-creator.md` | User wants to change what claude-mem records — new observation types, concept tags, Telegram alerts — even if they never say "mode." Requires a local worker install and Node 20+; see its `compatibility` note. Bundled scripts/references live under `assets/mode-creator/`. |

Read only the workflow that matches the current request. Do not load every workflow in the family. `how-it-works` and `mode-creator` have supporting files under `assets/<name>/` (scripts, references, evals) — the workflow doc tells you when to read or run them.

## Routing precedence

1. A question about *past* sessions or prior work → `mem-search`.
2. A question about *how the system itself functions*, no action requested → `how-it-works`.
3. A request to sync/back up the memory database to cmem.ai → `cloud-sync`.
4. A request to compile a topic-specific, queryable corpus from observations → `knowledge-agent`.
5. A request to change what gets captured, tagged, or alerted on → `mode-creator`.

When two routes remain plausible (e.g. "what have we learned about X" could be `mem-search` or `knowledge-agent`), prefer `mem-search` for a single lookup and `knowledge-agent` only when the user wants a durable, reusable corpus to query repeatedly.

## Non-goals

- Editing or planning changes to the user's project code — see `planning-execution-suite`.
- Generating narrative reports from the timeline — see `reporting-narrative-suite` (`timeline-report`, `weekly-digests`).

## Completion gate

Before finishing, confirm the correct sub-skill was read (not guessed from memory), any interactive prompts it requires were actually asked, and destructive or worker-restart steps (`mode-creator`) were only taken after explicit confirmation.
