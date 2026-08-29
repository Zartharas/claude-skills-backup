# Bug Resolution Record Template

Target file: `docs/bugs/<short-slug>.md` (one file per significant bug)

Purpose: a record of a bug significant enough that a future session
benefits from knowing it happened, what caused it, and how it was resolved
— not a substitute for an issue tracker, and not meant for routine, minor
fixes.

---

## Worked example

```markdown
# Bug: <short title>

**Status:** Open | Investigating | Fixed | Won't fix (with reason)
**First observed:** <date, if known>
**Resolved:** <date, if resolved>

## Symptom

<What was actually observed — the specific, concrete behavior. Not the
suspected cause; just what happened.>

## Root cause

**Observed:** <if confirmed by reproduction/investigation, state it as fact>
**Hypothesized:** <if not yet confirmed, label it clearly as a hypothesis,
not a conclusion>

## Fix

<What was changed to resolve it, and where. Link to the relevant commit or
file if useful.>

## Verification

<How the fix was confirmed to work — a test added, manual reproduction
steps that no longer trigger the bug, etc. If not yet verified, say so
rather than implying it was.>

## Related

<Links to relevant decisions, other bugs, or progress entries this connects to.>
```

## Notes for the agent filling this in

- **Never claim a fix is verified without evidence it was actually
  checked.** "Should fix it" and "verified fixed" are different claims —
  keep them distinct.
- Root cause: don't collapse "hypothesized" into "observed" because the
  hypothesis is plausible. If it hasn't been confirmed, it stays a
  hypothesis in the record, even after a fix has shipped that seems to have
  worked — a fix can resolve symptoms without the root cause ever being
  confirmed.
- This template is for bugs worth a durable record — something that took
  real investigation, had a non-obvious cause, or is likely to resurface in
  a similar form. A routine typo fix doesn't need one.
- Update **Status** as it changes rather than leaving a stale "Investigating"
  on something that was actually fixed weeks ago.
