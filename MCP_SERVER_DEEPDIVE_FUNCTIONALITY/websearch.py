from mcp.server.fastmcp import FastMCP 
from openai import OpenaAI  

mcp = FastMCP("Web Search")

@mcp.tool()
def perform_websearch(query:str)-> str:
    """Performs a web search for a query.
    Args:
      query: The query to web search.
    """

    messages=[
        {
         "role":"system",
         "content":("You are an AI assistant that searches the web and respon to questions")
         },

        {
         "role":"system",
         "content":(query)
         }]
    client = OpenaAI(api_key="YOUR_API_KEY", base_url="https://www.perplexity.ai")

    #chat completion without streaming
    response = client.chat.completions.create(
        MODEL="sonar-pro" , 
        messages=messages
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    mcp.run()