from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")  # خفيف وسريع
def embed_text(text):
    return model.encode(text).tolist()  # قائمة أرقام
