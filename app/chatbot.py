from app.rag_chain import ask_rag


while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    result = ask_rag(question)

    print("\nAnswer:")
    print(result["answer"])

    print("\nSources:")

    for i, doc in enumerate(result["sources"]):

        print("\n" + "=" * 50)

        print(f"Source {i+1}")

        print(doc.page_content[:200])