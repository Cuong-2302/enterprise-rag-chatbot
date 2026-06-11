print("TEST FILE STARTED")

from app.multi_query import (
    multi_query_search
)

docs = multi_query_search(
    "What projects did Cuong build?"
)

print(
    f"\nTotal Docs: {len(docs)}"
)

for i, doc in enumerate(docs):

    print("\n" + "=" * 50)
    print(f"Result {i+1}")

    print(
        doc.page_content[:400]
    )