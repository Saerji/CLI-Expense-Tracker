from modules.save import saveExpense, loadExpense

def view():
    expenses = loadExpense()

    for key, value in expenses.items():#prints the whole expense summary, in order to display index for indication on what expense to update
        for i, val in enumerate(value, start=1):
            print(f"----- Expense #{i} -----")
            print(f"Expense Description: {val['description']}")
            print(f"Amount: {val['amount']}")
            print(f"Time Added: {val['time']}")
            