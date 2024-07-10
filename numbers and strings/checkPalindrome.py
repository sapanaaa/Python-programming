#code 3 to check if the number is palindrome or not
#the logic here i used is checking if inputted number is equal to reversed number


def palindrome(x):
    rev=0
    while x!=0:
       r=x%10
       rev=rev*10+r
       x=x//10
    return rev
n=int(input("enter a number:"))  
rev=palindrome(n)  
print("the reversed number is:", rev)   
 
print(f"{rev}=={n}")  
if rev==n:
    print("the number is palindrome")
else:
    print("the number is not palindrome")  