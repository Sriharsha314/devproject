# Expense Tracker System - Jenkins Compatible Version

expenses = []

def add_expense(date, category, amount, note=""):
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
        print("No expenses recorded.")
        return

    print("\nALL EXPENSES")
    for e in expenses:
        print(f"{e['date']} | {e['category']} | ₹{e['amount']} | {e['note']}")

def total_expense():
    total = sum(e["amount"] for e in expenses)
    print("\nTotal Expense: ₹", total)

def category_summary():
    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    print("\nCATEGORY-WISE SUMMARY")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")

# --------- AUTO EXECUTION FOR JENKINS ---------

print("===== EXPENSE TRACKER (JENKINS MODE) =====")

add_expense("10-01-2026", "Food", 250, "Lunch")
add_expense("11-01-2026", "Travel", 120, "Bus fare")
add_expense("12-01-2026", "Shopping", 500, "Groceries")

view_expenses()
total_expense()
category_summary()

print("\nExpense Tracker execution completed successfully.")
