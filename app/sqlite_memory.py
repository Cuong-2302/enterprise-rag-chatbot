import sqlite3

conn = sqlite3.connect(
    "memory.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(

    role TEXT,

    content TEXT
)
""")

conn.commit()


def add_message(
    role,
    content
):

    cursor.execute(
        """
        INSERT INTO messages
        VALUES (?,?)
        """,
        (
            role,
            content
        )
    )

    conn.commit()


def history_to_text():

    cursor.execute(
        """
        SELECT role, content
        FROM messages
        """
    )

    rows = cursor.fetchall()

    text = ""

    for role, content in rows:

        text += (
            f"{role}: "
            f"{content}\n"
        )

    return text
