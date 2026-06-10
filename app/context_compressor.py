# app/context_compressor.py

def compress_context(
    docs,
    max_chars=3000
):

    context = ""

    for doc in docs:

        text = doc.page_content

        if len(context) + len(text) > max_chars:
            break

        context += text + "\n\n"

    return context