import unittest
from level3 import main, step, goNorth, goSouth, goEast, goWest, isOutOfBounds

class CalcRowTests(unittest.TestCase):
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
                3,
                16,
                8,
                'S', 'E', 'E', 'N', 'N', 'E', 'E', 'S'
            ]),
            '1 8'
        )

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
                'N', 'W', 'W'
            ]),
            '-1 3'
        )

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
                14,
                'S', 'E', 'E', 'S', 'S', 'S', 'W', 'W', 'W', 'N', 'N', 'N', 'N', 'W'
            ]),
            '-1 3'
        )

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
                11,
                'S', 'W', 'W', 'W', 'N', 'N', 'E', 'E', 'S', 'S'
            ]),
            '-1 10'
        )

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
                'S', 'S', 'W'
            ]),
            '-1 2'
        )

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
                4,
                'N', 'W', 'S', 'E'
            ]),
            '-1 4'
        )

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
                10,
                'S', 'W', 'W', 'W', 'N', 'N', 'E', 'E', 'S', 'S'
            ]),
            '-1 10'
        )

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
                10,
                'S', 'W', 'W', 'W', 'N', 'E', 'E', 'N', 'W', 'S'
            ]),
            '-1 10'
        )

        

    def test_goNorth(self):
        # 1 2 3 4
        # 5 6 7 8
        self.assertEqual(goNorth(7, 4), 3)
        self.assertEqual(goNorth(5, 4), 1)
        self.assertEqual(goNorth(3, 4), -1)

    def test_goSouth(self):
        # 1 2 3 4
        # 5 6 7 8
        self.assertEqual(goSouth(3, 4, 2), 7)
        self.assertEqual(goSouth(1, 4, 2), 5)
        self.assertEqual(goSouth(6, 4, 2), -1)

    def test_goEast(self):
        # 1 2 3 4
        # 5 6 7 8
        self.assertEqual(goEast(3, 4), 4)
        self.assertEqual(goEast(5, 4), 6)
        self.assertEqual(goEast(8, 4), -1)

    def test_goWest(self):
        # 1 2 3 4
        # 5 6 7 8
        self.assertEqual(goWest(4, 4), 3)
        self.assertEqual(goWest(6, 4), 5)
        self.assertEqual(goWest(1, 4), -1)

    def test_isOutOfBounds(self):
        self.assertEqual(isOutOfBounds(1, 4, 5), False)
        self.assertEqual(isOutOfBounds(0, 4, 5), True)
        self.assertEqual(isOutOfBounds(21, 4, 5), True)
        self.assertEqual(isOutOfBounds(-1, 4, 5), True)

    def test_step(self):
        # 1 2 3 4
        # 5 6 7 8
        self.assertEqual(step('S', 2, 4, 2), 6)
        self.assertEqual(step('S', 7, 4, 2), -1)

        self.assertEqual(step('N', 7, 4, 2), 3)
        self.assertEqual(step('N', 3, 4, 2), -1)

        self.assertEqual(step('E', 1, 4, 2), 2)
        self.assertEqual(step('E', 4, 4, 2), -1)

        self.assertEqual(step('W', 6, 4, 2), 5)
        self.assertEqual(step('W', 1, 4, 2), -1)

if __name__ == '__main__':
    unittest.main()
