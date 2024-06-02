class Person:
    def __init__(self, name):
        print("Person Unit")
        self.__name = name

    def sayHello(self):
        return f"hello {self._Person__name} in Person class"


class User:
    def __init__(self, name):
        self.__name = name
        print("User Unit")

    def sayHello(self):
        return f"hello {self._User__name} in User class"

    def sayGoodbye(self):
        return f"goodbye {self._User__name}"


class Admin(Person, User):
    def __init__(self, name):
        print("Admin Unit")
        # super().__init__(name)
        User.__init__(self, name)
        Person.__init__(self, name)


person_1 = Admin("mohammad")

# __mro__
# mro()
# help(cls)

print(Admin.__mro__)
print(Admin.mro())
print(help(Admin))

# print(person_1.name)
# print(person_1.sayHello())
# print(person_1.sayGoodbye())
# print(person_1._Person__name)
# print(person_1._User__name)
# print(isinstance(person_1,Admin))
# print(isinstance(person_1,Person))
# print(isinstance(person_1,User))
