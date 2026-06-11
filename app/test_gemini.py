# app/test_gemini.py

from app.llm import get_llm

llm = get_llm()

response = llm.invoke("Hello")

print(response.content)
