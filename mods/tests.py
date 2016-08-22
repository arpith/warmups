import unittest
from mods import mods

class TestMods(unittest.TestCase):
    def test_example(self):
        print("Testing example")
        ret = mods([9, 5, 3, 302], 3)
        expected = [[9, 3], [], [5, 302]]
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
