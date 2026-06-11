from app.sqlite_memory import (
    add_message,
    history_to_text
)

from app.query_rewriter import rewrite_query

from app.multi_query import (
    multi_query_search
)

from app.reranker import (
    rerank_documents
)

from app.context_compressor import (
    compress_context
)

from app.prompts import (
    RAG_PROMPT
)

from app.llm import get_llm


llm = get_llm()


def retrieve_documents(
    question,
    history
):

    rewritten_question = rewrite_query(
        question,
        history
    )

    docs = multi_query_search(
        rewritten_question
    )

    docs = rerank_documents(
        rewritten_question,
        docs,
        top_k=5
    )

    from app.parent_retriever import (
        get_parent_chunks
    )

    docs = get_parent_chunks(
        docs
    )

    return (
        rewritten_question,
        docs
    )


def build_context(
    docs
):

    context = compress_context(
        docs,
        max_chars=3000
    )

    return context


def generate_answer(
    context,
    question
):

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(
        prompt
    )

    return response.content


def ask_rag(question):

    print("\n" + "=" * 50)
    print("RAG PIPELINE")
    print("=" * 50)

    history = history_to_text()

    try:

        rewritten_question, docs = (
            retrieve_documents(
                question,
                history
            )
        )

        print(
            f"\nRewritten Query:\n{rewritten_question}"
        )

        print(
            f"\nRetrieved Docs: {len(docs)}"
        )

        context = build_context(
            docs
        )

        print(
            f"\nContext Length: {len(context)}"
        )

        answer = generate_answer(
            context,
            rewritten_question
        )

    except Exception as e:

        answer = (
            f"RAG Error: {str(e)}"
        )

        docs = []

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
        "sources": docs,
        "rewritten_query":
            rewritten_question
            if "rewritten_question"
            in locals()
            else question
    }