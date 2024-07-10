#code 2 of reversing a number
x=int(input("enter a number:"))
rev=0
while x!=0:
    r=x%10
    rev=rev*10+r
    x=x//10
print("the reversed number is:", rev)    