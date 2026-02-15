'''
Funstions in python 
A function is a block of code which runs when we call that function by object.
'''

#How to create a function ?
def greeting():
    print("Hello rakesha")

# Declaring The Function.
def greeting():
    print("Hello Umesh")
greeting()




#Arguments Used In Functions.
'''Information can be passed to the function called arguments'''



def greeting(fname):
    print("My name is:-",fname)            # fname is the parameter
greeting("pawan")
greeting("rohan")
greeting("Sham")                           # sham is the argument



#types of arguments

# 1. Arbitrary Arguments (*args)

def my_function(*kids):
    print("Kids name are :- ",kids)
    print("Name of Second Kid :- ",kids[1])
my_function("Rahul","Tejas","Radha","Raju","Kaveri")

