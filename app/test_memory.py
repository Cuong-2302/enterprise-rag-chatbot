from app.memory import *

add_message(
    "user",
    "Hello"
)

add_message(
    "assistant",
    "Hi"
)

print(history_to_text())