from mcp.server.fastmcp import FastMCP

mcp=FastMCP("server")

@mcp.tool()
def greerting(name: str) -> str:
    "Sends a greeting message."
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")   