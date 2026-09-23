# custom_mcp_server

[![CI](https://github.com/linkedajay2018/custom-mcp-server/actions/workflows/ci.yml/badge.svg)](https://github.com/linkedajay2018/custom-mcp-server/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)

A minimal MCP (Model Context Protocol) server built with the `mcp` Python SDK. Exposes three tools: `add`, `save_note`, `search_notes`. Built as a learning project — not intended for production use.

## Requirements

- Python ≥ 3.10 (`mcp[cli]` doesn't support 3.9)
- Node.js + npx (only for the MCP Inspector)

## Setup

```bash
python3.11 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
```

## Running directly

```bash
.venv/bin/python3 server.py
```

Starts the server on stdio. Meant to be launched by an MCP client (Inspector, Claude Desktop, Claude Code) — not run interactively.

## Running with the MCP Inspector

```bash
npx @modelcontextprotocol/inspector "$(pwd)/.venv/bin/python3" "$(pwd)/server.py"
```

Prints a URL with an auth token — open it in your browser. The server card connects automatically over stdio. `Ctrl+C` to stop.

## Testing

```bash
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/pytest -q
```

Runs on every push/PR via [GitHub Actions](.github/workflows/ci.yml).

## Registering with Claude Code

From the project root:

```bash
claude mcp add --scope project my-first-server -- "$(pwd)/.venv/bin/python" "$(pwd)/server.py"
```

This writes `.mcp.json` with absolute paths. Since `.mcp.json` is committed to git, swap them for `${CLAUDE_PROJECT_DIR}` so the config works on any checkout:

```json
{
  "mcpServers": {
    "my-first-server": {
      "type": "stdio",
      "command": "${CLAUDE_PROJECT_DIR}/.venv/bin/python",
      "args": ["${CLAUDE_PROJECT_DIR}/server.py"],
      "env": {}
    }
  }
}
```

- Verify: `claude mcp get my-first-server` (shows resolved absolute paths)
- Remove: `claude mcp remove my-first-server --scope project`
- First load of a project's `.mcp.json` prompts for approval

## Notes

- `NOTES` storage in `server.py` is in-memory only and resets on restart.

## License

[MIT](LICENSE)
