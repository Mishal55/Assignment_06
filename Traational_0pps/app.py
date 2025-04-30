




#using self

from os import name
from typing import Counter, Self


class Student:
    def _init_(self,name,marks):
    #Self.name = name
    #Self.marks = marks

    #def display(self):
        print(f"Student Name: {self,name}")
        print(f"Marks: {self.marks}")

        student1 = Student ("Mishal",24)
        student1.display()

     #using CLS

    class  Counter:
        count = 0
        def __init__(self):
            Counter.count += 1

    @classmethod
    def display_counter(cls):
        print(f"My total created object are: {cls.count}")   

        obj1 = Counter()
        obj2 = Counter()
        obj3 = Counter()
        obj4 = Counter()

        Counter.display_counter()

        # public Variable and Method
        class Bank:
             
    # Class variable (shared by all instances)
           bank_name = "Meezan Bank"

    def __init__(self, account_holder):
        # Instance variable
        self.account_holder = account_holder

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    # Instance method to display account details
    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")


# Creating objects
        account1 = Bank("Usia")
        account2 = Bank("Abhia")

# Display initial bank info
        account1.display()
        account2.display()

# Changing the bank name using class method

        Bank.change_bank_name("HBL")


        account1.display()
        account2.display()

    


        # class Vaeiable and class Methods

class Bank:
            bank_name = "Default bank"

            def __init__(self, account_holder):
                self.account_holder = account_holder

                @classmethod
                def change_bank_name(cls,name):
                    cls.bank_name = name

                def display(self):
                    print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")

                    account1 =  Bank("Mishal")
                    account2 =  Bank("Nadeem")

                    account1 =  display()
                    account1 =  display()

                    Bank.change_bank_name("HBL")

                    account1.dispaly()
                    account2.dispaly()

           # Static variable and Static Method

            class MathUtils:
                def add(a,b):
                    return a+b
                
                
            result = MathUtils.add(10,5)
            print("Sum of my 2 numbers are :", result)

            # constraction and Destructors

            class Logger:
                def __init__(self):
                    print(" Message Before:Logger object created.")  

                def _del_(self): 
                   print(" Message After:Logger object destructor")   

            log = Logger ()
            del log


# The Super Function

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with the name: {self.name}")

class Teacher (Person):
    def __init__(self, name,subject):
        super().__init__(name) 
        self.subject = subject
        print(f"Teacher teach:  {self.subject}")

t = Teacher ("Mishal","GIAIC python Course")

#Abstract Classs and Method


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    
class Rectuangle(Shape):
        def _init_(self, length, width):
             self.length = length
             self.width = width

        def area(self):
             return self.length * self.width 
rect = Rectuangle(5,8)
print ("Area of Rectuanfle:",rect.area())

# Intense Method

class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed


    def bark(self):
        print(f"{self.name} is barking! Woof woof!")

# Creating objects of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "German Shepherd")

# Calling the bark method
dog1.bark()
dog2.bark()

# Class Method

# Defining the Book class
class Book:
    # Class variable to keep count of total books
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Call class method to increment book count
        Book.increment_book_count()

    # Class method to update total_books
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Creating book objects
book1 = Book("The Alchemist")
book2 = Book("1984")
book3 = Book("Harry Potter")

# Printing total number of books
print("Total books created:", Book.total_books)

# Static Method
# Defining the TemperatureConverter class
class TemperatureConverter:
    
    # Static method to convert Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Using the static method without creating an object
temp_celsius = 25
temp_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_celsius)

print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")

