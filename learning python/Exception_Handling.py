'''
Exception Handling
'''

'''
What is Exception Handling
    - Exception Handling is used to handle errors in a program.
    - It prevents the program from crashing.
    - It allows the program to continue running even after an error.
'''

'''
Why we need Exception Handling
    - To handle runtime errors.
    - To show proper error messages.
    - To make the program safe and user-friendly.
'''

'''
Common Errors in Python
    - ZeroDivisionError
    - ValueError
    - TypeError
    - NameError
    - IndexError
'''


#Example of Exception Handling
try:
    num = int(input("Enter a number:- "))
    print(10 / num)
except:
    print("Error occurred!")


