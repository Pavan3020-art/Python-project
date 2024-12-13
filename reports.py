import sqlite3
from database import DB_NAME

def generate_reports(username, report_type):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Get user_id
    user_id = get_user_id(username, connection)
    if not user_id:
        print("User not found!")
        return

    if report_type == "monthly":
        month = input("Enter month (MM): ")
        year = input("Enter year (YYYY): ")

        cursor.execute("""
        SELECT category, type, SUM(amount) 
        FROM transactions 
        WHERE user_id = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
        GROUP BY category, type
        """, (user_id, month, year))
    elif report_type == "yearly":
        year = input("Enter year (YYYY): ")

        cursor.execute("""
        SELECT category, type, SUM(amount) 
        FROM transactions 
        WHERE user_id = ? AND strftime('%Y', date) = ?
        GROUP BY category, type
        """, (user_id, year))

    report = cursor.fetchall()
    total_income, total_expense = 0, 0

    print("\nFinancial Report:")
    print(f"{'Category':<20}{'Type':<10}{'Amount':<10}")
    print("-" * 40)
    for row in report:
        category, type_, amount = row
        print(f"{category:<20}{type_:<10}{amount:<10.2f}")
        if type_ == "income":
            total_income += amount
        elif type_ == "expense":
            total_expense += amount

    savings = total_income - total_expense
    print("\nSummary:")
    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expense: {total_expense:.2f}")
    print(f"Savings: {savings:.2f}")

    connection.close()

def get_user_id(username, connection):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    return user[0] if user else None