import streamlit as st
#from pypdf import PdfReader
import ollama
from langchain_community.document_loaders import UnstructuredPDFLoader,OnlinePDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate,ChatPromptTemplate
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough,Runnable
from langchain_core.output_parsers import StrOutputParser







llm=ChatOllama(model="llama3.2")
ollama.pull("nomic-embed-text")

def load_process_pdf(doc_path):
    loader=UnstructuredPDFLoader(file_path=doc_path)
    data=loader.load()

    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1200,chunk_overlap=300)
    chunks=text_splitter.split_documents(data)
    return chunks

#function to initialize the vector database
def create_vector_db(chunks):
    #pulling the embedding model from ollama
    #creating the vector database
    vector_db=Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model="nomic-embed-text"),
        collection_name="simple-rag",
    )
    return vector_db

def create_retriever(vector_db):
    #setup the prompt template for multi-query retrieval
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
    return retriever

#Function to generate answers based on the RAG setup
def generate_answer(retriever,question):
    docs=retriever.invoke(input={"question":question})
    if not docs:
        return "Sorry, could not find the relevant documents for  your question"
    context="\n".join([doc.page_content for doc in docs])

    template="""Answer the question based ONLY on the following context 
    {context}
    Question: {question}
    """
    prompt=ChatPromptTemplate.from_template(template)

    input_data={
        "context":context,
        "question":question
    }


    chain=(
        RunnablePassthrough()
        | prompt
        | llm
        | StrOutputParser()
    )
    res= chain.invoke(input=input_data)
    if not res:
        return "sorry could not generate any answer"
    return res

#streamlit UI

st.title("RAG System - Document Question Answering")

#File Upload
uploaded_pdf=st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_pdf is not None:
    doc_path = './temp_uploaded_pdf.pdf'
    with open(doc_path, 'wb') as f:
        f.write(uploaded_pdf.getbuffer())

    #Display uploaded PDF
    st.write("Uploaded PDF successfully. Processing...")

    #Processing pdf and creating vector database
    chunks=load_process_pdf(doc_path)
    vector_db=create_vector_db(chunks)

    #create retriever
    retriever=create_retriever(vector_db)

    #asking the user for a question
    question=st.text_input("Ask a question about the document:")

    if question:
        #Generate the answer
        print("answer is being generated")
        answer=generate_answer(retriever,question)

        st.write(f"Answer: {answer}")