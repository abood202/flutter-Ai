from github import Github
import os
g = Github(os.getenv("GITHUB_TOKEN"))
def search_repos(q="topic:flutter language:dart", per_page=30):
    res = g.search_repositories(query=q)
    for repo in res:
        yield {"id":repo.id, "url":repo.html_url, "name":repo.full_name, "stars":repo.stargazers_count, "description":repo.description, "source":"github"}
