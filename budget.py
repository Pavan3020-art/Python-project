import sqlite3
from database import DB_NAME

def manage_budget(username):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Get user_id
    user_id = get_user_id(username, connection)
    if not user_id:
        print("User not found!")
        return

    print("\n1. Set Budget")
    print("2. View Budget")
    print("3. Check Budget Status")
    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category: ")
        limit = float(input("Enter budget limit: "))

        cursor.execute("""
        INSERT INTO budgets (user_id, category, limit)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id, category) DO UPDATE SET limit = excluded.limit
        """, (user_id, category, limit))
        connection.commit()
        print(f"Budget for '{category}' set to {limit} successfully!")

    elif choice == "2":
        cursor.execute("SELECT category, limit FROM budgets WHERE user_id = ?", (user_id,))
        budgets = cursor.fetchall()
        print("\nYour Budgets:")
        for category, limit in budgets:
            print(f"{category}: {limit:.2f}")

    elif choice == "3":
        category = input("Enter category to check: ")
        cursor.execute("""
        SELECT b.limit, IFNULL(SUM(t.amount), 0)
        FROM budgets b
        LEFT JOIN transactions t
        ON b.category = t.category AND b.user_id = t.user_id AND t.type = 'expense'
        WHERE b.user_id = ? AND b.category = ?
        """, (user_id, category))
        budget = cursor.fetchone()

        if budget:
            limit, total_spent = budget
            remaining = limit - total_spent
            print(f"\nCategory: {category}")
            print(f"Budget Limit: {limit:.2f}")
            print(f"Total Spent: {total_spent:.2f}")
            print(f"Remaining: {remaining:.2f}")
            if remaining < 0:
                print("Warning: You have exceeded your budget!")
        else:
            print("No budget set for this category.")

    connection.close()

def get_user_id(username, connection):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    return user[0] if user else None