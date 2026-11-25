# FastMCP

Example remote MCP server built with [FastMCP](https://gofastmcp.com). FastMCP is a Python framework for building Model Context Protocol (MCP) servers, which let AI assistants use external tools and data.

## Deploy settings

| Field | Value |
| --- | --- |
| Build | Railpack |
| Project directory | `/` |
| Install command | leave empty |
| Build command | leave empty |
| Start command | leave empty |
| Application port | `8000` |
| Health check path | `/health` |

## <a name="dev"></a>Run locally

```bash
# virtual environment and dependencies
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# start the server
python3 main.py
```

Server address: `http://localhost:8000/mcp`, health check: `http://localhost:8000/health`.
Requires Python 3.11 or later.
