from dataclasses import dataclass


@dataclass
class Paper:
    id: str
    title: str
    doi: str | None
    publication_year: int | None
    type: str | None
    cited_by_count: int
    abstract: str | None
    is_open_access: bool
    pdf_url: str | None
    landing_page_url: str | None
    referenced_works: list[str]