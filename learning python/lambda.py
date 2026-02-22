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