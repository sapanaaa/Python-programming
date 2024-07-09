#brief introduction to the concept of handling positional arguments
def volume(length, breadth, height):
    vol=length*breadth*height
    print(vol)
#volume(6,2,3)
volume(breadth=2, height=3, length=6) #unlike normal way the positions of arguments can be altered