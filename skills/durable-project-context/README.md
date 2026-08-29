# durable-project-context

A Claude Code skill that maintains small, repository-native project memory — a
context index, a progress tracker, decision records, and bug-resolution
records — so a future session (agent or human) can reconstruct project state
by reading the repository, without re-deriving it or re-asking someone who
already explained it once.

## Why this exists

Agent coding sessions are stateless between invocations. Without something
durable committed to the repository, every new session either re-explores
from scratch or relies on the person re-explaining context that was already
established. This skill keeps that context current, in the smallest form
that's actually useful — not a documentation project, a memory-maintenance
one.

## What it produces

| Artifact | Purpose |
|---|---|
| `docs/project-context.md` | What the project is, entry points, current architecture, links to the rest |
| `docs/progress.md` | Completed / in-progress / blocked, dated |
| `docs/decisions/*.md` | One ADR-formatted file per decision |
| `docs/bugs/*.md` | One file per significant bug, symptom through resolution |

These are fallback paths for a repository with nothing established yet. If a
repository already has an equivalent under a different name or convention
(an `AGENTS.md` with a status section, an existing `docs/` layout, a wiki),
this skill extends that instead of introducing a competing structure.

## Checked for overlap before building

This account already has two skills adjacent to this territory. Neither does
the same job, but the boundaries are worth stating precisely rather than
leaving them implicit:

**`engineering:documentation`** (plugin) writes technical documentation on
request — README, API docs, runbooks, architecture docs, onboarding guides.
It's request-triggered, produces polished human-facing docs, and has no
concept of inspecting a repository for staleness or maintaining an ongoing
index across sessions. Route a general "write docs for X" request there;
route a "the project's context is stale/missing" situation here.

**`engineering:architecture`** (plugin) produces a single ADR on direct
request, on demand. This skill's own `docs/decisions/` output uses the same
ADR structure that skill produces (see `references/decisions-template.md`),
specifically so a decision captured through either path lands in a
compatible format rather than fragmenting into two conventions. If a single
decision needs recording right now on request, either skill can produce it
compatibly; this skill's job is noticing when a decision is *missing* from
the record as part of a broader context sweep.

**`karpathy-guidelines`** (already installed) governs coding-session
discipline generally, including a "Surgical Changes" principle this skill
explicitly borrows for documentation edits — touch only what the gap
requires, don't reorganize surrounding content that wasn't part of the
problem. Different job (this skill is about *what gets recorded*, not
*how a coding task is executed*), no merge needed, same underlying ethos.

**`claude-mem`** / the memory-core-suite (already installed) is a different
mechanism entirely: it captures session observations into a queryable,
tool-dependent corpus. This skill produces plain, git-diffable markdown that
requires no tool to read — portable to any agent or human that can open a
file. The two are complementary, not competing: claude-mem can index *why*
something happened across many sessions in rich detail; this skill keeps the
canonical, human-readable summary that survives even without claude-mem
installed.

**Conclusion:** no existing skill inspects a repository for context gaps,
maintains an ongoing index, or applies the fact/assumption/decision/
open-question separation this skill requires. Built new rather than
upgrading something else, with the two genuine overlaps (ADR format,
documentation-request boundary) resolved by explicit routing rather than
left ambiguous.

## Usage

This skill activates automatically when a repository shows signs of missing
or stale durable context — no explicit invocation required. To invoke it
directly:

> "Set up durable project context for this repo."
> "The progress tracker hasn't been updated since the auth rewrite — bring it current."
> "Record the decision we just made about the queue backend."

## File tree

```
durable-project-context/
├── SKILL.md
├── README.md
├── references/
│   ├── context-index-template.md
│   ├── progress-template.md
│   ├── decisions-template.md
│   └── bug-resolution-template.md
└── scripts/
    └── inspect_project_context.py
```
