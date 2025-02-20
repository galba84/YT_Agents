
# AI_Agents

A Python-based research agent leveraging **CrewAI**, **LangChain**, and **OpenAI/Ollama LLMs** to conduct automated research on specified topics.

## 🚀 Setup Instructions

### 1. Create a Virtual Environment
Run the following commands to create and activate a Python virtual environment:

#### On Windows (PowerShell)
```sh
python3.11 -m venv myenv
myenv\Scripts\activate
pip install crewai python-dotenv langchain_openai langchain_community
pip install 'crewai[tools]'
