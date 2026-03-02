'''
OOPs
what is OOPs :- to map with real world scenarios , we started using object in code.
               this is colled as oops 
'''
















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