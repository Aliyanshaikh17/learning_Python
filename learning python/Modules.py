'''
Modules in python 
'''

'''
A module is a file that contains Python code (functions, variables, classes).
We can reuse this code in another file using the import keyword.
'''

#example of Modules
import math

print(math.sqrt(25))
print(math.pi)



#Import Specific Functions

'''
from module import function
    - Used to import specific functions from a module.
'''

from math import sqrt, pi

print(sqrt(25))
print(pi)




#Import with Alias

'''
alias
    - We can give a short name to a module using "as".
'''

import math as m

print(m.sqrt(36))
print(m.pi)



#Import All Functions
'''
from module import *
    - Imports all functions from the module.
'''

from math import *

print(sqrt(49))
print(pi)



#User Defined Module
'''
User Defined Module
    - We can create our own module.
    - Save functions in a Python file and import it.
'''

#Step 1: Create file my_module.py

def greet(name):
    print("Hello", name)

def add(a, b):
    print(a + b)




#Step 2: Use the module

#import my_module

#my_module.greet("rohit")
#my_module.add(5, 3)



# Built-in Modules Examples

'''
Some Built-in Modules

math        → Mathematical operations
random      → Generate random numbers
datetime    → Work with date and time
os          → Work with operating system
sys         → System related functions
'''


import random
print(random.randint(1, 10))


