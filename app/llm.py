# from dotenv import load_dotenv
# import os

# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# def get_llm():

#     api_key = os.getenv("GEMINI_API_KEY")

#     print("KEY FOUND:", api_key is not None)

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-2.0-flash",
#         google_api_key=api_key,
#         temperature=0
#     )

#     return llm
from langchain_ollama import ChatOllama


def get_llm():

    llm = ChatOllama(
        model="qwen3:8b",
        temperature=0
    )

    return llm