from pathlib import Path

from app.services.openalex import search_papers
from app.services.pdf_downloader import download_pdf
from app.services.pdf_reader import extract_text
from app.services.chunker import chunk_text
from app.services.index_builder import build_paper_index
from app.services.index_manager import save_index


DATA_DIR = Path("data/papers")


def ingest_papers(query: str, limit: int = 5):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    papers = search_papers(query, limit)

    all_chunks = []
    ingested_papers = []

    for paper in papers:
        if not paper.pdf_url:
            continue

        paper_id = paper.id.split("/")[-1]
        pdf_path = DATA_DIR / f"{paper_id}.pdf"

        try:
            downloaded = download_pdf(
                paper.pdf_url,
                str(pdf_path),
            )

            if not downloaded:
                continue

            text = extract_text(str(pdf_path))

            chunks = chunk_text(
                text,
                paper_id,
            )

            all_chunks.extend(chunks)
            ingested_papers.append(paper)

        except Exception as error:
            print(
                f"Failed to ingest {paper.title}: {error}"
            )

    if not all_chunks:
        return {
            "papers": [],
            "chunks": [],
            "index": None,
        }

    index = build_paper_index(all_chunks)

    save_index(
        index,
        all_chunks,
    )

    return {
        "papers": ingested_papers,
        "chunks": all_chunks,
        "index": index,
    }