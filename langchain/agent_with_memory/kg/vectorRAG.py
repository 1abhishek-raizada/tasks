
import ollama
from langchain_ollama import OllamaEmbeddings

from langchain_community.vectorstores import Neo4jVector
from dotenv import load_dotenv
import os

load_dotenv()
ollama.pull("nomic-embed-text")
def query_vector_rag(
    question: str,
    vector_index_name: str,
    vector_node_label: str,
    vector_source_property: str,
    vector_embedding_property: str,
    top_k: int = 3
):
    # initialize the Neo4j-backed vector store
    vector_store = Neo4jVector.from_existing_graph(
        embeddings=OllamaEmbeddings(model="nomic-embed-text"),
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
        index_name=vector_index_name,
        node_label=vector_node_label,
        text_node_properties=[vector_source_property],
        embedding_node_property=vector_embedding_property,
    )
    # directly run a similarity search with scores
    docs_and_scores = vector_store.similarity_search_with_score(
        question,
        k=top_k
    )

    return docs_and_scores