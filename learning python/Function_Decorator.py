'''
 Functions Decorator in Python
'''

'''
Definition :- 

A decorator is a function that modifies or extends the 
behavior of another function without changing its original code.
'''



#example of functions decorator

def my_decorator(func):
    def wrapper():
        print("Something before function")
        func()
        print("Something after function")
    return wrapper

def say_hello():
    print("Hello")
# Applying decorator manually
say_hello = my_decorator(say_hello)
say_hello()


