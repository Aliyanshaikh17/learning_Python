'''
OOPs
what is OOPs :- to map with real world scenarios , we started using object in code.
               this is colled as oops 
'''


''' 
class
is the blueprint for creating object
'''

'''
Object
An object is an instance of a class.
'''


#ex :-
class student:
    name = "karan"

s1 = student()
print(s1.name)





class person:
    name = "prashant"
    post = "maneger"
    age = 25
    def info(self):
        print(f"{self.name} is a {self.post}")

a = person()
b = person()

a.name = "bhushan"
a.post = "hr"

a.info()
b.info()



# Class with Multiple Attributes
class person:
    name = "prashant"
    post = "manager"
    age = 25

    def info(self):
        print(f"{self.name} is a {self.post}")

a = person()
b = person()

a.name = "bhushan"
a.post = "HR"

a.info()
b.info()




#init Constructor
'''
Constructor
    - __init__ method runs automatically when object is created.
    - It is used to initialize object data.
'''
