import sqlite3
from contextlib import contextmanager


@contextmanager
def sqlite_manager(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        conn.commit()
        conn.close()


def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')


def insert_user(cursor, name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))


def get_users(cursor):
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()


def update_user(cursor, user_id, name, age):
    cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, user_id))


def delete_user(cursor, user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))


# Usage example
with sqlite_manager('example.db') as cursor:
    create_table(cursor)
    insert_user(cursor, 'Alice', 25)
    insert_user(cursor, 'Bob', 30)
    print("Users after insertion:")
    print(get_users(cursor))

    update_user(cursor, 1, 'Alice', 26)
    print("Users after update:")
    print(get_users(cursor))

    delete_user(cursor, 2)
    print("Users after deletion:")
    print(get_users(cursor))
