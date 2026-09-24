from langchain_tavily import TavilySearch
from config import DEFAULT_MODEL, TAVITY
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv() 

web_search = TavilySearch(
    max_results=5,
    topic="general",
)
result = web_search.invoke({"query":"What is the latest news on AI?"})
print(result)

# @tool
# def web_search(query:str)->str:
#     """search the web for information"""
#     TavilySearch(
#         max_results=5,
#         topic="general",
#     )
# result = web_search.invoke("What is the latest news on AI?")
# print(result)