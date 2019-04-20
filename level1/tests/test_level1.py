import unittest
from level1 import calcRow, calcCol, main

class Level1Tests(unittest.TestCase):
    def test_FirstRow(self):
        self.assertEqual(calcRow(1, 4), 1)

    def test_SecondRow(self):
        self.assertEqual(calcRow(2, 1), 2)

    def test_FirstCol(self):
        self.assertEqual(calcCol(1, 4), 1)

    def test_SecondCol(self):
        self.assertEqual(calcCol(6, 4), 2)

    def test_Main(self):
        # 
        # INPUT:
        #   <rows> <cols> <n-pos> <pos-1> <pos-2> ... <pos-n>
        #
        # OUTPUT:
        #   <row-1> <col-1> <row-2> <col-2> ... <row-n> <col-n>
        #
        # 1 2 3 4 5
        # 6 7 8 9 0
        # 1 2 3 4 5
        # 6 7 8 9 0

        self.assertEqual(main([4, 5, 3, 1, 17, 13]), '1 1 4 2 3 3')

if __name__ == '__main__':
    unittest.main()