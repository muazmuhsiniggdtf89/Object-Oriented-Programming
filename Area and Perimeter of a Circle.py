import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (3.14 * self.radius ** 2)

    def perimeter(self):
        return (2 * 3.14 * self.radius)


# Example usage
radius = int(input("Enter the radius of the circle (integer): "))
circle = Circle(radius)

print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())
