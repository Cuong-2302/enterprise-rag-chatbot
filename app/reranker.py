from sentence_transformers import CrossEncoder

model = CrossEncoder(
    "BAAI/bge-reranker-base",
    device="cuda"
)


def rerank_documents(
    query,
    docs,
    top_k=5
):

    pairs = [
        [query, doc.page_content]
        for doc in docs
    ]

    scores = model.predict(pairs)

    ranked = sorted(
        zip(scores, docs),
        key=lambda x: x[0],
        reverse=True
    )

    return [
        doc
        for score, doc in ranked[:top_k]
    ]