import json
from pathlib import Path

import faiss


INDEX_PATH = Path("data/index/faiss.index")
CHUNKS_PATH = Path("data/index/chunks.json")


def save_index(index, chunks):
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)

    faiss.write_index(index, str(INDEX_PATH))

    chunk_data = [
        {
            "id": chunk.id,
            "paper_id": chunk.paper_id,
            "text": chunk.text,
        }
        for chunk in chunks
    ]

    CHUNKS_PATH.write_text(
        json.dumps(chunk_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_index():
    index = faiss.read_index(str(INDEX_PATH))

    chunk_data = json.loads(
        CHUNKS_PATH.read_text(encoding="utf-8")
    )

    return index, chunk_data