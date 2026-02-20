'''what is recursion'''

'''  A recursive function is a function that 
calls itself and stops when a base condition is satisfied. '''


#Basic Example – Counting Numbers

# Recursion Example

def countDown(n):
    if n == 0:          # Base Condition (Stopping Condition)
        print("Done!")
    else:
        print(n)
        countDown(n-1)  # Function calling itself
countDown(5)





# Factorial Program using Recursion

def factorial(n):
    if n == 1:              # Base Condition
        return 1
    else:
        return n * factorial(n-1)   # Recursive Call

num = int(input("Enter the number :- "))
print("Factorial is :- ", factorial(num))




def sumOfNumbers(n):
    if n == 0:
        return 0
    else:
        return n + sumOfNumbers(n-1)

num = int(input("Enter the number :- "))
print("Sum is :- ", sumOfNumbers(num))
