# claude-skills-backup

Backup of `~/.claude/skills/` — Claude Code Agent Skills installed locally, for restoring to a new machine.

## Restore on a new machine

```bash
git clone https://github.com/Zartharas/claude-skills-backup.git
mkdir -p ~/.claude/skills
cp -R claude-skills-backup/skills/. ~/.claude/skills/
```

## Notes

- `agent-browser` was originally a symlink to `~/.agents/skills/agent-browser` on the source machine; it's stored here as a real copy so the repo is self-contained. If your new machine also has `~/.agents/skills/agent-browser` and you want the symlink relationship back, replace the copied folder with a symlink after restoring.
- `skills/.claude/settings.local.json` holds directory-scoped permission grants (not secrets) — review before reuse on another machine.
- `memory-core-suite`, `planning-execution-suite`, `repo-governance-suite`, and `reporting-narrative-suite` are consolidations of the claude-mem plugin's individual skills (mem-search, make-plan, do, babysit, etc.), each preserved as a subfolder under its suite with a router `SKILL.md` at the top. The other `*-suite` folders follow the same pattern, built from a separate Codex/ChatGPT skill catalog.
