from app.retriever import get_retriever
from app.reranker import rerank_documents

retriever = get_retriever()

docs = retriever.invoke(
    "What projects did Cuong build?"
)

reranked = rerank_documents(
    "What projects did Cuong build?",
    docs
)

for i, doc in enumerate(reranked):

    print("\n" + "="*50)

    print(f"Rank {i+1}")

    print(doc.page_content[:300])