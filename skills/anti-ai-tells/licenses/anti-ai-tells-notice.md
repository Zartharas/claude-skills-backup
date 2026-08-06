# NOTICE — Attribution and Modifications

This skill is an upgrade of the pre-existing `anti-ai-tells` skill, incorporating
original additions from `blader/humanizer` (github.com/blader/humanizer),
MIT-licensed, full text in `LICENSE-MIT-blader`.

## What came from blader/humanizer

Concepts adapted (not copied verbatim — rephrased and integrated into this
skill's existing structure and voice):
- The no-fabrication rule (rewrites never invent facts/names/dates/citations
  not in the source)
- Voice calibration from a user-supplied writing sample
- The two-pass "audit as if checking whether it's obviously AI-generated" workflow
- Specific patterns: copula avoidance, synonym cycling, significance inflation,
  manufactured punchlines/staccato drama, chatbot artifacts, curly quotes

blader/humanizer's own primary source is Wikipedia's "Signs of AI writing"
guide (WikiProject AI Cleanup) — credited here for completeness, two levels
upstream.

## What was NOT carried over

- blader/humanizer's Chinese-language pattern set (out of scope for this
  account's usage so far — can be added if needed)
- Its single-register approach — this skill keeps its own, more developed,
  casual/professional/academic register system rather than replacing it
- Its model-fingerprinting subsection (removed upstream in blader/humanizer's
  own v2.6.0 changelog; not reintroduced here)

## A third source — two ideas only, not the package

`ldm2060/research_copilot` (github.com/ldm2060/research_copilot), MIT-licensed,
source of the "Academic De-AI Assistant" mcpmarket listing. Its `paper-deai`
skill contributed two specific rules, rephrased and integrated into the
Academic register section:
- Present-perfect tense for describing prior work in related-work sections
- The "no edit is better than a forced edit" modification threshold, plus the
  LaTeX-safety note (preserve math, preserve required character escaping)

Not adopted: the rest of that project's package. Its core purpose duplicates
this skill's existing scope; it's narrower (LaTeX/CS-conference-specific);
it's built as one half of a two-skill validation-gate pair meant for a larger
multi-agent orchestration pipeline that has no equivalent here; and it has
minimal community validation (1 star, single author) relative to the primary
source above. Its own marketing listing frames one use case as "reducing AI
detection scores... in research paper submissions" — that framing is not
present in the skill file itself and is not the basis on which these two rules
were adopted; they were adopted because they're specific, correct, narrow
technical points about prose quality.

## Also evaluated, not used

`cnfjlhj/ai-collab-playbook` (source of the "Writing Anti-AI & Humanizer"
mcpmarket listing) ships no LICENSE file — no legal grant to redistribute, so
none of its content is present here regardless of quality.

## Version

This is v2 of this account's `anti-ai-tells` skill. v1 content is fully
preserved; nothing was removed, only extended.
