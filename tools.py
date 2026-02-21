import os

def write_code_to_file(filename, content):
    """Simple function to save text to a file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except:
        return False
