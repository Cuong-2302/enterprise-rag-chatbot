from rank_bm25 import BM25Okapi

from app.ingest import (
    load_pdf,
    split_documents
)

from app.retriever import get_retriever


docs = None
bm25 = None


def initialize_bm25():

    global docs
    global bm25

    if docs is None:

        print("Loading PDF...")

        docs = split_documents(
            load_pdf()
        )

        print("Building BM25...")

        tokenized_docs = [
            doc.page_content.split()
            for doc in docs
        ]

        bm25 = BM25Okapi(
            tokenized_docs
        )

        print("BM25 Ready")


def hybrid_search(
    query,
    top_k=10
):

    initialize_bm25()

    retriever = get_retriever()

    dense_docs = retriever.invoke(
        query
    )

    scores = bm25.get_scores(
        query.split()
    )

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:top_k]

    sparse_docs = [
        docs[i]
        for i in ranked_indices
    ]

    merged = {}

    for doc in dense_docs + sparse_docs:

        merged[
            doc.page_content
        ] = doc

    return list(
        merged.values()
    )