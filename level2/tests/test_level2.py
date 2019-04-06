import unittest
from level2 import manhattanDinstance

class CalcRowTests(unittest.TestCase):
    def test_manhattanDinstance1(self):
        self.assertEqual(manhattanDinstance(1, 2, 4), 1)
        self.assertEqual(manhattanDinstance(2, 1, 4), 1)
        self.assertEqual(manhattanDinstance(1, 5, 4), 1)
        self.assertEqual(manhattanDinstance(5, 1, 4), 1)
    
    def test_manhattanDinstance3(self):
        self.assertEqual(manhattanDinstance(1, 10, 3), 3)
        self.assertEqual(manhattanDinstance(10, 1, 3), 3)
        self.assertEqual(manhattanDinstance(6, 1, 3), 3)

if __name__ == '__main__':
    unittest.main()