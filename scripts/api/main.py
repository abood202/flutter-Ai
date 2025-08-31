from fastapi import FastAPI
from pydantic import BaseModel
from storage.chroma_store import client
app = FastAPI()

@app.get("/search")
def search(q: str, k:int=5):
    collection = client.get_collection("resources")
    res = collection.query(query_texts=[q], n_results=k)
    # عدّل شكل الإخراج حسب الحاجة
    return res
