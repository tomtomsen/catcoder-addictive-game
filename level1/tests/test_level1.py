import unittest
from level1 import calcRow, calcCol

class CalcRowTests(unittest.TestCase):
    def test_FirstRow(self):
        self.assertEqual(calcRow(1, 4), 1);

    def test_SecondRow(self):
        self.assertEqual(calcRow(2, 1), 2);

    def test_FirstCol(self):
        self.assertEqual(calcCol(1, 4), 1);

    def test_SecondCol(self):
        self.assertEqual(calcCol(6, 4), 2);

if __name__ == '__main__':
    unittest.main()