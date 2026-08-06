---
name: academic-publishing
description: Guide the research-to-publication workflow for building an academic profile — framing a research question, literature search and synthesis with citation-integrity discipline (verify every citation before it's used, never cite from memory), paper structuring (IMRaD, thematic review, case study), drafting support, a peer-review-style self-critique pass before submission, journal/venue selection including predatory-journal screening, and revise-and-resubmit support. Use when working on a paper, journal article, or a publication meant to build a research track record. Does not run live bibliographic database queries — verification happens via web search against public sources, not an API integration.
---

# Academic Publishing

The job: take a research idea to a publishable, defensible paper in a venue that
actually helps a track record — without the two failure modes that quietly wreck
an academic profile: citations that don't say what you claim, and venues that
don't count.

## When to use

- Framing a research question or gap
- Literature search, synthesis, or related-work writing
- Structuring or drafting a paper section
- Self-reviewing a draft before submission
- Choosing where to submit, or vetting whether a venue is legitimate
- Responding to reviewer comments / preparing a revision

## Approach

### 1. Frame before you search

A vague topic produces a vague literature search. Get to a one-sentence research
question with a stated gap: *what's known, what's missing, what this paper adds.*
If the gap can't be stated in a sentence, the search that follows will be
unfocused and the related-work section will read as a list, not an argument.

### 2. Literature search and synthesis — citation integrity is the load-bearing rule

This is the single highest-risk part of academic work done with AI assistance.
Published audits have found large numbers of citations in AI-assisted or
AI-generated text that don't exist, or exist but don't support the claim attached
to them — and the problem is invisible until someone checks. Treat every citation
as a claim requiring evidence, because it is one.

**The rule: verify before you cite, every time, no exceptions for "well-known"
papers.**

- Use `web_search` / `web_fetch` to locate the actual source before citing it —
  never cite a paper from training-data memory of "this is roughly what it says."
  Memory of a paper's *existence* is not verification of its *content*.
- If a source can't be located and confirmed, say so explicitly — `[COULD NOT
  VERIFY]` — rather than citing it anyway or quietly dropping the claim it was
  supporting.
- Match the *specific claim* to the *specific source*, not just the topic. A
  citation attached to "X causes Y" needs to actually support causation, not just
  be a paper that mentions X and Y.
- Don't inflate a related-work section by citing papers you haven't actually
  read/verified just to show breadth. Reviewers check. Padding it is one of the
  fastest ways to damage credibility with an editor.
- Watch for **citation stacking and self-citation abuse** — citing your own prior
  work, or a small in-group's work, beyond what the argument needs. Journals
  increasingly flag this in ethics review; it reads as gaming metrics, which is
  exactly what it is.
- See `references/citation-integrity-checklist.md` for the full verification
  workflow.

### 3. Structure to the argument, not the template

Pick the structure the argument needs, then follow its conventions:

- **IMRaD** (Introduction/Methods/Results/Discussion) — empirical research
- **Thematic literature review** — synthesis across a body of work, organized by
  theme/tension, not paper-by-paper summary
- **Theoretical/conceptual paper** — argument-driven, no methods section
- **Case study** — bounded context, explicit generalizability limits
- **Policy brief** — recommendation-first, evidence-supporting

A common failure: writing a thematic review as a list of "Author (Year) found X. 
Author (Year) found Y." That's an annotated bibliography, not a review. A review
argues — it groups sources by what they agree/disagree on, identifies the actual
gap, and makes a case for what the field still doesn't know.

### 4. Draft with the reader's actual question in mind

Every section answers a question the reader is implicitly asking:

| Section | Reader's question |
|---|---|
| Introduction | Why should I keep reading? |
| Related work | What's already known, and what's this paper's actual contribution? |
| Methods | Could I reproduce this? |
| Results | What did you find, stated plainly before interpretation? |
| Discussion | What does it mean, and what are the limits of that meaning? |

Keep results and discussion separated even when it's tempting to interpret as you
report — a reviewer needs to see the finding before your spin on it.

### 5. Self-critique before it goes anywhere

Run a critique pass before submission — not as a formality, as the step most
likely to catch what a real reviewer will catch first. **Use the installed
`multi-expert-analysis` skill for this**, but override its default lenses; its
Security/Legal/Business panel is built for engineering decisions, not peer review.
For a paper, request it with these lenses instead:

- **Methodology & statistics** — does the method answer the stated question; are
  statistical claims (significance, effect size, sample size) actually supported
- **Novelty & contribution** — is the "gap" genuinely unaddressed, or is this
  incremental dressed as novel
- **Reproducibility** — could someone else run this from what's written
- **Research ethics** — IRB/consent where human subjects are involved, data
  provenance, conflicts of interest, authorship criteria (did everyone listed meet
  authorship criteria, e.g. ICMJE's four criteria — not just "helped somehow")
- **Clarity & argument** — does each section answer its reader's question; is the
  through-line from question → gap → finding → implication intact

This mirrors the concession-threshold instinct worth naming explicitly: a
critique pass that agrees with everything on first pushback isn't doing its job.
Push on the weakest claim in the paper, not just the strongest.

### 6. Venue selection — this is where a profile is actually built or damaged

The venue matters more than most first-time authors expect. A paper in a
predatory or low-quality venue doesn't build a profile — it can actively harm one,
and it's hard to undo once published.

**Screen every unfamiliar venue before submitting.** Use `references/predatory-journal-screening.md`
for the full checklist. The short version: verify DOAJ/index membership
independently (don't trust a badge on the journal's own site), check the editorial
board is real and reachable, look for unrealistic review turnaround claims (a
"peer review" completed in days is not peer review), and confirm fee structure is
transparent before submission, not revealed after acceptance.

**Check current metrics, don't rely on memory.** Journal rankings, impact
factors, and quartile placements change yearly and any AI's training-data
knowledge of them is likely stale. Use `web_search` to confirm current standing
(Scimago, JCR, or the field's disciplinary ranking list) before recommending or
ruling out a venue.

**Match ambition to the paper, not the profile goal.** A strong paper in a
respected field journal builds more credibility than a rejected submission to a
reach venue followed by drift toward whatever will publish it. If unsure, discuss
a realistic shortlist (reach / solid match / safety) rather than a single pick.

### 7. Revision and response to reviewers

- Address every point a reviewer raises, even ones you disagree with — disagree
  explicitly and with evidence, don't silently ignore.
- A response letter is itself a piece of writing that gets judged; point-by-point,
  specific, non-defensive in tone even when the review was harsh.
- Track what changed between rounds — an editor comparing R1 to R2 needs to find
  the changes, not re-read the whole paper hunting for them.

## Building a profile over multiple papers

A profile is a portfolio, not a single paper. A few things that compound:

- **Consistent identity**: ORCID on every submission, consistent name form, so
  work is attributable to one record rather than fragmenting across name variants.
- **Preprints where the field norm allows** (arXiv, SSRN, field-specific servers)
  — establishes priority and gets earlier feedback, but check target journal
  policy on prior preprint posting first; it varies by field and venue.
- **Read your own past reviews for patterns** — if the same critique recurs across
  submissions (weak related-work synthesis, overclaiming in discussion), that's
  the highest-leverage thing to fix before the next paper, not per-paper polish.

## Resources

- `references/citation-integrity-checklist.md` — the verify-before-cite workflow
- `references/predatory-journal-screening.md` — venue vetting checklist

## Guardrails

- **Not a substitute for domain expertise, an IRB, or institutional guidance.**
  This structures the work; it doesn't validate a methodology or clear ethics
  review.
- **No fabricated citations, ever, under any framing.** If a claim needs a source
  and none can be verified, say so and flag the gap — don't paper over it with a
  plausible-sounding but unverified reference.
- **No guarantee of acceptance.** Journal decisions involve fit, timing, and
  reviewer variance beyond what any preparation can control for; frame
  recommendations as improving odds, not promising outcomes.
- **Venue and metrics claims are time-sensitive.** Verify current standing via
  search rather than stating rankings from memory.
