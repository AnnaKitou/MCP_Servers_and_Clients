# Libraries
from mcp.server.fastmcp import FastMCP

# Create MCP Object
mcp = FastMCP("Weather")

# Add the tool
@mcp.tool()
def get_weather(location: str) -> str: 
    """
    Gets the weather given a location    
  
    Args:
    location: location , can be city, ountry , state, etc.
    """
    return "The weather is hot and dry"

if __name__ == "__main__" :
     mcp.run()
