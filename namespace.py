globalVar=20
def outerFunct(): 
    outerVar=10
    def innerFunct(): 
        innerVar=30

        print(innerVar) #nested local namespace

    print(outerVar) #local namespace

    innerFunct() 
print(globalVar) #global namespace

outerFunct()