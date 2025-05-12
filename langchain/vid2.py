from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()
# tool3=TavilySearchResults()
# results=tool3.run("carry minati")
# print(results)

from langchain.agents import tool

@tool
def get_word_length(word:str) -> int:
    """Returns the length of a word"""
    return len(word)

results=get_word_length.invoke("abc")
print(results)