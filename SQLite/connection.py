import sqlite3

def createTable():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create a table to store user credentials
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            hashed_password TEXT,
            salt TEXT
        )
    ''')
    conn.commit()
    conn.close()