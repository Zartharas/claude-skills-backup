# Progress Tracker Template

Target file: `docs/progress.md`

Purpose: a dated, reproducible record of what's done, what's underway, and
what's stuck — the three states kept explicitly separate, never collapsed
into each other for convenience.

---

## Worked example

```markdown
# Progress

_Last updated: <date>_

## Completed

- **<item>** (<date completed, if known>) — <one line, observed fact:
  what exists and where, not "should work">
- **<item>** — <one line>

## In progress

- **<item>** (started <date, if known>) — <what's done so far, what's left,
  and who/what is working on it if known>

## Blocked

- **<item>** — **blocked on:** <the specific blocker, not just "blocked">
  <if there's an owner or a condition that unblocks it, state that too;
  if unknown, say so as an open question rather than guessing>

## Recently changed since last update

<Optional — useful when this file is updated incrementally rather than
rewritten. What moved between "in progress" and "completed" or "blocked"
since the last "Last updated" date.>
```

## Notes for the agent filling this in

- "Completed" means observed as done — a file exists, a test passes, a
  feature is reachable in the running app. Not "the PR was opened."
- Don't infer "completed" from a commit message or a closed issue alone
  without checking the actual state — commit messages and issue titles can
  be aspirational or wrong.
- If something has been "in progress" for a long time with no visible
  movement, that's worth surfacing as a risk or open question rather than
  leaving it to look like normal, active work.
- Keep entries to one or two lines each. This file is a tracker, not a
  narrative — link to a decision or bug record instead of explaining the
  full story inline.
