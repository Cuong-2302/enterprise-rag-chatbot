from app.retrieval import similarity_search


query = "What AI projects has Cuong worked on?"

results = similarity_search(
    query=query,
    k=3
)

for i, doc in enumerate(results):

    print("\n" + "=" * 60)

    print(f"Result {i+1}")

    print(doc.page_content)

    print(doc.metadata)