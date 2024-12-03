import unittest

from Day3.day3 import part_one,part_two


class MyTestCase(unittest.TestCase):
    def test_memory_corruption_1(self):
        self.assertEqual(part_one('day3/resources/testInput.txt'), 161)  # add assertion here

    def test_memory_corruption_2(self):
        self.assertEqual(part_two('day3/resources/testInput2.txt'), 48)  # add assertion here


if __name__ == '__main__':
    unittest.main()
