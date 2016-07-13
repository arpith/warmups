import unittest
from ee101 import ee101

class TestEE101(unittest.TestCase):
    def test_compute_i(self):
        res = ee101({'v': 6, 'r': 2})
        self.assertEqual(res, {'i': 3})

    def test_compute_v(self):
        res = ee101({'r': 3, 'i': 4})
        self.assertEqual(res, {'v': 12})

if __name__ == '__main__':
    unittest.main()
