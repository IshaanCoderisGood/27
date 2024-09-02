class Parrot:
  species="bird"
     
  def __init__(self,name,age):
    self.name=name
    self.age=age

Blu = Parrot('blu','4')
rio = Parrot('rio','900')

print("blu is"+Blu.species)
print("rio is"+rio.species)

print("blu is"+Blu.name)
print("rio is"+rio.name)


