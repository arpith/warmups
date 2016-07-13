import unittest
from counter import counter

class TestCounter(unittest.TestCase):
    def test_remove_spaces(self):
        counts = counter([' '])
        self.assertEqual(len(counts.keys()), 0)

    def test_total_count(self):
        total = 0
        s = 'someTextWithoutSpaces'
        counts = counter(list(s))
        for k, v in counts.iteritems():
            total += v
        self.assertEqual(len(s), total)

if __name__ == '__main__':
    unittest.main()
