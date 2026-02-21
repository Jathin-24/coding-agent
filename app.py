import streamlit as st
import os
from agents import CodingAgents

# --- PAGE CONFIG ---
st.set_page_config(page_title="Multi-Agent Coding AI", page_icon="🤖", layout="wide")

# --- STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #4CAF50; color: white; }
    .agent-tag { background-color: #1e2130; padding: 10px; border-left: 5px solid #4CAF50; margin: 10px 0; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("⚙️ Configuration")
    model_name = st.text_input("Local Model Name", value="tinyllama")
    st.divider()
    st.markdown("### � Project Files")
    st.info("The logic is split into:")
    st.code("tools.py  -> Handlers\nagents.py -> Brains\napp.py    -> Interface")

# --- INITIALIZE AGENTS ---
agents = CodingAgents(model_name=model_name)

# --- UI LAYOUT ---
st.title("🚀 Multi-Agent Local AI Coder")
st.markdown("Teaching students how specialized AI agents work together using **LangChain** and **Ollama**.")

user_input = st.text_area("Challenge the AI:", placeholder="e.g. Write a python script to scrape a website.")

if st.button("Execute Multi-Agent Workflow"):
    if user_input:
        # Step 1: Programmer Agent
        st.markdown('<div class="agent-tag">🤖 <b>Step 1: Programmer Agent</b> is thinking...</div>', unsafe_allow_html=True)
        with st.spinner("Generating logic..."):
            generated_code = agents.programmer_agent(user_input)
            
        st.code(generated_code, language="python")

        # Extract filename from the first line comment
        filename = "output_code.py"
        if "# filename:" in generated_code:
            filename = generated_code.split('\n')[0].replace("# filename:", "").strip()

        # Step 2: File Manager Agent
        st.markdown(f'<div class="agent-tag">📂 <b>Step 2: File Manager Agent</b> is saving to {filename}...</div>', unsafe_allow_html=True)
        with st.spinner("Writing to disk..."):
            save_result = agents.file_manager_agent(filename, generated_code)
            
        if "Success" in save_result:
            st.success(save_result)
        else:
            st.error(save_result)

        # Show verification
        st.divider()
        st.subheader("🏁 Workflow Complete")
        st.write("You can now find the file in your current folder!")
    else:
        st.warning("Please enter a task for the agents.")

st.divider()
st.caption("A modular multi-agent demonstration for educational purposes.")
