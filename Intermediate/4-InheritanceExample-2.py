class Person: # father Class

    classAttribute="test value"
    def __init__(self, name, family, age):
        self.name=name
        self.family=family
        self.age=age

    def showFullName(self):   #Child class
        return f"{self.name} {self.family}"

    @classmethod
    def showClassAttribute(cls):
        return cls.classAttribute
class User(Person):
    pass

mohammad=Person("mohammad","zare",27)
sara=User("sara","amini",23)
print(mohammad.showFullName()) #father
print(sara.showFullName()) #child
print(User.classAttribute) #child
print(User.showClassAttribute())

