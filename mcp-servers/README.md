# MCP server configs

Stdio MCP server entries with no secrets in them, backed up for restoring on a new machine.
Each `<name>.json` file is the value that goes under `mcpServers.<name>` in
`~/Library/Application Support/Claude/claude_desktop_config.json` (Claude Desktop) and
is equivalent to what `claude mcp add --scope user <name> -- <command> <args...>` writes
into `~/.claude.json` for Claude Code.

## markitdown

[microsoft/markitdown](https://github.com/microsoft/markitdown) — converts PDFs, Office
docs, images, audio, HTML, and more to Markdown.

Restore:

```bash
# CLI tool (also used standalone, outside the MCP server)
uv tool install 'markitdown[all]'

# Claude Code (all projects)
claude mcp add --scope user markitdown -- uvx markitdown-mcp

# Claude Desktop: merge mcp-servers/markitdown.json into
# claude_desktop_config.json's "mcpServers" object, e.g.:
jq '.mcpServers.markitdown = input' \
  ~/"Library/Application Support/Claude/claude_desktop_config.json" \
  mcp-servers/markitdown.json > /tmp/merged.json && \
  cp /tmp/merged.json ~/"Library/Application Support/Claude/claude_desktop_config.json"
```

First run of `uvx markitdown-mcp` fetches and caches the package (~30-45s); Claude Code's
initial connection check can time out during that cold start — run `uvx markitdown-mcp --help`
once manually first, then it connects instantly.
