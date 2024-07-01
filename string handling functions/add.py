#__add__ is used to add two objects and return a third object

class fruit:
    def __init__(self, f1):
        self.f1 = f1
    def __add__(self, f2):
        return fruit(self.f1 + f2.f1)    
obj1=fruit("apple")
obj2=fruit("orange")
obj3= obj1 + obj2
print(obj3.f1)
