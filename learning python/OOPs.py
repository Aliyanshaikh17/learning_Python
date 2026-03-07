'''
OOPs
what is OOPs :- to map with real world scenarios , we started using object in code.
               this is colled as oops 
'''


''' 
class
is the blueprint for creating object
'''

'''
Object
An object is an instance of a class.
'''


#ex :-
class student:
    name = "karan"

s1 = student()
print(s1.name)





class person:
    name = "prashant"
    post = "maneger"
    age = 25
    def info(self):
        print(f"{self.name} is a {self.post}")

a = person()
b = person()

a.name = "bhushan"
a.post = "hr"

a.info()
b.info()



# Class with Multiple Attributes
class person:
    name = "prashant"
    post = "manager"
    age = 25

    def info(self):
        print(f"{self.name} is a {self.post}")

a = person()
b = person()

a.name = "bhushan"
a.post = "HR"

a.info()
b.info()




#init Constructor
'''
Constructor
    - __init__ method runs automatically when object is created.
    - It is used to initialize object data.
'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student("rohit", 20)
s1.display()




'''Types of Variables'''

'''
Instance Variable
    - Defined inside constructor using self.
    - Different for each object.

Class Variable
    - Defined inside class but outside constructor.
    - Same for all objects.
'''


class College:
    college_name = "ABC College"   # Class Variable

    def __init__(self, name):
        self.name = name           # Instance Variable

s1 = College("Rahul")
s2 = College("Aman")

print(s1.name)
print(s2.name)
print(College.college_name)




'''Types of Methods'''

'''
1) Instance Method
    - Uses self
    - Works with object data

2) Class Method
    - Uses @classmethod
    - Uses cls parameter

3) Static Method
    - Uses @staticmethod
    - Does not use self or cls
'''

class Demo:

    def show(self):
        print("Instance Method")

    @classmethod
    def display(cls):
        print("Class Method")

    @staticmethod
    def greet():
        print("Static Method")

d = Demo()
d.show()
Demo.display()
Demo.greet()





'''Four Pillars of OOPs'''

#1 Encapsulation
'''
Encapsulation
    - Wrapping data and methods into a single unit (class).
    - Data hiding using private variables.
'''

class Bank:
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def show_balance(self):
        print("Balance:", self.__balance)

b = Bank(5000)
b.show_balance()




#2. Abstraction
'''
Abstraction
    - Hiding internal details and showing only important features.
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

c = Car()
c.start()



