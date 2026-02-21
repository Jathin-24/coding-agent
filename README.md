# 🤖 Modular Multi-Agent AI Coder

This demo is designed to show students how to build a **Modular AI System**. Instead of one big file, we have separated the concerns into specialized files.

## 📂 File Architecture (The "Team")

1.  **`tools.py` (The Toolshelf)**:
    *   Contains the actual functions that interact with the real world (like saving a file).
    *   In AI terms, these are called **Tools**.

2.  **`agents.py` (The Brains)**:
    *   Defines the "Personas" of our AI.
    *   **Programmer**: Knows how to write code.
    *   **File Manager**: Knows how to use the "Tool" to save code.

3.  **`app.py` (The Manager)**:
    *   Provides the user interface (Streamlit).
    *   Orchestrates the order of work (Work-flow).

## 🚀 Setup

1.  **Ollama**: Ensure it's running with `tinyllama`.
2.  **Pull the model**:
    ```bash
    ollama pull tinyllama
    ```
3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run**:
    ```bash
    streamlit run app.py
    ```

## 👨‍🏫 Lesson for Students
Explain to students that in the "real world," AI isn't just one prompt. It's a team of specialized agents. By splitting the code into files, we make it:
*   **Easier to test**: You can test the tool without the AI.
*   **Easier to scale**: You can add a "Reviewer Agent" just by adding a function in `agents.py`.
*   **Easier to understand**: Each file has one specific job.
