import feedparser, requests, hashlib, time
from tenacity import retry, wait_exponential, stop_after_attempt

FEED="https://pub.dev/feed.atom"
@retry(wait=wait_exponential(min=1, max=10), stop=stop_after_attempt(3))
def fetch_feed():
    d = feedparser.parse(FEED)
    for entry in d.entries:
        url = entry.link
        title = entry.title
        published = entry.published
        # تفريغ اسم الحزمة من الرابط
        pkg = url.rstrip('/').split('/')[-1]
        score = None
        try:
            r = requests.get(f"https://pub.dev/api/packages/{pkg}/score", timeout=15)
            if r.ok: score = r.json()
        except Exception:
            pass
        yield {"id": hashlib.sha256(url.encode()).hexdigest(), "url": url, "title": title, "published": published, "source":"pubdev", "pkg":pkg, "score":score}
        time.sleep(0.2)  # معدل مرن
