#code 4 to reverse a string
def revString(st):
    rev=''
    for i in st:
     rev= i+ rev
    return rev
str= input(str("enter a string:"))
revString(str)
print(revString(str))