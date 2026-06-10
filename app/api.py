from fastapi import FastAPI

from app.rag_chain import ask_rag

app = FastAPI()


@app.post("/chat")
def chat(request):

    return ask_rag(
        request["question"]
    )