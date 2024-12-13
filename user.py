import sqlite3
from database import DB_NAME
from getpass import getpass

def register_user(username, password):
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connection.commit()
        print(f"User {username} registered successfully!")
    except sqlite3.IntegrityError:
        print(f"Username {username} already exists!")
    finally:
        connection.close()

def login_user(username, password):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        print(f"Welcome back, {username}!")
    else:
        print("Invalid username or password!")
    connection.close()