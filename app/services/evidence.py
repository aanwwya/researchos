def build_evidence(results):
    evidence = []

    for result in results:
        evidence.append(
            {
                "paper_id": result["paper_id"],
                "chunk_id": result["chunk_id"],
                "distance": result["distance"],
                "text": result["text"],
            }
        )

    return evidence