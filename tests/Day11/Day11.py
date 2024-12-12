import unittest

from avoc2024.Day11.Day11 import part_one


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(part_one("resources/testInput.txt",25), 55312)  # add assertion here


if __name__ == '__main__':
    unittest.main()
