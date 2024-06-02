class User:

    def __init__(self,name, family,age):
        self.name=name
        self.family=family
        self.age=age

    def __repr__(self):
        return f"{self.name} + {self.family} + {self.age}"

me= User("mohammad","ordukhani",20)
you = User("sara","zare",20)
print(me)
print(you)