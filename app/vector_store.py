from langchain_community.vectorstores import FAISS

from app.embeddings import get_embedding_model
from app.config import VECTOR_DB_DIR


def create_vector_store(chunks):

    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_store


def save_vector_store(vector_store):

    vector_store.save_local(
        str(VECTOR_DB_DIR)
    )


def load_vector_store():

    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        str(VECTOR_DB_DIR),
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store