'''
Data Types in Python
(int, float, complex, boolean)
'''


# Integer (int)

a = 10                  # positive integer
b = -20                 # negative integer
c = 0                   # zero value
print(a, b, c)
print(type(a))

# user input (int)
num = int(input("Enter an integer value:- "))
print(num)



# Float (float)


x = 10.5                # decimal number
y = -3.14
z = 0.0
print(x, y, z)
print(type(x))

# user input (float)
price = float(input("Enter price:- "))
print(price)




# Complex (complex)


a = 3 + 4j              # complex number (real + imaginary)
b = complex(5, 2)       # using constructor
print(a)
print(b)
print(type(a))

# access real & imaginary part
print(a.real)           # real part
print(a.imag)           # imaginary part


# Type Conversion

a = 10
b = float(a)            # int to float
print(b)

x = 10.8
y = int(x)              # float to int
print(y)

print(bool(100))        # True
print(bool(0))          # False




# Summary

# int      -> whole numbers (10, -5, 0)
# float    -> decimal numbers (10.5, 3.14)
# complex  -> real + imaginary (2+3j)
# bool     -> True / False
