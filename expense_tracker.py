import csv
from datetime import datetime

FILE = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]


def create_file():
    try:
        with open(FILE, "x", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
        print("Expense file created successfully!")

    except FileExistsError:
        pass


create_file()

def add_expense():
    print("\n--- Add New Expense ---")

    # Get and validate date
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date! Please use YYYY-MM-DD format.")

    # Get category
    category = input("Enter category (Food/Travel/Study/Bills/Fun): ").strip()

    if not category:
        print("Category cannot be empty!")
        return

    # Get description
    description = input("Enter description: ").strip()

    if not description:
        print("Description cannot be empty!")
        return

    # Get and validate amount
    while True:
        try:
            amount = float(input("Enter amount (₹): "))

            if amount <= 0:
                print("Amount must be greater than zero!")
            else:
                break

        except ValueError:
            print("Please enter a valid number!")

    # Save expense
    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow(expense)

    print("\nExpense added successfully!")



def view_expenses():
    print("\n========== ALL EXPENSES ==========")

    with open(FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        expenses = list(reader)

    if not expenses:
        print("No expenses recorded yet!")
        return

    print("-" * 75)
    print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount (₹)':>15}")
    print("-" * 75)

    for expense in expenses:
        print(
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<25}"
            f"{float(expense['amount']):>15.2f}"
        )

    print("-" * 75)



def filter_expenses():
    print("\n========== FILTER EXPENSES ==========")
    print("1. Filter by Category")
    print("2. Filter by Month")

    choice = input("Enter your choice: ")

    with open(FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        expenses = list(reader)

    if not expenses:
        print("No expenses available!")
        return

    filtered = []

    if choice == "1":
        category = input("Enter category: ").strip().lower()

        filtered = [
            expense for expense in expenses
            if expense["category"].lower() == category
        ]

    elif choice == "2":
        month = input("Enter month (YYYY-MM): ").strip()

        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            print("Invalid month! Please use YYYY-MM format.")
            return

        filtered = [
            expense for expense in expenses
            if expense["date"].startswith(month)
        ]

    else:
        print("Invalid choice!")
        return

    if not filtered:
        print("No matching expenses found!")
        return

    print("\n---------- FILTERED EXPENSES ----------")
    print("-" * 75)
    print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount (₹)':>15}")
    print("-" * 75)

    for expense in filtered:
        print(
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<25}"
            f"{float(expense['amount']):>15.2f}"
        )

    print("-" * 75)


def expense_summary():
    print("\n========== EXPENSE SUMMARY ==========")

    with open(FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        expenses = list(reader)

    if not expenses:
        print("No expenses available!")
        return

    category_totals = {}
    grand_total = 0

    for expense in expenses:
        category = expense["category"].capitalize()
        amount = float(expense["amount"])

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

        grand_total += amount

    print("\n--- Spending by Category ---")

    for category, total in category_totals.items():
        print(f"{category:<15} ₹{total:.2f}")

    print("\n--------------------------------")
    print(f"Grand Total: ₹{grand_total:.2f}")

    biggest = max(expenses, key=lambda x: float(x["amount"]))

    print("\n--- Biggest Expense ---")
    print(f"Category: {biggest['category']}")
    print(f"Description: {biggest['description']}")
    print(f"Amount: ₹{float(biggest['amount']):.2f}")

    print("--------------------------------")

def main():
    while True:
        print("\n===================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("===================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Expense Summary")
        print("5. Quit")
        print("===================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            expense_summary()

        elif choice == "5":
            print("\nThank you for using Personal Expense Tracker!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please select between 1 and 5.")


main()