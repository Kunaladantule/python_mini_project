expenses = []

def add_expense():

    date = input("Enter the date (DD/MM/YYYY):")
    category = input("Enter the category:")
    amount = float(input("Enter the amount:"))
    expenses.append({'date': date, 'category': category, 'amount': amount})

    print("Expense added successfully")


def view_Expenses():

    for expense in expenses:

        print(f"date: {expenses['date']}, category: {expense['category']}, Amount: {expense['amount']}")


def edit_expense():

    date_to_edit = input("Enter the date of the expense to edit: ")
    for i, expense in enumerate(expenses):
        if expense['date'] == date_to_edit:
            new_date = input("Enter the new date: ")
            new_category = input("Enter the new category: ")
            new_amount = float(input("Enter the new amount: "))
            expenses[i] = {'date': new_date, 'category': new_category, 'amount': new_amount}

            print("Expense edited successfully!")
            return
        
    print("Expense not found.")

def delete_expense():

    date_to_delete = input("Enter the date of the expense to delete: ")
    for i, expense in enumerate(expenses):
        if expense['date'] == date_to_delete:
            del expenses[i]

            print("Expense deleted successfully!")
            return
        
    print("Expense not found.")

def generate_report():
    total_spent = sum(expense['amount'] for expense in expenses)

    print(f"Total Spending: {total_spent}")


while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Generate Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        edit_expense()
    elif choice == '4':
        delete_expense()
    elif choice == '5':
        generate_report()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")