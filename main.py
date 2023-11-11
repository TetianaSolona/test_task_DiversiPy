from shape import Square, Rectangle, Circle, Triangle

if __name__ == '__main__':
    shapes = [
        Square(1, 1, 1),
        Rectangle(1, 1, 2, 2),
        Circle(0, 0, 1),
        Triangle(0, 5, 0, 15, 10, 10)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__}: perimeter: {shape.perimeter()}, area: {shape.area()}")
