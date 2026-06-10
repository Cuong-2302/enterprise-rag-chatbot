from app.hybrid_retrieval import hybrid_search

docs = hybrid_search(
    "What AI projects did Cuong build?"
)

for i, doc in enumerate(docs):

    print("\n" + "=" * 50)

    print(f"Result {i+1}")

    print(doc.page_content[:300])