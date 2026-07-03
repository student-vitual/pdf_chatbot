from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

import numpy as np
import faiss
import pickle

# Load PDF
loader = PyPDFLoader(r"C:\Users\Admin\Desktop\ai\ai_ml.pdf")
docs = loader.load()

print("Pages:", len(docs))

# Split PDF
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

print("Chunks:", len(chunks))

# Embedding Model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Convert chunks into vectors
texts = [chunk.page_content for chunk in chunks]

embedding_matrix = np.array(
    embeddings.embed_documents(texts)
).astype("float32")

print(embedding_matrix.shape)

# Create FAISS Index
dimension = embedding_matrix.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embedding_matrix)

print("Vectors:", index.ntotal)

# Save index
faiss.write_index(
    index,
    "pdf_index.faiss"
)

# Save chunks
with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("Saved Successfully")