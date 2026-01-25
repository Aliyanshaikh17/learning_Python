'''
Operators in python
'''

# Arithmetic Operators
operator1 = 5
operator2 = 10
print(f"Addition of {operator1} and {operator2} is :- {operator1+operator2}")

num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the second number:- "))
print("Addition operators:- ",num1 + num2)
print("substaction operators:- ",num1 - num2)
print("Multiplication operators:- ",num1 * num2)
print("Division operators:- ",num1 / num2)
print("Exponrntion operators:- ",num1 ** num2)
print("Floor Division operators:- ",num1 // num2)




#assingment operator
num = int(input("Enter the number:- "))

print("Assignment (=) operator:- ", num)

num += 5
print("Add and assign (+=) operator:- ", num)

num -= 3
print("Subtract and assign (-=) operator:- ", num)

num *= 2
print("Multiply and assign (*=) operator:- ", num)

num /= 2
print("Division and assign (/=) operator:- ", num)

num //= 2
print("Floor division and assign (//=) operator:- ", num)

num %= 3
print("Modulus and assign (%=) operator:- ", num)

num **= 2
print("Exponent and assign (**=) operator:- ", num)




#comparison operators

num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the second number:- "))

print("Equal to (==) operator:- ", num1 == num2)
print("Not equal to (!=) operator:- ", num1 != num2)
print("Greater than (>) operator:- ", num1 > num2)
print("Less than (<) operator:- ", num1 < num2)
print("Greater than or equal to (>=) operator:- ", num1 >= num2)
print("Less than or equal to (<=) operator:- ", num1 <= num2)





#logical operator
num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the second number:- "))

print("Logical AND (and) operator:- ", num1 > 0 and num2 > 0)
print("Logical OR (or) operator:- ", num1 > 0 or num2 > 0)
print("Logical NOT (not) operator on num1:- ", not(num1 > 0))
print("Logical NOT (not) operator on num2:- ", not(num2 > 0))

