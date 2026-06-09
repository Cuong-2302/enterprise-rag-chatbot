from langchain_community.vectorstores import FAISS

from app.embeddings import get_embedding_model
from app.config import VECTOR_DB_DIR


def create_vector_store(chunks):

    embedding_model = get_embedding_model()

    vector_store = FAISS.from_documents(
        chunks,
        embedding_model
    )

    return vector_store


def save_vector_store(vector_store):

    vector_store.save_local(
        str(VECTOR_DB_DIR)
    )