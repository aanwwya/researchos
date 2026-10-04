from dataclasses import dataclass


@dataclass
class Chunk:
    id: str
    paper_id: str
    text: str