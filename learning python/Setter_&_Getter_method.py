
'''
Getter and Setter Method

Getter
    - A getter method is used to get (read) the value of a private variable.

Setter
    - A setter method is used to set (update) the value of a private variable.
'''


#Example of Getter Method
class Student:

    def __init__(self, name, marks):
        self.__marks = marks   # private variable
        self.name = name

    # Getter Method
    def get_marks(self):
        return self.__marks


s1 = Student("rohit", 85)

print(s1.get_marks())





#Example of Setter Method
class Student:

    def __init__(self, name, marks):
        self.__marks = marks
        self.name = name

    # Setter Method
    def set_marks(self, marks):
        self.__marks = marks


s1 = Student("rohit", 80)

s1.set_marks(95)

print(s1._Student__marks)



#Getter and Setter Together
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

s1 = Student("rohit", 70)

print(s1.get_marks())

s1.set_marks(90)

print(s1.get_marks())





#Using @property (Modern Getter & Setter)

class Student:

    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        self.__marks = value

s = Student(80)

print(s.marks)

s.marks = 95

print(s.marks)


