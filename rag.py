import faiss
import pickle
import numpy as np

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

index = faiss.read_index("pdf_index.faiss")

with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


def retrieve_context(query, k=3):

    query_embedding = np.array([embeddings.embed_query(query)]).astype("float32")

    distances, indices = index.search(query_embedding,k)

    context = ""

    for idx in indices[0]:
        context += chunks[idx].page_content
        context += "\n\n"

    return context