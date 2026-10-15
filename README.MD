# JobHunt MCP Server

An MCP (Model Context Protocol) server that runs my India job hunt.
Any AI client can discover and call its tools.

## Tools

| Tool | What it does |
|------|--------------|
| `list_targets` | Lists my 5 target companies and roles (Hyderabad) |
| `log_application` | Logs a new application with today's date |
| `get_status` | Shows all logged applications |
| `next_actions` | Suggests today's actions: applied vs still-to-apply |

## Run it

```bash
pip install "mcp<2"
python test_client.py
