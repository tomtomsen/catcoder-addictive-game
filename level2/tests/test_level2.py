import unittest
from level2 import manhattanDinstance, main

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

    def test_Main(self):
        # 
        # INPUT:
        #   <rows> <cols> <n-pairs> <pos-1> <color-1> <pos-2> <color-2>... <pos-n/2> <color-n/2>
        #
        # OUTPUT:
        #   <manhattan-distance-1> <manhattan-distance-2> ... <manhattan-distance-n/2>
        #
        # 1 2 3 4 5
        # 6 7 8 9 0
        # 1 2 3 4 5
        # 6 7 8 9 0

        self.assertEqual(main([4, 5, 4,   1, 2,   17, 1,   5, 1,   12, 2]), '6 3')

if __name__ == '__main__':
    unittest.main()