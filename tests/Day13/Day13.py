import unittest

from avoc2024.Day13.Day13 import part_one, part_two


class MyTestCase(unittest.TestCase):
    def test_something_part_one(self):
        self.assertEqual(part_one("Day13/resources/testInput.txt"), 480)  # add assertion here

    def test_something_part_two(self):
        self.assertEqual(part_two("Day13/resources/testInput.txt"), 875318608908)  # add assertion here

if __name__ == '__main__':
    unittest.main()
