import unittest

from avoc2024.Day12.Day12 import part_one, part_two


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(part_one("resources/testInput.txt"), 1930)  # add assertion here
    def test_something(self):
        self.assertEqual(part_two("resources/testInput.txt"), 1206)  # add assertion here

if __name__ == '__main__':
    unittest.main()
