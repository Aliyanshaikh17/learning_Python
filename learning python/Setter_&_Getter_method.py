
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

