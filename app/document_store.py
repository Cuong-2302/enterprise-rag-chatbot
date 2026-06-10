# app/document_store.py

from app.ingest import (
    load_pdf,
    split_documents
)

documents = split_documents(
    load_pdf()
)