from dotenv import load_dotenv
from google import genai

import os

from rag import retrieve_context

load_dotenv()

client = genai.Client(
    api_key=os.getenv(GOOGLE_API_KEY)
)

question = "What is machine learning?"

context = retrieve_context(question)

prompt = f"""
Answer only from the context.

Context:
{context}

Question:
{question}

Answer:
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",contents=prompt)

print(response.text)