from expense_views import view_expenses,calculate_total
from expense_operations import add_expense
import json
expenses = []
try:
    with open("expenses.json","r") as file:
        expenses = json.load(file)
except (FileNotFoundError,json.JSONDecodeError):
    expenses = []

if __name__ == "__main__":
    while True: 
        print("======================")
        print("   EXPENSE TRACKER    ")
        print("======================")
        print("1. Add Expense \n2. View Expenses \n3. View Total Spending \n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid Input.")