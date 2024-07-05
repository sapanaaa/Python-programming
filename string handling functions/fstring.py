#fstring is used to format strings, quite similar to format()
name='sapana'
age=20
roll=39

# print("my name is " +name+ "i am"+ age +" years old" ) shows error
print("my name is " +name+ "i am"+ str(age) +" years old" ) #typecast method
print(f"my name is {name}i am {age} years old" ) #using fstring method