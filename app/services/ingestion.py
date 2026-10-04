from app.services.chunker import chunk_text
from app.services.embedder import embed_chunks
from app.services.index_builder import build_paper_index
from app.services.pdf_reader import extract_text


def ingest_pdf(pdf_path: str, paper_id: str):
    text = extract_text(pdf_path)

    chunks = chunk_text(
        text,
        paper_id,
    )

    index = build_paper_index(chunks)

    return index, chunks