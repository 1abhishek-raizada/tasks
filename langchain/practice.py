from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI



llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest",temperature=0)
history=ChatMessageHistory()

memory=ConversationBufferMemory(memory_key='history',chat_memory=history,return_messages=True)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a friendly assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain=(
    {
        "input":lambda x:x["input"],
        "history":lambda _: memory.load_memory_variables({})["history"]
    }
    |prompt
    |llm
)
response=chain.invoke({'input':"hello my name is abhsihek"})
print(response.content)
memory.save_context({"input": "hello my name is abhishek"}, {"output": response.content})
