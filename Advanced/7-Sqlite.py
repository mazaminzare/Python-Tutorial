import sqlite3


class SQLiteManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
        self.conn.commit()
        self.conn.close()
        return True  # Suppresses the exception if one occurred

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        ''')

    def insert_user(self, name, age):
        self.cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))

    def get_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def update_user(self, user_id, name, age):
        self.cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, user_id))

    def delete_user(self, user_id):
        self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))


# Usage example
with SQLiteManager('example.db') as db:
    db.create_table()
    db.insert_user('Alice', 25)
    db.insert_user('Bob', 30)
    print("Users after insertion:")
    print(db.get_users())

    db.update_user(1, 'Alice', 26)
    print("Users after update:")
    print(db.get_users())

    db.delete_user(2)
    print("Users after deletion:")
    print(db.get_users())
