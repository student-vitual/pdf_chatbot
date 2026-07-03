# 📄 PDF RAG Chatbot

A simple Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF using Google Gemini and FAISS.

## Features

- Load PDF documents
- Split documents into chunks
- Generate embeddings
- Store vectors in FAISS
- Retrieve relevant context
- Generate answers using Google Gemini
- FastAPI backend
- Streamlit frontend

## Technologies Used

- Python
- FastAPI
- Streamlit
- Google Gemini API
- LangChain
- Hugging Face Embeddings
- FAISS

## Run the backend

```bash
uvicorn dm:app --reload
```

## Run the frontend

```bash
streamlit run frontend.py
```

## Project Structure

```
chatbot/
│
├── chatbot.py
├── create_index.py
├── dm.py
├── frontend.py
├── pdf.py
├── rag.py
├── requirements.txt
└── README.md
```