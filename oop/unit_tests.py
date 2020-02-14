import unittest
from homework import Cat


class TestCat(unittest.TestCase):

    def test_avg_speed_young_age(self):
        cat = Cat(1)
        self.assertEqual(12, cat.average_speed)

    def test_avg_speed_middle_age(self):
        cat = Cat(10)
        self.assertEqual(9, cat.average_speed)

    def test_avg_speed_old_age(self):
        cat = Cat(13)
        self.assertEqual(6, cat.average_speed)

    def test_increase_saturation_level(self):
        my_cat = Cat(1)
        my_cat._increase_saturation_level(10)
        self.assertEqual(my_cat.saturation_level, 60)

    def test_increase_saturation_level_1(self):
        my_cat = Cat(1)
        my_cat._increase_saturation_level(60)
        self.assertEqual(my_cat.saturation_level, 100)

    def test_reduce_saturation_level(self):
        my_cat = Cat(1)
        my_cat._reduce_saturation_level(10)
        self.assertEqual(my_cat.saturation_level, 40)

    def test_reduce_saturation_level_1(self):
        my_cat = Cat(1)
        my_cat._reduce_saturation_level(60)
        self.assertEqual(my_cat.saturation_level, 0)

    def test_eat_fodder(self):
        cat = Cat(1)
        cat._increase_saturation_level(10)
        self.assertEqual(cat.saturation_level, 60)

    def test_eat_apple(self):
        cat = Cat(1)
        cat._increase_saturation_level(5)
        self.assertEqual(cat.saturation_level, 55)

    def test_eat_milk(self):
        cat = Cat(1)
        cat._increase_saturation_level(2)
        self.assertEqual(cat.saturation_level, 52)

    def test_eat_other(self):
        cat = Cat(1)
        cat._increase_saturation_level(0)
        self.assertEqual(cat.saturation_level, 50)

    def test_run_1(self):
        cat = Cat(1)
        cat._reduce_saturation_level(2)
        self.assertEqual(cat.saturation_level, 48)

    def test_run_2(self):
        cat = Cat(1)
        cat._reduce_saturation_level(5)
        self.assertEqual(cat.saturation_level, 45)

    def test_run_3(self):
        cat = Cat(1)
        cat._reduce_saturation_level(50)
        self.assertEqual(cat.saturation_level, 0)

    def test_saturation_level(self):
        cat = Cat(2)
        cat._reduce_saturation_level(50)
        self.assertEqual(cat.saturation_level, 0)


if __name__ == "__main__":
    unittest.main()
