import unittest

from Day5.day5 import part_one, part_two


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(part_one("day5/resources/testInput.txt"), 143)

    def test_something_2(self):
        self.assertEqual(part_two("day5/resources/testInput.txt"), 123)
    # add assertion here


if __name__ == '__main__':
    unittest.main()
