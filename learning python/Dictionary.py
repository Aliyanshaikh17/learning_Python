'''
Dictionary in python 
'''

#Dictionary
''' are use to store data in key value pair
are ordered , changeble and not allow duplicate value 
 '''

data = {
    "name":"prashant",
    "RollNo":"19",
    "Address":"niphad",
    "clss":"bsc"
}
print(data)

#access only key value pair

print(data["name"])

print(len(data))          #for length
print(type(data))         #for cheking type
print(dict(data))         #for collection to dict 




#for updating dict

data = {
    "name":"prashant",
    "RollNo":"19",
    "Address":"niphad",
    "clss":"bsc"
}
data.update({"college":"mvp"})
print(data)




#for removeing
data = {
    "name": "prashant",
    "RollNo": "19",
    "Address": "niphad",
    "clss": "bsc"
}

data.pop("Address")   # remove specific key
# data.popitem()      # remove last item
# data.clear()        # remove all items


#del method
data = {
    "name":"prashant",
    "address":"Niphad",
    "college":"mvp"
    }
del data["address"]
print(data)


#for copy dictionary

data = {
    "name": "prashant",
    "RollNo": "19",
    "Address": "niphad",
    "clss": "bsc"
}
data1 = dict(data)
print(data1)
print(data)