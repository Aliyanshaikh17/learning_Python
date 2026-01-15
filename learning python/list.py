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





#extend 2 list                                combine 2 list 
std1 = ["aditya","aman","kunal"]
std2 = [1,2,3,4]
std1.extend(std2)
print(std1)


#extand list with taple                         combine 2 tuple
std1 = ["aditya","aman","kunal"]
std2 = (1,2,3,4)
std1.extend(std2)
print(std1)


#extand list with set                          combine 2 set
std1 = ["aditya","aman","kunal"]
std2 = {1,2,3,4}
std1.extend(std2)
print(std1)


#extand list with dictionary                     combine 2 dictionary
std1 = ["aditya","aman","kunal"]                 #only keys are extand
std2 = {"x":10,"y":90}
std1.extend(std2)
print(std1)

#remove data from the list using revome method          1 remove the data    
name = ["kunal","aman","prashant"]                      #2 if there is same data in the
name.remove("kunal")                                   #list then tha first is remove
print(name)





#append method                                   enter data in list on end of list
a = [1,2,3,4,5,6,7]
a.append("the")
print(a)

#pop method
name = ["kunal","aman","prashant"]                  #if pop(1) then delete 2nd  =  pop(1)
name.pop()                                        #last name is delete = pop()
name.pop(1)                                 
print(name)


#del method (delete)
name = ["kunal","aman","prashant"]
del name[0]                       
print(name)

#clear
name = ["kunal","aman","prashant"]
name.clear()
print(name)


#Sort list
name = ["kunal","prashant","aman"] 
name.sort()
print(name)


#Sort by descending order
name = [100, 80,30,101, 8]
name.sort(reverse=True)
print(name)


#reverse the list
name = ["aman","prashant","z","y","A", "Z","C"]
name.reverse()
print(name)


#Join Two List
name1 = ["aman","prashant","z","y","A", "Z","C"]
name2 = [1,2,3,4,5]
addList = name1 + name2
print(addList)
