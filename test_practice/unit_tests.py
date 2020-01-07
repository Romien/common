import unittest
from unittest.mock import patch
from tasks import (
    common_in_lists,
    check_a,
    check_power,
    add_digits,
    move_zeroes,
    check_progression,
    single_num,
    missing_num,
    count_elem,
    reverse_order,
    fibonacci_seq_task_14
)


class TestTasks(unittest.TestCase):

    def test_common_in_lists(self):
        list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        expected_result = [1, 2, 3, 5, 8, 13]
        actual_result = common_in_lists(list1, list2)
        self.assertEqual(expected_result, actual_result)

    def test_a(self):
        s = "I am a good developer. I am also a writer"
        expected_result = 5
        actual_result = check_a(s)
        self.assertEqual(expected_result, actual_result)

    def test_power_true(self):
        num = 9
        num1 = 27
        num2 = 3

        self.assertTrue(check_power(num))
        self.assertTrue(check_power(num1))
        self.assertTrue(check_power(num2))

    def test_power_false(self):
        self.assertFalse(check_power(10))

    def test_add_digits(self):
        self.assertEqual(add_digits(34), 7)
        self.assertEqual(add_digits(59), 5)

    def test_move_zeroes(self):
        list_1 = [0, 2, 3, 4, 0, 6, 7, 10]
        expected = [2, 3, 4, 6, 7, 10, 0, 0]
        self.assertEqual(move_zeroes(list_1), expected)

    def test_check_progression(self):
        l = [5, 7, 9, 11]
        self.assertTrue(check_progression(l))
        self.assertFalse(check_progression([5, 7, 10, 13]))
        l = [1]
        self.assertFalse(check_progression(l))

    def test_single_num(self):
        l = [5, 3, 4, 3, 4]
        self.assertEqual(single_num(l), 5)
        self.assertEqual(single_num([25, 0, 68, 25]), 0, 68)

    def test_missing_num(self):
        actual_result = [1, 2, 3, 4, 6, 7, 8]
        self.assertEqual(missing_num(actual_result), 5)

    def test_count_elem(self):
        self.assertEqual(count_elem([1, 2, 3, (1, 2), 3]), 3)

    def test_reverse_order(self):
        s = "Hello World and Coders"
        expected = "sredoC dna dlroW olleH"
        self.assertEqual(reverse_order(s), expected)

    @patch("tasks.fibonacci_seq_task_14", return_value="1, 1, 2,")
    def test_fibonacci_seq(self, fibonacci_seq_task_14):
        self.assertEqual(fibonacci_seq_task_14(), "1, 1, 2,")


if __name__ == "__main__":
    unittest.main()
