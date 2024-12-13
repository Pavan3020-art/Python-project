import argparse
from user import register_user, login_user
from transactions import manage_transactions
from reports import generate_reports
from budget import manage_budget
from database import initialize_database

def main():
    # Initialize the database
    initialize_database()
    
    parser = argparse.ArgumentParser(description="Personal Finance Manager")
    subparsers = parser.add_subparsers(dest="command")

    # User registration
    user_parser = subparsers.add_parser("register", help="Register a new user")
    user_parser.add_argument("--username", required=True, help="Username")
    user_parser.add_argument("--password", required=True, help="Password")

    # Login
    login_parser = subparsers.add_parser("login", help="Login as a user")
    login_parser.add_argument("--username", required=True, help="Username")
    login_parser.add_argument("--password", required=True, help="Password")

    # Manage transactions
    transaction_parser = subparsers.add_parser("transactions", help="Manage income and expenses")
    transaction_parser.add_argument("--username", required=True, help="Username")

    # Generate reports
    report_parser = subparsers.add_parser("reports", help="Generate financial reports")
    report_parser.add_argument("--username", required=True, help="Username")
    report_parser.add_argument("--type", required=True, choices=["monthly", "yearly"], help="Report type")

    # Manage budget
    budget_parser = subparsers.add_parser("budget", help="Manage budget settings")
    budget_parser.add_argument("--username", required=True, help="Username")

    args = parser.parse_args()
    if args.command == "register":
        register_user(args.username, args.password)
    elif args.command == "login":
        login_user(args.username, args.password)
    elif args.command == "transactions":
        manage_transactions(args.username)
    elif args.command == "reports":
        generate_reports(args.username, args.type)
    elif args.command == "budget":
        manage_budget(args.username)
    else:
        parser.print_help()

if _name_ == "_main_":
    main()