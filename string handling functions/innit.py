#__innit__ function is used to assign value to variables in this case f1 & f2
class fruit:
  def __init__(self, f1, f2):
    self.f1 = f1
    self.f2 = f2

p1 = fruit("apple", "banana")

print(p1.f1)
print(p1.f2)