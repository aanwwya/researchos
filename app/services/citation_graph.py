from collections import defaultdict


def build_citation_graph(papers):
    graph = defaultdict(list)

    for paper in papers:
        paper_id = paper.id.split("/")[-1]

        for referenced_work in paper.referenced_works:
            referenced_id = referenced_work.split("/")[-1]

            graph[paper_id].append(referenced_id)

    return dict(graph)


def build_reverse_citation_graph(graph):
    reverse_graph = defaultdict(list)

    for paper_id, references in graph.items():
        for referenced_id in references:
            reverse_graph[referenced_id].append(paper_id)

    return dict(reverse_graph)