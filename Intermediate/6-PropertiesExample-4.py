class Person:

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self._age = age

    # first approach
    # if age >= 0:
    #     self._age = age
    # else:
    #     self._age = 0

    # second Approach
    # def get_age(self):
    #     return self._age
    #
    # def set_age(self, ageValue):
    #     if ageValue >= 0:
    #         self._age = ageValue
    #     else:
    #         raise ValueError("age can not be negetive")

    @property
    def age(self):  # getter function
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("value is not valid")

    @property
    def fullName(self):
        return f"{self.name} {self.family}"
    def showFullName(self):
        return f"{self.name} {self.family}"


me = Person('ali', 'milad', -23)
print(me.age)
me.age = 40
print(me.age)
print(me.showFullName())
print(me.fullName)
# me.set_age(15)
# print(me.get_age())
# print(me.set_age(-10))
# print(me.get_age())
