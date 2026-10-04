import json
from pathlib import Path


GRAPH_PATH = Path("data/index/citation_graph.json")


def save_citation_graph(graph, reverse_graph):
    GRAPH_PATH.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "forward": graph,
        "reverse": reverse_graph,
    }

    GRAPH_PATH.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )


def load_citation_graph():
    data = json.loads(
        GRAPH_PATH.read_text(encoding="utf-8")
    )

    return data["forward"], data["reverse"]