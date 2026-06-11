from app.embeddings import get_embedding_model

model = get_embedding_model()

vector = model.embed_query(
    "What is Artificial Intelligence?"
)

print(type(vector))

print(len(vector))

print(vector[:10])