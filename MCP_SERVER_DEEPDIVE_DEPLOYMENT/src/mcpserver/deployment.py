# server.py
from mcp.server.fastmcp import FastMCP

# Create an mcp server instance
mcp=FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two numbers together.
    """
    return a + b 