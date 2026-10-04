import faiss
import numpy as np


def build_index(vectors):
    vectors = np.asarray(vectors).astype("float32")

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)

    return index


def search_index(index, chunks, query_vector, top_k: int = 3):
    query_vector = np.asarray(query_vector).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []

    for distance, index_position in zip(distances[0], indices[0]):
        chunk = chunks[index_position]

        if hasattr(chunk, "id"):
            chunk_id = chunk.id
            paper_id = chunk.paper_id
            text = chunk.text
        else:
            chunk_id = chunk["id"]
            paper_id = chunk["paper_id"]
            text = chunk["text"]

        results.append({
            "paper_id": paper_id,
            "chunk_id": chunk_id,
            "text": text,
            "distance": float(distance),
        })

    return results