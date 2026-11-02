while True: 
    print("======================")
    print("   EXPENSE TRACKER    ")
    print("======================")
    print("1. Add Expense \n2. View Expenses \n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        print("Add Expense Selected.")
    elif choice == "2":
        print("View Expense Selected.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid Input.")