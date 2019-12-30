import unittest
from homework import Rectangle


class TestRectangleCase(unittest.TestCase):

    def test_rectangle_perimeter(self):
        my_obj = Rectangle(3, 4)
        expected = 14
        self.assertEqual(my_obj.get_rectangle_perimeter(), expected)

    def test_get_rectangle_square(self):
        test_obj = Rectangle(3, 4)
        expected = 12
        self.assertEqual(test_obj.get_rectangle_square(), expected)

    def test_get_sum_of_corners(self):
        test_obj = Rectangle(3, 4)
        expected_sum = 270
        self.assertEqual(test_obj.get_sum_of_corners(3), expected_sum)

    def test_get_sum_of_corners_invalid_value(self):
        test_obj = Rectangle(3, 4)
        with self.assertRaises(ValueError):
            test_obj.get_sum_of_corners(5)

    def test_get_rectangle_diagonal(self):
        test_obj = Rectangle(3, 4)
        expected = 5
        self.assertEqual(test_obj.get_rectangle_diagonal(), expected)

    def test_get_radius_of_circumscribed_circle(self):
        test_obj = Rectangle(3, 4)
        expected = 2.5
        self.assertEqual(
            test_obj.get_radius_of_circumscribed_circle(), expected)

    def test_get_radius_of_inscribed_circle_valid(self):
        test_obj = Rectangle(6, 6)
        expected = 6
        self.assertEqual(test_obj.get_radius_of_inscribed_circle(), expected)

    def test_get_radius_of_inscribed_circle_invalid(self):
        test_obj = Rectangle(6, 5)
        with self.assertRaises(ValueError):
            test_obj.get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()
