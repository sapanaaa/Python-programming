#delattr function is used to delete an attribute from an object
class person :
    name= "sapana"
    age= 20

delattr(person, "age")# age attribute has been deleted so we don't get output when
# print(person.age) # we print it
print(person.name) #we get output for name only
