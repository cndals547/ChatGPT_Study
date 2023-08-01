import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

os.environ["SERPAPI_API_KEY"] = "6f4a909e5237d8770afc0095c48217f452df20a5ad2553798296c14406333d80"
os.environ["OPENAI_API_KEY"] = "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"

llm = OpenAI(temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("드라마 더 글로리 출연진이 누구야?")
