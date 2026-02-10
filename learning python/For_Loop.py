
'''
what is loops
    - A loop is used to run the same set of statements multiple times automatically.
'''


'''
1)  for loop
    - A for loop executes a block of code for each item in a sequence.
'''

#ex :-
# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Print even numbers
for i in range(2, 11, 2):
    print(i)

# Loop through string
name = "Python"
for ch in name:
    print(ch)



#for loop with user input

num = int(input("Enter a number:- "))
for i in range(1, num + 1):
    print(i)


#for loop with break
# - reak stops the loop immediately

for i in range(1, 11):
    if i == 5:
        break
    print(i)


# for loop with continue
# continue skips the current iteration


for i in range(1, 11):
    if i == 5:
        continue
    print(i)


