import getpass
import os

from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langsmith import Client

# client = Client()
tools = [TavilySearch()]
# llm = ChatOllama(temperature=0, model="deepseek-r1:8b")
llm = ChatOpenAI(temperature=0, model="openai/gpt-4o-mini")
agent = create_agent(
    model=llm, tools=tools, system_prompt="You are a helpful search assistant."
)

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API key:\n")
if not os.environ.get("OPENAI_API_BASE"):
    os.environ["OPENAI_API_BASE"] = getpass.getpass("OpenAI API base:\n")
if not os.environ.get("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = getpass.getpass("Tavily API key:\n")


def main():
    print("Hello from langchain-course!")
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "search for 3 job postings for an AI engineer using langchain and langgraph in gurgaon area on linkedin and list thier details",
                    # "content": "search top 3 tourist places in india"
                }
            ]
        }
    )
    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()
