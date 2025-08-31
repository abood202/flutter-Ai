import praw, os
r = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                user_agent="your_app/0.1")
def fetch_subreddit(sub="FlutterDev", limit=100):
    for post in r.subreddit(sub).new(limit=limit):
        yield {"id": post.id, "url": post.url, "title": post.title, "selftext": post.selftext, "created": post.created_utc, "source":"reddit"}
