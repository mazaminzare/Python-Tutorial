from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Test the functionality
if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6)
    ]

    for shape in shapes:
        print(f"A {shape.__class__.__name__} with area: {shape.area()}")
