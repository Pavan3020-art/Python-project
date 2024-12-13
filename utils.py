import datetime

def validate_date(date_str):
    """
    Validates a date string in the format YYYY-MM-DD.
    
    :param date_str: The date string to validate.
    :return: A datetime.date object if valid, otherwise None.
    """
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

def format_currency(amount):
    """
    Formats a numeric amount as currency.
    
    :param amount: The amount to format.
    :return: A string formatted as currency.
    """
    return f"${amount:,.2f}"

def confirm_action(prompt="Are you sure? (y/n): "):
    """
    Prompts the user for a confirmation.
    
    :param prompt: The confirmation message to display.
    :return: True if the user confirms, False otherwise.
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        else:
            print("Please enter 'y' or 'n'.")

def display_menu(options):
    """
    Displays a numbered menu and prompts the user to select an option.
    
    :param options: A list of menu options.
    :return: The selected option index (1-based).
    """
    print("\nMenu:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def handle_error(message):
    """
    Prints an error message in a standardized format.
    
    :param message: The error message to display.
    """
    print(f"Error: {message}")