'''
Definition:
A lambda function is a small anonymous function written using the lambda keyword.
'''


greeting = lambda: print("Hello")
greeting()


'''
 Lambda With Arguments
'''

greeting = lambda fname: print("My name is:-", fname)

greeting("Pawan")
greeting("Rohan")
greeting("Sham")



'''
Lambda With Return Value

Lambda automatically returns the expression result.
'''

square = lambda x: x * x
print(square(5))



'''
Lambda Inside Another Function
'''

def outer(x):
    return lambda y: x + y

result = outer(10)
print(result(5))



    
'''
Lambda With Conditional (if-else)
'''

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(10))
print(check(7))


