#to split bill among friends


print(" input value for total number of friends: ")
total_friends= int(input())

print(" input value for total bill: ")
total_bill=float(input())

# calculate the tax amount
tax=0.2*total_bill
total_bill= tax+total_bill

# divide bill among friends
per_person=total_bill/total_friends

# print the split amount
print("per person split bill is:",per_person)