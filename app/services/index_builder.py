from app.services.embedder import embed_chunks
from app.services.vector_store import build_index


def build_paper_index(chunks):
    vectors = embed_chunks(chunks)

    return build_index(vectors)