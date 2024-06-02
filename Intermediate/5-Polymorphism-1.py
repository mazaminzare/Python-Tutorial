#
# # poly => multi
# #morph => form
#
class Animal: #Polymorphism
    def makeSound(self):
        raise NotImplementedError


class Dog(Animal):
    def makeSound(self):
        return "dog make sound"



class Cat(Animal):
    def makeSound(self):
        return "cat make sound"
class Worm(Animal):
    def makeSound(self):
        return f"worm make no sounds"
dog = Dog()
cat = Cat()
worm=Worm()
print(cat.makeSound())
print(dog.makeSound())
print(worm.makeSound())

# numbers=[1,2,3,4,5,6,6,7]
# myNumbs={1,2,3,4,5,6}
# person={"name":"sara","family":"milani"}
#
# numbers.copy()
# myNumbs.copy()
# person.copy()
#
# print(len(numbers))
# print(len(myNumbs))
