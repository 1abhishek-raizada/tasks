"""
1. Ingest PDF file.
2. Extract text from the PDF file and split into small chunks.
3. Send the chunks to the embedding model.
4. Save the embeddings to a vector database.
5. Perform similarity search on the vector database to find similar documents.
6. Retrieve the similar documents and present them to the user.

"""
from langchain_community.document_loaders import UnstructuredPDFLoader,OnlinePDFLoader

doc_path="./data/BOI.pdf"
model="llama3.2"

#local pdf file upload

if doc_path:
    loader=UnstructuredPDFLoader(file_path=doc_path)
    data=loader.load()
    print("done loading....")
else:
    print("upload a pdf file")


#preview first page
content=data[0].page_content
print(content[:100])

#ending the ingestion of the PDF

from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Split and chunk

text_splitter=RecursiveCharacterTextSplitter(chunk_size=1200,chunk_overlap=300)
chunks=text_splitter.split_documents(data)

print("done splitting...")
# print(f"Number of chunks: {len(chunks)}")
# print(f"Example chunk: {chunks[0]}")

#ADD TO VECTOR DATABASE

import ollama
ollama.pull("nomic-embed-text")

vector_db=Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name="simple-rag",
)
print("done adding to vector database...")

#RETRIEVAL 
from langchain.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_ollama import ChatOllama

from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever

#setup the model to use

llm=ChatOllama(model=model)

#a simple technique to generate multiple questions from a single question and then retrieve documents
#based on those questions, getting the best of the both worlds.

QUERY_PROMPT=PromptTemplate(
    input_variables=['question'],
    template="""You are an AI language model assistant. Your task is to generate five different
    versions of the given user question to retrieve relevant documents from a vector database.
    By generating multiple perspectives on the user question, your goal is to help the user
    overcome some of the limitations of the distance-based similarity search. Provide these 
    alternative questions separated by newlines.
    Original question: {question} """,
)


retriever=MultiQueryRetriever.from_llm(
    vector_db.as_retriever(),llm,prompt=QUERY_PROMPT
)

#RAG prompt

template="""Answer the question based ONLY on the following context
{context}
Question: {question}
"""

prompt=ChatPromptTemplate.from_template(template)

chain=(
    {"context":retriever,"question":RunnablePassthrough()}
    | prompt
    | llm 
    | StrOutputParser()
)

# res=chain.invoke(input=("what is the docuement about?",))
# print(res)

# res=chain.invoke(input=("what are the main points as a business owner I should be aware of?",))
# print(res)
res=chain.invoke(input=("how to report BOI?",))
print(res)