from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent
from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()
search_tool=TavilySearchResults(search_depth="basic")
tools=[search_tool]

llm=ChatGoogleGenerativeAI(model='gemini-1.5-pro')
#verbose tells about what the agent is thinking
agent=initialize_agent(tools=tools,llm=llm,agent="zero-shot-react-description",verbose=True)
agent.invoke("give me a funny tweet about today's weather in Bangalore")
# agent.invoke("when was the last spaceX launch happened and  how many days ago from this instant?")



# result=llm.invoke("tell me about the tweet about chandigarh's temperature")
# print(result)