from langchain_postgres import PGVector
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
embedding_function = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
)
vectorstore = PGVector(
    embeddings=embedding_function,
    collection_name=os.getenv("PGVECTOR_COLLECTION_NAME"),
    connection=os.getenv("PGVECTOR_DB_URL"),
)

def search_tool(query: str, k: int = 5) -> list:
    """Search for the most relevant documents in the vector store."""
    docs = vectorstore.similarity_search(query, k=k)
    data = '\n'.join([doc.page_content for doc in docs])
    return data
