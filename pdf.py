import streamlit as st
import requests

st.set_page_config(page_title="PDF RAG Chatbot",page_icon="🤖",layout="wide")

st.title("🤖 PDF RAG Chatbot")

question = st.text_input("Ask a question about your PDF")

if st.button("Ask"):

    if question:

        response = requests.post("http://127.0.0.1:8001/ask",
            json={
                "question": question
            }
        )

        if response.status_code == 200:

            answer = response.json()["answer"]

            st.success(answer)

        else:

            st.error(response.text)