import httpx

from app.models.paper import Paper
from app.services.paper_normalizer import normalize_paper


BASE_URL = "https://api.openalex.org/works"


def search_papers(query: str, limit: int = 10) -> list[Paper]:
    params = {
        "search": query,
        "per-page": limit,
    }

    response = httpx.get(BASE_URL, params=params)
    response.raise_for_status()

    papers = response.json()["results"]

    return [normalize_paper(paper) for paper in papers]