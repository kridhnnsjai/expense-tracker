import json
expenses = []
try:
    with open("expenses.json","r") as file:
        expenses = json.load(file)
except (FileNotFoundError,json.JSONDecodeError):
    expenses = []
while True: 
    print("======================")
    print("   EXPENSE TRACKER    ")
    print("======================")
    print("1. Add Expense \n2. View Expenses \n3. View Total Spending \n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter expense name:").strip()
        if not name:
            print("Name can't be empty.")
            continue
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
                    continue
            except ValueError:
                print("Please enter a valid number. ")
                continue
    elif choice == "2":
        if not expenses:
            print("Expenses list is empty")
            continue
        else:
            print("=======Your Expenses========")
            for exp in expenses:
                print(f"Expense: {exp['name']} \n Amount: {exp['amount']}")
    elif choice == "3":
        total = 0
        if not expenses:
            print("You haven't spent anything.")
            continue
        else:
            for exp in expenses:
                total = total + exp["amount"]
            print("======================")
            print(f"Your Total Spending: {total}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid Input.")