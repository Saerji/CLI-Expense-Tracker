import argparse

from modules.save import saveExpense, loadExpense

from modules.add import addExpense
from modules.delete import deleteExpense
from modules.summary import summary
from modules.view import view
from modules.update import updateExpense

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
parser.add_argument("command", choices=["add", "update", "delete", "view", "summary"])
args = parser.parse_args()

match args.command:
    case 'add':
        addExpense()
    case 'view':
        view()
    case 'summary':
        summary()
    case 'delete':
        deleteExpense()
    case 'update':
        updateExpense()
    case _:
        parser.print_help()