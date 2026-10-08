from sentence_transformers import CrossEncoder


MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

model = CrossEncoder(MODEL_NAME)


def rerank(query: str, results: list[dict]) -> list[dict]:
    if not results:
        return []

    pairs = [
        (query, result["text"])
        for result in results
    ]

    scores = model.predict(pairs)

    reranked_results = []

    for result, score in zip(results, scores):
        reranked_results.append(
            {
                **result,
                "rerank_score": float(score),
            }
        )

    reranked_results.sort(
        key=lambda result: result["rerank_score"],
        reverse=True,
    )

    return reranked_results