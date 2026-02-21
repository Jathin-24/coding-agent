from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from tools import write_file_tool

class CodingAgents:
    def __init__(self, model_name="tinyllama"):
        # We initialize the Local LLM via Ollama
        self.llm = ChatOllama(model=model_name, temperature=0)

    def programmer_agent(self, user_prompt: str):
        """
        Role: Python Developer
        Task: Think about the logic and generate clean Python code.
        """
        prompt = f"""You are an expert Python Programmer. 
        Task: {user_prompt}
        
        Rules:
        1. Generate ONLY the Python code.
        2. No markdown blocks (no ```python).
        3. Add a comment on the first line with a suggested filename, e.g., '# filename: script.py'
        """
        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content.strip()

    def file_manager_agent(self, filename: str, code: str):
        """
        Role: System Administrator
        Task: Take the code and use the 'write_file_tool' to save it.
        """
        # In a complex system, this agent would decide which tool to use.
        # Here, we show how it calls the tool directly for the demo.
        result = write_file_tool.invoke({"filename": filename, "content": code})
        return result
