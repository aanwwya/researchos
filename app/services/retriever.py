from app.services.embedder import embed_query
from app.services.vector_store import search_index


def retrieve(chunks, index, query: str, top_k: int = 3):
    query_vector = embed_query(query)

    return search_index(
        index,
        chunks,
        query_vector,
        top_k,
    )