This project is a simple AI-powered tool that analyzes GitHub issues and provides a structured summary, classification, priority estimation, and suggested labels using a Large Language Model (LLM).
The goal of this project is to help developers quickly understand and triage GitHub issues.

Features
.Fetches GitHub issue details using repository URL and issue number
.Uses an AI model to:
  .Summarize the issue
  .Classify issue type (bug, feature request, documentation, etc.)
  .Estimate priority
  .Suggest labels
  .Describe potential impact
  .Clean JSON output
  .Simple web interface using Streamlit

  Setup & Run
  .Clone the repository
     git clone https://github.com/<your-username>/github-issue-ai-assistant.git
     cd github-issue-ai-assistant
  .Create virtual environment
     python -m venv venv
  .Activate it
    venv\Scripts\activate
  .Install dependencies
    pip install -r requirements.txt
  .Set environment variable
    GROQ_API_KEY=your_groq_api_key_here
  .Start the backend
    uvicorn backend.main:app --reload
  .Start the frontend (new terminal)
     streamlit run frontend/app.py



    
