from fastapi import FastAPI, HTTPException
from backend.github_api import fetch_issue
from backend.llm_service import analyze_issue

app = FastAPI()

@app.post("/analyze")
def analyze(repo_url: str, issue_number: int):
    try:
        issue = fetch_issue(repo_url, issue_number)
        result = analyze_issue(issue)
        return result
    except Exception as e:
        print("BACKEND ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))
