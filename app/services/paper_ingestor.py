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
    skipped_papers = []

    for paper in papers:
        paper_id = paper.id.split("/")[-1]

        if not paper.pdf_url:
            skipped_papers.append(
                {
                    "paper_id": paper_id,
                    "title": paper.title,
                    "reason": "no_pdf_url",
                }
            )
            continue

        pdf_path = DATA_DIR / f"{paper_id}.pdf"

        if pdf_path.exists():
            skipped_papers.append(
                {
                    "paper_id": paper_id,
                    "title": paper.title,
                    "reason": "already_ingested",
                }
            )
            continue

        try:
            downloaded = download_pdf(
                paper.pdf_url,
                str(pdf_path),
            )

            if not downloaded:
                skipped_papers.append(
                    {
                        "paper_id": paper_id,
                        "title": paper.title,
                        "reason": "downloaded_file_is_not_pdf",
                    }
                )
                continue

            text = extract_text(str(pdf_path))

            if not text.strip():
                skipped_papers.append(
                    {
                        "paper_id": paper_id,
                        "title": paper.title,
                        "reason": "pdf_has_no_extractable_text",
                    }
                )
                continue

            chunks = chunk_text(
                text,
                paper_id,
            )

            all_chunks.extend(chunks)
            ingested_papers.append(paper)

        except Exception as error:
            skipped_papers.append(
                {
                    "paper_id": paper_id,
                    "title": paper.title,
                    "reason": str(error),
                }
            )

    if not all_chunks:
        from app.services.index_manager import load_index

    try:
        index, chunks = load_index()
    except FileNotFoundError:
        index = None
        chunks = []

    return {
        "papers": [],
        "chunks": chunks,
        "index": index,
        "skipped_papers": skipped_papers,
    }