import unittest

import Day7.day7


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Day7.day7.part_one("day7/resources/testInput.txt"), 3749)  # add assertion here

    def test_somethingtwo(self):
        self.assertEqual(Day7.day7.part_two("day7/resources/testInput.txt"), 11387)  # add assertion here


if __name__ == '__main__':
    unittest.main()
