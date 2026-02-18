'''
Funstions in python 
A function is a block of code which runs when we call that function by object.
'''

#How to create a function ?
def greeting():
    print("Hello rakesha")

# Declaring The Function.
def greeting():
    print("Hello Umesh")
greeting()




#Arguments Used In Functions.
'''Information can be passed to the function called arguments'''



def greeting(fname):
    print("My name is:-",fname)            # fname is the parameter
greeting("pawan")
greeting("rohan")
greeting("Sham")                           # sham is the argument



#types of arguments

# 1. Arbitrary Arguments (*args)

def my_function(*kids):
    print("Kids name are :- ",kids)
    print("Name of Second Kid :- ",kids[1])
my_function("Rahul","Tejas","Radha","Raju","Kaveri")



#2. Keyword Arguments (kwargs)
'''You can pass arguments using key = value syntax'''

def my_function(boy1, boy2, boy3):
    print("Name of First boy :- ",boy1)
    print("Name of Second boy :- ",boy2)
    print("Name of Third boy :- ",boy3)
my_function(boy3 = "Chetan", boy2 = "Rakesh", boy1 ="Kedar")




def details(**info):
    print(info)

details(name="Aliyan", age=20, city="Pune")



# 3. Arbitrary Keyword Arguments (**kwargs)
'''  If you dont know how many keyword arguments will be passed, use **kwargs '''

def StudentInfo(**kwargs):
    print("First name of student :- ",kwargs["firstName"])
    print("Middle name of student :- ",kwargs["middleName"])
    print("Last name of student :- ",kwargs["lastName"])
StudentInfo(firstName = "Chetan", middleName = "Uttam",lastName = "Khairnar")


#4. Default Parameter Value

def select(lang = "Python"):
    print("My favorite programming language is ",lang)
select("Java")
select("C")
select()
select("C++")
