def ifPrime(num):
    for i in range(2,num):
        if num %i==0:
            return False
        else:
            return True

def printPrime(num2): 
    primeNum=[]
    for i in range(2,num2+1):
        if ifPrime(i) is True:
            primeNum.append(i)
    return primeNum        
x=int(input("enter a number:"))            
primeNum=printPrime(x)
print ("The prime numbers upto the entered number are: \n", primeNum)