from income import *
from information import *
from expense import *

#creating objects
person = Person()
expenses = Expense()
paycheck = Hourly()

#testing thing
def information():
    person.getInformation()
    person.displayInformation()
def purchase():
    expenses.inputPurchase()
    expenses.displayPurchase()
def paid():
    response = int(input("How often do you get paid?\nWeekly: 1\nBiWeekly: 2\n"))
    if response == 1:
        paycheck.wk1enterIncome()
        paycheck.displayIncome()
    elif response == 2:
        paycheck.wk1enterIncome()
        paycheck.wk2enterIncome()
        paycheck.displayIncome()
    else:
        print("Invalid input. Please try again.")
        paid()
def newCyclism():
    expenses.newCycle()


purchase()
purchase()
newCyclism()
purchase()
purchase()
newCyclism()







