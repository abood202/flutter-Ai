from google.cloud import firestore
db = firestore.Client()
def save_doc(doc):
    # doc هو dict الذي يحتوي الحقول الموضوعة سابقاً
    db.collection("resources").document(doc["id"]).set(doc)
