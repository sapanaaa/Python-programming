#hash function returns hash value of an object
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
p1=person('sapana', 20)        
p2= person('misty', 2)
print(hash(p1))
print(hash(p2))