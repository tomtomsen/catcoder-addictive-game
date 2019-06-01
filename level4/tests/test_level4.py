import unittest
from level4 import main, addPathToGrid

class CalcRowTests(unittest.TestCase):
    def test_AddPathToGrid(self):
        self.assertEqual(
            addPathToGrid(
                [   0,
                    0, 0,
                    0, 0
                ],               # grid
                [1, 3, 3, 1, 4], # path
                2                # color
            ),
            [   0,
                2, 0,
                2, 2
            ]
        ) 


if __name__ == '__main__':
    unittest.main()
