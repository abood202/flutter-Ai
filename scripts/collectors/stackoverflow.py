import requests, time
API="https://api.stackexchange.com/2.3/questions"
KEY="YOUR_KEY"
def fetch_so(tag="flutter", fromdate=None):
    page=1
    while True:
        params={"order":"desc","sort":"creation","tagged":tag,"site":"stackoverflow","pagesize":100,"page":page,"key":KEY}
        if fromdate: params["fromdate"]=int(fromdate)
        r=requests.get(API, params=params, timeout=30)
        r.raise_for_status()
        data=r.json()
        for q in data.get("items",[]):
            yield {"id": q["question_id"], "url": q["link"], "title": q["title"], "source":"stackoverflow", "body": q.get("body",""), "tags": q.get("tags",[])}
        if not data.get("has_more"): break
        backoff=data.get("backoff")
        if backoff: time.sleep(backoff)
        page+=1
