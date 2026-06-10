from langchain_community.vectorstores import FAISS

from app.embeddings import get_embedding_model
from app.config import VECTOR_DB_DIR


def get_retriever():

    embedding_model = get_embedding_model()

    db = FAISS.load_local(
        str(VECTOR_DB_DIR),
        embedding_model,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k":3,
            "fetch_k":10
        }
    )

    return retriever