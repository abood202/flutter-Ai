import hashlib
import requests
from collectors import pubdev, sitemap_crawler, stackoverflow, github, reddit
from processors.cleaner import html_to_text
from processors.embedder import embed_text
from storage.firestore_store import save_doc
from storage.chroma_store import save_embedding

def process_item(item):
    # item يحتوي مثلا url, title, source
    # 1. جلب html إن لزم
    html = requests.get(item["url"], timeout=20).text
    text = html_to_text(html)
    item["text"] = text[:5000]  # تقطيع لحجم مناسب
    # 2. fingerprint/dedup
    item["fingerprint"] = hashlib.sha256(item["text"].encode()).hexdigest()
    # 3. embedding
    emb = embed_text(item["text"])
    # 4. تخزين
    save_doc(item)
    save_embedding(item["id"], emb, {"title": item.get("title"), "url": item.get("url"), "source": item.get("source")})
