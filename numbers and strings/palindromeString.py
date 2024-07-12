#to check whether a string is palindrome or not
def revString(st):
    rev=''
    for i in st:
     rev= i+ rev
    return rev
str= input(str("enter a string:"))
x=revString(str) #x holds the reversed string
if str==x:
   print("the string is palindrome")
else:
   print("the string is not palindrome")   
