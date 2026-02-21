import streamlit as st
from agents import SimpleCodingAgent
from tools import write_code_to_file

st.title("🤖 Simple AI Coder")

# 1. Setup the AI
model = st.sidebar.text_input("Local Model", value="tinyllama")
ai = SimpleCodingAgent(model)

# 2. User Input
user_query = st.text_input("What should the AI write?", value="An HTML landing page for a coffee shop")
filename = st.text_input("Save as (include extension, e.g., index.html):", value="index.html")

# 3. Running the AI
if st.button("Write & Save Code"):
    st.write("AI is thinking...")
    
    # Get code from AI
    ai_response = ai.ask_ai(f"Write only python code for: {user_query}. No markdown, no backticks.")
    
    # Show the code
    st.code(ai_response, language="python")
    
    # Save the file
    success = write_code_to_file(filename, ai_response)
    
    if success:
        st.success(f"✅ Saved to {filename}!")
    else:
        st.error("❌ Failed to save file.")
