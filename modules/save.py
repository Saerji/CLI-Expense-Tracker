import os
import json

def loadExpense(): #load expenses
    if os.path.exists("expense.json"):
        with open ("expense.json", "r") as file:
            return json.load(file)
    return {} #returns a list since we will store multiple dict entries and will also be used for indexing

def saveExpense(expense):
    with open("expense.json", "w") as file:
        json.dump(expense, file, indent=4)