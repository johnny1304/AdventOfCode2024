import unittest

from avoc2024.Day10.day10 import part_one, part_two


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(part_one("resources/testInput.txt"), 36)  # add assertion here

    def test_something2(self):
        self.assertEqual(part_two("resources/testInput.txt"), 81)


if __name__ == '__main__':
    unittest.main()
