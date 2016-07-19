import unittest
from fizzfactory import fizzfactory

class TestFlatten(unittest.TestCase):
    def test_to_13(self):
        factory = {2:'hi', 3:'world', 4:'!'}
        fizzfactored = fizzfactory(factory)
        upto_13 = fizzfactored[:13]
        expected = ['1', 'hi', 'world', 'hi!', '5', 'hiworld', '7', 'hi!', 'world', 'hi', '11', 'hiworld!', '13']
        self.assertEqual(upto_13, expected)

if __name__ == '__main__':
    unittest.main()
