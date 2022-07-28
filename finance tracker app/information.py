from sys import *


print("Imported information.py")
class Person:
    def __init__(self):
        self.first = ""
        self.last = ""
        self.phone = ""
    def getInformation(self):
        self.first = input("Enter first name: ")
        self.last = input("Enter last name: ")
        self.phone = input("Enter phone number: ")
    def displayInformation(self):
        print(f"Your first name is {self.first}")
        print(f"Your last name is {self.last}")
        print(f"Your full name is {self.first} {self.last}")
        print(f"Your phone number is {self.phone}")
        
