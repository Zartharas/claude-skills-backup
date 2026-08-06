---
name: repo-governance-suite
description: "Use for process work around a repo's PRs, issue backlog, branches, and releases: watching a PR to merge, clustering an issue backlog into plan-master issues, running a read-only standup across worktrees/branches/PRs, or cutting a versioned release. Route by which of these four governance tasks is being asked for."
---

# Repo Governance Suite

## Purpose

Four original skills that manage repository process rather than code content: keeping a PR moving (`babysit`), turning a messy issue backlog into a roadmap (`oh-my-issues`), comparing in-flight work across worktrees/branches/PRs (`standup`), and cutting a release (`version-bump`).

## Source aliases

Recognize these original skill names as explicit aliases: `babysit`, `oh-my-issues`, `standup`, `version-bump`.

| Original alias | Read | Use when |
|---|---|---|
| `babysit` | `workflows/babysit.md` | Asked to watch/monitor a specific PR until it's actually mergeable — comments, reviews, and CI all resolved, not just one pass. |
| `oh-my-issues` | `workflows/oh-my-issues.md` | An issue tracker has accumulated many reports sharing root causes and needs clustering into plan-master issues + one PR per cluster. |
| `standup` | `workflows/standup.md` | Need a read-only comparison across git worktrees, branches, or PRs producing one consolidation plan. Ships its own CLI (`assets/standup/standup.mjs`) and `assets/standup/agent-brief.md` — read both before running. |
| `version-bump` | `workflows/version-bump.md` | Asked to cut a release: version bump across manifests, changelog generation, git tag, GitHub release. Everything must end committed and pushed except npm publish, which is handed to the human. Uses `assets/version-bump/scripts/generate_changelog.js`. |

Read only the workflow that matches the current request. Do not load every workflow in the family.

## Routing precedence

1. One named PR needs to be watched to completion → `babysit`.
2. A backlog of many issues needs root-cause clustering → `oh-my-issues`.
3. Comparing state across multiple worktrees/branches/PRs, no single PR named → `standup`.
4. Cutting an actual version/release → `version-bump`.

## Non-goals

- Writing the implementation that a PR or plan contains — see `planning-execution-suite`.
- Narrative/report generation about project history — see `reporting-narrative-suite`.

## Completion gate

Before finishing, confirm no destructive or externally-visible action (pushing, closing issues, tagging a release, publishing) was taken without explicit user authorization, and that `version-bump` in particular ends with a clean `git status`.
