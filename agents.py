from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

class SimpleCodingAgent:
    def __init__(self, model_name="tinyllama"):
        # Connect to Ollama
        self.llm = ChatOllama(model=model_name, temperature=0)

    def ask_ai(self, prompt):
        # The System Prompt defines the AI's personality and rules
        system_message = SystemMessage(content="""
        You are a professional Full-Stack Developer.
        Rule 1: Give ONLY the raw source code (Python, HTML, CSS, etc.).
        Rule 2: Do NOT include explanations, comments, markdown blocks, or backticks.
        Rule 3: Ensure the code is clean, working, and ready to be saved.
        """)
        
        user_message = HumanMessage(content=prompt)
        
        # Send both messages to the AI
        response = self.llm.invoke([system_message, user_message])
        return response.content
