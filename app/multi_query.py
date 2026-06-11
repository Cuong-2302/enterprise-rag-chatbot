from app.hybrid_retrieval import hybrid_search

from app.query_generator import (
    generate_search_queries
)


def multi_query_search(
    question,
    top_k=10
):

    queries = generate_search_queries(
        question
    )

    print("\nGenerated Queries:")
    print(queries)

    all_docs = []

    for query in queries:

        docs = hybrid_search(
            query,
            top_k=top_k
        )

        all_docs.extend(docs)

    unique_docs = {}

    for doc in all_docs:

        unique_docs[
            doc.page_content
        ] = doc

    return list(
        unique_docs.values()
    )