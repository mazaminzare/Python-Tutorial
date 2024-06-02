class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    @property
    def fullName(self):
        return f"{self.name} {self.family}"
    # @fullName.setter
    # def fullName(self,fullName):
    #     pass

class User(Person):

    def __init__(self,name,family,email):
        super().__init__(name,family)
        # Person.__init__(self,name,family)
        self.email=email


mohammad=User("mohammad","zare","test@test.com")
print(mohammad.name)
print(mohammad.family)
print(mohammad.fullName)