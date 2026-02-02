'''
Conditional Statements in python
'''

#if conditions  :-  
#The if statement checks a condition.
#If the condition is True, the code inside it runs.

#ex :-
num = 10
if num > 0:
    print("Number is positive")



#if-else Statement:-
'''It checks another condition only if the previous if condition is False.'''


#ex :-
num = -5
if num > 0:
    print("Positive number")
else:
    print("Negative number")



#ex :-
age = int(input("enter your age :- "))
if(age >= 18):
    print("you able to vote")
else:
    print("you not eble to vote")




#if-elif-else Statement
'''The else statement runs when all conditions above are False.'''

#ex :- 

a = -10
if a < 0:
    print( "number is negative" )
elif a > 0:
    print("number is positive")
else:
    print("number is zero")




marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")


#Nested if Statement

'''A nested if means an if statement inside another if statement.'''


#ex:- 
country = input("Enter the country name :- ")
age = int(input("Enter your name:- "))

if country == "india":
    if age >= 18:
        print("you are eligible for vote")
    else:
        print("you are not eligible for vote")
else:
    print("You are not eligible for vote")