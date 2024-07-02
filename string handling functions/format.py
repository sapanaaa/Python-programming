#formatting is done in following ways

f1= "my name is {name},i'm {age}".format(name="sapana",age=20)#using named indexes:

f2= "my name is {0}, i'm {1}, my roll number is {2}".format("sapana",36, 39)#using numbered indexes

f3= "my name is {}, i'm {}".format("sapana",36)#using empty placeholders:

print(f1)
print(f2)
print(f3)