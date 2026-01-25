from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Prompt")

@mcp.prompt()
def get_prompt(topic: str) -> str:
    """
    Returns:
       A prompt that will do detailed analysis on a topic
    Args:
       topic: The topic to analyze
    """
    return f"Do a detailed analysis of the following topic: {topic}"

@mcp.prompt()
def write_detailed_historical_report(topic: str, number_of_paragraphs: int) -> str:
   """
   Writes a detailed historical report.
   Args:
      topic: the topic to do research on
      number_of_paragraphs: The number of paragraphs that the main body should be
   """
   prompt = """
     Create a consise researsh repost on the history of {topic}.
     The report should contain 3 section: INTRODUCTION, MAIN BODY, CONCLUSION.
     The MAIN BODY should contain {number_of_paragraphs} paragraphs long.
     Include a timeline of key events.
     The conclusion should be in bullet points format.
     """
   prompt = prompt.format(topic=topic, number_of_paragraphs=number_of_paragraphs)
   return prompt

if __name__ == "__main__":
    mcp.run()