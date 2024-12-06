import unittest

from Day6.day6 import part_one, part_two


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(part_one("day6/resources/testInput.txt"), 41)

    def test_something2(self):
        self.assertEqual(part_two("day6/resources/testInput.txt"), 41)
    # add assertion here


if __name__ == '__main__':
    unittest.main()
