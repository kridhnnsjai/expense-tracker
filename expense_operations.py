import json
def add_expense(expenses):
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