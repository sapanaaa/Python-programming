'''
to display following pattern:
         *
        ***
       *****
      *******
     *********    
'''

for i in range(1, 6):
        # Print spaces
    for j in range(6 - i):
        print(" ", end="")
        
        # Print * for the current row
    for k in range(1, 2*i):
        print("*", end="")
    print()
   
