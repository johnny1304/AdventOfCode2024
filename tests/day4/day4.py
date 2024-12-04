import unittest

from Day4.day4 import part_one, part_two


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(part_one("day4/resources/testInput.txt"), 18)

    def test_something2(self):
        self.assertEqual(part_two("day4/resources/testInput.txt"), 18)
    # add assertion here


if __name__ == '__main__':
    unittest.main()
