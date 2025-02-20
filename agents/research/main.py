import os

from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
# from langchain_community.llms import Ollama
import litellm
litellm._turn_on_debug()
load_dotenv()

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")

print("SERPER_API_KEY:", os.getenv("SERPER_API_KEY"))
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("OPENAI_API_BASE:", os.getenv("OPENAI_API_BASE"))


search_tool = SerperDevTool()

def create_research_agent(use_gpt = True):
    

    if use_gpt:
        llm = ChatOpenAI(model="gpt-4o")
    else:
        # llm = OllamaLLM(model="llama3.2:latest", base_url="http://localhost:11434")
        
    return Agent(
        role="Research Specialist",
        goal="Conduct through research on given topics",
        backstory="You are an experienced researcher with expertise in finding and synthesizing information from various sources.",
        verbose=True,
        allow_delegation=False,
        tools=[search_tool],
        llm=llm
    )
    
def create_research_task(agent, topic):
    return Task(
        description=f"Research the following topic and provide a comprehensive summary: {topic}",
        agent=agent,
        expected_output="up to five pro and cons"
    )
    
def run_research(topic, use_gpt=True):
    print(f"Starting research on: {topic}")
    agent = create_research_agent(use_gpt)
    print("Agent created.")
    task = create_research_task(agent, topic)
    print("Task created.")
    crew = Crew(agents=[agent], tasks=[task])
    print("Crew initialized, starting task execution...")

    result = crew.kickoff()

    print("Research Result:", result)
    
    return result

if  __name__ == "__main__":
    print("Welcome to research Agent!")
    use_gpt = input("Do you want to use gpt yes/no? ").lower() == 'yes'
    topic = input("Enter the research topic: ")
    
    result = run_research(topic, use_gpt)
    print("\nresearch result:")
    print(result)