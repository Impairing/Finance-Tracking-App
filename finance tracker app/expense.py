from income import *
from information import *
print("Imported expense.py")


class Expense(Person):
    def __init__(self):
        self.good = ""
        self.price = 0
        self.date = ""
        self.numberOfItems = 0
        self.goods = {}
        self.allGoods = {}
    def inputPurchase(self):
        self.numberOfItems = str(len(self.goods) + 1)
        self.good = input("Name of good: ")
        self.price = input("Price of good: ")
        self.date = input("Date of purchase: ")
        self.goods[f"item{self.numberOfItems}"] = self.good, self.price, self.date
    def displayPurchase(self):
        print(f"You purchased {self.good} for ${self.price} on {self.date}")
        print(self.goods)
        print(self.goods[f"item{self.numberOfItems}"][0])
        print(self.goods[f"item{self.numberOfItems}"][1])
        print(self.goods[f"item{self.numberOfItems}"][2])
    def newCycle(self):
        for i in self.goods:
            self.allGoods[f"item{len(self.allGoods)+1}"] = self.goods[f"{i}"][0], self.goods[f"{i}"][1], self.goods[f"{i}"][2]
        self.goods = {}
        print(self.goods)
        print(self.allGoods)
    