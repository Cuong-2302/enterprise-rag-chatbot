from langchain_community.vectorstores import FAISS

from app.embeddings import get_embedding_model
from app.config import VECTOR_DB_DIR

embedding_model = get_embedding_model()

db = FAISS.load_local(
    str(VECTOR_DB_DIR),
    embedding_model,
    allow_dangerous_deserialization=True
)

query = "What projects has Cuong built?"

results = db.similarity_search_with_score(
    query,
    k=5
)

for doc, score in results:

    print("=" * 50)
    print(score)
    print(doc.page_content[:300])