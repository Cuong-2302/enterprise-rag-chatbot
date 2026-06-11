from app.ingest import (
    load_pdf,
    split_documents
)

chunks = split_documents(
    load_pdf()
)


def get_parent_chunks(
    retrieved_docs
):

    parent_ids = set()

    for doc in retrieved_docs:

        parent_ids.add(
            doc.metadata.get(
                "parent_id"
            )
        )

    parent_docs = []

    for chunk in chunks:

        if (
            chunk.metadata.get(
                "parent_id"
            )
            in parent_ids
        ):

            parent_docs.append(
                chunk
            )

    return parent_docs