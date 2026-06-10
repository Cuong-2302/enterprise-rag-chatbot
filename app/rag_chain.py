from app.memory import (
    add_message,
    history_to_text
)

from app.query_rewriter import rewrite_query
from app.hybrid_retrieval import hybrid_search
from app.reranker import rerank_documents

from app.prompts import RAG_PROMPT

from app.llm import get_llm
from app.context_compressor import compress_context


llm = get_llm()


def ask_rag(question):

    history = history_to_text()

    rewritten_question = rewrite_query(
        question,
        history
    )

    docs = hybrid_search(
        rewritten_question
    )

    docs = rerank_documents(
        rewritten_question,
        docs,
        top_k=5
    )

    context = compress_context(
    docs,
    max_chars=3000

)

    prompt = RAG_PROMPT.format(
        context=context,
        question=rewritten_question
    )

    response = llm.invoke(
        prompt
    )

    answer = response.content

    add_message(
        "user",
        question
    )

    add_message(
        "assistant",
        answer
    )

    return {
        "answer": answer,
        "sources": docs
    }