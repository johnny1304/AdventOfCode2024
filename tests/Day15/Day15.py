import unittest

from avoc2024.Day15.Day15 import part_one


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(part_one("Day15/resources/testInput.txt","Day15/resources/testInputMoves.txt"), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
