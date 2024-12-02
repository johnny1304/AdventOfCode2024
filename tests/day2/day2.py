import unittest

from Day2.day2 import part_one, part_two


class MyTestCase(unittest.TestCase):
    def test_safe_reactors(self):
        self.assertEqual(part_one('day2/resources/testInput.txt'), 2)  # add assertion here

    def test_safe_reactors_2(self):
        self.assertEqual(part_two('day2/resources/testInput.txt'), 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
