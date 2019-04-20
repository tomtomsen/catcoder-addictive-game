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

    def test_Main(self):
        
        self.assertEqual(
            main([
                5, 5, 
                8, 
                7, 1, 
                9, 1, 
                10, 2, 
                16, 3, 
                17, 2, 
                19, 4, 
                20, 3, 
                25, 4,
                1,
                1,
                9,
                3,
                'W', 'W', 'W'
            ]),
            '-1 3'
        )

if __name__ == '__main__':
    unittest.main()
