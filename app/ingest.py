from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import PDF_FILE
from app.vector_store import (
    create_vector_store,
    save_vector_store
)
from app.metadata_filter import detect_section
import uuid



def load_pdf():

    print("Loading PDF Loader...")

    loader = PyPDFLoader(str(PDF_FILE))

    print("Reading PDF...")

    documents = loader.load()

    print("PDF Loaded")

    return documents



def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    all_chunks = []

    for page_doc in documents:

        page_chunks = splitter.split_documents(
            [page_doc]
        )

        parent_id = str(
            page_doc.metadata.get(
                "page",
                0
            )
        )

        for chunk in page_chunks:

            chunk.metadata["section"] = (
                detect_section(
                    chunk.page_content
                )
            )

            chunk.metadata["parent_id"] = (
                parent_id
            )

        all_chunks.extend(
            page_chunks
        )

    return all_chunks

if __name__ == "__main__":

    print("=" * 50)
    print("STEP 1: Loading PDF")
    print("=" * 50)

    docs = load_pdf()

    print(f"Pages Loaded: {len(docs)}")

    print("\nMetadata Example:")
    print(docs[0].metadata)

    print("\n" + "=" * 50)
    print("STEP 2: Chunking Documents")
    print("=" * 50)

    chunks = split_documents(docs)

    print(f"Total Chunks: {len(chunks)}")

    print("\nChunk Examples:")
    print("-" * 50)

    for i, chunk in enumerate(chunks[:3]):

        print(f"\nChunk {i}")
        print("Metadata:")
        print(chunk.metadata)

        print("\nContent:")
        print(chunk.page_content[:300])

        print("-" * 50)

    print("\n" + "=" * 50)
    print("STEP 3: Creating Vector Store")
    print("=" * 50)

    vector_store = create_vector_store(chunks)

    print("Vector Store Created")

    print("\n" + "=" * 50)
    print("STEP 4: Saving Vector Store")
    print("=" * 50)

    save_vector_store(vector_store)

    print("Vector DB Saved Successfully")

    print("\nDone!")