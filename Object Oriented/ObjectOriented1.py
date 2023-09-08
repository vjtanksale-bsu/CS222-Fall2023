class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


def print_area(shape):
    print(f"Area: {shape.area()}")


circle = Circle(5)
rectangle = Rectangle(4, 6)

print_area(circle)
print_area(rectangle)
