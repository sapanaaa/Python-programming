# provides shorter syntax while creating new list based on values of existing list

fruits = ["apple", "banana","kiwi", "grape","melon", "orange"]
newlist= []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)  #prints items with letter a only 