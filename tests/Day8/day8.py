import unittest

import Day8.day8
import Day8.day8Pt2


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Day8.day8.part_one("day8/resources/testInput.txt"), 14)  # add assertion here

    def test_somethingtwo(self):
        self.assertEqual(Day8.day8Pt2.part_two("day8/resources/testInput.txt"), 34)  # add assertion here


if __name__ == '__main__':
    unittest.main()
