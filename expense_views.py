def view_expenses(expenses):
    if not expenses:
        print("Expenses list is empty")
        return
    else:
        print("=======Your Expenses========")
        for exp in expenses:
            print(f"Expense: {exp['name']} \n Amount: {exp['amount']}")
            
def calculate_total(expenses):
    total = 0
    if not expenses:
        print("You haven't spent anything.")
        return
    else:
        for exp in expenses:
            total = total + exp["amount"]
        print("======================")
        print(f"Your Total Spending: {total}")