'''
while loop

A while loop is a loop that keeps running until its condition becomes false.
When the condition becomes false, the loop stops.
'''


#example of while loop 

i = 1
while(i <= 10):
    print(i)
    i = i+ 1


# ex :- print numbers from 1 to 5

i = 1
while i <= 5:
    print(i)
    i = i + 1



# ex :- print even numbers from 1 to 10

i = 2
while i <= 10:
    print(i)
    i = i + 2



# ex :- sum of numbers from 1 to 10

i = 1
total = 0
while i <= 10:
    total = total + i
    i = i + 1

print("Sum =", total)



# while loop with user input

num = int(input("Enter a number :- "))
i = 1
while i <= num:
    print(i)
    i = i + 1



# Infinite while loop
# (runs forever if condition never becomes False)

'''
while True:
    print("Hello")
'''
