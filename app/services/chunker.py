from app.models.chunk import Chunk


def chunk_text(
    text: str,
    paper_id: str,
    chunk_size: int = 1000,
    overlap: int = 200,
) -> list[Chunk]:
    words = text.split()

    chunks = []

    start = 0
    chunk_number = 0

    while start < len(words):
        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(
            Chunk(
                id=f"{paper_id}_chunk_{chunk_number}",
                paper_id=paper_id,
                text=chunk,
            )
        )

        chunk_number += 1
        start += chunk_size - overlap

    return chunks