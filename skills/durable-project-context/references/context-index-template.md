# Project Context Index Template

Target file: `docs/project-context.md`

Purpose: the single entry point a new session reads first. Keep it short —
this is an index and orientation, not the full record. Link out to
`progress.md`, `decisions/`, and `bugs/` rather than duplicating their
content here.

---

## Worked example

```markdown
# Project Context: <project name>

_Last updated: <date>. Update this line whenever this file changes._

## What this is

<One to three sentences. What the project does and who/what it's for.
Observed from README/package manifest/entry point — don't editorialize
beyond what's actually established.>

## Entry points

- `<path>` — <one line: what starts here>
- `<path>` — <one line>

## Current architecture (summary only)

<A few sentences or a short list of the major components and how they
relate. Link to a dedicated architecture doc if one exists rather than
duplicating it here — this section is orientation, not the full design.>

## Conventions this project follows

<Only conventions actually observed in the repo — a specific test framework,
a commit-message format, a directory-naming pattern. Don't state a
convention you inferred from one example; note it as an assumption instead
if it's not clearly established by multiple instances.>

## Status at a glance

See `docs/progress.md` for detail. Summary:
- **Completed:** <one line>
- **In progress:** <one line>
- **Blocked:** <one line, or "none">

## Key decisions

See `docs/decisions/` for full records. Most consequential:
- <decision title> — <one line why it matters> ([record](decisions/<file>.md))

## Known risks and limitations

<Only what's actually known — an unresolved edge case, a dependency on an
unmaintained library, a scaling limit that hasn't been tested. Not a
speculative list of things that could theoretically go wrong.>

## Open questions

<Genuinely unresolved items a future session should know are unresolved,
not quietly assumed one way or another.>
```

## Notes for the agent filling this in

- Every section above is optional if there's nothing real to put in it —
  an empty "Open questions: none currently" is fine and honest; a filled-in
  section with speculative content is not.
- The "Last updated" line is load-bearing — it's how a future session judges
  whether this file is still trustworthy. Keep it accurate.
- If the repository's README already covers "what this is" well, link to it
  instead of restating it here.
