from modules.save import saveExpense, loadExpense
import modules.getMonth
from datetime import datetime

def addExpense():
    now = datetime.now() #get the time in runtime
    monthNow = now.strftime("%B %Y") #extract the month in datetime
    expenses = loadExpense() #load the entire file, if doesnt exist, make expenses a list instead
    
    desc = input("Add Expense Description: ")
    
    while True: #error handling, the input will not go through if it is not a float number
        try:
           amount = float(input("Add expense amount in peso: "))
           break
        except ValueError:
            print("Invalid amount, please input a number!")
            
    entry = {
            "description" : desc,
            "amount" : amount,
            "time" : now.strftime("%Y-%m-%d %I:%M %p")
            }
    
    if monthNow in expenses: #if the month alrdy exists, the new data will be instead be added in the dict with the month key
        expenses[monthNow].append(entry)
    else: #else, the system will make new dict with the month key
        expenses[monthNow] = [entry]
    
    print(f"Expense is added at {now.strftime("%Y-%m-%d %I:%M %p")}")
    saveExpense(expenses) #save the dict as json
