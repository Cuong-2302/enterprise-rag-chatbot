from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():

    model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={
            "device": "cuda"
        }
    )

    return model