from fastapi import FastAPI

from app.services.openalex import search_papers
from app.services.researcher import research


app = FastAPI()


@app.get("/")
def home():
    return {"message": "researchos is running"}


@app.get("/papers/search")
def search(query: str, limit: int = 10):
    return {
        "query": query,
        "papers": search_papers(query, limit),
    }

@app.get("/research")
def run_research(query: str, top_k: int = 3):
    result = research(query, top_k)

    return result