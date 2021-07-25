class Dog :
    species = 'firstdog'

    def __init__(self,name,age):
        self.name= name
        self.age = age

print(Dog)
a = Dog('mikky','5')
print(a.name)