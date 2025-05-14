from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest",temperature=0)

def chat_session(session_id): 
    history=ChatMessageHistory(session_id='abhishek')
    memory=ConversationBufferMemory(memory_key='history',chat_memory=history,return_messages=True)
    prompt=ChatPromptTemplate.from_messages([
        ("system","You're a friendly assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human","{input}")
    ])
    chain=(
        {
            "input":lambda x:x["input"],
            "history":lambda _: memory.load_memory_variables({})["history"]
        }
        |prompt
        |llm
    )
    return chain,memory
 


def chatting(str:input):
  response=chain.invoke({'input':str})
  print(response.content)
  memory.save_context({"input": str}, {"output": response.content})
  
chain,memory=chat_session('abhishek')