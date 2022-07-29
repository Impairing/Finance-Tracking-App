from income import *
from information import *
print("Imported expense.py")


class Expense(Person):
    def __init__(self):
        self.good = ""
        self.price = 0
        self.date = ""
        self.numberOfItems = 0
        self.priceWeekly = 0
        self.allWeekly = {}
        self.goods = {}
        self.allGoods = {}
        
    def inputPurchase(self): #user puts in details of purchase/stores in dictionary for weekly purchases
        self.numberOfItems = str(len(self.goods) + 1)
        self.good = input("Name of good: ")
        self.price = input("Price of good: ")
        self.date = input("Date of purchase: ")
        self.goods[f"item{self.numberOfItems}"] = self.good, self.price, self.date
        
    def displayPurchase(self): #display items purchased during week and their details
        print(f"You purchased {self.good} for ${self.price} on {self.date}")
        print(self.goods)
        print(self.goods[f"item{self.numberOfItems}"][0])
        print(self.goods[f"item{self.numberOfItems}"][1])
        print(self.goods[f"item{self.numberOfItems}"][2])
        
    def spentWeekly(self): #flaws here, logs prices of purchases made in a week
        self.priceWeekly = 0
        for i in self.goods:
            self.priceWeekly = self.priceWeekly + int(self.goods[i][1])
        self.allWeekly[f"week{len(self.allWeekly)+1}"] = self.priceWeekly
        print(self.allWeekly)
        
    def newCycle(self): #resets purchased items in the week but keeps them in an archive for later use
        for i in self.goods:
            self.allGoods[f"item{len(self.allGoods)+1}"] = self.goods[f"{i}"][0], self.goods[f"{i}"][1], self.goods[f"{i}"][2]
        self.goods = {}
        print(self.goods)
        print(self.allGoods)
    