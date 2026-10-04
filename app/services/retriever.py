from app.services.embedder import embed_query
from app.services.vector_store import search_index
from app.services.index_manager import load_index


def is_reference_heavy(text: str) -> bool:
    reference_markers = [
        "references",
        "authors' contributions",
        "all authors declare",
    ]

    text_lower = text.lower()

    marker_count = sum(
        marker in text_lower
        for marker in reference_markers
    )

    return marker_count >= 2


def retrieve(query: str, top_k: int = 3):
    index, chunks = load_index()

    query_vector = embed_query(query)

    candidate_count = min(
        top_k * 3,
        index.ntotal,
    )

    results = search_index(
        index,
        chunks,
        query_vector,
        candidate_count,
    )

    filtered_results = [
        result
        for result in results
        if not is_reference_heavy(result["text"])
    ]

    return filtered_results[:top_k]