from langchain.tools import tool
import os

@tool
def write_file_tool(filename: str, content: str) -> str:
    """
    A tool that writes content to a file. 
    Useful for the File Manager Agent to save code.
    """
    try:
        # We ensure the filename is safe and write it to the current directory
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ Success: Code saved to {filename}"
    except Exception as e:
        return f"❌ Error: Could not save file. {str(e)}"
