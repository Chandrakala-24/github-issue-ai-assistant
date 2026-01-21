import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_issue(issue):
    prompt = f"""
Analyze the following GitHub issue and return ONLY valid JSON.
DO NOT include explanations, markdown, or extra text.

Title: {issue['title']}
Body: {issue['body']}
Comments: {issue['comments']}

Return EXACT JSON in this format:
{{
  "summary": "",
  "type": "bug | feature_request | documentation | question | other",
  "priority_score": "1-5 with justification",
  "suggested_labels": [],
  "potential_impact": ""
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw_text = response.choices[0].message.content.strip()

    # 🔧 Extract JSON safely (CRITICAL FIX)
    match = re.search(r"\{[\s\S]*\}", raw_text)
    if not match:
        raise ValueError("LLM did not return JSON")

    return json.loads(match.group())
