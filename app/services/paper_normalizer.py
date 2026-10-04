from app.models.paper import Paper


def reconstruct_abstract(inverted_index: dict | None) -> str | None:
    if not inverted_index:
        return None

    words = []

    for word, positions in inverted_index.items():
        for position in positions:
            words.append((position, word))

    words.sort()

    return " ".join(word for _, word in words)


def normalize_paper(paper: dict) -> Paper:
    best_oa = paper.get("best_oa_location") or {}

    return Paper(
        id=paper.get("id"),
        title=paper.get("title"),
        doi=paper.get("doi"),
        publication_year=paper.get("publication_year"),
        type=paper.get("type"),
        cited_by_count=paper.get("cited_by_count", 0),
        abstract=reconstruct_abstract(
            paper.get("abstract_inverted_index")
        ),
        is_open_access=paper.get("open_access", {}).get("is_oa", False),
        pdf_url=best_oa.get("pdf_url"),
        landing_page_url=best_oa.get("landing_page_url"),
        referenced_works=paper.get("referenced_works", []),
    )