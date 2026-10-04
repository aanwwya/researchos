from fastapi import FastAPI

from app.services.openalex import search_papers


app = FastAPI()


@app.get("/")
def home():
    return {"message": "ResearchOS is running"}


@app.get("/papers/search")
def search(query: str, limit: int = 10):
    return {
        "query": query,
        "papers": search_papers(query, limit),
    }