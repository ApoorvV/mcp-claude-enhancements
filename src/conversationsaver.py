from mcp.server.fastmcp import FastMCP
import os
from datetime import datetime

mcp = FastMCP("ConversationSaver")

@mcp.tool()
def save_conversation(conversation: str) -> str:
    """Save the current conversation to a text file on the desktop"""
    desktop_path = os.path.expanduser("~/Desktop")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(desktop_path, f"claude_chat_{timestamp}.txt")
    try:
        with open(file_path, "w") as f:
            f.write(conversation)
        return f"Conversation saved at: {file_path}"
    except Exception as e:
        return f"Error saving conversation: {str(e)}"

if __name__ == "__main__":
    mcp.run()