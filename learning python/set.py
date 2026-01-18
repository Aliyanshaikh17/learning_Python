'''
set in python 
'''

intSet = {1, 2, 3, 4, 5, 5, True, False, 0}

print(intSet)
print("length of the set is :- ", len(intSet))

strSet = {"aman", "mustafa", "umesh"}
print(strSet)

boolSet = {True, False}
print(boolSet)

mixSet = {"umesh", 2, True, 5.9, 7+8j}
print(mixSet)

exTuple = (1, 2, 3, 4, 5) 
print("type of exTuple ", type(exTuple))
convertToSet = set(exTuple)
print("Converted set :-", convertToSet)
print("Type of convertToSet ", type(convertToSet))

