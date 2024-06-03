class PositiveInteger:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{self.name} must be a positive integer")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person:
    age = PositiveInteger("age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Test the functionality
if __name__ == "__main__":
    # Create a person with a valid age
    person = Person("Amin", 30)
    print(person.age)  # Output: 30

    # Set a valid age
    person.age = 40
    print(person.age)  # Output: 40

    # Attempt to set an invalid age
    try:
        person.age = -5
    except ValueError as e:
        print(e)  # Output: age must be a positive integer

    # Attempt to set a non-integer age
    try:
        person.age = "thirty"
    except ValueError as e:
        print(e)  # Output: age must be a positive integer
