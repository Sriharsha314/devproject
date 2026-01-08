# Expense Tracker System - Mini Project

expenses = []

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional): ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }
    expenses.append(expense)
    print("Expense added successfully.")

def view_expenses():
    if not expenses:
        print(" No expenses recorded.")
        return

    print("\n ALL EXPENSES")
    for e in expenses:
        print(f"{e['date']} | {e['category']} | ₹{e['amount']} | {e['note']}")

def total_expense():
    total = sum(e["amount"] for e in expenses)
    print(" Total Expense: ₹", total)

def category_summary():
    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    print("\n CATEGORY-WISE SUMMARY")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Exiting Expense Tracker.")
        break
    else:
        print(" Invalid choice.")
