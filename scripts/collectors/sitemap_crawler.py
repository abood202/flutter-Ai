import requests, xml.etree.ElementTree as ET, gzip, io
from tenacity import retry, wait_exponential, stop_after_attempt

def fetch_sitemap_urls(sitemap_url):
    r = requests.get(sitemap_url, timeout=30)
    content = r.content
    # بعض sitemaps قد تكون مضغوطة
    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        # try gz
        content = gzip.GzipFile(fileobj=io.BytesIO(content)).read()
        root = ET.fromstring(content)
    ns = {"sm":"http://www.sitemaps.org/schemas/sitemap/0.9"}
    for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        yield loc.text
