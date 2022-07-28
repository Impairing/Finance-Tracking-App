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
        self.weeklyIncome = 0
    def wk1enterIncome(self):
        self.hours = int(input("Enter hours worked this week: "))
        self.pay = int(input("Enter hourly wage: "))
        self.weeklyIncome = self.pay * self.hours
        self.totalIncome = self.weeklyIncome
    def wk2enterIncome(self):
        self.hours = int(input("Enter hours worked next week: "))
        self.totalIncome = self.weeklyIncome + self.pay * self.hours
    def displayIncome(self):
        print(f"You worked {self.hours} hours")
        print(f"Your hourly wage is ${self.pay} per hour")
        print(f"Your next paycheck will be ${self.totalIncome}")
    