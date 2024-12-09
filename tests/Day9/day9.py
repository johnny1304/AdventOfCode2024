import pathlib
import unittest

from avoc2024.Day9.day9 import part_one
from avoc2024.Day9.day9pt2 import part_two


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(pathlib.Path.cwd() )
        self.assertEqual(part_one("resources/testInputday9.txt"), 1928)

    def test_something2(self):
        self.assertEqual(part_two("resources/testInputday9.txt"), 2858)
    # add assertion here

if __name__ == '__main__':
    unittest.main()
