from app.llm import get_llm


def generate_search_queries(question):

    llm = get_llm()

    prompt = f"""
Generate 3 different search queries
for retrieving documents.

Question:
{question}

Return ONLY the queries.
One query per line.
"""

    response = llm.invoke(prompt)

    queries = [
        q.strip()
        for q in response.content.split("\n")
        if q.strip()
    ]

    return queries[:3]