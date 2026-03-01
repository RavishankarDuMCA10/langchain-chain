from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-chain!")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="Search for 3 job postings for an ai engineer using langchain in the Delhi NCR region on linkedin and list their details."
            )
        }
    )
    print(result)


if __name__ == "__main__":
    main()
