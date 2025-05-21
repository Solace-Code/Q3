from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method with no implementation

# Subclass that implements the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage:
rect = Rectangle(5, 10)
print("Area of rectangle:", rect.area())
