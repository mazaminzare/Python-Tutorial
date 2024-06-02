class Person:
    def __init__(self, name, family, age, money):
        self.name = name
        self.age = age
        self.family = family
        self.money = money

    def __repr__(self):
        return f"{self.name} {self.family}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.money + other.money

    def __mul__(self, other):
        return self.money * self.money

    def __truediv__(self, other):
        return self.money / self.money


person_1 = Person('mohammad', 'ordukhani', 24, 1500)
person_2 = Person('amin', 'Zare', 24, 15744)
print(person_1)
print(len(person_1))

print(person_1 + person_2)
print(person_1 * person_2)
print(person_1 / person_2)
