import chromadb
from chromadb.config import Settings
client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="/data/chroma"))
collection = client.get_or_create_collection("resources")
def save_embedding(id, embedding, metadata):
    collection.add(ids=[id], embeddings=[embedding], metadatas=[metadata], documents=[metadata.get("text","")])
