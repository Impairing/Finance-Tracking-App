from information import *
print("Imported income.py")

class Salary:
    def __init__(self, salary):
        self.salary = salary
        
        
class Hourly():
    def __init__(self):
        self.hours = 0
        self.pay = 0
        self.totalIncome = 0
    def enterIncome(self):
        self.hours = int(input("Enter hours worked this week: "))
        self.pay = int(input("Enter hourly wage: "))
        self.totalIncome = self.pay * self.hours
    def displayIncome(self):
        print(f"You worked {self.hours} hours this week")
        print(f"Your hourly wage is ${self.pay} per hour")
        print(f"Your total income this week is ${self.totalIncome}")
    