# app/memory.py

MAX_HISTORY = 10

chat_history = []


def add_message(role, content):

    chat_history.append(
        {
            "role": role,
            "content": content
        }
    )

    if len(chat_history) > MAX_HISTORY:
        chat_history.pop(0)


def get_history():

    return chat_history


def clear_history():

    chat_history.clear()


def history_to_text():

    history = chat_history[-6:]

    text = ""

    for item in history:

        text += (
            f"{item['role']}: "
            f"{item['content']}\n"
        )

    return text