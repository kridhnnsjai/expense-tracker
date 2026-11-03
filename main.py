import json
expenses = []
try:
    with open("expenses.json","r") as file:
        expenses = json.load(file)
except (FileNotFoundError,json.JSONDecodeError):
    expenses = []
def view_expenses():
    if not expenses:
        print("Expenses list is empty")
        return
    else:
        print("=======Your Expenses========")
        for exp in expenses:
            print(f"Expense: {exp['name']} \n Amount: {exp['amount']}")
def calculate_total():
    total = 0
    if not expenses:
        print("You haven't spent anything.")
        return
    else:
        for exp in expenses:
            total = total + exp["amount"]
        print("======================")
        print(f"Your Total Spending: {total}")
def add_expense():
    name = input("Enter expense name:").strip()
    if not name:
        print("Name can't be empty.")
        return
    else:
        try:
            amt = float(input("Enter your expense amount:"))
            if amt>0:
                expense = {
                    "name": name,
                    "amount": amt
                }
                expenses.append(expense)
                with open("expenses.json","w") as file:
                    json.dump(expenses,file,indent=4)
                print("Expense added successfully")
                print(f"Total Expenses: {len(expenses)}")
            else:
                print("Amount must be greater than zero!")
                return
        except ValueError:
            print("Please enter a valid number. ")
            return
def show_expense_count(expenses):
    print(f"You have {len(expenses)} expenses recorded.")
while True: 
    print("======================")
    print("   EXPENSE TRACKER    ")
    print("======================")
    print("1. Add Expense \n2. View Expenses \n3. View Total Spending \n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
       view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid Input.")