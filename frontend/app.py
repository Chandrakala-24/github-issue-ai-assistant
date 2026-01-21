import streamlit as st
import requests

st.set_page_config(page_title="AI GitHub Issue Assistant")

st.title("AI GitHub Issue Assistant")

repo_url = st.text_input("GitHub Repository URL")
issue_number = st.number_input("Issue Number", min_value=1, step=1)

if st.button("Analyze Issue"):
    if not repo_url:
        st.warning("Please enter a GitHub repository URL")
    else:
        with st.spinner("Analyzing issue..."):
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                params={
                    "repo_url": repo_url,
                    "issue_number": issue_number
                }
            )

            if response.status_code == 200:
                st.subheader("AI Analysis Result")
                try:
                    st.json(response.json())
                except Exception:
                    st.error("Invalid JSON returned from backend")
                    st.text(response.text)
            else:
                st.error(f"Backend error: {response.status_code}")
                st.text(response.text)
