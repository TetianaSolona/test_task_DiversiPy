import unittest
from shape import Square, Rectangle, Circle, Triangle


class TestShapes(unittest.TestCase):
    def test_square(self):
        square = Square(1, 1, 1)
        self.assertEqual(square.calculate_perimeter(), 4)
        self.assertEqual(square.calculate_area(), 1)

    def test_rectangle(self):
        rectangle = Rectangle(2, 2, 1, 1)
        self.assertEqual(rectangle.calculate_perimeter(), 4)
        self.assertEqual(rectangle.calculate_area(), 1)

        negative_rectangle = Rectangle(-2, -2, -1, -1)
        self.assertEqual(negative_rectangle.calculate_perimeter(), 4)
        self.assertEqual(negative_rectangle.calculate_area(), 1)

    def test_circle(self):
        circle = Circle(0, 0, 5)
        self.assertAlmostEqual(circle.calculate_perimeter(), 31.42, places=2)
        self.assertAlmostEqual(circle.calculate_area(), 78.54, places=2)

    def test_triangle(self):
        triangle = Triangle(0, 5, 0, 15, 10, 10)
        self.assertAlmostEqual(triangle.calculate_perimeter(), 32.36, places=2)
        self.assertAlmostEqual(triangle.calculate_area(), 49.99, places=2)

        negative_triangle = Triangle(0, 0, 0, -5, -10, -5)
        self.assertAlmostEqual(negative_triangle.calculate_perimeter(), 26.18, places=2)
        self.assertAlmostEqual(negative_triangle.calculate_area(), 25, places=2)

    def test_floating_point(self):
        rectangle_float_point = Rectangle(2.5, 2, 1.55, 1)
        self.assertAlmostEqual(rectangle_float_point.calculate_perimeter(), 3.9, places=2)
        self.assertAlmostEqual(rectangle_float_point.calculate_area(), 0.95, places=2)

        square_float_point = Square(1, 1, 1.55)
        self.assertAlmostEqual(square_float_point.calculate_perimeter(), 6.2, places=2)
        self.assertAlmostEqual(square_float_point.calculate_area(), 2.4, places=2)

        circle_float_point = Circle(0, 0, 1.25)
        self.assertAlmostEqual(circle_float_point.calculate_perimeter(), 7.85, places=2)
        self.assertAlmostEqual(circle_float_point.calculate_area(), 4.91, places=2)

        triangle_float_point = Triangle(0, 5.25, 0, 15, 10.50, 10)
        self.assertAlmostEqual(triangle_float_point.calculate_perimeter(), 32.9, places=2)
        self.assertAlmostEqual(triangle_float_point.calculate_area(), 51.15, places=2)

    def test_invalid_shape(self):
        with self.assertRaises(ValueError):
            zero_side_square = Square(0, 0, 0)
            zero_radius_circle = Circle(0, 0, 0)
            invalid_rectangle = Rectangle(0, 0, 0, 0)
            invalid_triangle = Triangle(0, 0, 1, 1, 2, 2)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            invalid_square = Square('a', 'b', {})
            invalid_circle = Circle([], 'b', 'c')


if __name__ == '__main__':
    unittest.main()