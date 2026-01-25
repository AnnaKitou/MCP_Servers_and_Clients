from mcp.server.fastmcp import FastMCP
import requests
 

mcp = FastMCP("Crypto")
 
@mcp.tool()
def get_cryptocurrency_price(crypto: str) -> str:
    """
    Appends the given content to the user's local notes.
    Args:
       crypto: The cryptocurrency symbol to get the price for.
    """
    try:
      # Use CoinGecko API to get the price in USD
      url=f"https://api.coingecko.com/api/v3/simple/price"
      params={"ids": crypto.lower(), "vs_currencies": "usd"}
      response = requests.get(url, params=params, timeout=10)
      response.raise_for_status()
      data = response.json()
      price = data.get(crypto.lower(), {}).get("usd")
      if price is not None:
            return f"The price of {crypto} is ${price} USD."
      else:
            return f"Could not find price for cryptocurrency: {crypto}."
    except Exception as e:
        return f"Error fetching price for {crypto}: {e}"
    

if __name__ == "__main__":
    mcp.run()