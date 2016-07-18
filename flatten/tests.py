import unittest
from flatten import flatten

class TestFlatten(unittest.TestCase):
    def test_example(self):
        l = [[1,2,3],[4,[5]]]
        res = flatten(l)
        f = [1,2,3,4,5]
        self.assertEqual(res, f)

if __name__ == '__main__':
    unittest.main()
