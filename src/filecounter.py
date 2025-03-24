from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server named "FileCounter"
mcp = FastMCP("FileCounter")

@mcp.tool()
def count_desktop_files() -> str:
    """Count the number of files on the desktop"""
    desktop_path = os.path.expanduser("~/Desktop")  # Gets desktop path (e.g., /Users/apoorv/Desktop)
    try:
        # List all items in desktop directory, filter to files only
        files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]
        file_count = len(files)
        return f"There are {file_count} files on your desktop."
    except Exception as e:
        return f"Error counting files: {str(e)}"

if __name__ == "__main__":
    mcp.run()