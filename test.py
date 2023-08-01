import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

os.environ["SERPAPI_API_KEY"] = "APIKEY"
os.environ["OPENAI_API_KEY"] = "APIKEY"

llm = OpenAI(temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("드라마 더 글로리 출연진이 누구야?")
