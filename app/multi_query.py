# app/multi_query.py

from app.llm import get_llm

llm = get_llm()


def generate_queries(query):

    prompt = f"""
Generate 4 different search queries.

Question:
{query}

Queries:
"""

    response = llm.invoke(prompt)

    queries = response.content.split("\n")

    return [
        q.strip("- ").strip()
        for q in queries
        if q.strip()
    ]