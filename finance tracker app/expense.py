from income import *
from information import *
print("Imported expense.py")


class Expense(Person):
    def __init__(self):
        self.good = ""
        self.price = 0
        self.date = ""
        self.goods = []
        self.prices = []
        self.dates = []
    def inputPurchase(self):
        self.good = input("Name of good: ")
        self.goods.append(self.good)
        self.price = int(input("Price of good: "))
        self.prices.append(self.price)
        self.date = input("Date of purchase: ")
        self.dates.append(self.date)
    def displayPurchase(self):
        print(f"You purchased {self.good} for ${self.price} on {self.date}")
        print(self.goods)
        print(self.prices)
        print(self.dates)
        
        
    