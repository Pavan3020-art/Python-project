import sqlite3
from database import DB_NAME

def manage_transactions(username):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    user_id = get_user_id(username, connection)
    if not user_id:
        print("User not found!")
        return

    print("1. Add Transaction")
    print("2. View Transactions")
    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category (e.g., Food, Rent): ")
        amount = float(input("Enter amount: "))
        type_ = input("Enter type (income/expense): ")
        date = input("Enter date (YYYY-MM-DD): ")

        cursor.execute("""
        INSERT INTO transactions (user_id, category, amount, type, date)
        VALUES (?, ?, ?, ?, ?)
        """, (user_id, category, amount, type_, date))
        connection.commit()
        print("Transaction added successfully!")

    elif choice == "2":
        cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
        transactions = cursor.fetchall()
        for transaction in transactions:
            print(transaction)

    connection.close()

def get_user_id(username, connection):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    return user[0] if user else None