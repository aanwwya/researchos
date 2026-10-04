import faiss
import numpy as np


def build_index(vectors):
    vectors = np.asarray(vectors).astype("float32")

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)

    return index


def search_index(index, query_vector, top_k: int = 3):
    query_vector = np.asarray(query_vector).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    return distances, indices