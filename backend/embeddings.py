from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load lightweight embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def create_index(text_chunks):
    embeddings = model.encode(text_chunks)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return index, embeddings


def search(query, index, texts, k=3):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)

    results = [texts[i] for i in indices[0]]
    return results