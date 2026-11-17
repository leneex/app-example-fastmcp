import os
from datetime import datetime, timezone

from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("Demo MCP server")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


@mcp.tool
def echo(text: str) -> str:
    """Return the text unchanged."""
    return text


@mcp.tool
def utc_now() -> str:
    """Current date and time in UTC, ISO 8601."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@mcp.custom_route("/", methods=["GET"])
async def index(request: Request) -> PlainTextResponse:
    return PlainTextResponse("MCP server is running. Endpoint: /mcp\n")


@mcp.custom_route("/health", methods=["GET"])
async def health(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK\n")


if __name__ == "__main__":
    # Порт передаёт платформа в переменной PORT; без неё — 8000
    mcp.run(transport="http", host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
