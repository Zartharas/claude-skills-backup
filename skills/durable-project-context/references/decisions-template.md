# Decision Record Template

Target file: `docs/decisions/<number>-<short-title>.md` (one file per
decision)

Purpose: this format intentionally matches a standard Architecture Decision
Record structure, the same one a dedicated architecture-decision skill would
produce on direct request. A decision captured through project-context
maintenance should be indistinguishable in format from one captured through
a direct "/architecture"-style request — same convention, whichever path
created it.

---

## Worked example

```markdown
# ADR-<number>: <Title>

**Status:** Proposed | Accepted | Deprecated | Superseded (by ADR-<n>)
**Date:** <date decided, not date recorded, if they differ — note both if so>
**Deciders:** <who, if known — otherwise omit the line rather than guess>

## Context

<What situation made this decision necessary. Observed facts about the
constraints in play — not a restatement of the decision itself.>

## Decision

<What was actually decided, stated plainly.>

## Options considered

### Option A: <name>
**Pros:** <list>
**Cons:** <list>

### Option B: <name>
**Pros:** <list>
**Cons:** <list>

## Consequences

<What follows from this decision — both intended effects and known
trade-offs accepted. Distinguish what's been verified from what's expected
but not yet confirmed.>

## Open questions

<Anything about this decision that remains unresolved — a follow-up needed,
a condition under which it should be revisited.>
```

## Notes for the agent filling this in

- **Never invent a decision that wasn't actually made.** If the repository
  shows evidence something was decided (a specific technology in use, a
  pattern applied consistently) but no record exists of *why*, that's a
  decision to document if the reasoning is known (e.g., the user just
  explained it) — not one to reconstruct by guessing plausible reasoning
  and presenting it as the original rationale.
- If a decision is being recorded after the fact rather than at the time
  it was made, say so in the Date line rather than implying it was written
  contemporaneously.
- **Status matters and should be kept current** — a decision later
  superseded should have its status updated and link to the ADR that
  replaced it, not be left marked "Accepted" indefinitely.
- One decision per file. Don't bundle several unrelated decisions into one
  record because they happened in the same session.
