from sys import *


print("Imported contact.py")
class Person:
    def __init__(self, first, last, phone):
        self.first = first
        self.last = last
        self.phone = phone
    def get_full_name(self):
       return f"{self.first} {self.last}"
        
