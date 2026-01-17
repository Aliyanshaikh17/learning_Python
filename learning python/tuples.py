'''
Tuple in Python
'''

# Tuple is an ordered, immutable collection

data = ("aliyan", "19", "niphad", "bsc")
print(data)

# access tuple elements

print(data[0])        # access by index
print(data[-1])       # last element

print(len(data))      # for length
print(type(data))     # for checking type
print(tuple(data))    # convert collection to tuple




# tuple with single element (important)

single = ("python",)
print(single)
print(type(single))


# tuple allow duplicate values

data = ("python", "java", "python", "c")
print(data)





# tuple slicing

data = ("a", "b", "c", "d", "e")
print(data[1:4])
print(data[:3])
print(data[2:])





# tuple is immutable (cannot update directly)

data = ("aliyan", "19", "niphad", "bsc")
# data[1] = "20"      # Error (tuple cannot be changed)


# update tuple using list conversion

data = ("aliyan", "19", "niphad", "bsc")
temp = list(data)
temp.append("mvp")
data = tuple(temp)
print(data)
