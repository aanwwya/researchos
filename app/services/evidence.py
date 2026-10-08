def build_evidence(results):
    evidence = []

    for result in results:
        evidence.append(
            {
                "paper_id": result["paper_id"],
                "chunk_id": result["chunk_id"],
                "rerank_score": result["rerank_score"],
                "text": result["text"],
            }
        )

    return evidence