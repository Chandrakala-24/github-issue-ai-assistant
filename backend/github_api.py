import requests

def fetch_issue(repo_url, issue_number):
    # Extract owner and repo
    parts = repo_url.replace("https://github.com/", "").split("/")
    owner, repo = parts[0], parts[1]

    issue_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    response = requests.get(issue_url)

    if response.status_code != 200:
        raise Exception("Failed to fetch issue from GitHub")

    issue_data = response.json()

    # Fetch comments
    comments = []
    if issue_data.get("comments", 0) > 0:
        comments_response = requests.get(issue_data["comments_url"])
        if comments_response.status_code == 200:
            comments = [c["body"] for c in comments_response.json()]

    return {
        "title": issue_data.get("title", ""),
        "body": issue_data.get("body", ""),
        "comments": comments
    }
