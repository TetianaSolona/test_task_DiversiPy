import unittest
from shape import Square, Rectangle, Circle, Triangle


class TestShapes(unittest.TestCase):
    def test_square(self):
        square = Square(1, 1, 1)
        self.assertEqual(square.perimeter, 4)
        self.assertEqual(square.area, 1)

    def test_rectangle(self):
        rectangle = Rectangle(2, 2, 1, 1)
        self.assertEqual(rectangle.perimeter, 4)
        self.assertEqual(rectangle.area, 1)

        negative_rectangle = Rectangle(-2, -2, -1, -1)
        self.assertEqual(negative_rectangle.perimeter, 4)
        self.assertEqual(negative_rectangle.area, 1)

    def test_circle(self):
        circle = Circle(0, 0, 5)
        self.assertAlmostEqual(circle.perimeter, 31.42, places=2)
        self.assertAlmostEqual(circle.area, 78.54, places=2)

    def test_triangle(self):
        triangle = Triangle(0, 5, 0, 15, 10, 10)
        self.assertAlmostEqual(triangle.perimeter, 32.36, places=2)
        self.assertAlmostEqual(triangle.area, 49.99, places=2)

        negative_triangle = Triangle(0, 0, 0, -5, -10, -5)
        self.assertAlmostEqual(negative_triangle.perimeter, 26.18, places=2)
        self.assertAlmostEqual(negative_triangle.area, 25, places=2)

    def test_floating_point(self):
        rectangle_float_point = Rectangle(2.5, 2, 1.55, 1)
        self.assertAlmostEqual(rectangle_float_point.perimeter, 3.9, places=2)
        self.assertAlmostEqual(rectangle_float_point.area, 0.95, places=2)

        square_float_point = Square(1, 1, 1.55)
        self.assertAlmostEqual(square_float_point.perimeter, 6.2, places=2)
        self.assertAlmostEqual(square_float_point.area, 2.4, places=2)

        circle_float_point = Circle(0, 0, 1.25)
        self.assertAlmostEqual(circle_float_point.perimeter, 7.85, places=2)
        self.assertAlmostEqual(circle_float_point.area, 4.91, places=2)

        triangle_float_point = Triangle(0, 5.25, 0, 15, 10.50, 10)
        self.assertAlmostEqual(triangle_float_point.perimeter, 32.9, places=2)
        self.assertAlmostEqual(triangle_float_point.area, 51.15, places=2)

    def test_invalid_shape(self):
        self.assertRaises(ValueError, Square, 0, 0, 0)
        self.assertRaises(ValueError, Circle, 0, 0, 0)
        self.assertRaises(ValueError, Rectangle, 0, 0, 0, 0)
        self.assertRaises(ValueError, Triangle, 0, 0, 1, 1, 2, 2)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, Square, 'a', 'b', {})
        self.assertRaises(ValueError, Circle, [], 'b', 'c')

    def test_square_negative(self):
        self.assertRaises(ValueError, Square, 0, 0, -1)
        self.assertRaises(ValueError, Circle, 0, 0, -1)


if __name__ == '__main__':
    unittest.main()
