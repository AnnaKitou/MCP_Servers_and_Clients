```python
$$
# MCP Server Deepdive Deployment

## Installation

To install and configure this MCP server in VS Code:

1. Ensure you have `uvx` installed. If not, install it via pip: `pip install uvx`

2. Add the following configuration to your VS Code settings.json:

```json
{
  "mcpServers": {
      "deepdive": {
      "command": "uvx",
      "args": [
        "--from",
        "mcp-server-deepdive-deployment @ https://github.com/AnnaKitou/mcpserverdeployment/archive/refs/heads/main.zip",
        "mcp-server"
      ]
    }
  }
}
```
$$
```