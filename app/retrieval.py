from langchain_community.vectorstores import FAISS

from app.config import VECTOR_DB_DIR
from app.embeddings import get_embedding_model


def load_vector_store():

    embedding_model = get_embedding_model()

    db = FAISS.load_local(
        str(VECTOR_DB_DIR),
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return db


def similarity_search(
    query: str,
    k: int = 3
):
    db = load_vector_store()

    results = db.similarity_search(
        query,
        k=k
    )

    return results
