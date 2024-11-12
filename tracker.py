from datetime import datetime

expenses = []

def add_expense():
    description = input("Enter description: ")
    category = input("Enter category (e.g., Food, Transport, Entertainment): ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    expenses.append({"description": description, "category": category, "amount": amount, "date": date})
    print("Expense added!")

def view_expenses():
    print("\nAll Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['description']} ({expense['category']}) - ${expense['amount']} on {expense['date']}")

def view_expenses_by_category():
    category = input("Enter category to filter by: ")
    print(f"\nExpenses in category '{category}':")
    filtered_expenses = [e for e in expenses if e["category"] == category]
    if filtered_expenses:
        for i, expense in enumerate(filtered_expenses, 1):
            print(f"{i}. {expense['description']} - ${expense['amount']} on {expense['date']}")
    else:
        print("No expenses found in this category.")

def calculate_total():
    total = sum(expense["amount"] for expense in expenses)
    print("Total Amount Spent: $", total)

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Expenses by Category")
    print("4. Calculate Total")
    print("5. Quit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        view_expenses_by_category()
    elif choice == '4':
        calculate_total()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
