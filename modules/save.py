import os
import json

def loadExpense():
    if os.path.exists("expense.json"):
        with open ("expense.json", "r") as file:
            return json.load(file)
    return {}

def saveExpense(expense):
    with open("expense.json", "w") as file:
        json.dump(expense, file, indent=4)