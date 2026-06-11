from app.multi_query import generate_queries

question = "What projects has Cuong built?"

queries = generate_queries(question)

print("\nGenerated Queries:\n")

for i, q in enumerate(queries, 1):
    print(f"{i}. {q}")