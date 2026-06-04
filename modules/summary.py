from modules.save import saveExpense, loadExpense
from datetime import datetime

def summary():
    expenses = loadExpense() #load the existing dict
    for key, value in expenses.items():#prints the whole expense summary, in order to display index for indication on what expense to update
        print(f"==================== {key} Expenses ====================")
        for i, val in enumerate(value, start=1):
            print(f"----- Expense #{i} -----")
            print(f"Expense Description: {val['description']}")
            print(f"Amount: {val['amount']}")
            print(f"Time Added: {val['time']}")