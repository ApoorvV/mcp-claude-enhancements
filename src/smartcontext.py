from mcp.server.fastmcp import FastMCP
import os
import PyPDF2  # For PDF text extraction

mcp = FastMCP("SmartContext")

# Hardcoded path to your leave policy PDF (edit this to your file’s location)
LEAVE_POLICY_PDF = "/Users/apoorv/Desktop/AV/Code/MCP/leave_policy.pdf"

@mcp.tool()
def fetch_context(query: str) -> str:
    """Fetch content from a leave policy PDF for leave-related queries"""
    query_lower = query.lower()

    # Only process if "leave" is in the query
    if "leave" not in query_lower:
        return "This tool only answers leave-related questions. Ask about leaves!"

    if not os.path.exists(LEAVE_POLICY_PDF):
        return f"Error: Leave policy PDF not found at {LEAVE_POLICY_PDF}!"

    try:
        # Read the PDF
        with open(LEAVE_POLICY_PDF, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            content = ""
            for page in pdf_reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    content += extracted_text + "\n"
            if not content:
                return "Error: No text could be extracted from the leave policy PDF!"

        # Return the content with the query for Claude
        return (f"Using context from {LEAVE_POLICY_PDF}:\n\n"
                f"Content:\n{content}\n\n"
                f"Query: {query}\n\n"
                f"Please answer based on the content above.")
    except Exception as e:
        return f"Error reading leave policy PDF: {str(e)}"

if __name__ == "__main__":
    mcp.run()