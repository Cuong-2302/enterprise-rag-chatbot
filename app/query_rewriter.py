# app/query_rewriter.py

from app.llm import get_llm

llm = get_llm()


def rewrite_query(
    question,
    history
):

    prompt = f"""
Conversation:

{history}

Rewrite the user question into
a standalone search query.

Question:
{question}

Standalone Query:
"""

    response = llm.invoke(prompt)

    return response.content