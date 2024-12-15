import unittest

from avoc2024.Day14.Day14 import part_one


class MyTestCase(unittest.TestCase):
    def test_something_part_one(self):
        self.assertEqual(part_one("Day14/resources/testInput.txt",100,10,6), 12)  # add assertion here

    # def test_something_part_two(self):
    #     self.assertEqual(part_two("Day13/resources/testInput.txt"), 875318608908)  # add assertion here

if __name__ == '__main__':
    unittest.main()
