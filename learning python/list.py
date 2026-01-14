'''
list in python 
'''


name = ["kunal","pranv","prashant"]                 #list []


#use of list() constructor :-

extuple = (1,2,3,4,5,6)                                 #convert extuple into list
afterconvertion =list((extuple))


#accessing data of the list    :-              #ex :-   print the name "umesh"  or  print 2nd value of list

name = ["kunal","aman","prashant"]                     # acess data using index (name[1]) , (name[-1])
print(name[2])
print(name[-0])





#list slicing
b = [1,2,3,4,5,6,7]
print(b[0:4])
print(b[0:])
print(b[:4])

#membership oprator                           #check the data is in the list or nat
a = [1,2,3,4,5,6,7]
print(1 in a)


#change the list using index
a = [1,2,3,4,5,6,7]                         #change the list data using index funtion
a[5] = "shaikh"
print(a)


#change len with range                      #change data of a specific range 
a = [1,2,3,4,5,6,7]  
a[:3] = "shaikh","aliyan","19"
print(a)


#change the data using index method                       #index method
a = [1,2,3,4,5,6,7]
a.insert (4,"laptop")
print(a)



