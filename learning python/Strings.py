'''
string in python 
'''

#declarations of string 

name1 = "rahul"      #double quotation
name2 = 'shinde'     #single quotation


#Quotes inside quotes
sent1 = ('I want to learn "Python"')
print(sent1)

sent2 = ("I want to learn 'Python'")
print(sent2)



# triple quotes Multiline String
multistr = ''' i  am python ,
Created by Guido van Rossum,
Released in 1991 '''



#Find String Length    len()
name4 = "python"
print(len(name4))


#Check Is String Is Present Or Not
name3 = "Created"
txt = "rea"
print(txt in name3)
print(txt not in name3)


#Slicing Strings

name = "india"
print(name[0:4])       #first 4 print
print(name[0:])        #full string print
print(name[:4])       
print(name[0:4:2])
print(name[-6:-1])
print(name[::-1])      #reverse string
print(name.upper())    #upper case
print(name.lower())    #lower case

name5 = " HELLO india "
print(name5.strip())
print(name.replace("a", "A"))
print(name.split())

