from fastapi import FastAPI
from pydantic import BaseModel

from chatbot import ask_question

app = FastAPI()


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "PDF RAG Chatbot Running"}


@app.post("/ask")
def ask(query: Query):

    answer = ask_question(query.question)

    return {
        "question": query.question,
        "answer": answer
    }