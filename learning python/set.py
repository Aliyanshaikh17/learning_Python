'''
set in python 
'''

''' A set is a collection data type
Unordered   ( order in integer form )
Mutable
unchangeble
Does NOT allow duplicate values 
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


# for adding single element
intSet = {2, 3, 4, 5, True, False}
intSet.add(6)
print(intSet)

#for removeing
intSet = {2,3,4,5,5,True,False}
intSet.remove(5)
print(intSet)


#pass  argument 
def select(Organization):
    for x in Organization:

        print(x)

companyName = ["TCS","Tata Technologies","WIPRO","Infosys"]
select(companyName)

