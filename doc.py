#doc provides documentation on python functions, classes, modules, etc
def funct():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
  
    return None
 
print("Using __doc__:")
print(funct.__doc__)
 
print("Using help:")
help(funct)