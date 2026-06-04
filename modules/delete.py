from modules.save import saveExpense, loadExpense

def deleteExpense():
    expenses = loadExpense() # load the expense dict
    print("Expenses Available:")
    for key, value in expenses.items():#prints the whole expense summary, in order to display index for indication on what expense to update
        for i, val in enumerate(value, start=1):
            print(f"----- Expense #{i} -----")
            print(f"Expense Description: {val['description']}")
            print(f"Amount: {val['amount']}")
            print(f"Time Added: {val['time']}")
        
    
    while True: #error handling of value and range of the expense index to update, will not proceed when the input is not an integer or the input is outside the index range (negative or exceeds the index available)
        try:
            indexChoice = int(input("Enter the expense # of the expense you would like to delete: "))
            if indexChoice < 1 or indexChoice > len(expenses):
                print(f"Error. Please enter index ranging from 1 to {len(expenses)}.")
                continue
            else:
                break
        except ValueError:
            print("Please input a number.")
                
    del expenses[indexChoice - 1]
    saveExpense(expenses)
    print("The expense information is deleted successfully.")