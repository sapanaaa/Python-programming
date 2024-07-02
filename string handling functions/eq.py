#eq function returns true if two objects have same value
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other): #if we print john==jane without this function then output is false
        return self.age == other.age 
john = Person( 'jane', 25)
jane = Person( 'jane', 25)
print(john == jane)
   