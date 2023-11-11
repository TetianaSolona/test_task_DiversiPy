import math
from abc import ABC, abstractmethod


class Shape(ABC):

    def validate_input(self, *args):
        if all(isinstance(coord, (int, float)) for coord in args):
            pass
        else:
            raise ValueError("Your input is not valid")

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Square(Shape):
    def __init__(self, top_right_x, top_right_y, side):
        self.validate_input(top_right_x, top_right_y, side)
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.side = side

    def validate_input(self, top_right_x, top_right_y, side):
        super().validate_input(top_right_x, top_right_y, side)
        if side == 0 or side < 0:
            raise ValueError("Side cannot be zero or negative")

    def calculate_perimeter(self):
        result = 4 * self.side
        return round(result, 2)

    def calculate_area(self):
        result = self.side * self.side
        return round(result, 2)


class Rectangle(Shape):
    def __init__(self, top_right_x, top_right_y, bottom_left_x, bottom_left_y):
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.bottom_left_x = bottom_left_x
        self.bottom_left_y = bottom_left_y
        self.height = abs(self.top_right_x - self.bottom_left_x)
        self.width = abs(self.top_right_y - self.bottom_left_y)
        self.validate_input(top_right_x, top_right_y, bottom_left_x, bottom_left_y)

    def validate_input(self, top_right_x, top_right_y, bottom_left_x, bottom_left_y):
        super().validate_input(top_right_x, top_right_y, bottom_left_x, bottom_left_y)
        if self.height == 0 and self.width == 0:
            raise ValueError("Both height and width should not be zero")

    def calculate_perimeter(self):
        result = 2 * (self.height + self.width)
        return round(result, 2)

    def calculate_area(self):
        result = self.height * self.width
        return round(result, 2)


class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        self.validate_input(center_x, center_y, radius)

        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def validate_input(self, center_x, center_y, radius):
        super().validate_input(center_x, center_y, radius)
        if radius == 0 or radius < 0:
            raise ValueError("Radius cannot be zero or negative")

    def calculate_perimeter(self):
        result = 2 * math.pi * self.radius
        return round(result, 2)

    def calculate_area(self):
        result = math.pi * (self.radius ** 2)
        return round(result, 2)


# We can create one more class for another shape, for example triangle
class Triangle(Shape):
    def __init__(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        self.point_1_x = point_1_x
        self.point_1_y = point_1_y
        self.point_2_x = point_2_x
        self.point_2_y = point_2_y
        self.point_3_x = point_3_x
        self.point_3_y = point_3_y

        self.side_1 = math.sqrt((self.point_2_x - self.point_1_x) ** 2 + (self.point_2_y - self.point_1_y) ** 2)
        self.side_2 = math.sqrt((self.point_3_x - self.point_2_x) ** 2 + (self.point_3_y - self.point_2_y) ** 2)
        self.side_3 = math.sqrt((self.point_1_x - self.point_3_x) ** 2 + (self.point_1_y - self.point_3_y) ** 2)
        self.validate_input(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y)

    def validate_input(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        super().validate_input(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y)
        if self.side_1 + self.side_2 <= self.side_3 or self.side_2 + self.side_3 <= self.side_1 \
                or self.side_1 + self.side_3 <= self.side_2:
            raise ValueError("Invalid sides for a triangle")

    def calculate_perimeter(self):
        result = self.side_1 + self.side_2 + self.side_3
        return round(result, 2)

    def calculate_area(self):
        semi_perimeter = self.calculate_perimeter() / 2
        result = math.sqrt(semi_perimeter * (semi_perimeter - self.side_1) * (semi_perimeter - self.side_2) * (
                semi_perimeter - self.side_3))
        return round(result, 2)
