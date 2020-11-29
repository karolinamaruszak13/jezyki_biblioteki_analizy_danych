import unittest
from jezyki_biblioteki_analizy_danych.zad6.line_equation import line_equation


class LineEquationTest(unittest.TestCase):
    def test_point_value(self):
        self.assertRaises(ValueError, line_equation, pointA=[1, 1], pointB=[1, 1])
        self.assertRaises(ValueError, line_equation, pointA=[0, 0], pointB=[0, 0])
        self.assertRaises(ValueError, line_equation, pointA=[-1.1, 0], pointB=[-1.1, 0])

    def test_equation(self):
        self.assertEqual(line_equation(pointA=[5, 6], pointB=[7, 11]), [2.5, -6.5])  # y=2.5x-6.5
        self.assertEqual(line_equation(pointA=[2, -3], pointB=[-5, 4]), [-1, -1])  # y=-x-1
        self.assertEqual(line_equation(pointA=[2, 3], pointB=[4, 7]), [2, -1])  # y=2x-1
        self.assertEqual(line_equation(pointA=[1, 2], pointB=[3, 4]), [1, 1])  # y=x+1
        self.assertEqual(line_equation(pointA=[1, 3], pointB=[2, 2]), [-1, 4])  # y=-x+3


if __name__ == '__main__':
    unittest.main()
