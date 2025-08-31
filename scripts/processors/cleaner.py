from bs4 import BeautifulSoup
import re
def html_to_text(html):
    soup = BeautifulSoup(html, "lxml")
    # ازالة سكربت/ستايل
    for s in soup(["script","style","noscript"]): s.extract()
    text = soup.get_text(separator="\n")
    # تبسيط المسافات
    text = re.sub(r'\n\s*\n+', '\n\n', text).strip()
    return text
