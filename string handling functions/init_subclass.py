#it is used to alter the behavior of subclasses which are inherited from superclass
class animal:
   def __init_subclass__(cls, **kwargs):
      super().__init_subclass__(**kwargs)
      if not hasattr(cls, 'species'):
         raise TypeError(f"{cls.__name__} must have a 'species' attribute")
   
class cat(animal): # a class cat is inherited from a class animal
   species = 'Feline' #an attribute called Feline is assigned to class cat

class dog(animal):
   species = 'Canine'

class fish(animal):  # This will raise a TypeError
   pass

