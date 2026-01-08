'''
 Variables in python
'''

# Variables

# A variable is a container used to store data in memory.

# Python Naming Conventions

nameOfStudent = "aliyan"      #1. camel Case
NameOfStudent = "aliyan"      #2  pascal case
name_of_student = "aliyan"    #3  snake case


#variable decalration

num1, num2, num3 = 1,2,3
print(num1,num2,num3)


#types of variables

#1 Global Variables
a = 5
def add():
    b = 10
    print("Additions of a and b is :-",(a+b))
add()


#2 Global keyword
num1 = 5
def addition():
 global num2
 num2 = 10

addition()
print("addition of num1 and num2 :- ",num1 + num2)


#3 Local Variables
def greet():
 a= "Local" 
 print("Hello", a)
greet()


