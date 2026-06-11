from app.query_rewriter import rewrite_query

history = """
User: Who is Cuong?
Assistant: Cuong is an AI Engineer.
"""

question = """
What projects did he build?
"""

result = rewrite_query(
    question,
    history
)

print(result)