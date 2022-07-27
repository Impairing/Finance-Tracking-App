from contact import *
print("Imported income.py")

class Salary:
    def __init__(self, salary):
        self.salary = salary
        
        
class Hourly(Person):
    def __init__(self, first, last, phone, wage, hours):
        super().__init__(first, last, phone)
        self.wage = wage
        self.hours = hours
        self.income = hours * wage
        
    def hourlyPay(self):
        print(f"{self.first}'s hourly pay is ${self.wage}/hr")
        
    def hoursWorked(self):
        print(f"{self.get_full_name()} is working {self.hours} hrs this week")
        
    def expectedIncome(self):
        print(f"{self.get_full_name()}'s expected income is ${self.income} this week.")