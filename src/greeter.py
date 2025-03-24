from mcp.server.fastmcp import FastMCP

# Create an MCP server named "Greeter"
mcp = FastMCP("Greeter")

@mcp.tool()
def greet() -> str:
    """Return this welcome message, when greeted with "Hi", "Hey" or "Hello"."""
    return "Hey Apoorv, Welcome to the world of MCPs!"

if __name__ == "__main__":
    mcp.run()