from app.hybrid_retrieval import (
    hybrid_search
)

from app.parent_retriever import (
    get_parent_chunks
)

docs = hybrid_search(
    "Vietnamese chatbot"
)

print(
    f"Retrieved: {len(docs)}"
)

parent_docs = get_parent_chunks(
    docs
)

print(
    f"Parent Docs: {len(parent_docs)}"
)

for doc in parent_docs:

    print("\n")
    print(
        doc.page_content[:300]
    )