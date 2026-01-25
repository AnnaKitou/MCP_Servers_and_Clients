from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio 
import traceback

server_params = StdioServerParameters (
    command="npx",
    args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"] #Optional Command line arguments
)

async def run():
    try:
        print("Starting stdio client...")
        async with stdio_client(server_params) as (read, write):
            print("Client connected, creating session...")
            async with ClientSession(read, write) as session:

                print("Initializing session...")
                await session.initialize()

                print("Listing tools...")
                tools = await session.list_tools()
                print("Available tools:", tools)
                
                print("Calling tools...")
                result = await session.call_tool("airbnb_search", arguments={"location":"California"})

                print("Tool result:", result)
    except Exception as e:
               print("An error occured:") 
               traceback.print_exc()           

if __name__=="__main__" :
    asyncio.run(run())
