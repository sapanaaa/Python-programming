#code 6 of finding sum of digits in a number
def sumdigit(n):
    sum=0
    while n!=0:
      r=n%10
      sum=sum+r
      n=n//10
    return sum  
x=int(input("enter a number:"))
sum= sumdigit(x)
print("the sum of digits is:",sum )