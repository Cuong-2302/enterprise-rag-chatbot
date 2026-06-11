import time

from app.rag_chain import (
    ask_rag
)

QUESTIONS = [

    "Who is Cuong?",

    "What projects did he build?",

    "What is his GPA?",

    "What skills does he have?"
]

for q in QUESTIONS:

    start = time.time()

    result = ask_rag(q)

    latency = (
        time.time() - start
    )

    print()

    print("=" * 50)

    print("QUESTION:")
    print(q)

    print()

    print("ANSWER:")
    print(
        result["answer"]
    )

    print()

    print(
        f"Latency: {latency:.2f}s"
    )